import argparse
import re
from collections import Counter

# Common English stop words to ignore
STOP_WORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 
    'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 
    'to', 'was', 'were', 'will', 'with'
}

def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            
            # Count sentences (simple approach: count punctuation marks)
            sentences = re.split(r'[.!?]+', text)
            num_sentences = len([s for s in sentences if s.strip()])
            
            # Extract words and clean them
            words = re.findall(r'\b\w+\b', text.lower())
            filtered_words = [word for word in words if word not in STOP_WORDS]
            
            # Calculate statistics
            total_words = len(words)
            avg_word_length = sum(len(word) for word in words) / total_words if total_words else 0
            
            # Get top 5 frequent words (excluding stop words)
            word_counts = Counter(filtered_words)
            top_words = word_counts.most_common(5)
            
            # Print the report
            print("\nFile Analysis Report:")
            print("---------------------")
            print(f"Total number of words: {total_words}")
            print("\nTop 5 most frequent words (excluding stop words):")
            for word, count in top_words:
                print(f"  - {word}: {count} occurrences")
            print(f"\nAverage word length: {avg_word_length:.2f} characters")
            print(f"Number of sentences: {num_sentences}")
            
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Analyze a text file and provide statistics.')
    parser.add_argument('file', help='Path to the text file to analyze')
    args = parser.parse_args()
    
    analyze_file(args.file)

if __name__ == "__main__":
    main()
