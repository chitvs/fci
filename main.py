import os
import random
from PIL import Image

def extract_correct_answer(answer_file_path):

    with open(answer_file_path, "r", encoding="utf-8") as file:
        return file.read().strip()

def display_image(image_path):

    if os.path.exists(image_path):
        img = Image.open(image_path)
        img.show()

def interactive_quiz():
    print("FCI quiz")

    questions_folder = "questions"
    answers_folder = "answers"
    images_folder = "images"
    
    question_files = [f for f in os.listdir(questions_folder) if f.endswith(".txt")]

    random.shuffle(question_files)

    answers = {}
    score = 0

    for i, question_file in enumerate(question_files):
        question_path = os.path.join(questions_folder, question_file)
        answer_file_path = os.path.join(answers_folder, question_file.replace(".txt", "+.txt"))
        image_path = os.path.join(images_folder, question_file.replace(".txt", ".png"))

        print(f"\nQuestion {i + 1}:")
        with open(question_path, "r", encoding="utf-8") as file:
            question_text = file.read()
            print(question_text)

        display_image(image_path)

        correct_answer = extract_correct_answer(answer_file_path)

        while True:
            answer = input("Your answer (type 'stop' to exit or 'skip'): ").strip().lower()
            
            if answer == "stop":
                print("\nQuiz Interrupted")
                i -= 1  # Stop doesn't count as an iteration
                break

            if answer == "skip":
                print("Skipping this question.\n")
                answers[f"Question {i + 1}"] = "skip"
                break
                
            if answer not in ["a", "b", "c", "d"]:
                print("Wrong answer format! Please type 'a', 'b', 'c', or 'd'.")
                continue

            answers[f"Question {i + 1}"] = answer
            break
            
        if answer == "stop":
            break

        if answer == "skip":
            print(f"Current score: {score} / {i+1}")
            continue

        if correct_answer and answer.strip().lower() == correct_answer.lower():
            score += 1
            print("Correct!")
        else:
            print(f"Wrong :(, correct answer was {correct_answer.lower()}.")
            
        print(f"Current score: {score} / {i+1}")

    print(f"Final score: {score} / {i+1}")

if __name__ == "__main__":
    interactive_quiz()
