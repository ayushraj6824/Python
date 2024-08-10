# WAP which will keep adding a stream of numbers inputted by the the user .
#  THe adding stops as soon as user pressws q key on the keyboard.

sum=0
while(True):
    userInput=input("Enter the item price or press q to quit: \n")
    if(userInput!='q'):
        sum+=int(userInput)
        print("order total so far: ",sum)
    else :
        print(f"Your Bill total is {sum}.Thanks for shopping.")
        break

