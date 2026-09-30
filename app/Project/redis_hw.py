import os

import redis
from dotenv import load_dotenv

load_dotenv()

r = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    username=os.getenv("REDIS_USERNAME", "default"),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True,
)

print("PING:", r.ping())


r.set("favorite_car", "Ferrari Testarossa")
print("favorite_car:", r.get("favorite_car"))


r.set("favorite_pet", "cat", ex=2 * 60 * 60)
print("favorite_pet:", r.get("favorite_pet"), "| TTL, с:", r.ttl("favorite_pet"))

r.delete("shopping_list")
r.rpush("shopping_list", "bread", "milk", "eggs", "cheese", "apples")
r.expire("shopping_list", 7 * 24 * 60 * 60)
print("shopping_list:", r.lrange("shopping_list", 0, -1))
print("shopping_list TTL, с:", r.ttl("shopping_list"))

r.delete("cake_ingredients")
r.hset("cake_ingredients", mapping={"flour": 250, "milk": 500, "eggs": 3})
print("cake_ingredients:", r.hgetall("cake_ingredients"))

r.hset("cake_ingredients", "sugar", 300)
print("+ sugar 300:", r.hgetall("cake_ingredients"))

r.hset("cake_ingredients", "sugar", 500)
print("sugar -> 500:", r.hgetall("cake_ingredients"))