
print("""
What do You want to convert for ? """)
enter_what_to_convert = print("""
1. Rupee to Doller
2. Doller to Rupee
3. Exit""")
option = int(input("Select option : "))
if option == 3:
    exit() 
else:
    amount = int(input("Enter the amount to convert : "))


# def rupeeToDollerConverter(dollerAmount):
    dollerAmount = float(amount/73.89)
# return


# def dollerToRupeeConverter(rupeeAmount):
    rupeeAmount = float(amount*73.89)
    # return rupeeAmount
            
    
# def options():
    if option == 3:
        quit()
    elif option == 1:
        print(f"The Doller Value of {amount} is : {dollerAmount}")
    elif option == 2:
        print(f"The Rupee Value of {amount} is : {rupeeAmount}")
    else:
        print("Enter Valid Option!!")


# rupeeToDollerConverter()
# dollerToRupeeConverter()
# options()

                

