import Element
import LinkedList

if __name__ == '__main__':
    # Nu oprettes en tom Liste.
    myLinkedList = LinkedList.linkedList_Class()

    node1 = Element.element_Class(1)
    myLinkedList.addFirst(node1)
    myLinkedList.print()

    node2 = Element.element_Class(2)
    myLinkedList.addFirst(node2)
    myLinkedList.print()

    node3 = Element.element_Class(3)
    myLinkedList.addFirst(node3)
    myLinkedList.print()
