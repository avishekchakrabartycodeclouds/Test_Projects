num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
perform = input("Enter the operation: ").strip().upper()


if perform == "ADD":
    
    example_code = f'''# Example code to add two numbers
a = {num1}
b = {num2}
sum = a + b
print("The sum of", a, "and", b, "is", sum)
'''   
    print("Here is the code")
    print(example_code)  

    
    file = "example.txt"
    with open(file, "w") as f:
        f.write(example_code)
    print(f" Snippet saved to '{file}'")



    





