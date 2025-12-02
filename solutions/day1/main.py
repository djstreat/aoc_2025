from argparse import ArgumentParser
from pathlib import Path

INITIAL_POSITION = 50
TOTAL_POSITIONS = 100
MAX_POSITION = 99


def parse_offset(offset_str: str) -> int:
    # TODO: Make this a regex match
    if not offset_str.strip():
        raise ValueError("Offset string is empty")
    match offset_str.strip()[0]:
        case "L":
            return -int(offset_str.strip()[1:])
        case "R":
            return int(offset_str.strip()[1:])
        case _:
            raise ValueError(f"Invalid offset: {offset_str}")


def calculate_dial_position(current_position: int, offset: int) -> int:
    new_position = current_position + (offset % TOTAL_POSITIONS)
    # Calculate the new position within the range of 0 to MAX_POSITION
    if new_position > MAX_POSITION:
        new_position -= TOTAL_POSITIONS
    elif new_position < 0:
        new_position += TOTAL_POSITIONS
    return new_position


def codebreak(input_path: Path) -> int:
    current_position = 50
    password = 0
    print(f"The dial starts by pointing at {current_position}.")
    with open(input_path, "r") as fp:
        offset_str = fp.readline()
        while offset_str:
            offset = parse_offset(offset_str)
            current_position = calculate_dial_position(current_position, offset)
            print(
                f"The dial is rotated {offset_str.strip()} to point at {current_position}."
            )
            if current_position == 0:
                password += 1
                print("***0***")
            offset_str = fp.readline()
    return password


def main():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input_path", required=True, type=Path)
    args = parser.parse_args()
    print(codebreak(args.input_path))


if __name__ == "__main__":
    main()
