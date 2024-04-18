class CPU:
    def __init__(self):
        self.registers = [0] * 8  # 8 general-purpose registers
        self.memory = [0] * 65536  # 64KB memory
        self.program_counter = 0  # Program counter register
        self.stack_pointer = 0xFFFF  # Stack pointer initialized to end of memory

    def execute_instruction(self, instruction):
        opcode = (instruction >> 12) & 0xF
        operand1 = (instruction >> 9) & 0x7
        operand2 = instruction & 0xFF

        if opcode == 0:  # MOV
            self.mov(operand1, operand2)
        elif opcode == 1:  # CALL
            self.call(operand2)
        elif opcode == 2:  # HALT
            self.halt()
        elif opcode == 3:  # PUSH
            self.push(operand2)
        elif opcode == 4:  # POP
            self.pop(operand1)
        elif opcode == 10:  # ARM (Allocate RAM)
            self.allocate_memory(operand2)
        # Add more instructions as needed

    def mov(self, dest_reg, value):
        self.registers[dest_reg] = value

    def call(self, address):
        # Save return address on the stack and jump to the specified address
        self.push(self.program_counter)
        self.program_counter = address

    def halt(self):
        # Halt the CPU
        pass

    def push(self, value):
        # Decrement stack pointer and store value on the stack
        self.stack_pointer -= 1
        self.memory[self.stack_pointer] = value

    def pop(self, dest_reg):
        # Pop value from the stack and store it in the specified register
        value = self.memory[self.stack_pointer]
        self.stack_pointer += 1
        self.registers[dest_reg] = value

    def allocate_memory(self, size):
        # Allocate memory based on the specified size
        self.memory = [0] * size

    def load_program(self, machine_code):
        for address, instruction in enumerate(machine_code):
            self.memory[address] = instruction

    def run(self):
        while True:
            instruction = self.memory[self.program_counter]
            self.execute_instruction(instruction)
            self.program_counter += 1
            if self.program_counter >= len(self.memory):
                break
