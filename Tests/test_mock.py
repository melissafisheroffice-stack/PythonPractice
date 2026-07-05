from unittest.mock import Mock

def greeting():

person = Mock()
person.name = "Alice"
greeting = "Hello"

print(greeting + person.name)