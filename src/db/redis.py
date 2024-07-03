import aioredis

redis = aioredis.from_url("redis://localhost:6379/0")

async def set_cache(key: str, value: str, expire: int = 3600):
    await redis.set(key, value, ex=expire)

async def get_cache(key: str):
    return await redis.get(key)
