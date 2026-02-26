#-----BASIC BUBBLE SORT PROGRAM-----
# print('-'*45)
print("Welcome to Bubble Sort Program")
# print('-'*45)

arr = [5,1,8,2,7,4,3,6,9]
n = len(arr)


def bubbleSort(arr, n):
    for i in range(n): ## loop ek baar run huyi ek largest element last me , to agar loop (n) baar run huyi to puri arr sort
        issorted = True
        for j in range(n-i-1):   # indirectly j-1 kar rhe hai
            if arr[j] > arr[j+1]:   # ye comparison pahse hai
                arr[j],arr[j+1] = arr[j+1], arr[j]    # ye swapping pahse hai
                issorted = False
        if issorted:   # esse time complexity reduce hogi code ki
            break

bubbleSort(arr,n)
print('-'*45)
print("Sorted arr:", arr)
print('-'*45)
print("\nTime Complexity: O(n^2)")