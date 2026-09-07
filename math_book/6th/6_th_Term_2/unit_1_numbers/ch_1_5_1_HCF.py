import sys
#from ch_1_4_Prime_factorisation import call_for_Prime_Factors
from ch_1_2_1_Find_PrimeNum_SE_Method import call_for_Prime_List


def call_for_HCF(numbers): # user need to provide list as a argument
    dividents = numbers
    Common_Prime_Factors = []
    HCF = 0
    prime_list = call_for_Prime_List(max(numbers))

    i = 0
    while i < len(prime_list):
        #print(i)
        
        j = 0
        #print(j)
        new_dividents = []
        
        while j < len(dividents):
            if dividents[j] % prime_list[i] == 0:
                #print('inside loop', j)
                new_dividents.append(dividents[j] // prime_list[i])
                #if dividents[j] == dividents[-1]: # biggest mistake consumes a lot time, the comparision happens for both vaues not addresses.
                if j == len(dividents)-1:
                    #print('enters',j)
                    dividents = new_dividents
                    Common_Prime_Factors.append(prime_list[i])
               
                    i -= 1 
            else:
                #i += 1
                break
            j += 1
        i += 1
    if len(Common_Prime_Factors) == 0:
        HCF = 1
        print(f'here is no CPF {Common_Prime_Factors} among those. so')
    else:
        HCF = Common_Prime_Factors[0]
        for i in range(1, len(Common_Prime_Factors)):
            HCF = HCF * Common_Prime_Factors[i]
        
    return HCF

if __name__ == '__main__':

    numbers = []
    while True:

        num = input("Enter number you want to find Highest Common Factor \n (enter enough if you done! ): ")
        
        if num == 'enough':
           break
        try:
            number = int(num)
            numbers.append(number)
        except ValueError:
            print("Enter a valid value! and try again from first!")
            sys.exit()

    HCF = call_for_HCF(numbers)
    print(f'HCF is: {HCF}')

'''
    print(f'\nRest_Dividents: {dividents}\n')

    print(*Common_Prime_Factors, sep=' * ',end=' ')
    print(' = ',HCF)
    print(f'\nSo, Highest Common Divisor(factor) is {HCF} for the given numbers')
'''

# belove is the one of the  way does think, but the caller module
# is not knowledge about it.
'''
 caller_module = inspect.currentframe().f_back.f_globals["__name__"]

    if caller_module == "__main__":
        # If this file is running directly, return everything for your prints
        return HCF_value, Common_Prime_Factors, dividents
    else:
        # If imported into ANY other file, return ONLY the single HCF integer!
        return HCF_value    
'''



