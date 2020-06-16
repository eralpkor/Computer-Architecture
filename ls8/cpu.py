"""CPU functionality."""
# LDI: load "immediate", store a value in a register, or "set this register to this value".
# PRN: a pseudo-instruction that prints the numeric value stored in a register.
# HLT: halt the CPU and exit the emulator.
import sys

# setup consts for op codes
LDI = 0b10000010 # LDI R0,8 130
PRN = 0b01000111 # PRN R0, 71
HLT = 0b00000001 # HLT
class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # create 256 bites of memory
        self.ram = [0] * 256
        # 8 bit register
        self.reg = [0] * 8
        # program counter PC
        self.pc = 0

    # Inside the CPU, there are two internal registers used for memory operations: 
    # the Memory Address Register (MAR) and the Memory Data Register (MDR).
    def ram_read(self, mar):
        self.ram[mar]

    def ram_write(self, mar, mdr):
        self.ram[mar] = mdr

    def load(self, file_name):
        """Load a program into memory."""
        try:
            address = 0
            # open the file
            with open(file_name) as f:
                for line in f:
                    # strip out the white space at a inline comment
                    clean_line = line.strip().split('#')
                    # grab string number
                    value = clean_line[0].strip()

                    # check if val is blank, if it is skip to next line
                    if value != '':
                        # number string to integer
                        num = int(value, 2) # we need to convert a binary string to a number ex. "100000010"
                        self.ram[address] = num
                        address += 1
                    else:
                        continue

        except FileNotFoundError:
            print("ERR: FILE NOT FOUND")
            sys.exit(2)


        # # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self, file_name):
        """Run the CPU."""
        # load the program into the memory
        self.load(file_name)
        read_ram = self.ram_read
        write_ram = self.ram_write

        # run the program
        while True:
            pc = self.pc # program counter
            # que the operation to start at default 0
            op = read_ram(pc)

            if op == LDI:
                self.reg[read_ram(pc + 1)] = read_ram(pc + 2)
                self.pc += 3
            elif op == PRN:
                print(self.reg[read_ram(pc + 1)])
                self.pc += 2

            elif op == HLT:
                sys.exit(1)

            else:
                print('ERR: UNKNOWN INPUT:\t', op)
                sys.exit(1)


# if len(sys.argv) == 2:
#     file_name = sys.argv[1]

#     c = CPU()
#     c.run(file_name)
# else:
#     # err message
#     print("""
# ERR: PLEASE PROVIDE A FILE NAME\n
# ex python cpu.py examples/FILE_NAME
# """)
#     sys.exit(2)

file_name = 'print8.ls8'

c = CPU()

c.run(file_name)


# file_name = sys.argv[1]
# 


