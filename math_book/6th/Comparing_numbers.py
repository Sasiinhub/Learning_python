#1.4 Comparison of Numbers
#1.4.2 Comparing numbers with unequal number of digits


\
# here problem is how do i know the user input length. ok we may choose the find Len() . but how we 
# ,  wait, letss try the 4 digit given steps on book.

place_names = ('ones','tens','hundreds','thousands','ten thousands','lakhs','Ten lakhs','Crores','Ten crores','Hundred crores','Thousand crores')
place_values = (1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000)

first_number = input('give a number: ')
second_number = input('give a second number to compare: ')

i = -1
for top_numbers in first_number:
    i += 1
    if top_numbers == second_number[i]:
        if len(first_number) - 1 > 0:
            continue
        else:
            print(f'Both {first_number} and {second_number} are equal.')
            break
    elif top_numbers > second_number[i]:
        print(f'The first_number  {first_number} is greater than\nThe second_number {second_number}')
        break

    elif top_numbers < second_number[i]:
        print(f'The second_number {second_number} is greater than\nThe first_number {first_number}')
        break
