


def simplify_ratio(numerator, denominator):
    numer_backup = numerator
    denom_backup = denominator

    while numerator != denominator:
        if denominator > numerator:
            denominator = denominator - numerator
        else:
            numerator = numerator - denominator
    gcd = denominator # or numerator . because both are now equal.
    #print(gcd)

    simplified_numer = numer_backup / gcd
    simplified_denom = denom_backup / gcd


    return int(simplified_numer) ,int(simplified_denom)

