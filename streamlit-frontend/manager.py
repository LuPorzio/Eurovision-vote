import streamlit as st

# Define the pages
main = st.Page("main.py", title="Eurovision Song Contest 2025", icon="🎤")
page1 = st.Page("page1.py", title="How to vote", icon="✨")
page2 = st.Page("page2.py", title="Partecipants", icon="👥")

# Set up navigation
pg = st.navigation([main, page1, page2])

# Run the selected page
pg.run()