numerator = int(input("Enter the numerator value: "))
denominator = int(input("Enter denominator value: "))


# from previous failures taught the normal divisor not the right one to divide all ratios.
# so, the necessity expects to use the concept of Greatest Common Divisor(Factor)

#To find GCD

#smaller_one = min(numerator, denominator)
#greater_one = max(numerator, denominator)

#gcd = greater_one % smaller_one 

numer_backup = numerator
denom_backup = denominator

# Actual strugle remover for this is Euclidean Algo
# but in book they doesnt provide how they find the common divisor. but used. how about the childs!
#the algo:  keep subtracting(instead of dividing) the smaller from the larger until they became same!
# in future, 1. by listing factors by hand 2. prime factors

while numerator != denominator:
    if denominator > numerator:
        denominator = denominator - numerator
    else:
        numerator = numerator - denominator
gcd = denominator # or numerator . because both are now equal.
print(gcd)

simplified_numer = numer_backup / gcd
simplified_denom = denom_backup / gcd


print(f"{int(simplified_numer)} : {int(simplified_denom)}")
