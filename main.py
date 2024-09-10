'''
Here we can import function name from different file
when we necessary to access the function foor run the program
'''
# Here, import form read.py file 
from read import load_furniture_data
# Here, import form write.py file 
from write import update_furniture_stock, create_bill, create_seller_bill,write_furniture_data
# Here, import form operation.py file 
from operation import display_furniture, sell_furniture, purchase_furniture

# define main loop this is a main method
def main_loop(data):
    """
    The main loop of the program that handles user interctions.

    Arguments:
      user choose the opetion given below
    Returns:
     The value in the foorm of dictionary containing that furniture data acoording to user response.
        """
    # Here, the continue loop is in the user choose exit the program
    while True:
        try:
            # Display menu options for the user want to do.
            print("_____________________________________________________________________")
            print("\t\t\tChoose your option here !!")
            print("_____________________________________________________________________")
            print("\t\t\tPress 1 for sell the product \n")
            print("\t\t\tPress 2 for purchase the product \n")
            print("\t\t\tPress 3 for exit the program")
            print("_____________________________________________________________________")

            # Get the user's choice what you want in program.
            ans = int(input("\n Enter your choice :"))
            # Here, create the space
            print(" ")
            
            # handle user's choice according to user input.
            #Here, user's choice is 1.
            if ans == 1:
                # Display all the BRJ furniture items with detials 
                display_furniture(data)
                # call the sell_furniture items with detials from operation.py 
                sell_furniture(data)
                # call the write furniture data update
                write_furniture_data(data)
                
            #Here, user's choice is 2.
            elif ans == 2:
                    
                # Display all the BRJ furniture items with detials
                display_furniture(data)
                    
                # call the purchase_furniture items with detials from operation.py 
                purchase_furniture(data)
                # call the write furniture data update
                write_furniture_data(data)
                   
            #Here, user's choice is 3.
            elif ans == 3:
                #Here, exit the selling and buying process.
                print("\n Thank you for using our system . Good Bye !!!")# Here, show the thank you message.
                #Here, break the loop 
                break
            else:
                #Here, whene user inpute not allow to input this program 
                print("\n Sorry your input is invalid ")# Here, show the invalid message.
        except ValueError:
            print("Sorry: Your input value is invalid. please enter a number(1-3)")
        except Exception as e:
            print("Sorry: This error occur in main.py", str(e))
#Here, define main function
def main():
    
    """
    The main function implement the program.
    """
    try:
        filename = "stock.txt"
        data = load_furniture_data(filename)
        main_loop(data)
    except FileNotFoundError:
        print("Sorry: I can't found your stoc.txt.")
    except Exception as e:
        print("You can seen this error found in 'stock.txt' main.py!!")
main()
        
