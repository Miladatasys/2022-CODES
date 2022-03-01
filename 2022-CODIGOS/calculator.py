#CALCULATOR

# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE

print("Select an operation to perform :   ")
print("1. ADD")
print("2. SUBSTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation   == "1" :
    #OPERATION FOR ADD
    num1 = input ("Enter first number:  ")
    num2 = input ("Enter second number: ")
    print("the sum is: "     + str(int(num1) + int(num2)))
elif operation == "2":
    #OPERATION FOR SUBSTRACT
    num1 = input ("Enter first number:  ")
    num2 = input ("Enter second number: ")
    print("the minus is: "   + str(int(num1) - int(num2)))
elif operation == "3":
    #OPERATION FOR MULTIPLY
    num1 = input ("Enter first number:  ")
    num2 = input ("Enter second number: ")
    print("the multiply is: " + str(int(num1) * int(num2)))
elif operation == "4":
    #OPERATION FOR DIVIDE
    num1 = input ("Enter first number:  ")
    num2 = input ("Enter second number: ")
    print("the divide is: "   + str(int(num1) / int(num2)))
else:
    print ("INVALID ENTRY")