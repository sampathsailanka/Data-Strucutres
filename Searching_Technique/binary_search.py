def binary_search(my_list,key):
    low = 0
    high = len(my_list)-1
    while(low <= high):
        mid = (low+high)//2
        if key == my_list[mid]:
            return mid
        elif key < my_list[mid]:
            high = mid-1
        else:
            low = mid+1            
    return -1
my_list = [1,5,8,17,18,24,35,44,69,77,80,91,116]
key = int(input("Enter the Element for search: "))
y = binary_search(my_list,key)
if( y == -1):
    print("The Element you entered is not found in the list")
else:
    print("The Element " + str(key) + " you have entered found at position: ", y+1)