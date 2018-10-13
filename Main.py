import Element
import LinkedList

if __name__ == '__main__':
    # Nu oprettes en tom Liste.
    myLinkedList = LinkedList.linkedList_Class()

    node0 = Element.element_Class(8)
    myLinkedList.addFirst(node0)
    myLinkedList.print()

    node1 = Element.element_Class(1)
    myLinkedList.addFirst(node1)
    myLinkedList.print()

    node2 = Element.element_Class(2)
    myLinkedList.addFirst(node2)
    myLinkedList.print()

    node4 = Element.element_Class(4)
    myLinkedList.addFirst(node4)
    myLinkedList.print()

    node3 = Element.element_Class(3)
    myLinkedList.addFirst(node3)
    myLinkedList.print()

    node5 = Element.element_Class(23)
    myLinkedList.addFirst(node5)
    myLinkedList.print()

    print("Antal elementer i listen er : " + str(myLinkedList.count()))

    #myLinkedList.removeFirst()
    #myLinkedList.print()
    #print("Antal elementer i listen er : " + str(myLinkedList.count()))
    print("")
    print("Før Sortering :")
    myLinkedList.print()

    myLinkedList.sort()
    print("")
    print("Efter Sortering :")
    myLinkedList.print()

