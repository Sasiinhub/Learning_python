#1.4 Comparison of Numbers
#1.4.2 Comparing numbers with unequal number of digits


#place_names = ('ones','tens','hundreds','thousands','ten thousands','lakhs','Ten lakhs','Crores','Ten crores','Hundred crores','Thousand crores')
#place_values = (1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000)

first_number = input('give a number: ')
second_number = input('give a second number to compare: ')

i = -1
for each_number in first_number:
    i += 1

    if len(first_number) != len(second_number):
        print(f'Both {first_number} and {second_number} are not equal in length.')
        print()
        first_number = input('give a correct number: ')
        second_number = input('give a second number to compare: ')
        if first_number != second_number:
            continue

    elif each_number == second_number[i]:
        if i < len(first_number)-1 : 
	#check with total same len num every time with -1.
	# so it points the actual end index number.
	#so, if the len 5 - 1 = 4,
	# when the i has been reaching upto 3 it proceed continue(skips the loop)
	# when it reaches i= 4, the condition is false, because len - 1 also 4.
	# so, it move to else, prints , then breaks.
            continue
        else:
            print(f'Both {first_number} and {second_number} are equal.')
            break
    elif each_number > second_number[i]:
        print(f'The first_number  {first_number} is greater than\nThe second_number {second_number}')
        break

    elif each_number < second_number[i]:
        print(f'The second_number {second_number} is greater than\nThe first_number {first_number}')
        break
        
        
#ruff:
# 
# here problem is how do i know the user input length. ok we may choose the find Len() . # # but how we 
#,  wait, letss try the 4 digit given steps on book.


