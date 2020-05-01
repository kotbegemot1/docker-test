import json
from functools import lru_cache

class JsonSerde(object):
    def serialize(self, key, value):
        if isinstance(value, str):
            return value, 1
        return json.dumps(value), 2

    def deserialize(self, key, value, flags):
       if flags == 1:
           return value.decode("utf-8")
       if flags == 2:
           return json.loads(value.decode("utf-8"))
       raise Exception("Unknown serialization format")

# @lru_cache(maxsize=None)
def fib(n):
  if n < 2:
    return n
  else:
    return fib(n-1) + fib(n-2)