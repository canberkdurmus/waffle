class LexLine:
    def __init__(self, line, debug=False):
        self.line = line
        self.debug = debug

        self.temp = ''
        self.flag = 0
        self.dot_flag = False
        self.current = ''
        self.tokens = []
        self.classified = []

        self.operators = ['<', '>', '=', '!', '*', '/', '%', '+', '-']
        self.symbols = ['{', '}', '[', ']', '(', ')', ',', '"']
        self.keywords = ['int', 'str', 'real', 'fun', 'if', 'else', 'loop', 'and', 'or']

        self.assign_ops = ['=', '*=', '/=' '%=', '+=', '-=']
        self.bool_ops = ['<', '>' '<=', '>=', '==', '!=']
        self.unary_ops = ['+', '-', '*', '/', '!', '++', '--', '%']
        self.identifier_set = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_")

        self.tokenize()
        self.classify()

    def tokenize(self):
        for current in self.line:
            self.current = current
            if self.debug:
                print(current, self.flag)

            if current in self.symbols:
                if self.flag == 0:
                    self.temp += self.current
                    self.terminate_token()
                else:
                    self.terminate_token()
                    self.tokens.append(self.current)
                # self.tokens.append(current)
                continue

            if self.flag == 0:
                # Head is not set yet
                # Check the current, if it is valid: set the flag, if not: continue to the next one with flag zero
                self.flag = self.flag_value()
                if self.flag != 0:
                    self.temp += self.current
                continue

            elif self.flag == 1:
                # Head is a letter
                # Terminate case: not letter or '_'
                # Continue case: letter or '_'
                if self.current.isalpha() or self.current == '_':
                    self.temp += self.current
                    continue
                else:
                    # TERMINATE TOKEN
                    self.terminate_token()
                    continue

            elif self.flag == 2:
                # Head is a number
                # Terminate case:
                #   if '.' and dot_flag is not set -> set the dot_flag, add '.' to temp and continue
                #   if '.' and dot_flag is set -> unset the dot_flag, raise error (number with two floating points)
                #   else if it is not a number terminate

                if self.current == '.':
                    if not self.dot_flag:
                        self.temp += self.current
                        continue
                    else:
                        # There are two dots in the number raise error
                        print('ERROR: There are two floating points in real number')
                        break
                elif self.current.isnumeric():
                    self.temp += self.current
                    continue
                else:
                    # TERMINATE TOKEN
                    self.terminate_token()
                    continue

            elif self.flag == 3:
                # Head is an operator
                # if current is an operator, add it to tokens and terminate
                # if current is not an operator, terminate token
                if self.current in self.operators:
                    self.temp += self.current
                    # TERMINATE TOKEN
                    # self.terminate_token()
                    continue
                else:
                    # TERMINATE TOKEN
                    self.terminate_token()
                    continue
        self.terminate_token()

    def terminate_token(self):
        if self.debug:
            print('terminate')
        if self.temp != '':
            self.tokens.append(self.temp)
        self.temp = ''
        self.flag = self.flag_value()
        if self.flag != 0:
            self.temp += self.current

    def flag_value(self):
        if self.current.isalpha():
            return 1
        elif self.current.isnumeric():
            return 2
        elif self.current in self.operators:
            return 3
        else:
            return 0

    def classify(self):
        for token in self.tokens:
            if token in self.symbols:
                self.classified.append(('symbol', token))
            elif token in self.keywords:
                self.classified.append(('keyword', token))
            elif token in self.assign_ops:
                self.classified.append(('assign_op', token))
            elif token in self.bool_ops:
                self.classified.append(('bool_op', token))
            elif token in self.unary_ops:
                self.classified.append(('unary_op', token))
            elif all(k in self.identifier_set for k in token):
                self.classified.append(('id', token))
            elif self.is_int(token):
                self.classified.append(('int_num', token))
            elif self.is_real_num(token):
                self.classified.append(('real_num', token))
            else:
                # RAISE UNKNOWN TYPE ERROR
                print('ERROR Unknown Type: ', token)
                self.classified.append(('unknown', token))

    def print_tokenized(self):
        print(self.line, end='')
        if len(self.line) < 50:
            for i in range(50 - len(self.line)):
                print('.', end='')
        else:
            print('\t', end='')
        print(self.tokens)

    def print_classified(self):
        print(self.line, end='')
        if len(self.line) < 50:
            for i in range(50 - len(self.line)):
                print('.', end='')
        else:
            print('\t', end='')
        print(self.classified)

    @staticmethod
    def is_real_num(number):
        try:
            float(number)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_int(number):
        try:
            a = float(number)
            b = int(a)
        except (TypeError, ValueError):
            return False
        else:
            return a == b


if __name__ == '__main__':
    test_line = 'result = one + two'
    lex = LexLine(test_line)
    lex.print_tokenized()
    lex.print_classified()
