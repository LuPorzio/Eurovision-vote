import streamlit as st
import pandas as pd
import requests
from streamlit_autorefresh import st_autorefresh

# Auto refresh every 2 seconds
st_autorefresh(interval=2000, limit=None, key="leaderboardrefresh")

# Main page content
st.markdown("# Eurovision Song Context 2025")
#st.sidebar.markdown("# Eurovision Song Context 2025")


DATE_COLUMN = 'date/time'
DATA_URL = ('http://subscriber:8000/scoreboard')

def load_data():
    data = requests.get(DATA_URL).json()
    
    return data

data = load_data()['leaderboard']
print(data)
df = pd.DataFrame(data, index=range(1, len(data['band'])+1))

# Ensure proper types
df['band'] = df['band'].astype(str)
df['votes'] = pd.to_numeric(df['votes'], errors='coerce').astype(int)

# Sort by score descending
df = df.sort_values(by="votes", ascending=False)#.reset_index(drop=True)

# # Optional: Add ranking
# df.insert(0, 'Rank', df.index + 1)

# Display as a nice table
# st.title("Eurovision Scoreboard")
st.table(df)