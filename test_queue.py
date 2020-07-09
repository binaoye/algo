

class Queue(object):
    def __init__(self):
        self.stacka = []
        self.stackb = []
        # self.queue = []

    def inqueue(self, node):
        if node:
            if self.stacka is None:
                self.stacka.append(node)
            else:
                while self.stacka:
                    x = self.stacka.pop()
                    self.stackb.append(x)
                self.stacka.append(node)
                while self.stackb:
                    y = self.stackb.pop()
                    self.stacka.append(y)
        print('after inqueue', self.stacka)

    def outqueue(self):
        if self.stacka:
            x = self.stacka.pop()
            return x
        else:
            return None

if __name__ == "__main__":
    a = Queue()
    a.inqueue(1)
    a.inqueue(2)
    a.inqueue(3)
    a.inqueue(4)
    print(a.outqueue())
    print(a.outqueue())

    b = []
    b.append(1)
    b.append(2)
    b.append(4)
    print(b)
    print(b.pop())