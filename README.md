# 🎤 Eurovision Song Contest 2025 Voting App

This project simulates and showcases a **live voting system** for the Eurovision Song Contest 2025 using **Redis**, **FastAPI**, and **Streamlit**. It includes real-time leaderboard updates, simulated and user-driven voting, and dynamic web scraping of participant names from Wikipedia.

---

## 🚀 Features

- ✅ Live voting simulation using Redis Pub/Sub and Sorted Sets  
- ✅ Real-time leaderboard updates  
- ✅ User voting interface (1 vote per user via email)  
- ✅ Dynamic web scraping of 2025 Eurovision participants  
- ✅ Modular multi-page Streamlit app  
- ✅ Dockerized setup for consistent deployment  

---

## 📦 Technologies Used

- **Python 3.9**
- **Redis** (Pub/Sub + Sorted Sets)
- **Streamlit** (for UI)
- **FastAPI** (for optional API endpoints)
- **BeautifulSoup4** (for scraping Wikipedia)
- **Docker** (for easy containerization)

---

## 🗳️ How It Works

1. **Scraping Participants**  
   `utils/web_scraper.py` dynamically extracts artist names from the official Eurovision 2025 Wikipedia page.

2. **Simulated Voting**  
   A background script (`publisher/vote.py`) simulates user votes with randomized user IDs and broadcasts the leaderboard.

3. **User Voting**  
   Real users can vote via the Streamlit interface by entering their **email address**. Votes are recorded in Redis and each email can vote **only once**.

4. **Real-Time Leaderboard**  
   The leaderboard is updated instantly and streamed to the frontend using Redis Pub/Sub.

---

## 🐳 Run with Docker

Build the image and run:

```bash
docker-compose up --build
```