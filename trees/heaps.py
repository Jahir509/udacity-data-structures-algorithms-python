'''
(Max & Min) (Binary) Heaps are the same (in concept) as binary trees and implemented
using a single array. Heaps are specific binary trees as they have two rules:
(1) The (Min & Max) heap has a specific order based on its goal (see below)
(2) The heap has its levels filled from left to right (i.e. "complete tree")

Applications of Heaps:
Max Binary Heap: find minimum k elements by replacing largest element with smaller element
Min Binary Heap: find maximum k elements by replacing smallest element with larger element

Heap Time & Space Complexity Analysis:
Search: Best Case: O(1) -> Root Value, Worst Case: O(n) -> random order
Insert: O(logn) -> based on height of heap
Remove (Root): O(logn) -> based on height of heap
Create: O(n) -> Check each node in heap
'''

class MinBinaryHeap:
    def __init__(self):
        self.list = [0] #Heap root will begin at index 1 for easy integer division
        self.size = 0

    def insert(self, element):
        self.list.append(element)
        self.size += 1
        #replace parent with element if element is smaller than parent
        self.up(self.size)

    def up(self, pos):
        while pos//2 > 0:
            if self.list[pos] < self.list[pos//2]:
                self.list[pos],self.list[pos//2] = self.list[pos//2],self.list[pos]
            pos = pos//2

    def findMin(self):
        return self.list[1]

    def removeMin(self):
        minval = self.list[1]
        self.list[1],self.list[self.size] = self.list[self.size],self.list[1]
        self.list.pop()
        self.size -= 1
        self.down(1)
        return minval

    def down(self, pos):
        while pos*2 <= self.size:
            mc = self.minChild(pos)
            if self.list[pos] > self.list[mc]:
                self.list[pos],self.list[mc] = self.list[mc],self.list[pos]
            pos = mc

    def minChild(self, pos):
        if pos*2 + 1 > self.size:
            return pos*2
        else:
            if self.list[pos*2] < self.list[pos*2 + 1]:
                return pos*2
            else:
                return pos*2 + 1

    def create(self, array):
        pos = len(array)//2
        self.size = len(array)
        self.list = [0] + array
        while pos > 0:
            self.down(pos)
            pos -= 1
