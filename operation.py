
from datetime import datetime
#import necessary function from writ.py
from write import update_furniture_stock, create_bill, create_seller_bill

# 
#Define a function to display BRJ Furniture items with detials.
def display_furniture(data):
    
    """
    Display the furniture detials in a tabular formate.
    Arguments:
    print different space line to show usre attractive.
    Return:
         furniture data according to the dictionary items.
        """
    #Here, just print this equal line to cover the items
    print("===============================================================================")
    print("ID\t Brand Name \t \t \t Product Name \t Quantity \t Price  ")
    print("===============================================================================")
    
    #Here, the for loop run show for key and values that furniture id and items
    for key, value in data.items():
       print(str(key) + " "*(5-len(str(key)))  + "\t"+ (value[0]+" "*(30-len(value[0]))) +" " 
                + (value[1]+" "*(5-len(value[1])))  +"\t" + (value[2]+" "*(5-len(value[2])))  +"\t" + "\t" + (value[3]+" "*(5-len(value[3]))))
       print("-------------------------------------------------------------------------------")


#Here, function define sell furniture.
def sell_furniture(data):
    try:
        # Get customer information
        customer_name = input("\n Enter you name: ")
        
        products = []
        while True:
            while True:
                try:
                    # Get Furniture Details.
                    valid = int(input("\n Enter the Furniture id:"))
                    if valid not in data:
                        print("Sorry:Your furniture ID is invalid.Enter(1-6)")
                        continue
                    break
                except ValueError:
                    print("Sorry:Your furniture ID is invalid.Entera number")
                    continue
                
            while True:
                try:    
                    validqty = int(input("\n Enter the quantity you want to sell:"))
                    
                    if validqty <= 0:
                        print("Sorry:Quantity must be equal or greater then (1) number.")
                        continue
                    if int(data[valid][2]) ==0:
                        print("Sorry: your available items in your store is zero")
                        break
                    
                    if validqty > int(data[valid][2]):
                        print("Sorry: Your selling Quantity is out of stock. Your available stock is:",data[valid][2])
                        continue
                    break
                    
                except ValueError:
                    print("Sorry:Your furniture Quantity is invalid.Enter a number.")
                    continue
                break
            if validqty > int(data[valid][2]):
                break
                
            products.append((valid, validqty))
            
            print(" ")
            print("_____________________________________________________________________________")
            print("Update Sell furniture items is here !!!")
            print("______________________________________________________________________________")
            print(" ")
            # insilize operation
            operation = 'sell'
            #for valid, validqty in products:
            data=update_furniture_stock(data, valid, validqty,operation)
            #Here, call the display furniture data after selling to update.
            display_furniture(data)
            
            # Ask customer if you want to more items purchase.
            add_more = input("\n Do you want to sell more items from your store? (yes/no): ")
            
            if add_more.lower() == 'yes':
                
               
                continue
            elif add_more.lower() == 'no':
                break
            else:
                print("\n Your input is invalid, Please enter 'yes' or 'no'.")
                continue
            
        
            
        # Get location for adding the shipping charge.
        location = input("\n Are you from  kathmandu valley  (yes/no):")
        # shiping charge inside valley and outside valley.
        
        if location.lower() == 'yes':# usre input yes then
            
            shipping_charge = 5 #add the shipping charge is $5
            
        elif location.lower() == 'no':# usre input no then
            
            shipping_charge = 7#add the shipping charge is $7
        else:
            #Here, the user input is mistake then
            print("\n Invalid location. Please enter 'yes' or 'no'.")# Here, show this message.
             # Here, return the value.
            return
                
        #Here current date and time 
        year = str(datetime.now().year)
        month = str(datetime.now().month)
        day = str(datetime.now().day)
        hour = str(datetime.now().hour)
        minute = str(datetime.now().minute)
        second = str(datetime.now().second)

        date = year +'-'+ month + "-" + day + " " + hour + " "+ minute + " " + second
        
        print("\n")
        # print the selling bill in console
        print("***********Selling bill from BRJ furniture store************")
        print("\n")
        print("Employee_name: " + customer_name)
        
        print("Date @ time:", date)
        print("===============================================================================")
        print("ID\t Brand Name \t \t \t Product Name \t Quantity \t Price")
        print("===============================================================================")
        for valid, validqty in products:
            value = data[valid]
            print(str(valid) + " "*(5-len(str(valid))) +"\t" + (data[valid][0]+" "*(30-len(data[valid][0])))+"\t"+ (data[valid][1])+" "*(5-len(str(data[valid][1]))) +"\t"+(str(validqty))+" "*(5-len(str(validqty)))
                     +"\t" + "\t" + (data[valid][3])+" "*(5-len(data[valid][3])))
        print("-------------------------------------------------------------------------------")
        print("\n")
        subtotals = []
        # calculate total price and bill amount including shipping charge
        for valid, validqty in products:
            
            subtotal = int(data[valid][3].replace("$","").replace(" ","")) * validqty
            
            subtotals.append(subtotal)
            
            total_price = sum(subtotals)
            
            print("Subtotal price of product: $", int(data[valid][3].replace("$","").replace(" ","")) * validqty)
        # calculate total price and bill amount including including vat amount
        total_price = sum(subtotals)
        vat_amount = total_price *0.13
        bill_amount = total_price + vat_amount + shipping_charge
        print("\n")
        print("Total Price(Before VAT):$", str(total_price))
        print("\n")
        print("Vat amount include (13%): $", str(float(vat_amount)))
        print("\n")
        print("Total price (After VAT): $", str(total_price + vat_amount))
        print("\n")
        print("Shipping Charge: ", str(shipping_charge))
        print("\n")
        print("Total amount you need to pay: $", str(bill_amount))
        print("\n")
        # create bills for manufacture and seller
        create_seller_bill(data, products, shipping_charge, vat_amount,date,customer_name,value)
        print("***********Thank you for using our system************")
        
    except ValueError:
        print("Sorry: Your input value is invalid. please enter a number(1-3)")
    except Exception as e:
        print("Sorry: This error occur in sell_furniture", str(e))
            

