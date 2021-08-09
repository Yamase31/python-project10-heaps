"""
File: linkedHeap.py
Names: Laurie Jones, Harry Pinkerton, James Lawson
Project: 10
"""


from p10utils.abstractHeap import AbstractHeap
from p10utils.bstNode import BSTNode
import math


class LinkedHeap(AbstractHeap):
   """A link-based implementation of a heap."""
   
   def __init__(self, sourceCollection = None):
      """Initialization of a heap."""
      self._heap = None
      super().__init__(sourceCollection)

   
   def add(self, item):
      """Adds item to the end of the array and then walks it up to the top,
         stopping when parent is less than the new item"""
      self._size += 1
      path = self._findPathToLastNode()
      parentPointer = self._heap
      
      if len(path) == 0:
         self._heap = BSTNode(item)
      else:
         for i in path[:-1]:
            if i == "left":
               parentPointer = parentPointer.left
            else:
               parentPointer = parentPointer.right
         if path[-1] == "left":
            parentPointer.left = BSTNode(item, None, None, parentPointer)
            self._walkUp(parentPointer.left)
         else:
            parentPointer.right = BSTNode(item, None, None, parentPointer)
            self._walkUp(parentPointer.right)
      
   def pop(self):
      """Swaps the top element with the last element, then walks the top
         element down until both children are larger than the current node."""
      if self.isEmpty():
         raise KeyError("The heap is empty.")

##      path[0] = path[-1]
##      
##      while path[0] > pointer.left and pointer.right:
##         path[0] = path[-1]

      path = self._findPathToLastNode()
      pointer = self._heap

      if len(path) == 0:
         removedNode = self._heap
         self._heap = None

      else:
         for i in path[:-1]:
            if i == "left":
               pointer = pointer.left
            else:
               pointer = pointer.right
         if path[-1] == "left":
            removedNode = pointer.left
            removedNode.data, self._heap.data = self._heap.data, removedNode.data
            pointer.left = None
         else:
            removedNode = pointer.right
            removedNode.data, self._heap.data = self._heap.data, removedNode.data
            pointer.right = None

         self._walkDown(self._heap)
      self._size -= 1

      return removedNode.data
     
   def _walkUp(self, node):
      """Walks node's data upwards through its parents while
         it is smaller than the parent."""
      newNode = node
      newParent = node.parent
      
      while newParent and newParent.data > newNode.data:
         newParent.data, newNode.data = newNode.data, newParent.data

         newNode = node
         newParent = node.parent
   
   def _walkDown(self, node):
      """Walks node's data upwards through its children while
         it is larger than a child."""
      newNode = node

      while newNode.left:
         minChild = newNode.left
         if newNode.right and newNode.right.data < newNode.left.data:
            minChild = newNode.right

         if minChild.data > newNode.data:
            break

         minChild.data, newNode.data = newNode.data, minChild.data
         newNode = minChild
   

   def _findPathToLastNode(self):
      """Uses binary representation of the number of nodes you would
         store in a complete tree to calculate the path to the last
         node in that tree."""
      
      n = len(self)
      path = []
      
      # Calculate the total number of bits
      numBits = math.floor(math.log(n, 2)) + 1
      
      # Extract bits, except for the leftmost bit
      for bit in range(numBits - 2, -1, -1):
         if (n >> bit) % 2 == 0:
            path.append("left")
         else:
            path.append("right")
      
   
      # Return list of directions
      return path


   
   def _getRoot(self):
      """Should return the way to access the root based on an implementation."""
      return self._heap
   
   def _getParent(self, pointer):
      """Returns access to the parent from the index or node."""
      return pointer.parent
   
   def _getLeftChild(self, pointer):
      """Returns access to the left child from the index or node."""
      return pointer.left
   
   def _getRightChild(self, pointer):      
      """Returns access to the right child from the index or node."""
      return pointer.right
   
   def _getData(self, pointer):
      """Returns the data from the index or node."""
      return pointer.data
   
   def _insideTree(self, node):
      """Returns True if the index or node is within the tree."""
      if node != None:
         return True
      else:
         return False
