from ch_1_2_1_Find_PrimeNum_SE_Method import  call_for_prime_list

def call_for_Prime_Factorisation(number):
    
    prime_numbers = call_for_prime_list(number)

    #print(prime_numbers)
    prime_factors = []
    divident = []


    i = 0
    j = 0


    while number > 1:
        prime = prime_numbers[j]
        # bug check: print(f'number {number} prime {prime} prime factors {prime_factors} divident {divident}') 
        if len(prime_factors) == 0:
            if number%prime == 0:

                divident.append(number) 
               
                divident.append(number // prime)
                #divident.append(number - divident[i])
                prime_factors.append(prime)
                number = divident[-1]
                #number -= divident[i+1]
                print(prime_factors[-1], '/```', divident[i],'```')
                i += 1
                continue
                
            else:
                j += 1
                #i += 1
                #prime = prime_numbers[j]
                continue

           
        if divident[i] % prime == 0: 
            divident.append(divident[i] // prime)
            prime_factors.append(prime)
            # number -= divident[-1] # wrong try
            number = divident[-1]
            print(prime_factors[-1], '/```', divident[i],'```')
            i += 1    
            continue
        elif j < len(prime_numbers):
            j += 1
            #i += 1
            #prime = prime_numbers[j]

    print(f'  /``` {divident[-1]} ```')
    return prime_factors


if __name__ == "__main__":

    number = int(input('Enter a number to get prime factorisation: '))
    num_copy = number # int is immutable so here both not have same reference 

    prime_factors = call_for_Prime_Factorisation(number)
    print('Prime Factors: ')
    print(*prime_factors, sep='*')

# bug check: print(f'number {number} prime {prime} prime factors {prime_factors} divident {divident}') 



#Failure 1:
'''def Division_By_Primes(given, prime_numbers)
    if given == 1 or given = 0:
        return 

    given/prime_numbers[]
'''
#failure 2:
'''

        #prime_factors.append(number // prime)
        #temp = prime_factors[i]
        #number -= temp
        
        #print(number, ' ', prime_factors[i])

'''
# failure 3(when trying diffrent numbers)
'''
ch_1_4_Prime_factorisation.py", line 27, in <module>
    print(prime_factors[i], '/```', divident[i],'```')
          ~~~~~~~~~~~~~^^^
IndexError: list index out of range
'''

#misunderstanding
'''
   # else:
  #      j -= 1
 #       prime = prime_numbers[j]
#        continue
'''
'''

    #else:
     #   j = 0
      #  prime = prime_number[j]
'''
