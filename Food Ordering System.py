import os
import time
import sys
from playsound import playsound as ps

def delete_lasttwo_line():
    for i in range(2):
        # cursor up one line
        sys.stdout.write('\x1b[1A')
        # delete last line
        sys.stdout.write('\x1b[2K')

def delete_lastthree_line():
     for i in range(3):
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

def delete_lastfour_line():
     for i in range(4):
        sys.stdout.write('\x1b[1A')
        
        sys.stdout.write('\x1b[2K')

def DeleteOrderItems():          # delete items in display.
    with open("Display Ordered Items.txt","w") as dele:
        dele.truncate()

def AddtoCart():                     # to display food items in cart.
    with open("Display Cart.txt", "a") as D:
        D.writelines(f"\n\t\t  -> {Quantity}{FoodItem} of Price :- {FinalPrice}.")

def DeleteItemsCart():          # delete Items in cart.
    time.sleep(0.5)                
    os.system("cls")
    with open("Display Cart.txt", "r") as d:
        firstline = d.readline()
    with open("Display Cart.txt", "w") as cl:
        cl.write(firstline)
        cl.truncate(cl.tell())

def Menu():                     # to display menu.
    with open("Menu.txt", "r") as M:
        print(M.read())

def foodIdCheck(foodId):              # to check id of the food ordered.
    check = [1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3, 2.4, 3.1, 3.2, 3.3, 3.4, 4.1, 4.2, 4.3,
             4.4, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 8.2, 8.3, 8.4]            
    for i in range(len(check)):
        if (float(foodId) == check[i]):
            return True
    return False

def StoreNameOrderedItem():             # to store name of orderd item.
    with open("Menu_for_order_logic.txt", "r") as f:
        for line in f:
            if foodId in line:
                global Name_Of_Food, Price, FoodItem
                Name_Of_Food, Price_Of_Food = line.strip(foodId).split(":-")    # Store Name and Price of food.
                FoodItem = Name_Of_Food
                Price = int(Price_Of_Food) 

def StoreOrderedData():             # to store Orderd Data.
    with open("Display Ordered Items.txt","a") as s:
        s.write(f"\n\t-> You have selected {Quantity}{Name_Of_Food} of price :- {FinalPrice}")

def DisplayOrderedItems():           # to display Order....
        os.system("cls")
        try:
            ps("SelectionPage.mp3")
        finally:
            with open("Display Ordered Items.txt","r") as doi:
                print(doi.read())
            time.sleep(2)

def CheckInput():             # to check input of CVV number.
        cpay = int(input(f"\n\tPress 1 to Pay {sum(TotalBill)}.\n\tPress 2 to Cancel Payment."))
        if ( cpay == 1):
            print(f"\n\t\t-)Your payment of {sum(TotalBill)} rupees is received successfull.")
            ps("payment.mp3")
            print("\n\t\t   Thank You For Visiting INDIAN FOOD TRUCK.")
            ps("thankyou.mp3")
            os.system('cls')
            exit()
        elif( cpay == 2):
            print(f"Payment Cancellation of  {sum(TotalBill)} rupees is successfull.")
            DeleteOrderItems()
            DeleteItemsCart()
            exit()
        else:
            print("Enter Valid input.")
            CheckInput()

def CheckCVVNo():           # to check card no.
        cvv = int(input("Enter CVV number ( in 3 digit ): "))
        checkcvv = str(cvv)
        if ( (len(checkcvv)==3)):
            CheckInput()
        else:
            print("Invalid CVV number.")
            time.sleep(1)
            delete_lasttwo_line()
            CheckCVVNo()

def CheckCardNo():          # to check card number valid or not.+
        print("---Enter Card Details---")
        cno = int(input("Enter your Card number ( in 12 digit ): "))
        checkCno = str(cno)
        if ((len(checkCno)==12)):
            CheckCVVNo()
        else:
            print("\tInvalid Card number.")
            time.sleep(1)
            delete_lastfour_line()
            CheckCardNo()

