from functools import wraps
from time import time 

""""
from random import choice
def make_laught_at_func(person):
    def get_laught():
        laught = choice(("HAHAHA",'LOL','THEHEHE'))
        return f"{laught} {person}"

    return get_laught
laught_at =make_laught_at_func("BBBEEERRRKKKAAAYYY")

print(laught_at())
print(laught_at())
print(laught_at())
print(laught_at())
______________________________________

#2 fonksyon arasinda speeed test yapan wrapper ornegi 

def speed_test(fn):
    @wraps(fn)
    def wrapper (*args , **kwargs):
        start_time = time()
        result =fn(*args , **kwargs)
        end_time = time()
        print(f"Executing {fn.__name__}")
        print(f"Time Elepsed {end_time - start_time}")
        return  result
    return wrapper

@speed_test
def sum_gen():
    return sum(x for x in range(50000000))

@speed_test     
def sum_list():
    return sum([x for x in range(50000000)])

print(sum_gen())
print(sum_list())



#wrapper ornegi
def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args , **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed ")
        return fn(*args,**kwargs)
    return wrapper

@ensure_no_kwargs
def great(name):
    print(f"Hi there {name}")

great("berkay")




#verilen ilk argumanun ne olmasi gerektigini kontril etmemizi saglayan wrapper ornegi
def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args , **kwargs):
            if args and args[0]!=val:
                return f"Firts arg needs to be {val}"
            return fn(*args, **kwargs)
        return wrapper
    return inner

"""

