#from ch_1_4_Prime_factorisation import call_for_Prime_Factors
from ch_1_5_1_HCF import call_for_CPF
def call_for_LCM(numbers):

    dividents = numbers
    prime_factors = call_for_CPF(numbers)
    LCM = 0

    i = 0
    while i < len(dividents):
        print(len(prime_factors))
        j = 0

        new_dividents = []

        while j < len(dividents):
            if dividents[j] % prime_factors[i] == 0:
                new_dividents.append(dividents[j] // prime_factors[i])
                if j == len(dividents)-1:
                    dividents = new_dividents
                    prime_factors = call_for_CPF(dividents)
                    print( prime_factors,' ', dividents)
                    i = -1 
                else:
                    #i -= 1
                    print('from round success deep else', i , j)
            else:
                print('from break else', i , j )
                i += 1
                break
            print('A',j,i)
            j += 1
        #if 
        print('B',i,j)
        i += 1 


if __name__ == '__main__':

    numbers = []
    while True:

        num = input("Enter number you want to find Least Common Multiples \n (enter enough if you done! ): ")

        if num == 'enough':
           break
        try:
            number = int(num)
            numbers.append(number)
        except ValueError:
            print("Enter a valid value! and try again from first!")
            sys.exit()
    LCM, prime_factors, dividents = call_for_LCM(numbers)
    print(f'LCM : {LCM} , {dividents}, {prime_factors}')
#    print(call_for_LCM(numbers))





'''
    i = 0
    j = 0
    while i < len(dividents):
        #j = 0
        new_dividents = []
    #while  j < len(dividents)
        if dividents[j] % prime == 0:
            if j == len(dividents)-1:
                prime_factors.append(prime)
                dividents = new_dividents
                #i -= 1
        if j == len(dividents)
            j = 0
        else:
            for num in range(prime+1):
                if num%2 == 0:
                    prime = num%2 == 0
                    break
        j += 1
        i += 1
    #if len(prime_factors) == 0:
        
    return LCM, prime_factors, dividents
'''

'''

    prime = 2
    i = 0
    while i < len(dividents):
        #print(i)
        
        j = 0
        #print(j)
        new_dividents = []
        
        while j < len(dividents):
            if dividents[j] % prime == 0:
                print('inside loop', j)
                new_dividents.append(dividents[j] // prime)
                #if dividents[j] == dividents[-1]: # biggest mistake consumes a lot time, the comparision happens for both vaues not addresses.
                if j == len(dividents)-1:
                    print('enters',j)
                    dividents = new_dividents
                    prime_factors.append(prime)
                    print(dividents)
                    i = 0
            else:

                for num in range(prime+1, max(dividents)):
                    if num%num == 1 and num%:
                        prime = num
                        break

            j += 1
        i += 1
    return LCM, prime_factors, dividents
'''
