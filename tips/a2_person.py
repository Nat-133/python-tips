import uuid


def generate_id() -> int:
    """ BAD: use staticmethod or util function file instead """
    return uuid.uuid4().int


class Person:
    def __init__(self, name: str):
        self._name_history = [name]
        self._id = Person.generate_id()

    @staticmethod
    def generate_id() -> int:
        return uuid.uuid4().int

    @property
    def name(self) -> str:
        return self._name_history[-1]

    @name.setter
    def name(self, value: str) -> None:
        self._name_history.append(value)

    def __repr__(self) -> str:
        return f"Person(id: {hex(self._id)}, _name_history: {self._name_history})"

    def __str__(self) -> str:
        return f"{self.name}"


if __name__ == "__main__":
    bob = Person("bob")
    bob2 = Person("bob")
    print(bob, bob2)
    print([bob, bob2])

    print(bob.name)
