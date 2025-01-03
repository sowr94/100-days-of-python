#Jan 3rd,25
######################
import keyword
print("The list of keywords are:" , keyword.kwlist)

######################
a = True
b = False

# Logical operations
print(a and b)  # AND: True if both a and b are True
print(a or b)   # OR: True if at least one of a or b is True
print(not a)    # NOT: Inverts the value of a

#in, is  -> keywords
print (a in ["a","b","c"])
####################

name = "Sowmya"
if "S" in name:
    print("Correct S is present in Sowmya")
else:
    print("Not present")

################
num = 0
for num in range(5):
    if num == 5:
        continue   
    print(num)

    
count = 0
while count < 4:
    count += 1
    if count == 3:
        break  # Exit the loop when count reaches 4
    print(count)