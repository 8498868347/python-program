This Python command-line tool analyzes a text file and generates a summary report with the following statistics:
Total word count
Top 5 most frequent words (excluding common stop words like "the," "is," "and")
Average word length
Number of sentences
It is designed to process .txt files and provide quick insights into text content, useful for writers, data analysts, and developers.
This Python script is a command-line tool that analyzes a text file and provides a summary report. It performs the following tasks:
Reads a .txt file - The script takes a file path as a command-line argument and reads the file.
Counts total words - It extracts all words from the file and counts them.
Finds top 5 most frequent words - It ignores common stopwords (like "the", "is", "and") and identifies the most frequently used words.
Calculates average word length - It computes the average length of all words in the file.
Counts the number of sentences - It detects sentence boundaries (using punctuation like ., !, ?) and counts the sentences.
Usage
Run the script from the terminal with:
python file_analyzer.py <file_path>
Example:
python file_analyzer.py sample.txt
