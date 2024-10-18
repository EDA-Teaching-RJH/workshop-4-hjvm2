def main():
    choice1 = int(input("1. Coffee, 2. Tea, 3. Hot Chocolate: "))
    coininserted = 0
    price = 0

    validnumber = inputcheck(choice1)
    #print(f"You entered a valid number: {validnumber}")
    if validnumber == 1:
        price = 75
    elif validnumber == 2:
        price = 60  
    elif validnumber == 3:
        price = 80  
    
    
    print(f"The price is {price}p")
    
    while coininserted < price:
        coins= [50 ,20, 10 ,5]
        coin = int(input("Insert coins (50p, 20p, 10p, 5p): "))
        if coin in coins:
            coininserted += coin
            print(f"Total inserted: {coininserted}p")
        else:
            print("Invalid coin!\n")
            print()
        if coininserted < price:
            print(f"Amount due: {price - coininserted}p")
        
        elif coininserted > price:
            change_due = abs(coininserted - price)
            print(f"Change due: {change_due} pence")
        else:
            pass

    print("Thanks for your purchase!")



def inputcheck(choice):
    while True:
        if 0< choice <4 :
           break 
        else:
            print("Your choice is invalid please try again!")
            choice = int(input("1. Coffee, 2. Tea, 3. Hot Chocolate: "))
    

    return choice
            


main()