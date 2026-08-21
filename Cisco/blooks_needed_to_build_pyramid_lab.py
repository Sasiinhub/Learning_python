blocks = int(input("Enter the number of blocks: "))

height = 0

need_for_next_layer = 1

while blocks >= need_for_next_layer:
    
    height = need_for_next_layer
    blocks = blocks - need_for_next_layer
    need_for_next_layer = need_for_next_layer + 1

#
# Write your code here.
#	

print("The height of the pyramid:", height)

