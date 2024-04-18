import os
from src.Assembler.parser_1 import Parser
from assembler import Assembler
from loader import Loader

def compile_fasm(input_file):
    # Create output directory if it doesn't exist
    output_dir = "out"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read input file
    with open(input_file, 'r') as f:
        fasm_code = f.read()

    # Parse and assemble the Fast Assembly code
    parser = Parser(fasm_code)
    parser.parse()
    
    assembler = Assembler(parser.parsed_instructions)
    assembler.assemble()

    loader = Loader(assembler.machine_code)

    # Save machine code to a file
    output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(input_file))[0] + ".bin")
    with open(output_file, 'wb') as f:
        for instruction in loader.machine_code:
            f.write(instruction.to_bytes(4, byteorder='big'))

    print(f"Compilation successful. Machine code saved to {output_file}")

if __name__ == "__main__":
    fasm_folder = "fasm"
    for fasm_file in os.listdir(fasm_folder):
        if fasm_file.endswith(".fasm"):
            compile_fasm(os.path.join(fasm_folder, fasm_file))
