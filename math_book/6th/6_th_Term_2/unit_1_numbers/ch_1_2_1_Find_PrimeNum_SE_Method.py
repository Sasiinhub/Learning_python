def call_for_prime_list(limit): # make this line active if it need standalone file and consider the change of limit parameter where ever it used
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



    numbers = []
    limit = int(limit)
    for number in range(1,limit+1):
        numbers.append(number)
    #print(numbers, '\n')

    del numbers[3::2]
    prime = [] #numbers.copy
    for i in numbers:
        if i == 1:
            continue
        prime = call_delete_multiples(numbers, i) # aware: it deletes all of its multiples in every loop
        #print(prime)
        #print(f'for{i}')
        #print()
    
    print(f'Prime numbers upto {limit}:\n{prime}')
    print(f'Total prime numbers are {len(prime)-1}')
    return prime


'''
learnings:
    * missed to note the shift of numbers every time calling the delete , 
     the delete deletes the all multiples of i through out the list in first attempt. so,
     the next loop doesn't contains all of the multiples like previous original list.

    
advice to improve from Aimode:
 1. we don't need to perform unwanted calculations after some numbers to eliminate multiples of primes up to some stop point.
    so, we do sqare root of the max number.

'''

if __name__ =='__main__':
    pass

