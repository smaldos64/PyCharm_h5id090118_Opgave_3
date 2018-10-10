import Element

class linkedList_Class():
    def __init__(self):
        self.first = None;

    def addFirst(self, element):
        element.next = self.first
        self.first = element

    def removeFirst(self):
        test = 2

    def count(self):
        test = 3

    def print(self):
        print("Elementer i den enkeltkædede Liste !!!")
        temp = self.first
        while (temp):
            print(temp.data)
            temp = temp.next

    def sort(self):
        test = 5
