from datetime import datetime
#import operation

def update_furniture_stock(data, valid, validqty,operation):
    """
    update the furniture stock based on the operation after order & sell

    Arguments:
           data: furniture data in dictionary
           valid: furniture id
           validqty: when we can order and sell then update the quantity
           operation: operation type is (sell, order)
    Returns value:
         Update data dictionary of furniture stock
    """
    try:
            
        # Get the current quantity of the furniture item
        quantity = int(data[valid][2].replace(" ",""))
            
        # Check if the furniture item exists in the data
        if valid in data:
            
            # Check the type of operation
            if operation == 'sell':
                
                # Check if there is enough stock available
                if quantity>= validqty:
                    
                    # Subtract the sold quantity from the available quantity
                    quantity-= validqty
                    data[valid][2] = str(quantity)
                        
                else:
                    print("Not enough stock available in this furniture store!")
                        
            elif operation == 'order':
                
                # Add the ordered quantity to the available quantity
                quantity += validqty
                data[valid][2] = str(quantity)
                     
            else:
                print(" Sorry, Furniture id not found!")
            return data
    except KeyError:
        print("Sorry:Your furniture id not found.")
    except ValueError:
        print("Sorry: Your furniture id must be number")
    except Exception as e:
        print("Sorry: This error is in update stock.",str(e))
        
               
# Define a function to create a bill for the manufacturer
def create_bill(data, products, vat_amount,date,Employee_name,value):
    """
    Create a purchase bill in .txt file after purchase the items

    Arguments:
         data: furniture data in dictionary
         products: this is product list with quantity
         vat_amount: vat amount is in float
         date: this is a current date and time for uniqe bill
         employee_name: purchaser name in string
         value: this is the total value of products
    Returns:
       None
    """
    try:
        #Here current date and time 
        year = str(datetime.now().year)
        month = str(datetime.now().month)
        day = str(datetime.now().day)
        hour = str(datetime.now().hour)
        minute = str(datetime.now().minute)
        second = str(datetime.now().second)

        date = year +'-'+ month + "-" + day + " " + hour + " "+ minute + " " + second
        
        filename = "purchase_bill" + date + ".txt"
        # open the file in write mode   
        file = open(filename, "w")
        
        file.write("***********Purchase bill from BRJ furniture store************"+ "\n")  
        file.write("Employee_name: " + (Employee_name)+ "\n")
        file.write("Date @ time:"+ date +"\n")
        file.write("\n")
            
        file.write("===============================================================================")
        file.write("\n")
        file.write("ID\t Brand Name \t \t \t Product Name \t Quantity \t Price")
        file.write("\n")
        file.write("===============================================================================")
        file.write("\n")
            
        for valid, validqty in products:
                
            value = data[valid]
            
            file.write("\n")
                
            file.write( str(valid) + " " *(5-len(str(valid))) + "\t" + (data[valid][0] + " "*(30-len(data[valid][0]))) + "\t" + (data[valid][1])+ " " *(5-len(str(data[valid][1]))) + "\t" + (str(validqty))
                        + " " *(5-len(str(validqty))) + "\t" + "\t" + (data[valid][3]) + " " *(5-len(data[valid][3])))
        file.write("\n")
        file.write("-------------------------------------------------------------------------------")
        file.write("\n")
        # Create a subtotals blank list  
        subtotals = []
        # calculate total price and bill amount including shipping charge
        for valid, validqty in products:
                
            subtotal = int(data[valid][3].replace("$","").replace(" ","")) * validqty
                
            subtotals.append(subtotal)
                
            total_price = sum(subtotals)
                
            file.write("Subtotal price of product: $" + str(int(data[valid][3].replace("$","").replace(" ","")) * validqty) + "\n")
                
        # calculate total price and bill amount including including vat amount
        total_price = sum(subtotals)
            
        vat_amount = total_price *0.13
            
        bill_amount = total_price + vat_amount
            
        file.write("Your total Price(With out vat): $" + str(total_price) + "\n")
            
        file.write("Vat amount includes (13%): $" + str(float(vat_amount)) + "\n")
            
        file.write("Your total price (With vat):$ " + str(total_price + float(vat_amount)) + "\n")
            
        file.write("You need to pay total amount is: $" + str(bill_amount)+"\n")
            
        file.write("\n")
            
        file.write("***********Thank you for using our system************"+ "\n")
        # Close the file       
        file.close()
    except KeyError:
        print("Sorry, Your furniture id is invalid.")
    except ValueError:
        print("Sorry, Your furniture quantity is invalid.")
    except IOError:
        print("Sorry, Your write file is not work.")
    except Exception as e:
        print("This error is in purchase bill:",str(e))
    
    
