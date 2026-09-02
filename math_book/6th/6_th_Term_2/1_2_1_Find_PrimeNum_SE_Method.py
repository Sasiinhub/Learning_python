numbers = []

for number in range(1,200001):
    numbers.append(number)
#print(numbers, '\n')

del numbers[3::2]

def call_delete_multiples(numbers, multifier):

    Table = []
    for n in numbers:
        
        if n % multifier == 0:
            Table.append(n)
    #print(Table)

    for num in Table:
        if num == multifier:
            continue
        numbers.remove(num)
    return numbers
    #print(numbers)
prime = []
for i in numbers:
    if i == 1:
        continue
    prime = call_delete_multiples(numbers, i)
    #print(prime)
    #print(f'for{i}')
    #print()
print(prime)
print(f'\nTotal prime numbers are {len(prime)-1}')

'''
advice to improve from Aimode:
 1. we don't need to perform unwanted calculations after some numbers to eliminate multiples of primes up to some stop point.
    so, we do sqare root of the max number.

