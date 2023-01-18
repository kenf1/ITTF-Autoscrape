#import modules
import pandas as pd
import plotly_express as px
import streamlit as sl

#import data
top_n_players = pd.read_csv("")
top_n_players = top_n_players[0:31]

#fig 1
#repeated title/subtitle components
titleRepeat = " (Top "+str(len(top_n_players))+" Players)"+"<br><sup>"+fullName+"</sup></br>"
#num players per assoc
fig1 = px.pie(top_n_players,"Assoc",title="Association Breakdown"+titleRepeat)
fig1.show()

#fig 2
#country + total points for top ranked players
fig = px.bar(top_n_players,x="Points",y="Name",color="Assoc",title="Number of Points"+titleRepeat)
fig.update_layout(yaxis={'categoryorder':'total ascending'})