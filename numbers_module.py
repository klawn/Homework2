
def main():
    num_1 = int(input("Please enter a number: "))
    num_2 = int(input("Please enter a number: "))

    if num_1 > num_2:
        print("Number 1 is bigger than Number 2.")
    elif num_2 > num_1:
        print("Number 2 is bigger than Number 1.")
    elif num_1 == num_2:
        print("Number 1 and Number 2 are the same.")

main()
