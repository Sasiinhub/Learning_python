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
if __name__ == '__main__':
    main()
    # newlly practice to use the main() method. and knowing the usage..
