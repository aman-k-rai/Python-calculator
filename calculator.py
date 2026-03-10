print("Python Calculator")

while True:
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

	again =  input ("Again? (y/n:) ")

	if again != "y":
		break
