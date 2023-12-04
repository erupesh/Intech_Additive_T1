#explanation:
#We need to add a min function to the stack that executes in O(1) time.
# One way to achieve this is by using a special stack data structure that supports all the stack operations like push(), pop(), isEmpty(), isFull() and an additional operation getMin() which should return minimum element from the SpecialStack.
# All these operations of SpecialStack will have a time and space complexity of O(1)

#one real-world use case where stack is better used than arrays is in function call implementations.
# When a function is called, the system must remember the point from which the function was called
# so that it can return to the correct point after the function has completed its execution.
# This is done by storing the return address of the function call on the stack. The stack is also used to store the local variables of the function.
class StackWithMin:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return None

        popped_value = self.stack.pop()
        if popped_value == self.min_stack[-1]:
            self.min_stack.pop()

        return popped_value

    def min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

stack = StackWithMin()
stack.push(3)
stack.push(5)
print("Current Min:", stack.min())  # Output: 3

stack.push(2)
print("Current Min:", stack.min())  # Output: 2

stack.pop()
print("Current Min:", stack.min())  # Output: 3


