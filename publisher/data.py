import redis
import random
import time
import requests
import json
from utils.web_scraper import find_artists

# Connect to Redis
r = redis.Redis(host='redis', port=6379, decode_responses=True)

# Band names
bands = find_artists()

# Initialize scores
for band in bands:
    r.zadd("bands", {band: 0})

# Simulate unique user votes
ids = list(range(int(10e5)))
random.shuffle(ids)
already_voted = set()

while True:
    for user in ids:
        if user not in already_voted:
            already_voted.add(user)
            voted_band = random.choice(bands)
            r.zincrby("bands", 1, voted_band)
            
            # Get current leaderboard with scores
            current_ranking = r.zrevrange("bands", 0, -1, withscores=True)
            # print(current_ranking[0][1])
            payload = {
                'band': [band[0] for band in current_ranking],
                'votes': [score[1] for score in current_ranking]
            }
            # Serialize to string for publishing
            message = json.dumps(payload)
            print(message)
            r.publish('leaderboard', str(message))
            
            print(f"User {user} voted for {voted_band}. Leaderboard: {current_ranking}")
            # time.sleep(0)
