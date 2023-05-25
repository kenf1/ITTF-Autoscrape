#Local demo ver (only downloads Men's Single Dataset)

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import sqlite3 as sql

#--- Functions ---#

#navigate from site homepage
def obtain_links(scrape_url):
    class siteContent:
    
    #find table from site
        html_data = BeautifulSoup(requests.get(scrape_url).content,"html.parser")
        table_data = html_data.find(class_="theiaStickySidebar").find_all("ul")[1].find_all("li")
    
    #extract & store urls in list
        cleanURLs = []
        for i in range(len(table_data)):
            cleanURLs.append(table_data[i].find("a",href=True)["href"])
    
    return siteContent

#obtain metadata
def scrape_metadata(cleanURL):
    class metadata:
        html_data = BeautifulSoup(requests.get(cleanURL).content,"html.parser").find(id="content")
    
    #name to save dataset under    
        filename = re.findall("[A-Z_]+",cleanURL)[1][1:]
    
    #colNames
        headers_list = []
        for i in html_data.find_all("tr",class_="tablehead"):
            title = i.text.strip()
            headers_list.append(title)
        colNames = headers_list[0].split("\n")
    
    #rankingType, datasetYear, datasetWeek    
        rankingType = html_data.find("td",class_="listdataleft").text.strip()
        datasetYear = re.sub(r"[^0-9]","",str(re.findall("\\d{4}",rankingType)))
        datasetWeek = re.split("\\d{4}",rankingType)[1]
    
    #save to df
        ittf_metadata = pd.DataFrame(columns=["rankingType","datasetYear","datasetWeek"])
        ittf_metadata.loc[len(ittf_metadata)] = [rankingType,datasetYear,datasetWeek]
    
    return metadata

#obtain data
def scrape_table(header_input,content_input):

#create df to store scraped data  
    new_colName = ",".join(header_input).replace("'","").split(" ")
    ittf_rank = pd.DataFrame(columns=new_colName)
    
#data
    content_input.find_all("tr",class_='rrow')
    for j in content_input.find_all("tr",class_="rrow")[0:]:
        row_data = j.find_all("td")
        ittf_rank.loc[len(ittf_rank)] = [tr.text for tr in row_data]
        
#rank & rank changes
    def rankExtract(position):
        temp = ittf_rank["Rank"].str.split(" ").str[position]
        return temp
    
    ittf_rank["Rank Only"] = rankExtract(0)
    ittf_rank["Rank Change"] = rankExtract(1)

#append to df
    ittf_rank = ittf_rank[["Rank Only","Rank Change","Name","Assoc","Points"]]
    ittf_rank[["Rank Only","Points"]] = ittf_rank[["Rank Only","Points"]].astype(int)
        
    return ittf_rank

#save scraped data into: csv & sql db
def save_dataset(metadata_df,data_df,filename,to_SQL=True):
    metadata_df.to_csv(f"./data/{filename}-metadata.csv",index=False)
    data_df.to_csv(f"./data/{filename}-data.csv",index=False)
    
    if to_SQL == True:
        connection = sql.connect(f"./data/{filename}.db")
        metadata_df.to_sql("metadata",connection,if_exists="replace")
        data_df.to_sql("M_rankings",connection,if_exists="replace")
        connection.close()
   
#--- Scrape & save ---#

#site homepage
rankings_link = "https://www.ittf.com/rankings/"

#links for each ranking dataset
siteContent = obtain_links(rankings_link)

#scrape & save
# for i in range(len(siteContent.cleanURLs)):
#     metadata = scrape_metadata(siteContent.cleanURLs[i])
#     final = scrape_table(metadata.colNames,metadata.html_data)
#     save_dataset(metadata.ittf_metadata,final,metadata.filename)

#demo ver specific
if __name__ == "__main__":
    siteContent = obtain_links(rankings_link)
    metadata = scrape_metadata(siteContent.cleanURLs[0])
    final = scrape_table(metadata.colNames,metadata.html_data)
    save_dataset(metadata.ittf_metadata,final,metadata.filename)
