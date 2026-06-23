secret_number = 7

guess = int(input("Guess the number (1-10): "))

while guess != secret_number:
    print("Wrong guess! Try again.")
    guess = int(input("Guess the number (1-10): "))

print("Congratulations! You guessed the correct number.")




def new_func1():
    def new_func():
        for i in range(1, 6):
            if i == 4:
                break
            print(i)

    new_func()

new_func1()


for i in range(1, 6):
    if i == 3:
        continue
    print(i)


