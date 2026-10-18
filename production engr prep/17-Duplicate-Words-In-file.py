'''
Write a script that reads an arbitrary number of csv files from the terminal and return a log of words that duplicate across different files.

response  should be like:
{
word1: [file1, file2, file3],
word2: [file 2, file3];
…}
'''


from collections import defaultdict
from sys import argv, exit

def find_duplicated_words(filepaths):
    '''
    approach is to use a dictionary to map each word to the files that it occurs in, then if it occurs in more than one file, those are the ones
    we are interested in.
    '''
    word_index = defaultdict(set)
    for filepath in filepaths:
        try:
            with open(filepath, "r") as file:
                for line in file:
                    words = line.strip().split(",")
                    words = [word.strip().lower() for word in words]
                    for word in words:
                        word_index[word].add(filepath)
        except OSError as e:
            raise OSError(f"Could not open {filepath}: {e}") from e
            
    return word_index

if __name__ == "__main__":
    cmd_arguments = argv
    if len(cmd_arguments) < 3:
        print(f"Usage is: {cmd_arguments[0]} <file1> [file2, ...]")
        exit(1)
    files = cmd_arguments[1:]
    word_index = find_duplicated_words(files)
    result = {word: list(files) for word, files in word_index.items() if len(files) > 1}
    print(result)