def PayBill():                       # for payment....
        os.system('cls')
        print(f"\n\t\t >>> Bill of your Order is {sum(TotalBill)}.") 
        payment_option = int(input("\n\t\t>>Press 1 to pay via card.\n\t\t>>Press 2 to pay via UPI.\n\t\t>>Press 3 for Cancel Payment and Exit.\n\t\t"))
        if (payment_option == 1):
            time.sleep(1)
            os.system("cls")
            CheckCardNo()
        elif (payment_option == 2):
            time.sleep(1)
            os.system("cls")          
            print("\n\t\tThe UPI ID is 1234567897.")
            time.sleep(1)
            print(f"\n\t\t-)Payment of {sum(TotalBill)} is recived.")
            ps("payment.mp3")
            print("\n\t\t   Thank You For Visiting INDIAN FOOD TRUCK.")
            ps("thankyou.mp3")
            os.system("cls")
            exit()
        elif (payment_option == 3):
            print(f"Payment Cancellation of  {sum(TotalBill)} rupees is successfull.")
            exit()
        else:
            print("Enter Correct Choice.")
            PayBill()

def DisplayCart():                   # to display items of cart and bill.
    os.system("cls")
    with open("Display Cart.txt", "r") as DC:
        print(DC.read())
    print(f"\n\t\t >>> Bill of your Order is {sum(TotalBill)}.")   
    display_bill = int(input("\n\n\tPress 1 to Pay Bill.\n\tPress 2 to Order More Items.\n\tPress 3 to Cancel Order and order again.\n\tPress 4 to exit.\n\t"))
    if(display_bill == 1):
        DeleteOrderItems()
        DeleteItemsCart()
        PayBill()
    elif(display_bill == 2):
        MenuPage()
    elif(display_bill == 3):
        TotalBill.clear()
        DeleteOrderItems()
        DeleteItemsCart()
        MenuPage()
    elif(display_bill == 4):
        DeleteOrderItems()
        DeleteItemsCart()
        time.sleep(0.5)
        os.system("cls")
        exit()
    else:
        print("Enter Valid input.")
        DisplayCart()      

def ReOrder():                         # for cart things to perform...
    re_order = int(input(('\n\t\tPress 1 to display cart.\n\t\tPress 2 to Order More items.\n\t\tPress 3 to Cancel Order and Order Again.\n\t\tPress 4 to Exit.\n\t\t')))
    print(" ")
    if (re_order == 1):
        DisplayCart()
    elif (re_order == 2):
        MenuPage()  
    elif (re_order == 3):
        TotalBill.clear()
        DeleteOrderItems()
        DeleteItemsCart()
        MenuPage()
    elif(re_order == 4):
        DeleteOrderItems()
        DeleteItemsCart()
        time.sleep(1)
        os.system("cls")
        exit()
    else:
        print("\t\tEnter Valid Choice.")
        ReOrder()

def quantity():
    global Quantity, FinalPrice
    Quantity = int(input(f"\t\t   Enter the Quantity of{Name_Of_Food} you would like to have : "))
    if ( Quantity > 0):
        delete_lasttwo_line()
        StoreNameOrderedItem()
        FinalPrice = Price * Quantity
        StoreOrderedData()
        AddtoCart()
        TotalBill.append(FinalPrice)
    else:
        print("\t\t\t  -> Enter Quantity Greater than ZERO.")
        time.sleep(2)
        delete_lasttwo_line()
        quantity()

def item_order():                       
    global foodId
    time.sleep(0.2)
    foodId = input(f"\t\t   Enter the ID of Item {i} of food that you will like to Order : ")
    global FinalPrice
    if(foodIdCheck(foodId) == True):
        StoreNameOrderedItem()
        quantity()
    elif (foodIdCheck(foodId) == False):
        print(f"\t\t\t   - The Food ID {foodId} is not avaliable.\n\t\t\t   - Enter Food ID again.")
        time.sleep(3)
        delete_lastthree_line()
        item_order()

def Order():                                # how many number of items to order.
    global ItemOrder
    ItemOrder = int(input("\n\t  -> How Many Items you would like to order : "))
    if ( ItemOrder > 0):
        global i
        for i in range(1,ItemOrder+1):
            item_order()   
        DisplayOrderedItems()
        ReOrder()   
    else:
        print("\t\t\t-> Enter Items Greater than ZERO.") 
        time.sleep(2)
        delete_lastthree_line()
        Order()

def MenuPage():                     # Customer on menu page.             
    os.system("cls")
    Menu() 
    Order() 

def Custinput():                    # for customer input.
    with open("Welcome Page.txt", "r") as H:
        print(H.read())
    try:
        ps("home1.mp3")                                         # sound......
    finally:
        CustomerInput = int(input("\t\t"))
        if (CustomerInput == 1 ):                               
            MenuPage()
        else:
            print(f"\n\t\t\t\t{CustomerInput} is a Not a Valid Input.")
            time.sleep(1)
            os.system("cls")   
            Custinput()

TotalBill = []
DeleteOrderItems()
DeleteItemsCart()
Custinput()
