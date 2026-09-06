import time
import tracemalloc
tracemalloc.start()
cpu_start = time.process_time() #timer only for single core, not multiprocessor libraries.

import sys


#Arrange them in all possible ways but maintain each row will be equal.

def call_for_factors(sticks):
    arrangements = []
    for row in range(1, sticks+1):
        for col in range(1, sticks+1):
            if row * col == sticks:
                print(f'{row} * {col} = {row*col}')

                arrangements.append([row,col])
                #arrangemnets.append(row)
    return arrangements
    #print(factors)


try:
    sticks = int(input('Enter no of sticks you want to arrange: '))
    if sticks < 2:
        raise ValueError
except ValueError:
    print('Enter natural number only!')
    sys.exit()  


arrangements = call_for_factors(sticks)
print('Arrangements:\n',arrangements, '\n')


if len(arrangements) == 2:
    prime_factors = [arrangements[0][0], arrangements[1][0]]
    print()
    print('Factors are: ', prime_factors)
    print(f'\nNumber of factors are {len(prime_factors)} not more than two')
    #print(prime_factors[0][0],prime_factors[1][0], sep="*")
    print(f'so, {sticks} is a prime number')
else:
    composite_factors = []
    for element in range(int(len(arrangements))):
        composite_factors.append(arrangements[element][0])
        #print(prime_factors[0][0],prime_factors[1][0], sep="*")
    print('Factores are: ',composite_factors)
    print(f'\nNumber of factors are {len(composite_factors)} more than two')
    print(f'so,{sticks} is a composite number')


    '''
    # Composite Factor also we can convert as prime factors! because they say any number is formed using prime! 
      so for conclusion the further prime factorisation chapter teaches how we get more than two prime factors for any number!(need to know the usage)
    
    # Finding a number is a composite helps to arrange things as a grid in equal way !
    # as is prime also  helps use to know there is only two way to arrange things to get equal grid.

    # we can find prime by dividing without fraction. which comes next.
    '''


current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
cpu_end = time.process_time()
time_taken = cpu_end - cpu_start
print(f'\n\n\nTime:\n{time_taken:.4f}')
print(f'bytes:\ncurrent: {current}\npeak: {peak}')
