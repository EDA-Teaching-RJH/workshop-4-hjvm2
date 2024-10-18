def main():
    choice = input("1. Coffee, 2. Tea, 3. Hot Chocolate: ")
    coininserted = 0
    price = 0
    
    if choice == '1':
        price = 75
    elif choice == '2':
        price = 60  
    elif choice == '3':
        price = 80  
    else:
        print("Invalid choice")
        return
    
    print(f"The price is {price} pence.")
    
    while coininserted < price:
        coin = int(input("Insert coins (50p, 20p, 10p, 5p): "))
        coininserted += coin
        print(f"Total inserted: {coininserted} pence.")
        
        if coininserted < price:
            print(f"Amount due: {price - coininserted} pence.")
        
        elif coininserted > price:
            minustopos = abs {price - conininserted}
            print(f"Change due: {price - coininserted} pence.")
        else:
            pass


    
    print("Thanks for your purchase!")

main()