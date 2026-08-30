list = ['A','B','c','d','e']

combinations = []

for i in range(len(list)-1):
    for j in range(len(list)-1):
        combinations.extend([list[i] + list[j]])
        #i += 1
        #j += 1
print('Combinations are:')
for k in range(len(combinations)-1):
    print(combinations[k])
    



'''
#Aimode
count = 0
print('Combinations: ')
for bit4 in range(2):
    for bit3 in range(2):
        for bit2 in range(2):
            for bit1 in range(2):
                print(f'{count:<4} | {bit4}{bit3}{bit2}{bit1}')
                count = count + 1
'''

