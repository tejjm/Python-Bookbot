# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

BookBot is a Python command-line program that scans a given book file (in .txt format) and performs text analysis. It counts the total number of words, determines the frequency of each character (A–Z), and displays results in a clean, readable format.

Features
Reads and analyzes any text file provided via command-line argument

Counts total number of words in the text

Generates frequency statistics for each alphabetic character (case-insensitive)

Outputs results in descending order of character frequency

Simple modular structure using functional programming

How It Works
The user runs the script from the command line with a text file path argument.

The program reads the file, counts the number of words, and builds a dictionary mapping each alphabetic character to its count.

The character-frequency data is sorted and displayed neatly.

Usage
Save your book (for example, frankenstein.txt) inside a books/ folder.

Run the script in the terminal:

text
python main.py books/frankenstein.txt
The console will display a formatted report showing:

Total word count

Each character’s frequency sorted from most to least frequent

What I Practiced & Learned
Handling command-line arguments with sys.argv

File reading and text processing

Building and sorting dictionaries in Python

String manipulation and conditional character filters

Organizing reusable utility functions across modules

File Structure
BookBot/
├── main.py
├── stats.py
├── books/ (contains .txt files)
└── README.md

Example Output
text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 78,432 total words
--------- Character Count -------
e: 9274
t: 6823
a: 6132
...
============= END ===============
