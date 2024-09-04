# Singly linked list
# Node class is the core structure (single node) required for a linked list.

class Node:
  def __init__(self, data=None, next=None):
      self.data = data
      self.next = next

# The class below is made to make it easier to create a linked list structure along with some other methods
class LinkedList:
  def __init__(self):
      self.head = None

  def print(self):
      if self.head is None:
          print("Linked list is empty")
          return
      itr = self.head
      llstr = ''
      while itr:
          llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
          itr = itr.next
      print(llstr)

  def get_length(self):
      count = 0
      itr = self.head
      while itr:
          count+=1
          itr = itr.next

      return count

  def insert_at_begining(self, data):
      node = Node(data, self.head)
      self.head = node

  def insert_at_end(self, data):
      if self.head is None:
          self.head = Node(data, None)
          return

      itr = self.head

      while itr.next:
          itr = itr.next

      itr.next = Node(data, None)

  def insert_at(self, index, data):
      if index<0 or index>self.get_length():
          raise Exception("Invalid Index")

      if index==0:
          self.insert_at_begining(data)
          return

      count = 0
      itr = self.head
      while itr:
          if count == index - 1:
              node = Node(data, itr.next)
              itr.next = node
              break

          itr = itr.next
          count += 1

  def remove_at(self, index):
      if index<0 or index>=self.get_length():
          raise Exception("Invalid Index")

      if index==0:
          self.head = self.head.next
          return

      count = 0
      itr = self.head
      while itr:
          if count == index - 1:
              itr.next = itr.next.next
              break

          itr = itr.next
          count+=1

  def insert_values(self, data_list):
      self.head = None
      for data in data_list:
          self.insert_at_end(data)
  
  # Reverse a LL via  iterative approach using two pointers (Iterative)
  # TC: O(n), MC O(1)
  def reverseListIter(self) -> Node:
    prev, curr = None, self.head
    
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    self.head = prev
  
  # cycle detection (Floyd's Tortoise and Hare algorithm)
  # TC: O(n), MC O(1)
  def hasCycle(self):
    slow, fast = self.head, self.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
        
    return False


# Doubly linked list
# Done slighly different to how I did singly LL node (this is G4G implementation)
class DoublyNode:
  def __init__(self, data=None):
      self.data = data
      self.prev = None
      self.next = None

'''
if __name__ == '__main__':
    ll = LinkedList() 
    ll.insert_values([1, 2, 3, 4, 5])
    # Testing reverse function:
    ll.reverseListIter() # Reversing 
    ll.print()
'''
ll = LinkedList() 
ll.insert_values([1, 2, 3, 4, 5])
# Testing reverse function:
ll.reverseListIter() # Reversing 
ll.print()
