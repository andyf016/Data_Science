import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('NBA Player Stats Explorer')

st.markdown("""
This app performs simple web scraping of NBA player stats data
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [Basketball-refrence.com](https://www.basketball-refrence.com/).
""")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950, 2020))))

#web scraping of NBA players stats
@st.cache
def load_data(year):
    url = 'https://www.basketball-refrence.com/leagues/NBA_' + str(year) + "_per_game.html"
    html = pd.read_html(url, header = 0) # Preform Web Scraping
    df = html[0]    
    raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating age
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis=1) # delete index column 
    return playerstats
playerstats = load_data(selected_year)

# Sidebar team selection
sorted_unique_team = sorted(playerstats.Tm.unique()) 
selectd_team = st.sidebar.multiselect('Team', sorted_unique_team)

# Sidebar position selection
unique_pos = ['C', 'PF', 'SF', 'PG', 'SG']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)