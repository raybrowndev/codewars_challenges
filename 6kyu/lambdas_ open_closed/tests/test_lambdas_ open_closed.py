from lib.lambdas_open_closed import greet, spoken, shouted, whispered


def test1():
    assert greet(spoken, "Hello") == "Hello."

def test2():
    assert greet(shouted, "Hello") == "HELLO!"

def test3():
    assert greet(whispered, "Hello") == "hello."
