class Node:
    def __init__(self, tokens):
        self.children = []
        self.parse_root(tokens)

    def add_leaf(self, leaf):
        if leaf == '$':
            return
        self.children.append(leaf)

    def add_leaves(self, leaves):
        for leaf in leaves:
            if leaf == '$':
                del leaves[leaves.index(leaf)]
        self.children = self.children + leaves

    def parse_decl(self, tokens):
        node = Node([])
        node.add_leaf(tokens)
        self.children.append(node)
        print('Declaration: ', tokens)
        print(len(self.children))

    def parse_fundecl(self, tokens, parameters, body):
        node = Node([])
        i = 0
        node.add_leaf(tokens[0])  # fun
        i += 1
        node.add_leaf(tokens[1])  # function name
        i += 1
        node.add_leaf(tokens[2])  # (
        i += 1
        tmp_node = Node([])
        tmp_node.add_leaves(parameters)
        i += len(parameters)
        node.add_leaf(tmp_node)  # parameters
        node.add_leaf(tokens[i])  # )
        i += 1
        node.add_leaf(tokens[i])  # {
        i += 1
        tmp_node = Node(body)
        node.add_leaf(tmp_node)  # function body
        i += len(body) + 1
        node.add_leaf(tokens[i])  # }
        i += 1
        self.add_leaf(node)
        print('Function: ', tokens)
        print(node.children)
        print(len(self.children))

    def parse_assignstat(self, tokens):
        print('Statement assignment', tokens)
        node = Node([])
        node.add_leaves(tokens)
        self.add_leaf(node)
        print(node.children)
        print(len(self.children))

    def parse_loopstat(self, tokens, boolexp, body):
        ...

    def parse_ifstat(self, tokens, boolexp, if_body, else_body):
        ...

    def parse_returnstat(self, tokens):
        ...

    def parse_root(self, tokens):
        if len(tokens) == 0:
            return
        index = 0
        token = tokens[index][1]
        token_type = tokens[index][0]
        while index < len(tokens) - 1:
            if index != 0:
                index, token, token_type = self.get_next_token(index, tokens)
                # print('parsing', index, token, token_type)

            if token == '$':
                index, token, token_type = self.get_next_token(index, tokens)
                continue

            elif token == 'int' or token == 'str' or token == 'real':
                # Declaration (one line)
                tmp_tokens = []
                while token != '$':
                    tmp_tokens.append(token)
                    index, token, token_type = self.get_next_token(index, tokens)
                self.parse_decl(tmp_tokens)

            elif token_type == 'id':
                # Assignment Statement (one line)
                tmp_tokens = []
                while token != '$':
                    tmp_tokens.append(token)
                    index, token, token_type = self.get_next_token(index, tokens)
                self.parse_assignstat(tmp_tokens)

            elif token == 'fun':
                # Function (multi line)
                tmp_tokens = []
                tmp_tokens.append(token)  # Add 'fun'
                index, token, token_type = self.get_next_token(index, tokens)
                tmp_tokens.append(token)  # Add 'function name
                index, token, token_type = self.get_next_token(index, tokens)
                tmp_tokens.append(token)  # Add '('
                index, token, token_type = self.get_next_token(index, tokens)

                parenthesis_stack = 1
                tmp_parameters = []
                while parenthesis_stack > 0:
                    if token == '(':
                        parenthesis_stack += 1
                    elif token == ')':
                        parenthesis_stack -= 1
                    tmp_tokens.append(token)
                    tmp_parameters.append(token)
                    index, token, token_type = self.get_next_token(index, tokens)
                del tmp_parameters[-1]

                tmp_tokens.append(token)  # Add '{'
                index, token, token_type = self.get_next_token(index, tokens)

                braces_stack = 1
                tmp_fun_body = []
                while braces_stack > 0:
                    if token == '{':
                        braces_stack += 1
                    elif token == '}':
                        braces_stack -= 1
                    tmp_tokens.append(token)
                    tmp_fun_body.append((token_type, token))
                    index, token, token_type = self.get_next_token(index, tokens)
                del tmp_fun_body[0]
                del tmp_fun_body[-1]

                self.parse_fundecl(tmp_tokens, tmp_parameters, tmp_fun_body)

            elif token == 'loop':
                # Loop Statement (multi line)
                tmp_tokens = []
                token_type = token
                tmp_tokens.append(token)  # Add 'loop'
                index, token, token_type = self.get_next_token(index, tokens)
                tmp_tokens.append(token)  # Add '('
                index, token, token_type = self.get_next_token(index, tokens)

                boolexp = []
                parenthesis_stack = 1
                while parenthesis_stack > 0:
                    if token == '(':
                        parenthesis_stack += 1
                    elif token == ')':
                        parenthesis_stack -= 1
                    tmp_tokens.append(token)
                    boolexp.append((token_type, token))
                    index, token, token_type = self.get_next_token(index, tokens)
                del boolexp[-1]

                tmp_tokens.append(token)  # Add '{'
                index, token, token_type = self.get_next_token(index, tokens)

                loop_body = []
                braces_stack = 1
                while braces_stack > 0:
                    if token == '{':
                        braces_stack += 1
                    elif token == '}':
                        braces_stack -= 1
                    tmp_tokens.append(token)
                    loop_body.append((token_type, token))
                    index, token, token_type = self.get_next_token(index, tokens)
                del loop_body[-1]

                self.parse_loopstat(tmp_tokens, boolexp, loop_body)

            elif token == 'if':
                # If Statement (multi line)
                tmp_tokens = []
                tmp_tokens.append(token)  # Add 'if'
                index, token, token_type = self.get_next_token(index, tokens)
                tmp_tokens.append(token)  # Add '('
                index, token, token_type = self.get_next_token(index, tokens)

                conditional = []
                parenthesis_stack = 1
                while parenthesis_stack > 0:
                    if token == '(':
                        parenthesis_stack += 1
                    elif token == ')':
                        parenthesis_stack -= 1
                    tmp_tokens.append(token)
                    conditional.append((token_type, token))
                    index, token, token_type = self.get_next_token(index, tokens)
                del conditional[-1]

                tmp_tokens.append(token)  # Add '{'
                index, token, token_type = self.get_next_token(index, tokens)

                if_body = []
                braces_stack = 1
                while braces_stack > 0:
                    if token == '{':
                        braces_stack += 1
                    elif token == '}':
                        braces_stack -= 1
                    tmp_tokens.append(token)
                    if_body.append((token_type, token))
                    index, token, token_type = self.get_next_token(index, tokens)
                del if_body[-1]

                else_body = []
                if token == 'else':
                    tmp_tokens.append(token)  # Add 'else'
                    index, token, token_type = self.get_next_token(index, tokens)
                    tmp_tokens.append(token)  # Add '{'
                    index, token, token_type = self.get_next_token(index, tokens)
                    braces_stack = 1
                    while braces_stack > 0:
                        if token == '{':
                            braces_stack += 1
                        elif token == '}':
                            braces_stack -= 1
                        tmp_tokens.append(token)
                        else_body.append((token_type, token))
                        index, token, token_type = self.get_next_token(index, tokens)
                    del else_body[-1]

                self.parse_ifstat(tmp_tokens, conditional, if_body, else_body)

            elif token == 'return':
                # Return Statement (one line)
                tmp_tokens = []
                while token != '$':
                    tmp_tokens.append(token)
                    index, token, token_type = self.get_next_token(index, tokens)
                self.parse_returnstat(tmp_tokens)

            else:
                # Raise error
                print('PARSER ERROR: ILLEGAL TOKEN: ', token_type, token)
                return

    @staticmethod
    def get_next_token(index, tokens):
        # print("get next", index, tokens[index][1], tokens[index][0])
        index += 1
        # Returns index, token, token_type
        return index, tokens[index][1], tokens[index][0]


class ParseTree:
    def __init__(self, tokens):
        self.root = Node(tokens)
