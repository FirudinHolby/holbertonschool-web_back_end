#!/usr/bin/env python3
'''Getting web page via get_page function'''
import requests
import redis


r = redis.Redis()


def get_page(url: str) -> str:
    '''Get Page and return its content while caching its value'''
    r.incr(f"count:{url}")
    cache = r.get(url)
    if cache:
        return cache.decode("utf-8")
    resp = requests.get(url)
    r.setex(url, 10, resp.text)
    return resp.text
