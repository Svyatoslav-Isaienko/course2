import os

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

pubsub = r.pubsub()
pubsub.subscribe(CHANNEL)
print(f"Підписалися на канал '{CHANNEL}'. Очікуємо повідомлення...\n")

for message in pubsub.listen():

    if message["type"] != "message":
        continue

    print(f"Отримано: {message['data']}")


    if message["data"] == "Hello Redis! Message #9":
        print("\nОтримано всі повідомлення, завершуємо роботу.")
        break

pubsub.unsubscribe(CHANNEL)
pubsub.close()
