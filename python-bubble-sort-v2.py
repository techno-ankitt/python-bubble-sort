#-----ADVANCED BUBBLE SORT PROGRAM-----
def bubble_sort(arr):
   
    n = len(arr)
    for i in range(n):
        issorted = True
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]: #comparison 
                
                arr[j], arr[j+1] = arr[j+1], arr[j] # swapping if (j > j+1)
                issorted = False
        
        # If the aarry is already Sorted then 'break'
        if issorted:
            break
    return arr

def main():
    print("--- Bubble Sort Program ---")
    user_input = input("Enter numbers (separated by space or comma): ")
    
    try:
        # for Handling both commas and spaces
        clean_input = user_input.replace(',', ' ')
        arr = [int(x) for x in clean_input.split()] # String ko int me convert krne ke
        
        print('-'*45)
        print(f"Original Array: {arr}")
        sorted_arr = bubble_sort(arr)
        print('-'*45)
        print(f"Sorted Array:   {sorted_arr}")
        print('-'*45)
        print("\nTime Complexity: O(n^2) ")
        
    except ValueError:
        print("Invalid input! Please enter only numbers.")

if __name__ == "__main__": # ye main function hi to mera sbse bda khel hai
    main()
