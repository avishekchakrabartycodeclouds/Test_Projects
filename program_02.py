# Take user inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
perform = input("Enter the operation (e.g., add): ").strip().lower()

if perform in ["add", "addition", "sum", "plus"]:
    correct_sum = num1 + num2
    print("✅ The calculated result is:", correct_sum)

    # Ask user to confirm if they agree with the result
    user_thinks = input("What do YOU think the result is? ").strip()

    # Check if user entered a number
    if user_thinks.isdigit():
        user_result = int(user_thinks)
        
        if user_result == correct_sum:
            print("🎉 That's correct! You got it right.")
        else:
            print("❌ Actually, that's not correct.")
            print(f"👉 The correct sum of {num1} and {num2} is {correct_sum}.")
            explain = input("Would you like to see how it was calculated? (yes/no): ").strip().lower()
            if explain == "yes":
                print(f"Step: {num1} + {num2} = {correct_sum}")
            else:
                print("👍 No problem. Happy learning!")
    else:
        print("⚠️ That doesn't look like a number.")

else:
    print("❌ Operation not supported (currently only addition is available).")
