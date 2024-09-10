'''
Define a function
To read and  load the data from  BRJ Furniture store  from Stock.txt file
'''
def load_furniture_data(stock):
    """
    data pass: Loads furniture data from a stock.txt file
    Argumenst:
    Stock : Is the name of the stock.txt file
    
    Returns value:
         return the value in the form of dictionary containing the furniture data from BRJ Furniture store.
   """
    try:
        
        #Here, the file is open for reading 
        file = open("stock.txt","r") # Here, the file is in open
        
        #Here, read all lines from the stock.txt file one by one.
        
        lines= file.readlines() #Here, read all line one by one this is reading mode.
        
        # Initialize an empty dictionary to store the furniture data
        data ={}
        
        # Here the each line start with 1
        key=1
        
        # Read the each line to the file
        for each in lines:
            #remove the newline character and split the lline into a list
            line = each.replace("\n", "").split(",")
                
            #Here,add the line data to the dictionary with the key
            data[key] = line
            # here the key value is added by one
            key = key+1
        
        # Here, i can print wellcom msg in terminal to make attractive.  
        print("---------------*Wellcome to our BRJ Furniture*---------------------------------------\n")
        print("---------------*We can provide good service with good quality products*---------------\n")
        print("---------------*We have current furniture stock*----------------------------------\n")
        
        # Return that data  in dictionary ways
        return data
    except FileNotFoundError:
        print("Sorry: I can't found your stoc.txt.")
    except Exception as e:
        print("You can seen this error found in read.py!!")
    
