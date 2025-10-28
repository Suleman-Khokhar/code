# # # #  ####### heap class 
 

# # # # class BinHeap:
# # # #     def __init__(self):
# # # #         self.heap_list = []
    
# # # #     def perculateUp(self,node = None):
# # # #         # a = [0,1,2,3,4,5,6,7,8,9.10]
# # # #         # lists = [10,4,11]
# # # #         # for i in 
        
# # # L = [10,9,1000]
        
# # # for i in range(len(L)):
# # #     li = 2*i+1
# # #     ri = 2*i+2
# # #     temp = L[i]
# # #     if temp > li and temp>ri:
# # #         continue
# # #     else:
# # #         if temp>li and temp<ri:
# # #             L[i],














     
    
# # #     # def insert(self,value):
# # #     #     pass
     
     
# # # # data = [20, 5, 15, 22, 40, 3, 8]
# # # #     print("Original:", data)

# # # #     bh = BinHeap()
# # # #     bh.buildHeap(data)
# # # #     print("Heap array (after buildHeap):", bh.heap_list)
# # # # Example test case:
# # # # data = [20, 5, 15, 22, 40, 3, 8]
# # # #     print("Original:", data)

# # # #     bh = BinHeap()
# # # #     bh.buildHeap(data)
# # # #     print("Heap array (after buildHeap):", bh.heap_list)

# # # #     bh.insert(30)
# # # #     print("Heap after insert(30):", bh.heap_list)

# # # #     max_val = bh.deleteMax()
# # # #     print("Deleted max:", max_val)
# # # #     print("Heap after deleteMax():", bh.heap_list)

# # # #     sorted_list = heap_sort(data)
# # # #     print("Heap-sorted ascending:", sorted_list)
# # class BinHeap:
# #     def _init__(self):
# #      self.heap_list = []
# #     def insert(self, value):
# #         self.heap_list.append(value)
# #         return self.percolateUp(len(self.heap_list) - 1)
# #     def percolateUp(self, index):
# #         while index>0:
# #                 parent=(index-1)//2
# #                 if self.heap_list[index]>self.heap_list[parent]:
# #                         index=parent
# #                 else:
# #                     break
# # # Example test case:
# # data = [20, 5, 15, 22, 40, 3, 8]
# # print("Original:", data)

# # bh = BinHeap()
# # # bh.buildHeap(data)
# # # print("Heap array (after buildHeap):", bh.heap_list)

# # bh.insert(20)
# # bh.insert(5)
# # bh.insert(15)
# # bh.insert(22)


# # print("Heap after insert(30):",)

# # # max_val = bh.deleteMax()
# # # print("Deleted max:", max_val)
# # # print("Heap after deleteMax():", bh.heap_list)

# # # sorted_list = heap_sort(data)
# # # print("Heap-sorted ascending:", sorted_list)

# class BinHeap:
#     def __init__(self):
#         self.heap_list = []

#     # -----------------------------
#     # Task 1: Heap Methods
#     # -----------------------------

#     def insert(self, value):
#         """Insert a value into the heap."""
#         self.heap_list.append(value)
#         self.perculateUp(len(self.heap_list) - 1)

#     def perculateUp(self, index):
#         """Move the element at index up to maintain Max Heap property."""
#         parent_index = (index - 1) // 2

#         # While not at root and child > parent
#         while index > 0 and self.heap_list[index] > self.heap_list[parent_index]:
#             # Swap
#             self.heap_list[index], self.heap_list[parent_index] = \
#                 self.heap_list[parent_index], self.heap_list[index]

#             # Move up
#             index = parent_index
#             parent_index = (index - 1) // 2

#     def deleteMax(self):
#         """Remove and return the maximum element from the heap."""
#         if len(self.heap_list) == 0:
#             return None

#         # Swap root with last element
#         max_value = self.heap_list[0]
#         last_value = self.heap_list.pop()

#         if len(self.heap_list) > 0:
#             self.heap_list[0] = last_value
#             self.perculateDown(0)

#         return max_value

#     def perculateDown(self, index):
#         """Move the element at index down to maintain Max Heap property."""
#         size = len(self.heap_list)

