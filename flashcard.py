import json
import random
import os

FLASHCARDS_FILE = 'flashcards.json'

def load_flashcards():
    if os.path.exists(FLASHCARDS_FILE):
        with open(FLASHCARDS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_flashcards(flashcards):
    with open(FLASHCARDS_FILE, 'w') as f:
        json.dump(flashcards, f, indent=4)

def add_flashcard(flashcards):
    question = input("Enter the question: ").strip()
    answer = input("Enter the answer: ").strip()
    if question and answer:
        flashcards.append({'question': question, 'answer': answer})
        print("Flashcard added successfully.")
    else:
        print("Both question and answer are required.")

def take_quiz(flashcards):
    if not flashcards:
        print("No flashcards available. Please add some first.")
        return
    score = 0
    random.shuffle(flashcards)
    for idx, card in enumerate(flashcards, 1):
        print(f"\nQuestion {idx}: {card['question']}")
        user_answer = input("Your answer: ").strip()
        if user_answer.lower() == card['answer'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {card['answer']}")
    print(f"\nQuiz completed. Your score: {score}/{len(flashcards)}")

def view_flashcards(flashcards):
    if not flashcards:
        print("No flashcards to display.")
        return
    for idx, card in enumerate(flashcards, 1):
        print(f"{idx}. Q: {card['question']} | A: {card['answer']}")

def main():
    flashcards = load_flashcards()
    while True:
        print("\nFlashcard App Menu:")
        print("1. Add Flashcard")
        print("2. Take Quiz")
        print("3. View Flashcards")
        print("4. Save and Exit")
        choice = input("Choose an option (1-4): ").strip()
        if choice == '1':
            add_flashcard(flashcards)
        elif choice == '2':
            take_quiz(flashcards)
        elif choice == '3':
            view_flashcards(flashcards)
        elif choice == '4':
            save_flashcards(flashcards)
            print("Flashcards saved. Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")



if __name__ == "__main__":
    main()
