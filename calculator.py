def calculator():
    while True:
        operation=input("enter the operation need to perform:") #type +,-,*,/
        number1=int(input("enter number 1:"))
        number2=int(input("enter number 2:"))
        
        

        if operation=='exit':
            print("exiting")
            break

        if operation not in ['+', '-', '*', '/']:
            print("invalid entry of operation")
            continue

        if operation=='+':
            result=number1+number2
        elif operation=='-':
            result=number1-number2
        elif operation=='*':
            result=number1*number2
        elif operation=='/':
            if number2!=0:
                result=number1/number2
            else:
                print("infinity")
        print("Result:",result)

calculator()