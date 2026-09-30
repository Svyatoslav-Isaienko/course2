import os
import time

import redis
from dotenv import load_dotenv

load_dotenv()

CHANNEL = "python_channel"

r = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    username=os.getenv("REDIS_USERNAME", "default"),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True,
)

print("PING:", r.ping())

for i in range(10):
    message = f"Hello Redis! Message #{i}"
    subscribers_count = r.publish(CHANNEL, message)
    print(f"Надіслано: {message} (отримали {subscribers_count} підписник(ів))")
    time.sleep(0.5)  # невелика пауза, щоб було видно процес у RedisInsight

print("\nВсі 10 повідомлень надіслано.")