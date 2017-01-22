#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def __iter__(self):
        """Iterate through the linked list"""
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    # Theta(n)
    def as_list(self):
        """Return a list of all items in this linked list"""
        result = []
        go = True
        current = None
        if self.head is None:
            return []
        else:
            current = self.head
        while go:
            result.append(current.data)
            if current is self.tail or current.next is None:
                go = False
            else:
                current = current.next
        return result

    # Theta(1)
    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None


    # O(n)
    # Omega(1)
    # Theta(n)
    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        if self.head == self.tail and self.head is not None:
            return 1
        elif self.is_empty():
            return 0
        finished = False
        count = 1
        current_node = self.head
        while not finished:
            if current_node is not self.tail and current_node.next is not None:
                count += 1
                current_node = current_node.next
            else:
                finished = True
        return count
        pass

    # O(1)
    # Omega(1)
    # Theta(1)
    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        # append given item
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            old_tail = self.tail
            old_tail.next = new_node
            self.tail = new_node
        pass

    # O(1)
    # Omega(1)
    # Theta(1)
    def prepend(self, item):
        # prepend given item
        """Insert the given item at the head of this linked list"""
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        pass



    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        if self.head is None:
            raise ValueError('Cannot Linked List is Empty')

        current = self.head

        if current.data == item:
            self.head = current.next
            if self.head is None:
                self.tail = None
            return

        while current.next is not None:
            if current.next.data == item:
                new_next = current.next.next
                if new_next is not None:
                    current.next = new_next
                else:
                    current.next = None
                    self.tail = current
                return
            current = current.next

        raise ValueError('Delete item failed')

    # O()
    # Omega(1)
    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # find item where quality(item) is True
        current = self.head
        while current is not None:
            if quality(current.data) is True:
                return current.data
            current = current.next
        return None
        pass

    def findNode(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # find item where quality(item) is True

        finished = False
        current_node = self.head

        while not finished:

            if quality(current_node):
                print("return")
                return current_node
            if current_node.next is not None:
                print("went to next")
                current_node = current_node.next
            else:
                finished = True
        return None

    def findPreviousNode(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # find item where quality(item) is True
        finished = False
        current_node = self.head
        previous_node = self.head
        while not finished:
            if quality(current_node):
                return previous_node
            if current_node is not self.tail:
                previous_node = current_node
                current_node = current_node.next
            else:
                finished = True
        return None

def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())


if __name__ == '__main__':
    test_linked_list()
