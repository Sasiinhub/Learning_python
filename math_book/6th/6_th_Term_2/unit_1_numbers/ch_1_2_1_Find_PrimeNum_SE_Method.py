def call_for_Prime_List(limit): 
    def call_for_Delete_Multiples(numbers, multifier):

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
    del numbers[0]
    del numbers[2::2]
    #print(numbers)
    #primes = numbers # just name change but both points the same object            #numbers.copy 
    primes = []
    for i in numbers:
        primes = call_for_Delete_Multiples(numbers, i) # aware: it deletes all of its multiples in every loop
        #print(prime)
        #print(f'for{i}')
        #print()
    
    print(f'Prime numbers upto {limit}:\n{primes}')
    print(f'Total prime numbers are {len(primes)}')
    return primes


'''
learnings:
    * missed to note the shift and shrink of numbers every time calling the delete , 
     the delete deletes the all multiples of i through out the list in first attempt. so,
     the next loop doesn't contains all of the multiples like previous original list.

    
advice to improve from Aimode:
 1. we don't need to perform unwanted calculations after some numbers to eliminate multiples of primes up to some stop point.
    so, we do sqare root of the max number.

'''

if __name__ =='__main__':
    pass

    check = call_for_Prime_List(36)
    print("print again: \n",check)
