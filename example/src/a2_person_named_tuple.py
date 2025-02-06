from collections import namedtuple
import uuid


Person = namedtuple("Person", ["name", "id"])


def create_person(name: str) -> Person:
    return Person(name=name, id=uuid.uuid4().int)


if __name__ == "__main__":
    bob = create_person("bob")
    bob2 = create_person("bob")

    print(f"{bob.name=}, {bob.id=}")
    print(f"{bob[0]=}, {bob[1]=}\n")

    print(bob, bob2)
    print([bob, bob2])
    print(f"{isinstance(bob, tuple)=}")
