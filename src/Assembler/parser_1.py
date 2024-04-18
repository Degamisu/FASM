class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.token_index = -1

    def advance(self):
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        else:
            self.current_token = None

    def parse(self):
        self.advance()  # Initialize current_token
        while self.current_token:
            if self.current_token[0] == 'MOV':
                self.parse_mov()
            elif self.current_token[0] == 'CALL':
                self.parse_call()
            elif self.current_token[0] == 'HALT':
                self.parse_halt()
            elif self.current_token[0] == 'PUSH':
                self.parse_push()
            elif self.current_token[0] == 'POP':
                self.parse_pop()
            elif self.current_token[0] == 'ARM':
                self.parse_arm()
            elif self.current_token[0].endswith(':'):
                self.parse_label()
            else:
                # Handle unrecognized tokens
                pass
            self.advance()
            self.advance()

    def parse_mov(self):
        # Parse MOV instruction
        self.advance()  # Move past 'MOV'
        dest = self.current_token[0]
        self.advance()  # Move past destination register
        self.advance()  # Move past ','
        value = self.current_token[0]
        print(f"MOV {dest}, {value}")

    def parse_call(self):
        # Parse CALL instruction
        self.advance()  # Move past 'CALL'
        function_name = self.current_token[0]
        print(f"CALL {function_name}")

    def parse_halt(self):
        # Parse HALT instruction
        print("HALT")

    def parse_push(self):
        # Parse PUSH instruction
        self.advance()  # Move past 'PUSH'
        register = self.current_token[0]
        print(f"PUSH {register}")

    def parse_pop(self):
        # Parse POP instruction
        self.advance()  # Move past 'POP'
        register = self.current_token[0]
        print(f"POP {register}")

    def parse_label(self):
        # Parse label
        label = self.current_token[0].rstrip(':')
        print(f"LABEL: {label}")

    def parse_arm(self):
        # Parse ARM (Allocate RAM) instruction
        self.advance()  # Move past 'ARM'
        total_ram = int(self.current_token[0])
        print(f"ARM {total_ram}")
        # Store total RAM size for later use by the loader
        self.total_ram = total_ram