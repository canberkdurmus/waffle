class Node:
    def __init__(self, tokens, value):
        self.children = []
        self.value = value
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
        node = Node([], 'decl')
        node.add_leaf(tokens)
        self.children.append(node)
        # print('Declaration: ', tokens)
        # print(len(self.children))

    def parse_fun_decl(self, tokens, parameters, body):
        node = Node([], 'functiondecl')
        i = 0
        node.add_leaf(tokens[i])  # fun
        i += 1
        node.add_leaf(tokens[i])  # function name
        i += 1
        node.add_leaf(tokens[i])  # (
        i += 1
        tmp_node = Node([], 'decls')
        tmp_node.add_leaves(parameters)
        i += len(parameters)
        node.add_leaf(tmp_node)  # parameters
        node.add_leaf(tokens[i])  # )
        i += 1
        node.add_leaf(tokens[i])  # {
        i += 1
        tmp_node = Node(body, 'compoundtat')
        node.add_leaf(tmp_node)  # function body
        i += len(body) + 1
        node.add_leaf(tokens[i])  # }
        i += 1
        self.add_leaf(node)
        # print('Function: ', tokens)
        # print(node.children)
        # print(len(self.children))

    def parse_assign_stat(self, tokens):
        # print('Statement assignment', tokens)
        node = Node([], 'assgstat')
        node.add_leaves(tokens)
        self.add_leaf(node)
        # print(node.children)
        # print(len(self.children))

    def parse_loop_stat(self, tokens, bool_exp, body):
        # print(bool_exp)
        # print(body)
        node = Node([], 'loopstat')
        i = 0
        node.add_leaf(tokens[i])  # loop
        i += 1
        node.add_leaf(tokens[i])  # (
        i += 1
        tmp_node = Node([], 'boolexp')
        tmp_node.add_leaves(bool_exp)
        i += len(bool_exp)
        node.add_leaf(tmp_node)  # bool_exp
        node.add_leaf(tokens[i])  # )
        i += 1
        node.add_leaf(tokens[i])  # {
        i += 1
        tmp_node = Node(body, 'compundstat')
        node.add_leaf(tmp_node)  # loop body
        i += len(body) + 1
        node.add_leaf(tokens[i])  # }
        i += 1
        self.add_leaf(node)
        # print('Loop: ', tokens)
        # print(node.children)
        # print(len(self.children))

    def parse_if_stat(self, tokens, bool_exp, if_body, else_body):
        # print(bool_exp)
        # print(if_body)
        # print(else_body)
        node = Node([], 'ifstat')
        i = 0
        node.add_leaf(tokens[i])  # if
        i += 1
        node.add_leaf(tokens[i])  # (
        i += 1
        tmp_node = Node([], 'boolexp')
        tmp_node.add_leaves(bool_exp)
        i += len(bool_exp)
        node.add_leaf(tmp_node)  # bool_exp
        node.add_leaf(tokens[i])  # )
        i += 1
        node.add_leaf(tokens[i])  # {
        i += 1
        tmp_node = Node(if_body, 'compoundstat')
        node.add_leaf(tmp_node)  # if body
        i += len(if_body) + 1
        node.add_leaf(tokens[i])  # }
        i += 1
        if len(else_body) != 0:
            node.add_leaf(tokens[i])  # else
            i += 1
            node.add_leaf(tokens[i])  # {
            i += 1
            tmp_node = Node(else_body, 'compoundstat')
            node.add_leaf(tmp_node)  # else body
            i += len(else_body) + 1
            node.add_leaf(tokens[i])  # }
            i += 1
        self.add_leaf(node)
        # print('If: ', tokens)
        # print(node.children)
        # print(len(self.children))

    def parse_return_stat(self, tokens):
        # print('Statement return', tokens)
        node = Node([], 'returnstat')
        node.add_leaves(tokens)
        self.add_leaf(node)
        # print(node.children)
        # print(len(self.children))

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
                self.parse_assign_stat(tmp_tokens)

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

                self.parse_fun_decl(tmp_tokens, tmp_parameters, tmp_fun_body)

            elif token == 'loop':
                # Loop Statement (multi line)
                tmp_tokens = []
                tmp_tokens.append(token)  # Add 'loop'
                index, token, token_type = self.get_next_token(index, tokens)
                tmp_tokens.append(token)  # Add '('
                index, token, token_type = self.get_next_token(index, tokens)

                bool_exp = []
                parenthesis_stack = 1
                while parenthesis_stack > 0:
                    if token == '(':
                        parenthesis_stack += 1
                    elif token == ')':
                        parenthesis_stack -= 1
                    tmp_tokens.append(token)
                    bool_exp.append((token_type, token))
                    index, token, token_type = self.get_next_token(index, tokens)
                del bool_exp[-1]

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
                del loop_body[0]
                del loop_body[-1]

                self.parse_loop_stat(tmp_tokens, bool_exp, loop_body)

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
                del if_body[0]
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
                    del else_body[0]
                    del else_body[-1]

                self.parse_if_stat(tmp_tokens, conditional, if_body, else_body)

            elif token == 'return':
                # Return Statement (one line)
                tmp_tokens = []
                while token != '$':
                    tmp_tokens.append(token)
                    index, token, token_type = self.get_next_token(index, tokens)
                self.parse_return_stat(tmp_tokens)

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
        self.root = Node(tokens, 'root')
        print("== Begin Parse Tree Traverse ==")
        self.traverse(self.root, 0)
        print("== End Parse Tree Traverse ==")

    def traverse(self, node, depth):
        for child in node.children:
            if not isinstance(child, Node):
                for i in range(depth):
                    print('|----', end='')
                print(' ', end='')
                print(child)
            else:
                for i in range(depth):
                    print('|----', end='')
                print(child.value)
                self.traverse(child, depth + 1)
