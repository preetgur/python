# function caching : save input and output of fxn when call again then use this cach function
import time
from functools import lru_cache

@lru_cache(maxsize = 3)   # save lastest 3 value of different inputs
def some_work(n):
    # some task taking n seconds
    time.sleep(n)
    return n

if __name__ == "__main__":
    some_work(3)    # store first value
    print("done")
    some_work(5)    # store second value
    print("done2") 
    some_work(3)     # same value
    print(".... Cache.. value , Skip")
    some_work(6)     # store third value
    print("done3")
    some_work(5)     # same value
    print(".... Cache.. value , Skip")

    some_work(4)
    print("Already used ")
    some_work(4)
    print("Delay because max-size is 3 : and we use different input")
