print("This Program is created by: Aldrick James A. Gicole From CS1D. ")
print("if you want to terminate the program please enter 0")

while True:
    start = int(input("Enter a number [start} : "))

    if start == 0:
        print("Program terminated.")
        break

    if start < 0:
        print("Enter a non-negative number.")
        continue

    end = int(input("Enter a number [end]: "))

    if end < start:
        print(f"Enter a number greater than the {start}. ")
        continue

    print(f"Prime numbers between {start} and {end} are: ", end="")

    for num in range(start, end + 1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
    print("\n")
