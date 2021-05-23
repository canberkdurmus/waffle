class Statement:
    def __init__(self, tokens, statement_type):
        self.success = True
        self.tokens = tokens
        self.statement_type = statement_type
        print('Statement', statement_type, tokens)


class Declaration:
    def __init__(self, tokens):
        self.success = True
        self.tokens = tokens
        print('Declaration: ', tokens)


class Function:
    def __init__(self, tokens):
        self.success = True
        self.tokens = tokens
        print('Function: ', tokens)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.token_type = self.tokens[self.index][0]
        self.token = self.tokens[self.index][1]
        self.parse()

    def get_next_token(self):
        self.index += 1
        self.token_type = self.tokens[self.index][0]
        self.token = self.tokens[self.index][1]

    def parse(self):
        return self.parse_program()

    def parse_program(self):
        while self.index < len(self.tokens) - 1:
            if self.index != 0:
                self.get_next_token()

            if self.token == 'int' or self.token == 'str' or self.token == 'real':
                # Declaration (one line)
                tmp_tokens = []
                while self.token != '$':
                    tmp_tokens.append(self.token)
                    self.get_next_token()
                declaration = Declaration(tmp_tokens)
                if not declaration.success:
                    return False

            elif self.token_type == 'id':
                # Assignment Statement (one line)
                tmp_tokens = []
                while self.token != '$':
                    tmp_tokens.append(self.token)
                    self.get_next_token()
                statement = Statement(tmp_tokens, 'assignment')
                if not statement.success:
                    return False

            elif self.token == 'fun':
                # Function (multi line)
                tmp_tokens = []
                tmp_tokens.append(self.token)  # Add 'fun'
                self.get_next_token()
                tmp_tokens.append(self.token)  # Add 'function name
                self.get_next_token()
                tmp_tokens.append(self.token)  # Add '('
                self.get_next_token()

                parenthesis_stack = 1
                while parenthesis_stack > 0:
                    if self.token == '(':
                        parenthesis_stack += 1
                    elif self.token == ')':
                        parenthesis_stack -= 1
                    tmp_tokens.append(self.token)
                    self.get_next_token()

                tmp_tokens.append(self.token)  # Add '{'
                self.get_next_token()

                braces_stack = 1
                while braces_stack > 0:
                    if self.token == '{':
                        braces_stack += 1
                    elif self.token == '}':
                        braces_stack -= 1
                    tmp_tokens.append(self.token)
                    self.get_next_token()

                statement = Function(tmp_tokens)
                if not statement.success:
                    return False

            elif self.token == 'loop':
                # Loop Statement (multi line)
                tmp_tokens = []
                token_type = self.token
                tmp_tokens.append(self.token)  # Add 'loop'
                self.get_next_token()
                tmp_tokens.append(self.token)  # Add '('
                self.get_next_token()
                parenthesis_stack = 1

                while parenthesis_stack > 0:
                    if self.token == '(':
                        parenthesis_stack += 1
                    elif self.token == ')':
                        parenthesis_stack -= 1
                    tmp_tokens.append(self.token)
                    self.get_next_token()

                tmp_tokens.append(self.token)  # Add '{'
                self.get_next_token()

                braces_stack = 1
                while braces_stack > 0:
                    if self.token == '{':
                        braces_stack += 1
                    elif self.token == '}':
                        braces_stack -= 1
                    tmp_tokens.append(self.token)
                    self.get_next_token()

                statement = Statement(tmp_tokens, token_type)
                if not statement.success:
                    return False

            elif self.token == 'if':
                # Loop Statement (multi line)
                tmp_tokens = []
                token_type = self.token
                tmp_tokens.append(self.token)  # Add 'if'
                self.get_next_token()
                tmp_tokens.append(self.token)  # Add '('
                self.get_next_token()
                parenthesis_stack = 1

                while parenthesis_stack > 0:
                    if self.token == '(':
                        parenthesis_stack += 1
                    elif self.token == ')':
                        parenthesis_stack -= 1
                    tmp_tokens.append(self.token)
                    self.get_next_token()

                tmp_tokens.append(self.token)  # Add '{'
                self.get_next_token()

                braces_stack = 1
                while braces_stack > 0:
                    if self.token == '{':
                        braces_stack += 1
                    elif self.token == '}':
                        braces_stack -= 1
                    tmp_tokens.append(self.token)
                    self.get_next_token()

                if self.token == 'else':
                    tmp_tokens.append(self.token)  # Add 'else'
                    self.get_next_token()
                    tmp_tokens.append(self.token)  # Add '{'
                    self.get_next_token()
                    braces_stack = 1
                    while braces_stack > 0:
                        if self.token == '{':
                            braces_stack += 1
                        elif self.token == '}':
                            braces_stack -= 1
                        tmp_tokens.append(self.token)
                        self.get_next_token()

                statement = Statement(tmp_tokens, token_type)
                if not statement.success:
                    return False

            else:
                # Raise error
                print('RAISE ERROR ILLEGAL TOKEN: ', self.token)
