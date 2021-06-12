from lexical_analyzer import LexicalAnalyzer
from parser import Parser

if __name__ == '__main__':
    lexical_analyzer = LexicalAnalyzer('light.waffle')

    parser = Parser(lexical_analyzer.tokens)

# Bug List:
# I can tokenize infinite number of symbols together
# I can tokenize infinite length numbers or strings

# Waffle Code:
# id, operators, symbols, constants, spaces, tabs, multi-line statements etc.

# To-do List:
# Add 'get_next_token' for assignment paper
# Driver code in main.py
# Create a tokenized string to put next to the raw string in a new file for checking tokenization
# Prepare a proper list of token types
# Add token classifier to lexical analyzer
# Create a proper and universal error handling procedure

# Principles:
# File should be read as array of lines
# Lines should be converted to array of LexLines, tokenization should be executed in initialization
# LexLines should be converted to further things for next steps
