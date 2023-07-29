#Difference between binary search and normal search(iterating) will be shown by this python program
import time
def normal_search(L,element):
    for i in range(len(L)):
        if L[i] == element:
            return (f"Element {element} found ")




def binary_search(L,element,low=None,high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(L)-1
    if high < low:
        return ("Element not found")

    mid = (low +high) //2

    if L[mid] == element:
        return (f"Element {element} found")
    elif element < L[mid]:
        binary_search(L,element,low,mid-1)
    else:
        binary_search(L,element,mid+1,high)

if __name__=='__main__':
    #L[1,2,3,4,5,10,15,17]
    #element = 3
    #normal_search(L,element)
    #binary_search(L,element)
    check_list =[]
    for i in range(10000):
        check_list.append(i)

    start = time.time()
    for i in check_list:
        normal_search(check_list,i)
    end = time.time()
    print("Time taken: ",(end-start),"seconds")

    start = time.time()
    for i in check_list:
        normal_search(check_list, i)
    end = time.time()
    print("Time taken: ", (end - start), "seconds")

