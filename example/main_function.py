from example.utils.util_functions import *


def main() -> None:
    """
    probably don't have your main function in a different file in a real example,
    or at least don't have a random extra top level file.
    """
    print("main function called")
    a = double_sum(1, 2, 3)
    print(a)


if __name__ == "__main__":
    main()
