# Merge Sort 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    print(mid)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer (Merge)
    a = merge(left, right)
    print(a)
    return a 

def merge(left, right):
    result = []
    i = j = 0
    
    # Compare and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Example
print(merge_sort([-5,3,2,1,-3,-3,7,2,2]))
