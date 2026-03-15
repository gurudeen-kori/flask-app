from flask import Flask
from sqlalchemy import create_engine, text
import redis
import os

app = Flask(__name__)

# Environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")

# Connect to MySQL
try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("Connected to MySQL")
except Exception as e:
    print("MySQL connection failed:", e)

# Connect to Redis
try:
    r = redis.Redis.from_url(REDIS_URL)
    r.set("test_key", "Hello Redis!")
    print("Connected to Redis")
except Exception as e:
    print("Redis connection failed:", e)

@app.route("/")
def hello():
    redis_val = r.get("test_key")
    return f"Hello World! Redis says: {redis_val.decode() if redis_val else 'nothing'}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
