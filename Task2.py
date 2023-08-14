def count_words(sentence):
    words = sentence.split()
    print (len(words))


print("--- Welcome to the *Word Counter* tool ---")
print("To use this program, please follow these steps:")
print("--> Enter your sentence when prompted.")
print("--> The program will count the number of words in your sentence.")

while True:
        start_exit = input("Enter 's' to start or 'e' to exit: ")
        if start_exit == "s":
            sentence = input("please enter your sentence: ")
            count_words(sentence)
        elif start_exit == "e":
            break
        else:
            print("Invalid input! Please enter 's' to start or 'e' to exit")
            print()
