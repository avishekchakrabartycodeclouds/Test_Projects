questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A) Mumbai", "B) Delhi", "C) Kolkata", "D) Chennai"],
        "answer": "B"
    },
    {
        "question": "What is the capital of Brazil?",
        "options": ["A) Rio de Janeiro", "B) São Paulo", "C) Brasília", "D) Salvador"],
        "answer": "C"
    },
    {
        "question": "What is the capital of Pakistan?",
        "options": ["A) Lahore", "B) Karachi", "C) Islamabad", "D) Peshawar"],
        "answer": "C"
    },
    {
        "question": "What is the capital of China?",
        "options": ["A) Shanghai", "B) Beijing", "C) Shenzhen", "D) Chengdu"],
        "answer": "B"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["A) Sydney", "B) Melbourne", "C) Canberra", "D) Brisbane"],
        "answer": "C"
    }
]

# Start with zero money
money = 0

# Loop through questions
for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    
    user_input = input("Your answer (A/B/C/D): ").strip().upper()

    if user_input == q["answer"]:
        money += 1000  # Add ₹1000
        print("✅ Correct! You have won Rs.", money)
   