#         while True:
#             left = 2 * index + 1
#             right = 2 * index + 2
#             largest = index

#             # Check left child
#             if left < size and self.heap_list[left] > self.heap_list[largest]:
#                 largest = left

#             # Check right child
#             if right < size and self.heap_list[right] > self.heap_list[largest]:
#                 largest = right

#             # If largest is still index, heap is fine
#             if largest == index:
#                 break

#             # Swap and continue
#             self.heap_list[index], self.heap_list[largest] = \
#                 self.heap_list[largest], self.heap_list[index]
#             index = largest

#     def buildHeap(self, values):
#         """Build a heap from a list of values."""
#         self.heap_list = values[:]
#         n = len(self.heap_list)

#         # Start from last non-leaf node and move upward
#         for i in range((n // 2) - 1, -1, -1):
#             self.perculateDown(i)

#     # -----------------------------
#     # Task 2: Heap Sort
#     # -----------------------------
#     def heapSort(self, values):
#         """Return a sorted list in ascending order using heap sort."""
#         # Step 1: Build a Max Heap
#         self.buildHeap(values)

#         sorted_list = []
#         # Step 2: Repeatedly delete max to get sorted order
#         for _ in range(len(values)):
#             sorted_list.insert(0, self.deleteMax())  # insert at start for ascending order

#         return sorted_list
# # Create heap
# heap = BinHeap()

# # Insert values
# for val in [10, 4, 7, 15, 2]:
#     heap.insert(val)

# print("Heap:", heap.heap_list)
# print("Deleted max:", heap.deleteMax())
# print("Heap after delete:", heap.heap_list)

# # Build heap directly
# heap.buildHeap([3, 9, 2, 1, 4, 5])
# print("Built heap:", heap.heap_list)

# # Heap sort
# unsorted_list = [12, 3, 19, 8, 5, 7]
# sorted_list = heap.heapSort(unsorted_list)
# print("Sorted list:", sorted_list)

class BinHeap:
    def __init__(self):
        self.heap_list = []

    def insert(self, value):
        self.heap_list.append(value)
        self.perculateUp(len(self.heap_list) - 1)

    def perculateUp(self, index):
        parent_index = (index - 1) // 2

        while index > 0 and self.heap_list[index] > self.heap_list[parent_index]:
            self.heap_list[index], self.heap_list[parent_index] = \
                self.heap_list[parent_index], self.heap_list[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def deleteMax(self):
        if not self.heap_list:
            return None

        max_value = self.heap_list[0]
        last_value = self.heap_list.pop()

        if self.heap_list:
            self.heap_list[0] = last_value
            self.perculateDown(0)

        return max_value

    def perculateDown(self, index):
        size = len(self.heap_list)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < size and self.heap_list[left] > self.heap_list[largest]:
                largest = left
            if right < size and self.heap_list[right] > self.heap_list[largest]:
                largest = right

            if largest == index:
                break

            self.heap_list[index], self.heap_list[largest] = \
                self.heap_list[largest], self.heap_list[index]
            index = largest

    def buildHeap(self, values):
        """Build a Max Heap from an existing list"""
        self.heap_list = values[:]
        n = len(self.heap_list)

        for i in range((n // 2) - 1, -1, -1):
            self.perculateDown(i)


def heap_sort(values):
    """Sort a list in ascending order using Max-Heap"""
    bh = BinHeap()
    bh.buildHeap(values)

    sorted_list = []
    while bh.heap_list:
        sorted_list.insert(0, bh.deleteMax())  
    return sorted_list



if __name__ == "__main__":
    data = [20, 5, 15, 22, 40, 3, 8]
    print("Original:", data)

    bh = BinHeap()
    bh.buildHeap(data)
    print("Heap array (after buildHeap):", bh.heap_list)

    bh.insert(30)
    print("Heap after insert(30):", bh.heap_list)

    max_val = bh.deleteMax()
    print("Deleted max:", max_val)
    print("Heap after deleteMax():", bh.heap_list)

    sorted_list = heap_sort(data)
    print("Heap-sorted ascending:", sorted_list)