#Define function define purchase furniture.
def purchase_furniture(data):
    
    try:
        
        # Get customer name
        Employee_name = input("\n Enter you name:")

        #Initialize products list
        products = []
        while True:
            while True:
                try:
                    # Get Furniture Details.
                    valid = int(input("\n Enter the Furniture id:"))
                    if valid not in data:
                        print("Sorry:Your furniture ID is invalid.Enter(1-6)")
                        continue
                    break
                except ValueError:
                    print("Sorry:Your furniture ID is invalid.Entera number")
                    continue
                break
            while True:
                try:    
                    validqty = int(input("\n Enter the quantity you want to purchase:"))
                    
                    if validqty <= 0:
                        print("Sorry:Quantity must be equal or greater then (1) number.")
                        continue
                    break
                except ValueError:
                    print("Sorry:Your furniture Quantity is invalid.Enter a number.")
                    continue
                break
            #Add product to products list
            products.append((valid, validqty))
            print(" ")
            print("_____________________________________________________________________________")
            print("Update Sell furniture items is here !!!")
            print("______________________________________________________________________________")
            print(" ")
            # insilize operation
            operation = 'order'
            #for valid, validqty in products:
            data=update_furniture_stock(data, valid, validqty,operation)
            #Here, call the display furniture data after selling to update.
            display_furniture(data)
            
            # Ask customer if you want to more items purchase.
            add_more = input("\n Do you want to purchase more items from our store? (yes/no): ")
            if add_more.lower() == 'yes':
               
                continue
            elif add_more.lower() == 'no':
                break
            else:
                print("\n Your input is invalid, Please enter 'yes' or 'no'.")
                continue
            
            
        #Here current date and time 
        year = str(datetime.now().year)
        month = str(datetime.now().month)
        day = str(datetime.now().day)
        hour = str(datetime.now().hour)
        minute = str(datetime.now().minute)
        second = str(datetime.now().second)

        date = year +'-'+ month + "-" + day + " " + hour + " "+ minute + " " + second
        print("\n")
        print("***********Purchase bill from BRJ furniture store************")
        print("\n")
        print("Employee_name: ", Employee_name)
        print("Date @ time:", date)
        print("\n")   
        print("===============================================================================")
        print("ID\t Brand Name \t \t \t Product Name \t Quantity \t Price")
        print("===============================================================================")
        for valid, validqty in products:
            value = data[valid]
            print(str(valid) + " "*(5-len(str(valid))) +"\t" + (data[valid][0]+" "*(30-len(data[valid][0])))+"\t"+ (data[valid][1])+" "*(5-len(str(data[valid][1]))) +"\t"+(str(validqty))+" "*(5-len(str(validqty)))
                           +"\t" + "\t" + (data[valid][3])+" "*(5-len(data[valid][3])))
        print("-------------------------------------------------------------------------------")
        print("\n")
        subtotals = []
        # calculate total price and bill amount including shipping charge
        for valid, validqty in products:
            subtotal = int(data[valid][3].replace("$","").replace(" ","")) * validqty
            subtotals.append(subtotal)
            total_price = sum(subtotals)
            print("Subtotal price of product: $", int(data[valid][3].replace("$","").replace(" ","")) * validqty)
        # calculate total price and bill amount including including vat amount
        total_price = sum(subtotals)
        vat_amount = total_price *0.13
        bill_amount = total_price + vat_amount
        print("\n")
        print("Total Price(Before VAT):$ ", str(total_price))
        print("\n")
        print("Vat amount include (13%):$ ", str(float(vat_amount)))
        print("\n")
        print("Total price (After VAT): $", str(bill_amount))
        print("\n")
        print("Total amount you need to pay:$ ", str(bill_amount))
        print("\n")
        # create bills for manufacture  Purchase
        create_bill(data, products, vat_amount,date,Employee_name,value)
        print("***********Thank you for using our system************")
    except ValueError:
        print("Sorry: Your input value is invalid. please enter a number(1-3)")
    except Exception as e:
        
        print("Sorry: This error occur in purchase_Furniture", str(e))
            
       


       

            
        
    
