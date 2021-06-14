class SymbolTable:
    def __init__(self):
        self.table = {}

    def add_symbol(self, symbol, symbol_type):
        if self.symbol_exists(symbol):
            print("TYPE CHECKING ERROR, SYMBOL ALREADY EXISTS (UNIQUENESS CHECK):", symbol, symbol_type)
        else:
            self.table[symbol] = symbol_type

    def symbol_exists(self, symbol):
        return symbol in self.table

    def get_type(self, symbol):
        return self.table[symbol]

    def print_table(self):
        print('--- Symbol Table ---')
        for key in self.table:
            print("|-------|-------|")
            print('|', key, '\t|', self.table[key], '\t|')
        print("|-------|-------|")
