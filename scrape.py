#import modules
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

#setup
URL = "https://www.ittf.com/wp-content/uploads/2023/01/2023_2_SEN_MS.html"
soup = BeautifulSoup(requests.get(URL).content,"html.parser")
results = soup.find(id="content")

#get dataset title
rankingType = results.find("td",class_="listdataleft").text.strip()

#extract year
datasetYear = re.sub(r"[^0-9]","",str(re.findall("\\d{4}",rankingType)))

#extract event & week
competition = re.split("\\d{4}",rankingType)

#event
datasetEvent = competition[0]

#week
datasetWeek = competition[1]

#store results of colNames (html table)
headers_list = []
for i in results.find_all("tr",class_="tablehead"):
    title = i.text.strip()
    headers_list.append(title)

#rm new lines
headers = headers_list[0].split("\n")

#convert list to string + tidy
new_header = ",".join(headers).replace("'","").split(" ")

fullName = f"{datasetEvent} {datasetYear}{datasetWeek}"

#create df to store results
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