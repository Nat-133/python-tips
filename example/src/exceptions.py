import timeit


def with_try_except(do_exception: bool) -> float:
    numerator = 1
    denominator = 0 if do_exception else 1
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return -1


def with_if(avoid_if_body: bool) -> float:
    numerator = 1
    denominator = 0 if avoid_if_body else 1

    if denominator != 0:
        return numerator / denominator
    return -1


if __name__ == "__main__":
    # Try/except marginally faster than checking when check unneeded, but not by a lot
    time = timeit.timeit(lambda: with_try_except(False), number=1000000)
    print(f"try/except no exception   {time=}")
    time = timeit.timeit(lambda: with_if(False), number=1000000)
    print(f"if statement avoid if     {time=}\n")

    # Try/except about 3 times slower than checking when triggered.
    time = timeit.timeit(lambda: with_try_except(True), number=1000000)
    print(f"try/except with exception {time=}")
    time = timeit.timeit(lambda: with_if(True), number=1000000)
    print(f"if statement go into if   {time=}\n")

    # because of the relatively minor performance impact, it is often idiomatic python to 'just do' something,
    # then ask for forgiveness later.
    # You should choose the one that results in more readable code, but often this is the try/except.

    try:
        print("some io operation")
        # raise IOError("could not find the thing")
        a = 5
    except IOError:
        a = 4

    print(f"{a=}")
    # you can assign values in try/except blocks, they are not a new namespace
