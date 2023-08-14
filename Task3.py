def create_list():
    n = int(input("Enter the number of elements: "))
    my_list = []

    for i in range(n):
        num = int(input("Enter a number: "))
        my_list.append(num)

    print("---> The list is:", my_list)
    return my_list


def check_order(my_list):
    if my_list == sorted(my_list, reverse=False):
        print("---> The list is sorted in ascending order.")
    elif my_list == sorted(my_list, reverse=True):
        print("---> The list is sorted in descending order.") 
    else:
        print("---> The list is not sorted in any order.")


print ("--- Welcome to the *List Sorter* tool ---")
print("To use this program, please follow these steps:")
print("--> Enter the number of elements you want to add to your list when prompted.")
print("--> Enter each element of your list when prompted.")
print("--> The program will create a list based on your inputs")
print("--> The program will then check if the list is sorted in ascending or descending order.")

while True:
        start_exit = input("Enter 's' to start or 'e' to exit: ")
        if start_exit == "s":
            my_list = create_list()
            check_order(my_list) 
        elif start_exit == "e":
            break
        else:
            print("Invalid input! Please enter 's' to start or 'e' to exit")
            print()

