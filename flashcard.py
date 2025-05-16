import tkinter as tk
import random
import json
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

class FlashcardApp:
    def __init__(self, master):
        self.master = master
        master.title("Flashcard App")

        self.flashcards = load_flashcards()
        self.current_card = {}
        self.score = 0

        self.question_label = tk.Label(master, text="", font=('Helvetica', 18))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(master, font=('Helvetica', 16))
        self.answer_entry.pack(pady=10)

        self.check_button = tk.Button(master, text="Check Answer", command=self.check_answer)
        self.check_button.pack(pady=5)

        self.feedback_label = tk.Label(master, text="", font=('Helvetica', 14))
        self.feedback_label.pack(pady=10)

        self.next_button = tk.Button(master, text="Next Question", command=self.next_card)
        self.next_button.pack(pady=5)

        self.score_label = tk.Label(master, text="Score: 0", font=('Helvetica', 14))
        self.score_label.pack(pady=10)

        self.next_card()

    def next_card(self):
        if not self.flashcards:
            self.question_label.config(text="No flashcards available.")
            return
        self.current_card = random.choice(self.flashcards)
        self.question_label.config(text=self.current_card['question'])
        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        correct_answer = self.current_card['answer']
        if user_answer.lower() == correct_answer.lower():
            self.feedback_label.config(text="Correct!", fg="green")
            self.score += 1
        else:
            self.feedback_label.config(text=f"Incorrect. The correct answer is: {correct_answer}", fg="red")
        self.score_label.config(text=f"Score: {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
if __name__=="__main__":
    main()   
