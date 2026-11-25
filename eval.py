from rag import ask

# 10 questions YOU write about your docs
QUESTIONS = [
    "What is the payroll cutoff process?",
    "How to create a new vendor?",
    "What are the approval levels for expense?",
    "How to run month-end close?",
    "What is the leave policy for contractors?",
    # Add 5 more from your docs
]

correct = 0
for q in QUESTIONS:
    ans, chunks = ask(q)
    print(f"\nQ: {q}\nA: {ans[:200]}...")
    # You manually mark 1 if good, 0 if bad
    score = int(input("Good? (1/0): "))
    correct += score

print(f"\nEval Result: {correct}/{len(QUESTIONS)} grounded answers")