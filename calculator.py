print("Python Calculator")

a = float(input("Enter your first number: "))
op = input("Operator (+,-,*,/): ")
b = float(input("Enter second number: "))

if op == "+":
	print (a + b)

elif op == "-":
	print (a - b)

elif op == "*":
	print (a * b)

elif op == "/":
	print (a / b)

else:
	print ("invalid operator")
