# Step 1: Inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
perform = input("Enter the operation (e.g., add): ").strip().lower()

if perform in ["add", "addition", "sum", "plus"]:
    correct_sum = num1 + num2
    print("✅ The calculated result is:", correct_sum)

    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        user_thinks = input("What do YOU think the result is? ").strip()

        if user_thinks.isdigit():
            user_result = int(user_thinks)

            if user_result == correct_sum:
                print("🎉 That's correct! You got it right.")
                break
            else:
                attempts += 1
                print("❌ That's not the correct sum.")

                if attempts == 1:
                    explain = input("Would you like me to explain it step-by-step? (yes/no): ").strip().lower()
                    if explain == "yes":
                        print(f"👉 Step: {num1} + {num2} = {correct_sum}")
                elif attempts == 2:
                    print("🤝 I understand your view, but math says the correct answer is:", correct_sum)
                elif attempts == max_attempts:
                    print("🧠 Let's agree to disagree for now. But I'm confident the sum is:", correct_sum)
        else:
            print("⚠️ Please enter a number.")
            attempts += 1
else:
    print("❌ Sorry, currently only addition is supported.")
