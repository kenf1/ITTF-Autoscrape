#import modules
import pandas as pd
import plotly_express as px

#import data
top_n_players = pd.read_csv("data/dataset.csv")[:10]

#Fig 1: num players per assoc
fig1 = px.pie(top_n_players,"Assoc",title="Association Breakdown")
fig1.show()

#Fig 2: country + total points for top ranked players
fig2 = px.bar(top_n_players,x="Points",y="Name",color="Assoc",title="Number of Points")
fig2.update_layout(yaxis={'categoryorder':'total ascending'})
fig2.show()