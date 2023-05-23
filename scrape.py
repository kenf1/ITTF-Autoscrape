#--- import modules ---#
#base
import re
import sqlite3 as sql

#supplement
import requests
from bs4 import BeautifulSoup
import pandas as pd

#--- scrape & save data ---#

#ITTF rankings home directory
rankings_link = "https://www.ittf.com/rankings/"

#function to scrape link
def bs4_setup(scrape_url):
    """function to scrape link

    Args:
        scrape_url (str): link to scrape from

    Returns:
        _type_: scraped results
    """
    temp = BeautifulSoup(requests.get(scrape_url).content,"html.parser")
    return temp

#obtain latest update (Men's singles)
soup = bs4_setup(rankings_link)
results = soup.find(class_="theiaStickySidebar").find_all("ul")[1].find("li").find("a",href=True)
current_link = results["href"]

#scrape from current_link
soup = bs4_setup(current_link)
results = soup.find(id="content")

#store results of colNames (html table)
headers_list = []
for i in results.find_all("tr",class_="tablehead"):
    title = i.text.strip()
    headers_list.append(title)

#--- obtain metadata ---#

class metadata:
    #extract dataset title
    rankingType = results.find("td",class_="listdataleft").text.strip()

    #extract year
    datasetYear = re.sub(r"[^0-9]","",str(re.findall("\\d{4}",rankingType)))

    #extract week
    datasetWeek = re.split("\\d{4}",rankingType)[1]

#create empty df
ittf_metadata = pd.DataFrame(columns=[metadata.rankingType,metadata.datasetYear,metadata.datasetWeek])

#store metadata
ittf_metadata.loc[len(ittf_metadata)] = [metadata.rankingType,metadata.datasetYear,metadata.datasetWeek]

#save to csv
ittf_metadata.to_csv("data/metadata.csv",index=False)

#--- wrangle scraped data ---#

#rm new lines (\n)
headers = headers_list[0].split("\n")

#convert list to string + tidy
new_header = ",".join(headers).replace("'","").split(" ")

#create empty df to store results
ittf_rank = pd.DataFrame(columns=new_header)

#store results of html table
results.find_all("tr",class_='rrow')
for j in results.find_all("tr",class_="rrow")[0:]:
    row_data = j.find_all("td")
    ittf_rank.loc[len(ittf_rank)] = [tr.text for tr in row_data]
    
#split rank into number + change from previous rank
def rankExtract(position):
    temp = ittf_rank["Rank"].str.split(" ").str[position]
    return temp

ittf_rank["Rank Only"] = rankExtract(0)
ittf_rank["Rank Change"] = rankExtract(1)

#reorder cols + drop Rank (w/ ranking change)
ittf_rank = ittf_rank[["Rank Only","Rank Change","Name","Assoc","Points"]]

#convert rank & points to numeric
ittf_rank[["Rank Only","Points"]] = ittf_rank[["Rank Only","Points"]].astype(int)

#save to csv
ittf_rank.to_csv("data/dataset.csv",index=False)

#save to sql db
connection = sql.connect("./data/ittf.db")
ittf_metadata.to_sql("metadata",connection,if_exists="replace")
ittf_rank.to_sql("M_rankings",connection,if_exists="replace")
connection.close()
