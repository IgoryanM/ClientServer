from functools import wraps


def log(func):
    @wraps(func)
    def callf(*args, **kwargs):
        with open('func_log.log', 'a') as f:
            f.write("Вызов %s: %s, %s\n" % (func.__name__, args, kwargs))
            r = func(*args, **kwargs)
            return r

    return callf
