import Element

class linkedList_Class():
    def __init__(self):
        self.first = None;

    def addFirst(self, element):
        element.next = self.first
        self.first = element
        test = 120


    def removeFirst(self):
        self.first = self.first.next

    def count(self):
        count = 0
        temp = self.first
        while (temp):
            count += 1
            temp = temp.next

        return (count)

    def print(self):
        print("Elementer i den enkeltkædede Liste !!!")
        temp = self.first
        while (temp):
            print(temp.data)
            temp = temp.next

    def sort(self):
        dataToTestAgainst = self.first
       
        while dataToTestAgainst:
            if dataToTestAgainst == self.first:
                nodeBefore = None

            minValue = dataToTestAgainst.data
            minValueOriginal = minValue
            dataToTest = dataToTestAgainst

            while dataToTest.next != None:
                if dataToTest.next.data < minValue:
                    minValue = dataToTest.next.data
                    placeholderBeforeMin = dataToTest
                    minData = dataToTest.next
                    placeholderAfterMin = dataToTest.next.next

                dataToTest = dataToTest.next

            if minValue != minValueOriginal:
                if nodeBefore == None:
                    # Vi tester på første element i den kædede liste
                    placeholderTop = self.first
                    self.first = minData
                    minData.next = placeholderTop
                    placeholderBeforeMin.next = placeholderAfterMin

                else:
                    placeholderTop = nodeBefore
                    minData.next = placeholderTop.next
                    placeholderTop.next = minData
                    placeholderBeforeMin.next = placeholderAfterMin

                nodeBefore = minData
                dataToTestAgainst = minData.next
            else:
                nodeBefore = dataToTestAgainst
                dataToTestAgainst = dataToTestAgainst.next

