from lex_line import LexLine


class LexicalAnalyzer:
    def __init__(self, filename):
        print('\n== Starting of lexical analysis == \n')
        source_file = open(filename, 'r')
        self.tokens = []

        lines = source_file.readlines()

        for line in lines:
            line = line.replace('\n', '')
            if len(line) == 0 or line[0] == '#':
                continue
            lex = LexLine(line, debug=False)
            lex.print_classified()

            for token in lex.classified:
                self.tokens.append(token)

            self.tokens.append(('symbol', '$'))

        # print(self.tokens)
        print('\n== End of lexical analysis == \n')
