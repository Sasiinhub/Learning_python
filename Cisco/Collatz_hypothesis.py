c0 = int(input("Enter any Non zero and non negative number: "))
i = 0
while c0 != 1:
    i+=1
    if c0 % 2 == 0:
        c0 = c0/2
        print(int(c0))
    elif c0 % 2 != 0:
        c0 = 3 * c0 + 1
        print(int(c0))    

print(f"Steps: {i}")
