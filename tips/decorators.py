from collections.abc import Callable
from typing import Any


def logger[T](func: Callable[[], T]):
    def decorator() -> T:
        print(f"before {func.__name__}")
        val: T = func()
        print(f"result was {val}")
        return val

    return decorator


@logger
def foo() -> int:
    print("running")
    return 10


def generic_decorator[T1, T2, R](func: Callable[[T1, T2], R]):
    def decorator(*args: T1, **kwargs: T2) -> R:
        print(f"{func.__name__} called with {args, kwargs}")
        result: R = func(*args, **kwargs)
        print(f"result was {result}")
        return result

    return decorator


@generic_decorator
def func_with_args(first: Any, second: Any, third: Any, x: Any = 5, y: Any = 2) -> int:
    print(f"{first=}")
    print(f"{second=}")
    print(f"{third=}")
    print(f"{x=}")
    print(f"{y=}")
    return 9


if __name__ == "__main__":
    foo()
    print()
    func_with_args(1, 2, 3, y=4)
