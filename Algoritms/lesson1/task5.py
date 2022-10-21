class Array_plates:
    def __init__(self):
        self.array = [[]]

    def pop(self):
        if len(self.array) == 0:
            return None
        else:
            lst = self.array[-1][-1]
            self.array[-1].pop(-1)
            if len(self.array[-1]) == 0:
                self.array.pop(-1)
            return lst

    def push(self, element):
        if len(self.array[-1]) < 5:
            self.array[-1].append(element)
        else:
            self.array.append([element])

    def size(self):
        if len(self.array) == 1:
            return len(self.array[0])
        else:
            return 5 * (len(self.array) - 1) + len(self.array[-1])

    def empty(self):
        return len(self.array) == 0


plates = Array_plates()
for i in range(45):
    plates.push(i)
print(plates.size())
print(plates.empty())
print('----------------------------------')
for i in range(46):
    print(plates.pop())
print('----------------------------------')
print(plates.empty())
