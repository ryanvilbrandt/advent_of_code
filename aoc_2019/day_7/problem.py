import itertools
from typing import Union, Tuple, Any

from aoc_2019.common.intcode import IntCode


def get_amplified_output(program: str, phase_setting: int, amp_input: int):
    intcode = IntCode(program, [phase_setting, amp_input])
    return intcode.run()


def run_amplifiers(program: str, amp_modes: Union[str, Tuple[Any]]):
    amp_modes = [int(c) for c in amp_modes]
    amplifiers = [IntCode(program) for _ in range(len(amp_modes))]
    # Set modes
    for amp, mode in zip(amplifiers, amp_modes):
        amp.add_to_input_buffer(mode)
    output = 0
    loop_output = None
    while all([not amp.halted for amp in amplifiers]):
        for amp in amplifiers:
            amp.add_to_input_buffer(output)
            output = amp.run()
            # print(output)
        if output is not None:
            loop_output = output
    return loop_output


def find_max_thrust(program: str, phase_list=None):
    if phase_list is None:
        phase_list = [0, 1, 2, 3, 4]
    results = [run_amplifiers(program, p) for p in itertools.permutations(phase_list)]
    return max(results)
