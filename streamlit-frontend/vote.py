import streamlit as st
import redis
import json
from utils.web_scraper import find_artists
from email_validator import validate_email, EmailNotValidError

def is_valid_email(email):
    try:
        # Validate and normalize the email
        valid = validate_email(email)
        return True
    except EmailNotValidError:
        return False

# Connect to Redis
r = redis.Redis(host='redis', port=6379, decode_responses=True)

st.title("🎤 Eurovision 2025 Voting Booth")

# Fetch bands
bands = find_artists()

# Get user input
user_id = st.text_input("👤 Enter your email:")
band_choice = st.selectbox("🎶 Choose your favorite artist:", bands)

if st.button("Submit Vote"):
    if not user_id.strip():
        st.error("Please enter a valid email.")
    elif not is_valid_email(user_id):
        st.error("❌ Please use a valid email address to vote.")
    elif r.sismember("voted_users", user_id):
        st.warning("⚠️ This email has already voted.")
    else:
        # Proceed with vote registration
        r.sadd("voted_users", user_id)
        r.zincrby("bands", 1, band_choice)

        current_ranking = r.zrevrange("bands", 0, -1, withscores=True)
        payload = {
            'band': [band[0] for band in current_ranking],
            'votes': [score[1] for score in current_ranking]
        }

        r.set("latest_leaderboard", json.dumps(payload))
        r.publish("leaderboard", json.dumps(payload))

        st.success(f"✅ Your vote for {band_choice} has been recorded!")