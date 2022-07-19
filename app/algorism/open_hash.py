class Cell:
    def __init__(self, value):
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.values = [None for _ in range(size)]

    def my_hash(self, value):
        length = 0
        for c in value:
            length += ord(c)
        return length % self.size

    def find(self, target):
        hash = self.my_hash(target)
        tmp = self.values[hash]
        while tmp:
            if tmp.value == target:
                return tmp
            else:
                tmp = tmp.next
                continue
        return None

    def insert(self, value):
        try:
            if self.find(value):
                print('[*] value already exists.')
                return False
            hash = self.my_hash(value)
            tmp = self.values[hash]
            self.values[hash] = Cell(value)
            self.values[hash].next = tmp
            return True
        except:
            print("[*] Failed to insert.")
            return False

    def delete(self, value):
        hash = self.my_hash(value)
        cell = self.values[hash]
        if not cell:
            print("Data not found.")
            return False
        elif cell.value == value:
            self.values[hash] = cell.next
            print('[*] Successfully deleted.')
            return True
        next = cell.next
        while next:
            if next.value == value:
                cell = next.next
                next = None
                print('[*] Successfully deleted.')
                return True
            elif next.next:
                cell = next
                next = next.next
        print("Data not found.")
        return False
