class LexLine:
    def __init__(self, line, debug=False):
        self.line = line
        self.debug = debug

        self.temp = ''
        self.flag = 0
        self.dot_flag = False
        self.tokens = []
        self.current = ''

        self.operators = ['<', '>', '=', '!', '*', '/', '%', '+', '-']
        self.symbols = ['{', '}', '[', ']', '(', ')', '.', ',', '"']
        self.keywords = ['int', 'str', 'real', 'fun', 'if', 'else', 'loop', 'and', 'or']

        self.tokenize()

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


if __name__ == '__main__':
    test_line = 'result = one + two'
    lex = LexLine(test_line)
    print(lex.tokens)
