
def bubble_sort_demo():
    # Use a list of unsorted integers
    arr = [64, 25, 12, 22, 11]
    
    print("=== Bubble Sort Demo ===")
    print("Initial unsorted list:", arr)
    print("-" * 35)
    
    n = len(arr)
    
    #  Utilize the bubble sort using nested loops

    for i in range(n):
        swapped = False
        
        # The inner loop compares adjacent pairs
      
        for j in range(0, n - i - 1):
            # Using list indexing to compare adjacent elements: arr[j] and arr[j+1]
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # Display the list at each pass of the outer loop to show progress

        print(f"Pass {i + 1}: {arr}")
        
        # Optimization: If no swaps occurred during this pass, the list is already sorted
        if not swapped:
            break

    print("-" * 35)
    
# Finally, show the sorted list
    print("Final sorted list:", arr)

if __name__ == "__main__":
    bubble_sort_demo()
