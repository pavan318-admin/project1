def calculator():
	print("Simple Calculator")
	print("Operations: +, -, *, /")

	first_number = float(input("Enter the first number: "))
	operator = input("Enter an operation: ")
	second_number = float(input("Enter the second number: "))

	if operator == "+":
		result = first_number + second_number
	elif operator == "-":
		result = first_number - second_number
	elif operator == "*":
		result = first_number * second_number
	elif operator == "/":
		if second_number == 0:
			print("Error: cannot divide by zero.")
			return
		result = first_number / second_number
	else:
		print("Error: unknown operation.")
		return

	print(f"Result: {result}")


if __name__ == "__main__":
	calculator()
