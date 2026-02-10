class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def main():
    obj = Queue()

    # preload queue with list values
    lst = [1, 2, 3, 4]
    for i in lst:
        obj.enqueue(i)

    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Is Empty")

    c = int(input("Enter your choice: "))

    if c == 1:
        val = int(input("Enter value to enqueue: "))
        obj.enqueue(val)
        print("Queue:", obj.items)

    elif c == 2:
        print("Dequeued value:", obj.dequeue())
        print("Queue:", obj.items)

    elif c == 3:
        print("Is queue empty?", obj.isEmpty())

    else:
        print("Invalid choice")


main()
