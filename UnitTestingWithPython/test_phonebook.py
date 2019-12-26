class Phonebook:

    def __init__(self) -> None:
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]


def test_lookup_by_name():
    phonebook = Phonebook()
    phonebook.add("Bob", "1234")
    assert "1234"  == phonebook.lookup("Bob")