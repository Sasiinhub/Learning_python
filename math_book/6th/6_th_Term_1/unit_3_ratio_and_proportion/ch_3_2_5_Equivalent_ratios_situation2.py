# i have 600 , i wants to divide it between two persion in the ratio 2 : 3.  who will get more and how much?

whole = int(input("what you have right now? "))

for_vimala = 0
for_yazhini = 0

ratio = [2 , 3]
#solution:

# divide the whole money into equal parts:

equal_parts_of_whole = ratio[0] + ratio[1] 

for_vimala =int((whole * ratio[0]) / equal_parts_of_whole)
for_yazhini =int((whole * ratio[1]) / equal_parts_of_whole)

if for_vimala > for_yazhini:
    print(f"vimala received {for_vimala} and it's more than yazhini {for_yazhini}")
else:
    print(f"vimala received {for_vimala} and it's less than yazhini {for_yazhini}")
