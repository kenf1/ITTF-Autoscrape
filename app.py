#--- import modules ---#
import pandas as pd
import plotly_express as px
import streamlit as sl

#import data
ittf_rank = pd.read_csv("data/dataset.csv")
ittf_metadata = pd.read_csv("data/metadata.csv")

#extract year & week
datasetYear = ittf_metadata["datasetYear"][0]
datasetWeek = ittf_metadata["datasetWeek"][0]

#--- interactive web app ---#

#sidebar title & description
sl.sidebar.title("Navigation")
sl.sidebar.markdown("Click on the buttons below to view the different pages of this interactive dashboard.")

#page selector
options = sl.sidebar.radio("Pages",options=["Home","Countries Represented","Total Points","Rank Changed","Full Dataset"])

#note
sl.sidebar.markdown("***Note:*** _All figures are interactive. Double-click anywhere inside the figures to reset to default view._")

#site text
def homepage():
    sl.title(f"ITTF Men's Singles Rankings for {datasetYear} {datasetWeek}")
    sl.markdown("By: [KF](https://github.com/kenf1)")
    sl.text("An auto-updating interactive dashboard to visualize the \n countries and total number of points \n for the world's top ranked 30 table tennis players.")
    sl.markdown("Data source: [ITTF Rankings](https://www.ittf.com/rankings/)")
    sl.image("https://www.theindianwire.com/wp-content/uploads/2018/08/table-tennis.jpeg")

#subset data (only keep top 30 players)
ittf_rank_short = ittf_rank[:30]

#figures
fig1 = px.pie(ittf_rank_short,"Assoc",title="Countries Represented")

fig2 = px.bar(ittf_rank_short,x="Points",y="Name",color="Assoc",title="Total Points Count for Each Player")
fig2.update_layout(yaxis={'categoryorder':'total ascending'})

#rm NaN rows in Rank Change
table1 = ittf_rank_short[~ittf_rank_short["Rank Change"].isna()]

#display pie output
def countries_rep():
    sl.markdown("#### The world's top 30 table tennis players are from these countries:")
    sl.plotly_chart(fig1)

#display bar output
def total_pt():
    sl.markdown("#### Total points (color coded by country) for each player:")
    sl.markdown("__Format:__ `Name` `SURNAME`")
    sl.plotly_chart(fig2)

#display table output
def rankchange():
    sl.markdown("#### All players whose rank has changed (`raised`/`dropped`).")
    sl.dataframe(table1)

#display full dataset
def full_dataset():
    sl.dataframe(ittf_rank,width=1000,height=750)

if options == "Home":
    homepage()
elif options == "Countries Represented":
    countries_rep()
elif options == "Total Points":
    total_pt()
elif options == "Rank Changed":
    rankchange()
elif options == "Full Dataset":
    full_dataset()