# Define a function to create a bill for the seller
def create_seller_bill ( data,  products,  shipping_charge,  vat_amount, date, customer_name, value):
    """
    Create a seller bill in .txt file after purchase the items

    Arguments:
         data: furniture data in dictionary
         products: this is product list with quantity
         vat_amount: vat amount is in float
         date: this is a current date and time for uniqe bill
         employee_name: purchaser name in string
         value: this is the total value of products
    Returns:
       None
    """
    try:
        #Here current date and time 
        year = str(datetime.now().year)
        month = str(datetime.now().month)
        day = str(datetime.now().day)
        hour = str(datetime.now().hour)
        minute = str(datetime.now().minute)
        second = str(datetime.now().second)
        date = year +'-'+ month + "-" + day + " " + hour + " "+ minute + " " + second
            
        filename = "seller_bill_" + date + ".txt"
        # open the file in write mode
        file = open ( filename, "w" )
            
                
        file.write("***********Selling bill from BRJ furniture store************"+ "\n")
        file.write("Employee_name: " + (customer_name)+ "\n")
        file.write("Date @ time:"+ date +"\n")
        file.write("\n")
            
        file.write("===============================================================================")
        file.write("\n")
        file.write("ID\t Brand Name \t \t \t Product Name \t Quantity \t Price")
        file.write("\n")
        file.write("===============================================================================")
        file.write("\n")
            
        for valid, validqty in products:
            value = data[valid]
            file.write("\n")
            file.write(str(valid) + " " *(5-len(str(valid))) + "\t" + (data[valid][0] + " " *(30-len(data[valid][0]))) + "\t" + (data[valid][1])+ " " *(5-len(str(data[valid][1]))) + "\t" + (str(validqty))
                        + " " *(5-len(str(validqty))) + "\t" + "\t" + (data[valid][3]) + " " *(5-len(data[valid][3])))
        file.write("\n")
            
        file.write("-------------------------------------------------------------------------------")
            
        file.write("\n")
        # Create a subtotals blank list      
        subtotals = []
            
        # calculate total price and bill amount including shipping charge
        for valid, validqty in products:
                
            subtotal = int(data[valid][3].replace("$","").replace(" ","")) * validqty
                
            subtotals.append(subtotal)
                
            total_price = sum(subtotals)
                
            file.write("Subtotal price of product: $" + str(int(data[valid][3].replace("$","").replace(" ","")) * validqty) + "\n")
                
        # calculate total price and bill amount including including vat amount
        total_price = sum(subtotals)
        vat_amount = total_price *0.13
        bill_amount = total_price + vat_amount + shipping_charge
            
        file.write("Your total Price(With out vat):$ " + str(total_price) + "\n")
            
        file.write("Vat amount include (13%):$ " + str(float(vat_amount)) + "\n")
            
        file.write("Total price (With vat):$ " + str(total_price + float(vat_amount)) + "\n")
            
        file.write("Shipping Charge:$ " + str(shipping_charge)+"\n")
            
        file.write("You need to pay your total amount: $ " + str(bill_amount ) +"\n" )
            
        file.write("\n")
            
        file.write("***********Thank you for using our system************"+ "\n")
        # Close the file  
        file.close()
    except KeyError:
        print("Sorry, Your furniture id is invalid.")
    except ValueError:
        print("Sorry, Your furniture quantity is invalid.")
    except IOError:
        print("Sorry, Your write file is not work.")
    except Exception as e:
        print("This error is in selling bill:",str(e))
    


       
# Function to write updated furniture data back to the text file
def write_furniture_data(data):
    """
    write the update furniture data  back to the stock file

    Arguments:
       data: Here, furniture data dictionary
    Returns:
       None
    """
    
    # open the file in write mode
    file =open("stock.txt", 'w')
    # Here, Iterater over the funiture data in dictionary
    for key, value in data.items():
        # Write each furniture item to the file
        file.write(",".join(value) + "\n")
    # Close the file    
    file.close()




 
