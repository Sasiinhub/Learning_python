number = int(input("Enter a number: "))

multiply = int(input("Enter 2 to Multiply it by 2: "))
multiplied = 0

add = 0
added = 0

divide = 0
divided = 0

subtract = 0 
subtracted = 0

while True:
    if multiply == 2:
        print("Mutiplying the number...")
        multiplied =  multiply * number
        print(f"Multiplied = {multiplied}")
    else:
        multiply = int(input("Enter Number 2 only. try again: "))
        if multiply == 2:
            multiplied =  multiply * number
        else:
            continue
    add = int(input("Enter number 20 to add: "))
    if add == 20:
        print(f"adding 20 to the {multiplied} value...")
        added = multiplied + add
    else:
        print("Try again! your input is wrong")
        continue
    divide = int(input("Enter number 2 to divide: "))
    if divide == 2:
        print(f"dividing {added} by 2.. ")
        divided = added / divide
        print(f"which is {divided}")
    else:
        print("Try again! the given number is wrong!")
        continue

    print(f"Subtracting the original number you had thought in beginning {number} with the final divided one{divided} ")
    subtracted = divided - number
    print(f"The result is: {subtracted}")
    print("surprised? We can do this the same will happen for other numbers too. we only get 10 at the end")
    print("intresting.. right?\nwe can do like this more in Algebra.")
    break
