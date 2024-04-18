class CPU68k:
    def __init__(self):
        # Initialize registers
        self.registers = {
            'd0': 0,
            'd1': 0,
            'd2': 0,
            'd3': 0,
            'd4': 0,
            'd5': 0,
            'd6': 0,
            'd7': 0,
            'a0': 0,
            'a1': 0,
            'a2': 0,
            'a3': 0,
            'a4': 0,
            'a5': 0,
            'a6': 0,
            'a7': 0,
        }
        self.memory = [0] * 65536  # 64KB memory

    def load_program(self, program):
        # Load program into memory starting at address 0x0000
        for i, instruction in enumerate(program):
            self.memory[i] = instruction

    def fetch_instruction(self):
        # Fetch the next instruction from memory
        instruction = self.memory[self.registers['pc']]
        self.registers['pc'] += 1
        return instruction

    def execute_instruction(self, instruction):
        # Decode and execute instructions
        opcode = (instruction >> 12) & 0xF

        if opcode == 0x0:
            # NOP instruction
            pass
        elif opcode == 0x4:
            # ADD instruction (immediate addressing mode)
            register = (instruction >> 9) & 0x7
            immediate = instruction & 0xFF
            self.registers['d' + str(register)] += immediate
        elif opcode == 0x7:
            # MOVE instruction (immediate addressing mode)
            dest_register = (instruction >> 9) & 0x7
            immediate = instruction & 0xFF
            self.registers['d' + str(dest_register)] = immediate

    def run(self):
        # Start executing instructions
        self.registers['pc'] = 0  # Program Counter
        while True:
            instruction = self.fetch_instruction()
            self.execute_instruction(instruction)
            print("Registers:", self.registers)  # Print registers after each instruction


def assemble(assembly_file):
    # This function reads an assembly file and assembles it into machine code
    machine_code = []
    with open(assembly_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(';'):
                continue  # Skip empty lines and comments
            parts = line.split()
            opcode = int(parts[0], 16)
            machine_code.append(opcode)
    return machine_code


# Example assembly file
assembly_file = "program.asm"

# Assemble the code
machine_code = assemble(assembly_file)

# Create CPU instance and load program
cpu = CPU68k()
cpu.load_program(machine_code)

# Run the CPU
cpu.run()
