from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


def have_birthday(person: Person = Person("John Doe", -1)):
    person.age = person.age + 1
    return person


def calculate_age_after_birthday(person: Person = None):
    if not person:
        person = Person("John Doe", -1)

    person.age = person.age + 1
    return person


if __name__ == "__main__":
    # reasons to NEVER use mutable values for default args
    # especially if the mutable value escapes function scope

    bob = Person("Bob", 26)
    print(f"{bob=}")
    print(f"{have_birthday(bob)=}")
    print(f"{bob=}\n")

    unnamed = have_birthday()
    print(f"{unnamed=}")
    unnamed.name = "Harry"
    print(f"{unnamed=}")

    unnamed2 = have_birthday()
    print(f"{unnamed2=}")
    print(f"{unnamed=}")
