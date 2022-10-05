def linear_search(my_list,key):
    for i in range(len(my_list)):
        if my_list[i] == key:
            return i
    return -1
my_list = [2,4,1,5,21,41,234,2435,221,23,667,33]
key = int(input("Enter the key Element: "))
x = linear_search(my_list,key)
if(x == -1):
    print("The Element you entered is not found in the list")
else:
    print("The Element " + str(key) + "you have entered found at position: ",x+1) 