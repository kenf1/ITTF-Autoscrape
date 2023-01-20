#--- import modules ---#
import pandas as pd
import plotly_express as px
import streamlit as sl

#--- import data ---#
ittf_rank = pd.read_csv("data/dataset.csv")

#--- interactive web app ---#

#site text
# sl.title(f"ITTF Men's Singles Rankings for {datasetYear} Wk:{datasetWeek}")
sl.markdown("By: [KF](https://github.com/kenf1)")
sl.text("A auto-updating interactive dashboard to visualize the \n countries and total number of points \n for the world's top ranked 30 table tennis players.")
sl.markdown("Data source: [ITTF Rankings](https://www.ittf.com/rankings/)")

#subset data (only keep top 30 players)
ittf_rank = ittf_rank[:30]

#figures
fig1 = px.pie(ittf_rank,"Assoc",title="Countries Represented")

fig2 = px.bar(ittf_rank,x="Points",y="Name",color="Assoc",title="Total Points Count for Each Player")
fig2.update_layout(yaxis={'categoryorder':'total ascending'})

#rm NaN rows in Rank Change
table1 = ittf_rank[~ittf_rank["Rank Change"].isna()]

#display outputs
sl.markdown("#### The world's top 30 table tennis players are from these countries:")
sl.plotly_chart(fig1)

sl.markdown("#### Total points (color coded by country) for each player:")
sl.plotly_chart(fig2)

sl.markdown("#### All players whose rank has changed (raised/dropped).")
sl.dataframe(table1)