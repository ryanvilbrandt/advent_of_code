class Program:

    def __init__(self, instructions, registers=None):
        self.instructions = instructions.strip('\n').split('\n')
        self.registers = {} if registers is None else registers
        self.mul_count = 0

    @staticmethod
    def is_prime_number(n):
        """Returns True if n is prime."""
        if n == 2:
            return True
        if n == 3:
            return True
        if n % 2 == 0:
            return False
        if n % 3 == 0:
            return False

        i = 5
        w = 2

        while i * i <= n:
            if n % i == 0:
                return False

            i += w
            w = 6 - w

        return True

    def get_register_value(self, register: str) -> int:
        """
        If register is a number, it just returns that number. Otherwise, it gets the value from that register.
        :param register:
        :return:
        """
        try:
            return int(register)
        except ValueError:
            pass
        return self.registers.get(register, 0)

    def run_instruction(self, instruction: str) -> int:
        """
        After processing an instruction, returns the amount of instructions that should advance by (default 1)
        :param instruction:
        :return:
        """
        instruction_list = instruction.split(' ')
        if len(instruction_list) == 2:
            instruction_list.append("")
        op, x, y = instruction_list
        if op == "set":
            self.registers[x] = self.get_register_value(y)
        elif op == "add":
            self.registers[x] = self.get_register_value(x) + self.get_register_value(y)
        elif op == "sub":
            self.registers[x] = self.get_register_value(x) - self.get_register_value(y)
        elif op == "mul":
            self.registers[x] = self.get_register_value(x) * self.get_register_value(y)
            self.mul_count += 1
        elif op == "mod":
            self.registers[x] = self.get_register_value(x) % self.get_register_value(y)
        elif op == "jnz":
            if self.get_register_value(x) != 0:
                if self.get_register_value(y) == 0:
                    raise Exception("INFINITE LOOP! FUUUUUUUUUUCK!!!")
                return self.get_register_value(y)
        elif op == "prime":
            if self.is_prime_number(self.get_register_value(x)):
                self.registers[y] = self.get_register_value(y) + 1
        elif op == "lbl":
            pass
        else:
            raise Exception(f"Bad instruction: {instruction}")
        return 1

    def run_program(self):
        index = 0
        tick_count = 0
        while True:
            # self.print_step(index)
            index += self.run_instruction(self.instructions[index])
            tick_count += 1
            if tick_count % 1e6 == 0:
                print(f"{tick_count}: {self.registers}")
            if not (0 < index < len(self.instructions)):
                break

    def print_step(self, index):
        print()
        print()
        for i, ins in enumerate(self.instructions):
            print("{} {}".format(">" if i == index else " ", ins))
        print()
        print(self.registers)



# with open("day 23.input") as f:
with open("day 23 compressed.input") as f:
    a = f.read()

p = Program(a, registers={'a': 1})
p.run_program()
print(p.mul_count)
