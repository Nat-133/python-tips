from typing import Any


def foo(arg1: Any, arg2: Any, arg3: Any) -> None:
    print(f"{arg1=}")
    print(f"{arg2=}")
    print(f"{arg3=}")


if __name__ == "__main__":
    # tuple unpacking is a core feature of python,
    # it's basic use is fairly self explanitory, but the unpacking operator can get a bit confusing
    things = (1,2,3)
    a, b, c = things
    print(f"{a=}")
    print(f"{b=}")
    print(f"{c=}\n")

    # The unpacking uperator used to match against all unused elements in things
    head, *tail = things
    print(f"{head=}")
    print(f"{tail=}\n")

    # calling foo with explicit arguments
    foo("a","b","c")
    print()
    # unpacking the values in `things`, then using them as the arguments
    foo(*things)
    print()

    # To unpack a single value, we need to use a trailing comma to indicate we're creating a tuple
    singleton = [1]
    print(f"{singleton=}")
    # without the comma here, we would just assign the full list to `element`.
    element, = singleton
    print(f"{element=}")
    # without the comma here, no tuple would be created, `(1)` would be interpreted as a number and we'd get an exception.
    print(f"{(1,)[0]=}")
