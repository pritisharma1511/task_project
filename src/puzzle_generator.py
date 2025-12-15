import random

def generate_puzzle(difficulty):
    """
    Generates a math puzzle based on the given difficulty.
    
    Args:
        difficulty (str): "Easy", "Medium", or "Hard".
        
    Returns:
        dict: containing 'question_text', 'answer', 'difficulty'
    """
    op = "+"
    num1 = 0
    num2 = 0
    
    if difficulty == "Easy":
        # Simple addition/subtraction, numbers 1-10
        op = random.choice(["+", "-"])
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        
    elif difficulty == "Medium":
        # Add/Sub 10-50, Mult 1-10
        op = random.choice(["+", "-", "*"])
        if op == "*":
            num1 = random.randint(2, 9)
            num2 = random.randint(2, 9)
        else:
            num1 = random.randint(10, 50)
            num2 = random.randint(10, 50)
            
    elif difficulty == "Hard":
        # Add/Sub 50-100, Mult 5-15, Div (integer results)
        op = random.choice(["+", "-", "*", "/"])
        if op == "*":
            num1 = random.randint(5, 15)
            num2 = random.randint(5, 15)
        elif op == "/":
            num2 = random.randint(2, 10)
            answer = random.randint(2, 12)
            num1 = num2 * answer
        else:
            num1 = random.randint(50, 100)
            num2 = random.randint(50, 100)
    
    # Ensure positive results for subtraction (optional, but good for kids)
    if op == "-" and num1 < num2:
        num1, num2 = num2, num1
        
    question_text = f"{num1} {op} {num2}"
    
    if op == "+":
        answer = num1 + num2
    elif op == "-":
        answer = num1 - num2
    elif op == "*":
        answer = num1 * num2
    elif op == "/":
        answer = num1 // num2
        
    return {
        "question": question_text,
        "answer": answer,
        "difficulty": difficulty
    }
