# 🐍 The Python Terminal Collection

A curated collection of interactive command-line applications built to master fundamental computer science concepts, algorithms, and Python data structures.

## 📂 The Projects

| Project | Description | Core Concepts Explored | 
 | ----- | ----- | ----- | 
| **💰 The Greedy Cash Register** | A checkout simulator that validates payments and dispenses exact change using the fewest possible bills and coins. | Greedy Algorithms, `while` Loops, Modulo Math | 
| **✈️ The Secure Aeronautical Black Box Analyzer** | A telemetry parser that scans immutable flight logs to extract maximum speeds and calculate altitude differentials. | Tuples, Immutability, Sequence Unpacking, Slicing | 
| **🎧 The Live DJ Queue Manager** | A dynamic, menu-driven tracklist simulator that handles standard queuing, VIP line-skipping, and duplicate prevention. | Lists, Array Methods, `try/except` Error Handling | 

## ✨ Technologies

* `Python 3`

* Standard Library (No external dependencies required)

## 📍 The Process

Each project in this repository tackles a specific programming challenge:

* **The Cash Register** forced me to navigate floating-point math errors by converting everything to cents and writing a cascade of modulo operations.

* **The Black Box Analyzer** taught me the importance of data integrity by utilizing strictly immutable `tuples` instead of lists.

* **The DJ Queue** brought it all together with robust interactive menus, protecting against user input errors and empty-list crashes.

It's a terminal-based playground, but I'm incredibly proud of how clean, robust, and crash-resistant the logic turned out across all three scripts!

## 🚦 Running the Repository Locally

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/OmarAwashreh/Python-Portfolio.git


2. Ensure you have Python 3 installed on your system.

3. Open your terminal and navigate into the project directory:
   
   ```bash
   cd Python-Portfolio

4. Run any of the individual scripts using Python:

   ```bash
   python TheLiveDJQueueManager.py
