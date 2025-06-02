# Quick Sort
# Time: O(n log n) (Average Case , Technically Worst Case is O(n^ 2)) 
# Space: O(n) 


c = [-3 , 3 ,2 , 1 , -5, -3 , 7 , 2, 2 ]


def quick_sort(arr):
    if len(arr) <= 1 : 
        return arr 
    
    p =  arr[-1]
    l = [ x for x in arr[:-1] if x <= p ]
    r = [ y for y in  arr[:-1]  if y > p ]
    L = quick_sort(l)
    R = quick_sort(r)

    return L + [p] + R 

print(quick_sort(c)) 