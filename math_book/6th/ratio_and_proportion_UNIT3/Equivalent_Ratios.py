#3.2.5
#finding which ratio is greater

import Simplifying_ratio_as_function as sf

# Scenario_idly batter compare with two batches
# ignoreing water and fenugreek

#to find how much simplest ratio of black_gram added in first batch
rice = int(input("How much rice you added: "))
black_gram = int(input("How much rice you added black_gram with same measuring instrument/gauge: "))
total = rice + black_gram


#to find how much simplest ratio of black_gram added in second batch
rice_2 = int(input("How much rice you added in this second batch: "))
black_gram_2 = int(input("black_gram with same measuring instrument/gauge in this batch: "))
total_2 = rice_2 + black_gram_2


# how much blackgram added on each batch if the two batches total(denominator) are same:
#tried:def make_the_denominator_even (batch_one, batch_two)

numerator, denominator = sf.simplify_ratio(black_gram, total)
numerator_2, denominator_2 = sf.simplify_ratio(black_gram_2, total_2)

print(f"\nnon simplified ratios are {black_gram} : {total} and second batch {black_gram_2} : {total_2}\n")
print(f"simplified ratios are {numerator} : {denominator} and second batch {numerator_2} : {denominator_2}\n")


simplified_batch1 = [numerator, denominator]
simplified_batch2 = [numerator_2, denominator_2]

#print(simplified_batch1, simplified_batch2)


list_of_numerator = []
list_of_numerator2 = []

list_of_denominator = []
list_of_denominator2 = []



k = -1
l = -1
m = 2
found = False

while True:

    list_of_numerator.append(numerator * m)
    list_of_denominator.append(denominator * m)
    #print(list_of_denominator)

    list_of_numerator2.append(numerator_2 * m)
    list_of_denominator2.append(denominator_2 * m)
    #print(list_of_denominator2)
    for i in  range(len(list_of_denominator)):
        for j in range(len(list_of_denominator2)):

            if list_of_denominator[i] == list_of_denominator2[j]: # comparing the right side with the same variable consumed lots of time and work.
                k = i
                l = j
                found = True
                print(f"\nby increasing batch sizes to compare equivalent total are ,\n we get {list_of_numerator[k]} / {list_of_denominator[k]} and second batch {list_of_numerator2[j]} / {list_of_denominator2[j]}")
                break
        if found:
            break
        
    if found:
        break
    m+=1

if list_of_numerator[k] > list_of_numerator2[l]:
    print(f"we can conclude that \nbatch one  {numerator} : {denominator} is more black gram ratio than \nbatch two  {numerator_2} : {denominator_2}")
elif list_of_numerator[k] < list_of_numerator2[l]:
    print(f"we can conclude that \nbatch one  {numerator} : {denominator} is lesser black gram ratio than \nbatch two  {numerator_2} : {denominator_2}")
else:
    print(f"we can conclude that \nbatch one  {numerator} : {denominator} is equal black gram ratio to \nbatch two  {numerator_2} : {denominator_2}")

