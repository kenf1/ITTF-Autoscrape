#convert -data.csv & -metadata.csv files inside ./data folder into respective SQL db

import os
import pandas as pd
import sqlite3 as sql

def csv2db(path,searchTerm,dbName):
    filename = []
    
    for file in os.listdir(path):
        if file.endswith(searchTerm):
            filename.append(file)
    
    con = sql.connect(dbName)
    
    for item in filename:
        df = pd.read_csv(f"{path}/{item}")
        tablename = os.path.splitext(item)[0].replace(searchTerm,"").replace("-data","").replace("SEN_","")
        df.to_sql(tablename,con,index=False,if_exists="replace")
        
    con.close()

csv2db("data","-data.csv","./data/player_rank.db")
csv2db("data","-metadata.csv","./data/metadata.db")
