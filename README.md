# python-bubble-sort
"Python-based Bubble Sort implementations showcasing algorithmic logic, dynamic user-input parsing, and optimized sorting techniques."

This repository contains two different implementations of the Bubble Sort algorithm, ranging from a basic static version to an advanced, user-interactive version.

**Versions Overview**

**1. Basic Bubble Sort (python-bubble-sort-v1.py)**
This version focus on the core logic of the algorithm using a predefined array.

Optimization: Includes an isSorted flag to terminate the loop early if the array becomes sorted before all passes are complete, improving efficiency.

Static Input: Uses a hardcoded array: [5, 1, 8, 2, 7, 4, 3, 6, 9].

Educational Focus: Clear comments explaining the comparison and swapping phases.

**2. Advanced Bubble Sort (python-bubble-sort-v2.py)**
A more robust and professional implementation suitable for real-world testing.

Dynamic Input: Allows users to enter numbers separated by either spaces or commas.

Error Handling: Utilizes try-except blocks to catch ValueError if the user enters non-numeric data.

Modular Structure: Organized using a main() function and the if __name__ == "__main__": idiom for better script execution control.

**How to Run**
Ensure you have Python installed on your system.

Clone this repository or download the files.

Open your terminal or command prompt and run the advanced version:

Bash
python python-bubble-sort-v2.py

Time Complexity AnalysisThe algorithm's efficiency is measured as follows:Best Case: $O(n)$ (When the array is already sorted, thanks to the optimization flag).Average/Worst Case: $O(n^2)$.

**Author**
Ankit Suthar
B.Tech in Computer Science and Engineering (Specialization: Data Science)

