
place_names = ('ones','tens','hundreds','thousands','ten thousands','lakhs','Ten lakhs','Crores','Ten crores','Hundred crores','Thousand crores')
place_values = (1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000)


list_of_apartments = {}

print('*****Apartment_list*****\n\n*Press enter if the enumeration done!')
while True:

    apartment_name = input('Apartment name: ')
    if apartment_name == '':
        break

    apartment_height = int(input('Apartment height: '))

    list_of_apartments[apartment_name] = apartment_height
    print(list(list_of_apartments.items())[-1])

print('Do you want final list?(yes or no): ')
list_request = input()
if list_request is 'yes' or 'Yes' or 'YES':
    print('*****Apartment_list*****\n',list_of_apartments,'\n')


print('Enter 1 to ascending\nEnter 2 for decending\nIf No press Enter: ')
asc_request = input()

sorted = {}
i = -1
if asc_request == '1':
    for name in list_of_apartments:
        #print(list_of_apartments[name])
        if 
        if list_of_apartments[name] < sorted[name] 
        #sorted += pair
        
else:
    print('Have a good day!')

