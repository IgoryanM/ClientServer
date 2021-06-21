import inspect
import datetime


def log(func):
    def decorated_func(*args, **kwargs):
        func(*args, **kwargs)
        with open('log.log', 'a') as f:
            f.write(
                f'{datetime.datetime.now().replace(microsecond=0)} - Функция func_z() вызвана из функции {inspect.getframeinfo(inspect.currentframe().f_back)[2]}()\n')

    return decorated_func


@log
def func_z():
    pass


def main():
    func_z()


if __name__ == '__main__':
    main()
