import time
import tracemalloc
tracemalloc.start()
cpu_start = time.process_time() #timer only for single core, not multiprocessor libraries.
place_names = ('ones','tens','hundreds','thousands','ten thousands','lakhs','Ten lakhs','Crores','Ten crores','Hundred crores','Thousand crores')
place_values = (1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000)


list_of_apartments = []


print('*****Apartment_list*****\n\n*Press enter if the enumeration done!')
while True:
    current_apt = {}
    current_apt['name'] = input('Apartment name: ')
    if current_apt["name"] == '':
        break

    current_apt['height'] = int(input('Apartment height: '))

    list_of_apartments.append(current_apt)
    print(list_of_apartments[-1]) # current_apt


list_request = input('Do you want final list?(yes): ') #.strip().lower()
if list_request == 'yes' or 'Yes' or 'YES' or 'y' or 'Y':
    print('*****Apartment_list*****\n',list_of_apartments,'\n')


print('Enter 1 to ascending\nEnter 2 for decending\nIf No press Enter: ')
sort_decision = input()

copy_of_original_before_swaping = list_of_apartments.copy()

n = len(list_of_apartments)
for i in range(n-1):
    for apartment in range(0, n-1):
        if list_of_apartments[apartment]["height"] > list_of_apartments[apartment+1]["height"]:
            continue
        elif  list_of_apartments[apartment]['height'] <  list_of_apartments[apartment+1]['height']:
            list_of_apartments[apartment+1], list_of_apartments[apartment] =  list_of_apartments[apartment], list_of_apartments[apartment+1]
        elif  list_of_apartments[apartment] ==  list_of_apartments[apartment+1]['height']:
            continue 


if sort_decision == '1':
    print('***Ascending Order***\n',list_of_apartments)

elif sort_decision == '2':
    print('***Descending Order***\n',list(reversed(list_of_apartments))) 
    # above commented print line alone reverse the original one, not a sorted one.
    # because the sorting never happens when it inside ascending.
    # so it needs to done before decision or both blocks need to sort.


elif sort_decision == '':
    print('Have a good day!\n')


current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
cpu_end = time.process_time()
time_taken = cpu_end - cpu_start
print(f'\n\n\nTime taken: {time_taken:.8f}')
print(f'bytes:\ncurrent: {current}\npeak: {peak}')
