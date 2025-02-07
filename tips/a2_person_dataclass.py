import uuid
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    id: int

    @staticmethod
    def generate_id() -> int:
        return uuid.uuid4().int


@dataclass(frozen=True)
class FrozenPerson:
    name: str
    id: int


if __name__ == "__main__":
    bob = Person("bob", Person.generate_id())
    bob2 = Person("bob", Person.generate_id())

    print(bob, bob2)
    print([bob, bob2])

    frozen_bob = FrozenPerson("bob", 5)

    bob.name = "not bob"
    print(f"\n{bob.name=}")

    frozen_bob.name = "not bob"
