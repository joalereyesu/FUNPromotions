from Stack import Stack
from Queue import Queue
import pytest

stack = Stack()
queue = Queue()

testVal = 45

for x in range(21):
    stack.push(x)
    queue.enqueue(x)


def test_Push():
    stack.push(testVal)
    assert stack.peek() == 45


def test_Pop():
    stack.push(testVal)
    stack.pop()
    assert stack.peek() == testVal


def test_Peek():
    stack.push(testVal)
    topVal = stack.peek()
    assert testVal == topVal


def test_Enqueue():
    queue.enqueue(testVal)
    assert queue.show()[0] == testVal


def test_Dequeue():
    queue.dequeue()
    assert queue.show()[-1] == 1
