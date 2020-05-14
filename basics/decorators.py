""" A decorator is a function that takes an another function as an argument and
adds some kind of functionality and
returns an other function without changing
the source code of the original function"""

"""
class DecoratorClass(object):

    def __init__(self, some_function):
        self.some_function = some_function

    def __call__(self, *args, **kwargs):
        print("hello from __call__() function")
        return self.some_function(*args, **kwargs)
"""

def log_decorator(some_function):
    import logging
    logging.basicConfig(filename="{}".format(some_function.__name__), level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info("wrapper ran with *args {} and **kwargs {}".format(args, kwargs))
        some_function(*args, **kwargs)
    return wrapper

def timer_decorator(some_function):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time()
        some_function()
        t2 = time.time() - t1
        print("{} took {} to run".format(some_function.__name__, t2))
    return wrapper

def decorator_function(some_function):
    def wrapper_function(*args, **kwargs):
        print("hello from wrapper() function")
        some_function(*args, **kwargs)
    return wrapper_function # We are returning "wrapper_function" waiting to be executed

@timer_decorator # This is equivalent to "hello = decorator_function(hello)". We can use decorator class as well @DecoratorClass
def hello():
    import time
    time.sleep(1)
    print("hello from hello() function")

hello()

"""chaining decorators

    @timer_decorator
    @log_decorator
    def hello():
        import time
        time.sleep(1)
        print("hello from hello() function")

    above snippet is equivalent to below line, which will not yield desired results
    hello = timer_decorator(log_decorator(hello))


    use wraps function from functools modules
    from functools import wraps

    add something like below on top of wrapper functions
    @wraps(some_function)
"""
