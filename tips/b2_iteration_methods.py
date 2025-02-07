if __name__ == "__main__":
    a = [4, 2, 6, 8]
    print(f"{a=}")

    # try to avoid indexing into a list manually if you don't need to
    for i in range(len(a)):
        print(a[i], end=", ")
    print()

    # far better
    for i in a:
        print(i, end=", ")
    print("\n")

    # but maybe you need both values
    for i in range(len(a)):
        v = a[i]
        print(f"{i=}, {v=}")
    # if you find yourself assigning a variable at the start of a for loop,
    # there's probably a better way to do it
    print()

    # in this case, enumerate handles it
    for i, v in enumerate(a):
        print(f"{(i, v)=}")
    print()

    #
    # but maybe you want to iterate over two lists at the same time
    l1 = [6, 7, 2, 3]
    l2 = [2, 8, 3]
    for i in range(min(len(l1), len(l2))):
        v1, v2 = l1[i], l2[i]  # notice the variable assignment
        print(f"{v1=}, {v2=}")
    print()

    # use zip instead, no variable assignment in for loop
    for pairs in zip(l1, l2):
        print(f"{pairs=}")
    print()

    # another use of it, do something with each pair of adjacent elements
    for v1, v2 in zip(a, a[1:]):
        print(f"{(v1, v2)=}", end=", ")
    print()

    #
    # buildBuiing up a list in a for loop can often be overly verbose
    in_list = [5, 2, 3, 8]
    out_list = []
    for v in in_list:
        if v % 2 == 0:
            out_list.append(v + 2)
    # consider list comprehensions for simple transformations
    out_list = [v + 2 for v in in_list if v % 2 == 0]
    # if memory is a concern, consider a generator instead
    out_generator = (v + 2 for v in in_list if v % 2 == 0)
    # generators are iterable like a list but values are calculated lazily.

    # maybe a more representative example
    headers = [("Accept", "application/json"), ("key", "sd1239sn3")]
    header_names = [name.lower() for name, _ in headers]

    # recommend looking through itertools to get an idea of what is available
    # https://docs.python.org/3/library/itertools.html
    # there are a load of niche iterables in it, like product and chain.
