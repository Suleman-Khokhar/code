# # class BinHeap:
# #     def __init__(self):
# #         self.heap_list = []
        

# Lists = [10,9,1000]

# for i in range(len(Lists)):
#         li = 2*i+1
#         ri = 2*i+2
#         temp = Lists[i]
#         if li <= len(Lists)-1:
#             if temp < Lists[li ]:
#                 Lists[i],Lists[2*i+1] = Lists[li],temp
    
#         elif li <= len(Lists)-1 and ri <= len(Lists)-1:
        
#             if temp > Lists[li] and temp > Lists[ri] :
#                 continue
#             elif temp > Lists[li ] and temp < Lists[ri]:
#                 Lists[i],Lists[2*i+2] = Lists[ri],temp
#             elif temp < Lists[li ] and temp > Lists[ri]:
#                 Lists[i],Lists[2*i+1] = Lists[li],temp
#         else:
#             continue
     

# print(Lists)
        
            
##################################
def heapify(arr, n, i):
    largest = i
    li = 2 * i + 1
    ri = 2 * i + 2

    if li < n and arr[li] > arr[largest]:
        largest = li
    if ri < n and arr[ri] > arr[largest]:
        largest = ri

    # If root is not largest, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

Lists = [10, 9, 1000]
build_max_heap(Lists)
print(Lists)

                        
        