#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

from exercise import replay

cache = Cache()

cache.store("foo")
cache.store("bar")
cache.store(42)

replay(cache.store)

# >>> cache = Cache()
# >>> cache.store("foo")
# >>> cache.store("bar")
# >>> cache.store(42)
# >>> replay(cache.store)
# Cache.store was called 3 times:
# Cache.store(*('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f
# Cache.store(*('bar',)) -> dcddd00c-4219-4dd7-8877-66afbe8e7df8
# Cache.store(*(42,)) -> 5e752f2b-ecd8-4925-a3ce-e2efdee08d20
