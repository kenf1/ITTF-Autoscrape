#--- import modules ---#
import pandas as pd
import requests
import plotly_express as px
import streamlit as sl

#page config
def pg_config():
    sl.set_page_config(initial_sidebar_state="expanded",layout="wide",page_icon="🏓",
                       menu_items={"Get help":None,
                                   "Report a Bug":links.gh_issue,
                                   "About":links.author})
    sl.sidebar.markdown("***Note:*** _All figures are interactive. Double-click anywhere inside the figures to reset to default view._")

#import data
class links:
#list of hosted & local ver   
    dataset = ["https://raw.githubusercontent.com/kenf1/ITTF-Autoscrape/main/data/SEN_MS-data.csv","../data/SEN_MS-data.csv"]
    metadata = ["https://raw.githubusercontent.com/kenf1/ITTF-Autoscrape/main/data/SEN_MS-metadata.csv","../data/SEN_MS-metadata.csv"]
#other links
    img = "https://www.theindianwire.com/wp-content/uploads/2018/08/table-tennis.jpeg"
    gh_issue = "https://github.com/kenf1/ITTF-Autoscrape/issues"
    author = "App by: [KF](https://github.com/kenf1)"

#check if dataset exists in GH repo, loads local csv file if not
def load_data(url_list):
    response = requests.head(url_list[0])
    if response.status_code == 200:
        df = pd.read_csv(url_list[0])
    else:
        df = pd.read_csv(url_list[1])
    return df

#store all data in class
class ittf:
    rank_df = load_data(links.dataset)
    metadata_df = load_data(links.metadata)
    year = metadata_df["datasetYear"][0]
    week = metadata_df["datasetWeek"][0]
    
    #subset data (only keep top 30 players)
    rank_short = rank_df[:30]

#--- interactive web app ---#

#fig1
fig1 = px.pie(ittf.rank_short,"Assoc",title="Countries Represented")

#fig4
# fig4 = px.bar(ittf.rank_short,x=ittf.rank_short["Assoc"].value_counts(),y=ittf.rank_short["Assoc"].value_counts().index,
#               title="Countries Represented in the Top 30")
# fig4.update_layout(yaxis={'categoryorder':'total ascending'})
# fig4.update_xaxes(title_text="Count")
# fig4.update_yaxes(title_text="Countries")

#fig2
fig2 = px.bar(ittf.rank_short,x="Points",y="Name",color="Assoc",title="Total Points Count for Each Player")
fig2.update_layout(yaxis={'categoryorder':'total ascending'})

#table1
table1 = ittf.rank_short[~ittf.rank_short["Rank Change"].isna()]

#fig3
fig3 = px.bar(table1,x="Points",y="Name",color="Assoc",title="Players with Rank Change")
fig3.update_layout(yaxis={'categoryorder':'total ascending'})

#display pie output
def countries_rep():
    sl.markdown("#### The world's top 30 table tennis players are from these countries:")
    sl.plotly_chart(fig1)
    # sl.plotly_chart(fig4)

#display bar output
def total_pt():
    sl.markdown("#### Total points (color coded by country) for each player:")
    sl.markdown("__Format:__ `Name` `SURNAME`")
    sl.plotly_chart(fig2)

#display table output
def rankchange():
    sl.markdown("#### All players whose rank has changed (`raised`/`dropped`).")
    sl.dataframe(table1)
    sl.plotly_chart(fig3)

#display full dataset
def full_dataset():
    sl.dataframe(ittf.rank_df,width=1000,height=750)

#homepage
def homepage():
    sl.set_page_config(initial_sidebar_state="expanded",layout="wide",page_icon="🏓",
                       menu_items={"Get help":None,
                                   "Report a Bug":links.gh_issue,
                                   "About":links.author})
    sl.title(f"ITTF Men's Singles Rankings for {ittf.year} {ittf.week}")
    sl.markdown(links.author)
    sl.text("An auto-updating interactive dashboard to visualize the countries \n and total number of points for the world's top ranked 30 table tennis players.")
    sl.image(links.img)

#sidebar
def sidebar():
    sl.sidebar.markdown("# Created By: [KF](https://github.com/kenf1)")
    sl.sidebar.markdown("   ")
    sl.sidebar.markdown("Data source: [ITTF Rankings](https://www.ittf.com/rankings/)")
    sl.sidebar.markdown("A copy of the dataset can be downloaded from: [Dataset link](https://github.com/kenf1/ITTF-Autoscrape/tree/main/data)")
