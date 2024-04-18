class Assembler:
    def __init__(self, machine_code):
        self.machine_code = machine_code
        self.memory = [0] * 65536  # 64KB memory
        self.total_ram = None

    def load_program(self):
        # Load machine code into memory
        for i, instruction in enumerate(self.machine_code):
            self.memory[i] = instruction

        # Check if total RAM size is specified
        if self.total_ram is not None:
            # Adjust memory size based on total RAM
            self.memory = [0] * self.total_ram

    def assemble(self):
        for instruction in self.parsed_instructions:
            opcode = instruction[0]
            if opcode == 'MOV':
                self.assemble_mov(instruction)
            elif opcode == 'CALL':
                self.assemble_call(instruction)
            elif opcode == 'HALT':
                self.assemble_halt(instruction)
            elif opcode == 'PUSH':
                self.assemble_push(instruction)
            elif opcode == 'POP':
                self.assemble_pop(instruction)
            else:
                # Handle unrecognized instructions
                pass

    def assemble_mov(self, instruction):
        dest = instruction[1]
        value = instruction[3]
        # Encode MOV instruction and append to machine_code
        # Example encoding: 0x00RRVV, where RR is the destination register and VV is the value
        machine_instruction = (0 << 12) | (int(dest[1:]) << 9) | int(value)
        self.machine_code.append(machine_instruction)

    def assemble_call(self, instruction):
        function_name = instruction[1]
        # Encode CALL instruction and append to machine_code
        # Example encoding: 0x1000FF, where FF is the function address (placeholder)
        # We'll resolve the function address later during linking
        self.machine_code.append(0x1000FF)

    def assemble_halt(self, instruction):
        # Encode HALT instruction and append to machine_code
        self.machine_code.append(0x200000)

    def assemble_push(self, instruction):
        register = instruction[1]
        # Encode PUSH instruction and append to machine_code
        # Example encoding: 0x30RR00, where RR is the register
        self.machine_code.append(0x30 + int(register[1:]) << 9)

    def assemble_pop(self, instruction):
        register = instruction[1]
        # Encode POP instruction and append to machine_code
        # Example encoding: 0x40RR00, where RR is the register
        self.machine_code.append(0x40 + int(register[1:]) << 9)

    def resolve_labels(self, symbol_table):
        # Resolve label addresses in CALL instructions
        for i, instruction in enumerate(self.machine_code):
            if instruction == 0x1000FF:
                function_name = self.parsed_instructions[i][1]
                function_address = symbol_table.get(function_name)
                if function_address is None:
                    raise ValueError(f"Undefined function: {function_name}")
                # Update the CALL instruction with the resolved function address
                self.machine_code[i] = (0x100000 | function_address)  # Example: 0x1000FF -> 0x1000A5
    
