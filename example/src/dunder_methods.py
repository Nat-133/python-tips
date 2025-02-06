

class InfiniteLoop:
    def __iter__(self):
        i: int = 0
        while True:
            yield i
            i += 1


class Indexable:
    def __getitem__(self, item: int|str) -> int:
        return item*2


if __name__ == "__main__":
    # python defines some special methods that allow you to interface with language features.
    # these take the form of 'dunder' (double underscore) methods
    # e.g. __add__, __iter__, __lt__, __str__, __repr__, etc...

    # using these allows for operator overloading
    # whether or not you agree with it as a feature, it's important to know it exists.
    # Many libraries use various dunder methods, and so you may see them in use in the wild.
    # every operation in python is effectively a method call.


    # you can see a few examples of their use below:

    max = 9

    for i in InfiniteLoop():
        print(i)
        if i >= max:
            break
    print()

    double = Indexable()
    print(f"{double[1]=}")
    print(f"{double["hello world!"]=}")
