import math
import os


def pause(massage='press any key to continue'):  # this function will pause the script with a default massage or a custome one.
    print(massage)
    os.system('pause >NULL')  # this will pause untill any key is pressed.
    return 0

class Node():
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()

    def update(self, value):
        self.value = value


class LinkedList():
    def __init__(self, root=None):
        self.head = root
        self.size = 0
        self.tail = root #if u realised queue or stack

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is not None:
            cur = self.current
            self.current = self.current.next
            return cur
        raise StopIteration

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value, end=' ')
            current = current.next
        print('')

    def __len__(self):
        return self.size

    def add_to_tail(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self.size += 1
        self.sorted()

#   FUNCTION FOR STACK
    def add_stack(self, value):
        node = Node(value)
        if self.tail is None:
            self.tail = node
            self.tail.previous = None
        else:
            current = self.tail
            node.previous = current
            self.tail = node
        self.size += 1


    def pop_stack(self):
        current = self.tail
        if current is None:
            return 'There is nothing to delete'
        else:
            self.tail = current.previous
            tmp = current.value
            current = None
            self.size -= 1
            return tmp

    def print_stack(self):
        current = self.tail
        while current is not None:
            print(self.pop_stack(), end=' ')
            current = self.tail
        print('')
#   FUNCTION FOR STACK


#   FUNCTION FOR QUEUE
    def add_queue(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.head.next = None
        else:
            current = self.tail
            current.next = node
            self.tail = node
        self.size += 1

    def pop_queue(self):
        current = self.head
        if current is None:
            print('There is nothing to delete')
        else:
            tmp = current.value
            tmp2 = current.next
            current = None
            self.head = tmp2
        self.size -= 1
        return tmp

    def print_queue(self):
        current = self.head
        while self.size > 0:
            print(self.pop_queue(),  end=' ')
            current = self.head
        print('')
#   FUNCTION FOR QUEUE


    def add_to_head(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            current_next = self.head.next
            self.head = node
            self.head.next = current
            self.head.next.next = current_next
        self.size += 1
        self.sorted()

    def is_empty(self):
        return self.size == 0

    def pop(self):
        current = self.head
        if current is None:
            print('There is nothing to delete')
        else:
            while current.next is not None:
                current = current.next
            tmp = current.value
            current = None
        return tmp

    def copy(self):
        copy_list = LinkedList()

        if self.is_empty == True:
            print('No elem in list')
        else:
            current = self.head
            while current is not None:
                copy_list.add_to_tail(current.value)
                current = current.next
        return copy_list

    def sorted(self):
        if self.is_empty == True:
            print('No elem in list')
        else:
            for ind in range(0, self.size - 1):
                current = self.head
                current_previous = self.head
                for ind2 in range(0, self.size - ind - 1):
                    if current.value > current.next.value:
                        tmp = current
                        tmp_next = current.next.next
                        if tmp == self.head:
                            self.head = current.next
                            self.head.next = tmp
                            self.head.next.next = tmp_next
                            current_previous = self.head
                            current = self.head.next

                        elif tmp != self.head:
                            current = current.next
                            current_previous.next = current
                            current.next = tmp
                            current.next.next = tmp_next
                            current_previous = current
                            current = current.next
                    # end of 'if'
                    ind2 += 1
                # end of 'while'
                ind += 1
        return self

    def reversed(self):
        reversed_list = self.copy()

        if reversed_list.is_empty == True:
            print('No elem in list')
        else:
            for ind in range(0, reversed_list.size - 1):
                current = reversed_list.head
                current_previous = reversed_list.head
                for ind2 in range(0, reversed_list.size - ind - 1):
                    tmp = current
                    tmp_next = current.next.next
                    if tmp == reversed_list.head:
                        reversed_list.head = current.next
                        reversed_list.head.next = tmp
                        reversed_list.head.next.next = tmp_next
                        current_previous = reversed_list.head
                        current = reversed_list.head.next

                    elif tmp != reversed_list.head:
                        current = current.next
                        current_previous.next = current
                        current.next = tmp
                        current.next.next = tmp_next
                        current_previous = current
                        current = current.next
                    ind2 += 1
                # end of 'for(in)'
                ind += 1

        return reversed_list

    def is_palindrome(self):
        palindrome_list = []
        current = self.head
        while current is not None:
            palindrome_list.append(current.value)
            current = current.next
        size = len(palindrome_list)
        for ind in range(0, math.ceil(size / 2)):
            if palindrome_list[ind] != palindrome_list[size - 1 - ind]:
                return False
        return True

    @staticmethod
    def middle(start, last):
        if start == None:
            return None
        slow = start
        fast = start.next
        while fast != last:
            fast = fast.next
            if fast != last:
                slow = slow.next
                fast = fast.next
        return slow

    def binarySearch(self, value):
        start = self.head
        last = None
        while True:
            mid = self.middle(start, last)
            if mid == None:
                return None
            if mid.value == value:
                return mid

            elif mid.value < value:
                start = mid.next
            else:
                last = mid
            if not (last == None or last != start):
                break
        # value not present
        return None


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add_to_tail(1)
    linked_list.add_to_tail(2)
    linked_list.add_to_head(5)
    linked_list.add_to_head(10)
    print('Iteration')
    for node in linked_list:
        print(node)

    assert len(linked_list) == 4
    assert linked_list.is_empty() == False
    # print(linked_list.pop())
    # s = input('f')
    assert linked_list.pop() == 10
    list_copy = linked_list.copy()
    list_copy.add_to_tail(12)
    list_copy.print_list()
    assert len(list_copy) != len(linked_list)
    sorted_copy = linked_list.sorted()
    print('Print sorted list')
    sorted_copy.print_list()
    assert sorted_copy.head.value == 1
    assert linked_list.is_palindrome() == False
    reversed_copy = linked_list.reversed()
    print('Print reversed list')
    reversed_copy.print_list()
    assert reversed_copy.head.value == 10
    print('all is good\n')
    print('Queue:')

    Queue = LinkedList()
    Queue.add_queue(1)
    Queue.add_queue(2)
    Queue.add_queue(5)
    Queue.add_queue(10)
    Queue.add_queue(11)
    Queue.add_queue(15)
    Queue.pop_queue()
    Queue.print_queue()


    print('\n\nStack:')
    Stack = LinkedList()
    Stack.add_stack(1)
    Stack.add_stack(2)
    Stack.add_stack(5)
    Stack.add_stack(10)
    Stack.add_stack(11)
    Stack.add_stack(15)
    Stack.pop_stack()
    Stack.print_stack()
    print('all is good')

