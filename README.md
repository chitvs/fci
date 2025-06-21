# Interactive quiz

This repository contains a collection of quiz questions designed for interactive assessments. These questions are primarily focused on topics related to **computer networks**, **signal processing**, **routing protocols**, **TCP**, and other core concepts, making them ideal for anyone preparing for exams or practicing foundational concepts in **telecommunications** and **internet fundamentals**.

## Repository structure

The repository is organized as follows:

- **Interactive quiz script:** the `main.py` Python script runs the quiz interactively. It selects questions randomly, displays them (along with images, if applicable), and provides immediate feedback on user responses.
  
- **Questions:** each question is stored in a separate `.txt` file located in the `/questions` folder (e.g., `q1.txt`, `q2.txt`, ...). The questions cover diverse topics and are numbered sequentially for easy identification and management.

- **Images:** some questions include diagrams or figures to aid understanding. These images are stored in the `/images` directory and are named corresponding to their question files (e.g., `q17.png` for question 17). These visuals are automatically displayed during the quiz (if applicable).

- **Answers:** the `/answers` folder contains the correct answers for each question in corresponding `.txt` files (e.g., `q1+.txt`, `q2+.txt`, ...). These are used to validate user responses during the interactive quiz.

## Getting started

1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/chitvs/fci.git
   cd fci
   ```

2. **Install Python** (if not already installed on your system).

3. **Run the script:**
   ```bash
   python main.py
   ```
   - The script will select and display questions randomly.
   - For questions with associated images, the script will open the corresponding image automatically for better understanding.
   - The user can type "stop" at any time to end the quiz.

4. **Manually browse questions:** if preferred, navigate through the `/questions` folder to view the `.txt` files. Use the images in the `/images` folder for visual references as needed.

## Customization

- **Modify the `main.py` script:** add new functionalities like scoring systems, time tracking, or support for multiple-choice formats.
- **Expand the question bank:** add/edit questions and images in the `/questions` and `/images` folders. Ensure that file naming follows the existing convention for smooth integration.
- **Apply this structure to other topics or exams:** use this repository as a template for quizzes in different subjects or areas of study.
