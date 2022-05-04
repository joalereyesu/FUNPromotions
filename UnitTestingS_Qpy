from Stack import Stack
from Queue import Queue

stack = Stack()
queue = Queue()

testVal = 45

for x in range(21):
    stack.push(x)
    queue.enqueue(x)


def testPush():
    stack.push(testVal)
    if stack.peek() == 45:
        return "Test was successful!"
    else:
        return "Test failed."


def testPop():
    stack.pop()
    if stack.peek() == testVal:
        return 'Test failed.'
    else:
        return 'Test was successful!'


def testPeek():
    stack.push(testVal)
    topVal = stack.peek()
    if testVal == topVal:
        return 'Test was successful!'
    else:
        return 'Test failed.'


def testEnqueue():
    queue.enqueue(testVal)
    if (queue.show()[0] == testVal):
        return "Test was successful!"
    else:
        return "Test failed!"


def testDequeue():
    queue.dequeue()
    if (queue.show()[-1] == 1):
        return "Test was successful!"
    else:
        return "Test failed!"


print("STACK FUNCTIONS TEST")
print(stack.getStackAsList())
print(testPush())
print(testPop())
print(testPeek())

print("QUEUE FUNCTIONS TEST")
print(queue.show())
print(testEnqueue())
print(testEnqueue())
