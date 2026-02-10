class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def main():
    obj = Stack()

    # preload stack with list values
    lst = [1, 2, 3, 4]
    for i in lst:
        obj.push(i)

    print("1. Push")
    print("2. Pop")
    print("3. Is Empty")

    c = int(input("Enter your choice: "))

    if c == 1:
        val = int(input("Enter value to push: "))
        obj.push(val)
        print("Stack:", obj.items)

    elif c == 2:
        print("Popped value:", obj.pop())
        print("Stack:", obj.items)

    elif c == 3:
        print("Is stack empty?", obj.isEmpty())

    else:
        print("Invalid choice")


main()
