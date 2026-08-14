
place_names = ('ones','tens','hundreds','thousands','ten thousands','lakhs','Ten lakhs')
place_values = (1,10,100,1000,10000,100000,1000000)
user_input_inte = int(input('Enter the number you want to expand: '))
user_input =str(user_input_inte)

print(f'Finding the place value of all the digits in {user_input}:')
i = -1
for digit in reversed(user_input):
    i += 1
    print(f'The Place value of {digit} is = {digit} {place_names[i]} = {digit} x {place_values[i]} = ', ((int(digit)) * place_values[i] ))
