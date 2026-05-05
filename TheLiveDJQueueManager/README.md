# 🎧 The Live DJ Queue Manager

A command-line Python application that simulates a live DJ booth's tracklist. It uses a dynamic menu-driven interface to manage a playlist, allowing users to queue, insert, remove, and play songs while actively preventing duplicates and handling user input errors.

## ✨ Technologies

- `Python 3`

## 🚀 Features

- Continuous interactive menu loop for real-time queue management
- Standard queuing (`.append()`) and VIP line-skipping (`.insert()`) functionality
- Built-in validation to prevent duplicate tracks and handle empty-queue crashes
- Index-based track replacement and safe specific-song removal
- Dynamic 1-based queue display with underlying 0-based Python indexing
 
## 📍 The Process

I wanted to build something that heavily utilized Python lists and their built-in methods, and a DJ queue felt like the perfect analogy! I started by creating a basic `while` loop and a menu, then mapped out the different list operations. I used `.append()` for standard requests, `.insert(0)` to let VIPs skip the line, and `.pop(0)` to "play" the next track. The best part was layering in the logic—adding `if/else` checks to prevent duplicate songs and `try/except` blocks to stop the program from crashing if someone tried to replace a song using a bad index or remove a song that wasn't there. It's a terminal app, but it was a fantastic way to master Python list manipulation and robust user input handling!

## 🚦 Running the Project

1. Clone the repository or download `TheLiveDJQueueManager.py`
2. Ensure you have Python 3 installed on your system
3. Open your terminal and navigate to the project directory
4. Run the script: `python TheLiveDJQueueManager.py`

## 🎞️ Preview

```
--- DJ Queue Menu ---
1) Welcome
2) Standard Add
3) VIP Insert
4) Play Next
5) Remove Specific Song
6) Replace Song at Index
7) Display Queue
8) Clear All
9) Exit

Enter your choice (1-9): 1
Welcome to the DJ Booth!

--- DJ Queue Menu ---
...
Enter your choice (1-9): 2
Enter the song name: starboy
Added 'Starboy' to the queue.

--- DJ Queue Menu ---
...
Enter your choice (1-9): 2
Enter the song name: levitating
Added 'Levitating' to the queue.

--- DJ Queue Menu ---
...
Enter your choice (1-9): 2
Enter the song name: starboy
WARNING: 'Starboy' is already in the queue. No duplicates allowed.

--- DJ Queue Menu ---
...
Enter your choice (1-9): 3
Enter the VIP song name: one dance
VIP INSERT: 'One Dance' is now next!

--- DJ Queue Menu ---
...
Enter your choice (1-9): 7

--- Current Queue ---
1. One Dance
2. Starboy
3. Levitating

--- DJ Queue Menu ---
...
Enter your choice (1-9): 4
🎧 NOW PLAYING: One Dance 🎧

--- DJ Queue Menu ---
...
Enter your choice (1-9): 6
Enter the NEW song name: bad guy
Enter the Python index number to replace: 1
Replaced 'Levitating' with 'Bad Guy'.

--- DJ Queue Menu ---
...
Enter your choice (1-9): 5
Enter the song name to remove: starboy
Removed 'Starboy' from the queue.

--- DJ Queue Menu ---
...
Enter your choice (1-9): 8
Queue has been wiped clean!

--- DJ Queue Menu ---
...
Enter your choice (1-9): 4
The queue is currently empty. Please add a song first.

--- DJ Queue Menu ---
...
Enter your choice (1-9): 9
Shutting down the DJ Booth. Goodnight!
```
