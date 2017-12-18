from time import sleep
from threading import Thread
from queue import Queue


class Song:
    instructions = None
    program_id = None
    queue = None
    registers = None
    partner = None
    count = 0

    def __init__(self, program_id: int, instructions: str):
        self.instructions = instructions.strip('\n').split('\n')
        self.program_id = program_id
        self.registers = {'p': program_id}
        self.queue = Queue()

    def set_partner(self, partner: "Song"):
        self.partner = partner

    def send(self, value):
        self.count += 1
        # print(f"{self.program_id}: Sent {value} / count: {self.count}")
        self.partner.queue.put(value)

    def receive(self):
        v = self.queue.get()
        # print(f"{self.program_id}: Received {v} / qsize: {self.queue.qsize()}")
        return v

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
        if op == "snd":
            self.send(self.get_register_value(x))
        elif op == "set":
            self.registers[x] = self.get_register_value(y)
        elif op == "add":
            self.registers[x] = self.get_register_value(x) + self.get_register_value(y)
        elif op == "mul":
            self.registers[x] = self.get_register_value(x) * self.get_register_value(y)
        elif op == "mod":
            self.registers[x] = self.get_register_value(x) % self.get_register_value(y)
        elif op == "rcv":
            self.registers[x] = self.receive()
        elif op == "jgz":
            if self.get_register_value(x) > 0:
                if self.get_register_value(y) == 0:
                    raise Exception("INFINITE LOOP! FUUUUUUUUUUCK!!!")
                return self.get_register_value(y)
        return 1

    def duet(self):
        self.registers = {'p': self.program_id}
        index = 0
        while True:
            index += self.run_instruction(self.instructions[index])
            # print(self.program_id, ":", self.instructions[index], self.registers)
            if not (0 < index < len(self.instructions)):
                break
        print(f"Exitting program {self.program_id}")

def start_duet(instructions: str):
    song_0 = Song(0, instructions)
    song_1 = Song(1, instructions)
    song_0.set_partner(song_1)
    song_1.set_partner(song_0)

    t1 = Thread(target=song_0.duet)
    t1.daemon = True
    t1.start()
    t2 = Thread(target=song_1.duet)
    t2.daemon = True
    t2.start()

    try:
        while True:
            if not t1.is_alive() and not t2.is_alive():
                print("Both programs finished. Exitting now.")
            elif song_0.queue.empty() and song_1.queue.empty():
                print("Deadlock reached. Exitting now.")
                break
            sleep(1)
    except KeyboardInterrupt:
        print("Interrupted. Exitting...")
    else:
        print(f"Song 0 = {song_0.count} / Song 1 = {song_1.count}")


# a = """
# set a 1
# add a 2
# mul a a
# mod a 5
# snd a
# set a 0
# rcv a
# jgz a -1
# set a 1
# jgz a -2
# """
with open("day 18.input") as f:
    a = f.read()

start_duet(a)
