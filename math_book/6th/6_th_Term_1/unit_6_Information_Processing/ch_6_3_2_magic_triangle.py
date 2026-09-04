#nodes = [1,2, 3, 4, 5, 6 ]
#node = [1,3,4,2,5,6]

arranged_numbers = []
print('Give any evenly spaced 6 numbers')
for i in range(6):
    arranged_numbers.append(int(input(f'Give number {i+1}: ')))
print(arranged_numbers)
#side_two = []
#side_three = []

#step 1: Larger nubers at the corner of the triangle

arranged_numbers.sort()
#larger_numbers = arranged_numbers[-3:]

# step 2 amaller numbers with fixed positions
#edge_nodes = []
bottom_side =  arranged_numbers[0]
right_side =  arranged_numbers[1]
left_side = arranged_numbers[2]
top_corner = arranged_numbers[3]
left_corner = arranged_numbers[4]
right_corner = arranged_numbers[5]

#for side in range(:3):
    #decision = input('Which side you want to add(left, right or bottom): ').lower().startswith('l' or 'r' or 'b')
print(f'left side: {left_corner} + {left_side} + {top_corner} = {top_corner+left_corner+left_side}')
print(f'left side: { right_corner} + {right_side} + {top_corner} = {top_corner+right_corner+right_side}' )
print(f'left side: {left_corner} + { right_corner} + {bottom_side} = {bottom_side+right_corner+left_corner}' )

print('\nsurprise right! if you does not get same total from all sides, \ncheck your numbers have evenly spaced like\n1 2 3 4 5 6 or 3 3 3 3 3 3 or 3 6 9 12 15 18 ')
