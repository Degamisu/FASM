import time

class Debugger:
    def __init__(self, cpu, loader):
        self.cpu = cpu
        self.loader = loader
        self.breakpoints = set()
        self.running = False

    def display_program_state(self):
        # Display program state information
        print("Welcome to the Fast Assembly Debugger!\n")
        print("[Program State]")
        print("Current Instruction:", self.cpu.current_instruction)
        print("Registers:")
        for reg, val in self.cpu.registers.items():
            print(f"  {reg}: 0x{val:04X}", end="   ")
        print("\n\n[Memory]")
        for i in range(0, 256, 16):  # Display memory in 16-byte rows
            print(f"0x{i:04X}:", end=" ")
            for j in range(16):
                print(f"0x{self.cpu.memory[i + j]:02X}", end=" ")
            print()

    def step(self):
        # Execute the next instruction and update program state
        self.cpu.execute_instruction()
        self.display_program_state()

    def run(self):
        # Run the program continuously until a breakpoint is encountered or execution is manually paused
        self.running = True
        while self.running:
            self.step()
            time.sleep(1)  # Adjust sleep duration as needed

    def set_breakpoint(self, address):
        # Set a breakpoint at the specified memory address
        self.breakpoints.add(address)

    def clear_breakpoint(self, address):
        # Clear a breakpoint at the specified memory address
        self.breakpoints.remove(address)

    def prompt(self):
        # Display debugger prompt and process user input
        while True:
            user_input = input("\nEnter command (step, run, break, clear, registers, memory, quit): ")
            if user_input == "step":
                self.step()
            elif user_input == "run":
                self.run()
            elif user_input.startswith("break"):
                address = int(user_input.split()[1], 16)
                self.set_breakpoint(address)
            elif user_input.startswith("clear"):
                address = int(user_input.split()[1], 16)
                self.clear_breakpoint(address)
            elif user_input == "registers":
                self.display_registers()
            elif user_input.startswith("memory"):
                address = int(user_input.split()[1], 16)
                self.display_memory(address)
            elif user_input == "quit":
                break

    def display_registers(self):
        # Display the current state of CPU registers
        print("\n[Registers]")
        for reg, val in self.cpu.registers.items():
            print(f"{reg}: 0x{val:04X}")

    def display_memory(self, address):
        # Display memory contents starting from the specified address
        print("\n[Memory]")
        for i in range(address, address + 256, 16):  # Display memory in 16-byte rows
            print(f"0x{i:04X}:", end=" ")
            for j in range(16):
                print(f"0x{self.cpu.memory[i + j]:02X}", end=" ")
            print()