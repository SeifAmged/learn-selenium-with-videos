# Learn Selenium with Videos

Welcome to the **Learn Selenium with Videos** project! 🎥🚀  
This project automates the process of finding random Selenium tutorial videos on YouTube, making learning Selenium a fun and interactive experience. It’s literally Selenium teaching you Selenium. 🤖💻

## Installation

Follow these simple steps to get started with the project:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SeifAmged/learn-selenium-with-videos.git
   cd Learn-Selenium-With-Videos
   ```

2. **Create and activate a virtual environment**:
   - On **Windows**:
     ```bash
     python -m venv env
     .\env\Scripts\activate
     ```
   - On **Mac/Linux**:
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

3. **Install the required libraries**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the script**:
   ```bash
   python app.py
   ```

## How It Works

This script, written in Selenium (yes, Selenium is teaching you about itself 😎), does the following:
- Randomly searches for Selenium tutorial videos on YouTube.
- Automatically plays the first video result it finds.
- Puts the video in fullscreen mode for a better learning experience.
- And guess what? It even refreshes your terminal after you're done! 🌀

## Features

- **Hands-free learning**: Let Selenium guide you through YouTube's vast library of tutorial videos.
- **Automated video selection**: No more decision fatigue—Selenium picks the video for you!
- **Fullscreen mode**: Maximize your focus with the video running in fullscreen.
- **History logging**: Every time you run the program, it saves a log of which videos were played and when.

## History Log File (`history.log`)

The program automatically creates a file called `history.log` every time you run the script. This file keeps a record of which videos were played and when.  
It's like your personal assistant that tracks your learning journey! 📜

### How to view the log:
1. After running the script, go to the project folder where the script is saved.
2. You will find a file named `history.log`.
3. Simply double-click on the file, and it will open in a text editor like Notepad (on Windows) or TextEdit (on Mac).
4. You will see entries like:
   ```
   2024-09-04 15:30: Played video: "Selenium Tutorial for Beginners", Search term: "Selenium Python guide"
   ```
   
Each entry tells you which video was played, and at what time. It's a simple way to keep track of your progress and see which videos you've already watched. 📅

## Why This Project?

Sometimes learning can feel like a chore, but with this project, we wanted to make it more fun and hands-free. Imagine Selenium guiding you through its own tutorials—it's like a teacher that never sleeps, never gets tired, and always finds something new for you to learn! Plus, there's a slight irony in using Selenium to teach itself. 😉

So sit back, relax, and let Selenium do the work for you. All you need is your coffee and a comfy chair!

## Conclusion

If you're looking to learn Selenium or just need a break from scrolling through endless tutorial lists, **Learn Selenium with Videos** is the perfect project for you. It's fun, it's simple, and it's powered by the very tool you're trying to learn.

Happy Learning! ☕📚
