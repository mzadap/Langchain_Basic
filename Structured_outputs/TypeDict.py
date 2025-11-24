from typing import TypedDict, Annotated

from docutils.nodes import description


class Person(TypedDict):
    name: str
    age: int
new_person: Person = {'name': "Nachiket", 'age': "Red hat"}

print(new_person)