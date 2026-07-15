from datetime import datetime
from functools import wraps


def log(filename=None):
    """
    Декоратор для логирования выполнения функций.
    """

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            params = ", ".join(map(str, args))
            if kwargs:
                params += ", " + ", ".join(f"{k}={v}" for k, v in kwargs.items())
            time_start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                time_end = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                msg = f"Время начала:{time_start} время окончания:{time_end} имя функции:{func.__name__} результат: {result}"

            except Exception as e:

                msg = f"Время начала:{time_start} ошибка: {type(e).__name__} имя функции:{func.__name__} параметры: {params}"
                raise
            finally:
                if filename:
                    with open(filename, "a") as f:
                        f.write(msg + "\n")

                else:
                    print(msg)

            return result

        return inner

    return wrapper
