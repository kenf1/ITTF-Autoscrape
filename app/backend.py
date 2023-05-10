#--- import modules ---#
import pandas as pd
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
    dataset="https://raw.githubusercontent.com/kenf1/ITTF-Autoscrape/main/data/dataset.csv"
    metadata="https://raw.githubusercontent.com/kenf1/ITTF-Autoscrape/main/data/metadata.csv"
    img="https://www.theindianwire.com/wp-content/uploads/2018/08/table-tennis.jpeg"
    gh_issue="https://github.com/kenf1/ITTF-Autoscrape/issues"
    author="App by: [KF](https://github.com/kenf1)"

ittf_rank = pd.read_csv(links.dataset)
ittf_metadata = pd.read_csv(links.metadata)

#dataset metadata
class dataset:
    year=ittf_metadata["datasetYear"][0]
    week=ittf_metadata["datasetWeek"][0]

#--- interactive web app ---#

#subset data (only keep top 30 players)
ittf_rank_short = ittf_rank[:30]

#fig1
fig1 = px.pie(ittf_rank_short,"Assoc",title="Countries Represented")

#fig4
# fig4 = px.bar(ittf_rank_short,x=ittf_rank_short["Assoc"].value_counts(),y=ittf_rank_short["Assoc"].value_counts().index,
#               title="Countries Represented in the Top 30")
# fig4.update_layout(yaxis={'categoryorder':'total ascending'})
# fig4.update_xaxes(title_text="Count")
# fig4.update_yaxes(title_text="Countries")

#fig2
fig2 = px.bar(ittf_rank_short,x="Points",y="Name",color="Assoc",title="Total Points Count for Each Player")
fig2.update_layout(yaxis={'categoryorder':'total ascending'})

#table1
table1 = ittf_rank_short[~ittf_rank_short["Rank Change"].isna()]

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
    sl.dataframe(ittf_rank,width=1000,height=750)

#homepage
def homepage():
    sl.set_page_config(initial_sidebar_state="expanded",layout="wide",page_icon="🏓",
                       menu_items={"Get help":None,
                                   "Report a Bug":links.gh_issue,
                                   "About":links.author})
    sl.title(f"ITTF Men's Singles Rankings for {dataset.year} {dataset.week}")
    sl.markdown(links.author)
    sl.text("An auto-updating interactive dashboard to visualize the countries \n and total number of points for the world's top ranked 30 table tennis players.")
    sl.image(links.img)

#sidebar
def sidebar():
    sl.sidebar.markdown("# Created By: [KF](https://github.com/kenf1)")
    sl.sidebar.markdown("   ")
    sl.sidebar.markdown("Data source: [ITTF Rankings](https://www.ittf.com/rankings/)")
    sl.sidebar.markdown("A copy of the dataset can be downloaded from: [Dataset link](https://github.com/kenf1/ITTF-Autoscrape/tree/main/data)")
