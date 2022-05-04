from random import random
from Stack import Stack

stack = Stack()

for x in range(21):
    stack.push(x)

print(stack.getStackAsList())
