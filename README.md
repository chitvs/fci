# Interactive quiz

This repository contains a collection of quiz questions designed for interactive assessments. These questions are primarily focused on topics related to **computer networks**, **signal processing**, **routing protocols**, **TCP**, and other core concepts, making them ideal for anyone preparing for exams or practicing foundational concepts in **telecommunications** and **internet fundamentals**.

## Repository structure

The repository is organized as follows:

```
fci/
├── main.py             
├── questions/        
├── images/           
└── answers/           
```

- Interactive quiz script: the `main.py` Python script runs the quiz interactively. It selects questions randomly, displays them (along with images, if applicable), and provides immediate feedback on user responses.
  
- Questions: each question is stored in a separate `.txt` file located in the `/questions` folder (e.g., `q1.txt`, `q2.txt`, ...). The questions cover diverse topics and are numbered sequentially for easy identification and management.

- Images: some questions include diagrams or figures to aid understanding. These images are stored in the `/images` directory and are named corresponding to their question files (e.g., `q17.png` for question 17). These visuals are automatically displayed during the quiz.

- Answers: the `/answers` folder contains the correct answers for each question in corresponding `.txt` files (e.g., `q1+.txt`, `q2+.txt`, ...). These are used to validate user responses during the interactive quiz.

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
   - The user can type "stop" at any time to end the quiz.
