class Loader:
    def __init__(self, machine_code):
        self.machine_code = machine_code
        self.memory = [0] * 65536  # 64KB memory

    def load_program(self):
        # Load machine code into memory
        for i, instruction in enumerate(self.machine_code):
            self.memory[i] = instruction

    def initialize_stack(self):
        # Initialize stack pointer
        self.memory[0xFFFE] = 0xFFFF  # Set stack pointer to end of memory

    def initialize_registers(self):
        # Initialize general-purpose registers
        # Example: Set register D0 to 0
        self.memory[0] = 0

    def initialize_program_counter(self):
        # Initialize program counter to start of program
        self.memory[0xFFFC] = 0  # Set program counter to start of memory

    def initialize_memory(self):
        # Perform any additional memory initialization if needed
        pass