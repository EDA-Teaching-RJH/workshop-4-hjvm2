def main():
    choice = int(input("1. Coffee, 2. Tea, 3. Hot Chocolate: "))
    coin_inserted = 0
    
    if choice == '1':
        price = 75
        print("Invalid choice")
        return
    
    print(f"The price is", {price})
    
    while coin_inserted < price:
        coin = int(input("Insert coins (50p,20p,10p,5p): "))
        coin_inserted += coin
        print(f"Total inserted:", {coin_inserted})
        
        if coin_inserted < price:
            print(f"Amount Due: ", {price - coin_inserted})
    
    print("Thanks for your purchase!")

main()

