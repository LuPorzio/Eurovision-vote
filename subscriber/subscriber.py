# import redis
# import json
# from fastapi import FastAPI
# from fastapi.responses import JSONResponse

# app = FastAPI()

# # Connect to Redis
# r = redis.Redis(host='redis', port=6379, decode_responses=True)
# pubsub = r.pubsub()
# pubsub.subscribe('leaderboard')

# while True:

#     @app.get("/")
#     def read_root():
#         return {"message": "FastAPI is working!"}

#     @app.get("/scoreboard")
#     def latest_scoreboard():
#         for message in pubsub.listen():
#             if message['type'] == 'message':
#                 try:
#                     # Parse the JSON-formatted leaderboard
#                     data = json.loads(message['data'])
#                     return JSONResponse(content={"leaderboard": data})
#                 except json.JSONDecodeError:
#                     return JSONResponse(content={"error": "Invalid data format"}, status_code=400)

import redis
import json
import threading
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# Connect to Redis
r = redis.Redis(host='redis', port=6379, decode_responses=True)
pubsub = r.pubsub()
pubsub.subscribe('leaderboard')

# Store latest leaderboard
latest_data = {"leaderboard": []}

# Background thread function
def listen_to_leaderboard():
    for message in pubsub.listen():
        if message['type'] == 'message':
            try:
                data = json.loads(message['data'])
                latest_data["leaderboard"] = data
            except json.JSONDecodeError:
                continue

thread = threading.Thread(target=listen_to_leaderboard, daemon=True)
thread.start()

# FastAPI routes
@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}

@app.get("/scoreboard")
def get_scoreboard():
    return JSONResponse(content=latest_data)
