''' If two ratios are in proportion ie., a:b::c:d (:: -> as of)
 then the product of the extremes is equal to the product of the 'means'.
 here a and d are the extremes and b and c are the means
and if two ratios are eqauls called cross product of proportions.
'''

# a heater uses 3 units of electricity in 40 minutes.
# How many units does it consume in 2 hours?

units_used_before = int(input("How many units used? "))

duration_time = int(input("For how much duration? "))

is_minutes = input("is it minutes? (y/n): ").lower().startswith('y')

if is_minutes == False:
    duration_time = duration_time * 60

need_to_know = int(input("The new Consumption duration now?\n to calculate the units :"))
is_minutes = input("is in minutes? (y/n): ").lower().startswith('y')

if is_minutes == False:
    need_to_know = need_to_know * 60

product_of_extremes = units_used_before * need_to_know

# divide the product_of_extreme by denominator of product_of_means
# to get the numerator of product_of_means we use the previous unit knowledge
units_consumed_now = product_of_extremes / duration_time

product_of_means = units_consumed_now * duration_time

print(f"so, the heater consumed {int(units_consumed_now)} units of electricity in {need_to_know}")
print(f"\nso, the product of extremes equal to product of means: {int(product_of_extremes)}::{int(product_of_means)}")
print(f"{units_used_before} * {need_to_know} = {product_of_extremes}\n{duration_time} * {units_consumed_now} = {product_of_means}")

print('''\nHere the concept of algebric usage is solving the unknow practice helps here
to find the numerator of the half done proportion 1:40::x:120.
''')
