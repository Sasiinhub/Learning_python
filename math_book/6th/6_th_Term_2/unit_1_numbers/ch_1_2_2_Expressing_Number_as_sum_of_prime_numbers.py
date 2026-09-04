import time
import tracemalloc
tracemalloc.start()
cpu_start = time.process_time() #timer only for single core, not multiprocessor libraries.


import ch_1_2_1_Find_PrimeNum_SE_Method

def main():
    sumed_numbers = []

    choosen_number = int(input('Enter any number greater than 3: '))

    prime_numbers_upto_choosen_number =  ch_1_2_1_Find_PrimeNum_SE_Method.call_for_prime_list(choosen_number)
    primes = prime_numbers_upto_choosen_number
    #for number in prime_numbers_upto_choosen_number:
    for i in range(len(primes)):
        for j in range(i, len(primes)):
           # print( primes[i] , primes[j])
            if primes[i] + primes[j] == choosen_number:
                temp = [primes[i] , primes[j]]
                sumed_numbers.extend(temp)
                print(f'{primes[i]} + {primes[j]} = {choosen_number}')
    print('\n', sumed_numbers)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    cpu_end = time.process_time()
    time_taken = cpu_end - cpu_start
    print(f'Time taken: {time_taken:.4f}')
    print(f'bytes:\ncurrent: {current}\npeak: {peak}')



if __name__ == '__main__':
    main()
    # newlly practice to use the main() method. and knowing the usage..

    
