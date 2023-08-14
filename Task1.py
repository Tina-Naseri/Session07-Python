def multiplication_table(rows, columns):
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            print(i*j, end="\t")
        print()


print("--- Welcome to the *Multiplication Table Generator* tool ---")
print("To use this program, please follow these steps:")
print("--> Enter the number of rows for your multiplication table when prompted.")
print("--> Enter the number of columns for your multiplication table when prompted.")
print("--> The program will generate a multiplication table based on your inputs.")

while True:
        start_exit = input("Enter 's' to start or 'e' to exit: ")
        if start_exit == "s":
            rows = int(input("The number of rows: "))
            columns = int(input("The number of columns: "))
            multiplication_table(rows, columns)
        elif start_exit == "e":
            break
        else:
            print("Invalid input! Please enter 's' to start or 'e' to exit")
            print()