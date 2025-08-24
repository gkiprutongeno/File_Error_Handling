📂 File Handling & Error Management.
This Python script demonstrates safe and interactive file reading with built-in error handling. It guides users through selecting a file, displays basic file statistics, and previews its content—all while gracefully managing common issues like missing files or permission errors.

🚀 Features
Prompt-based file selection with exit option

Automatic creation of sample text files for testing

Error handling for:

Missing files

Permission issues

Non-text files

Keyboard interruptions

Displays:

Character, word, and line counts

A preview of the first 3 lines of the file

Lists available files in the current directory if input fails

🧰 How It Works
Startup When the script runs, it creates four sample files:

hello.txt

data.txt

emptyfile.txt

list.txt

User Interaction The user is prompted to enter a filename. If the file exists and is readable, the script:

Opens the file

Displays basic stats

Shows a preview of its content

Error Handling If the file is missing or unreadable, the script:

Displays a helpful message

Lists up to 5 available files in the current folder

Continues prompting until the user types exit
