#Local variables, the variables defined inside a function are called local variables
#Example1
def things():
    a = "Things in room 116 - Used only by S & A"
    print(a)
things()

############################################

#global variables : defined outside any function are global and can be accessed inside functions
wf = "Hey I am a ABC company water filter ALL the first floor rooms can make use of me."

def waterfilter ():
    rm116 = "Water filter used by room 116 member S & A"
    print(rm116)

waterfilter()
print(wf)

############################################
#Swapping funtion
x,y =  7,8
x,y = y,x
print(x,y)
############################################
#Counting the characters in a string
name = "Sowmya"
length = len(name)
print("The total character in the string is", length)