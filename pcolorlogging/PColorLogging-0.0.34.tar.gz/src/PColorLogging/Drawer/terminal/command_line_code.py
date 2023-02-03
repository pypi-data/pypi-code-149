class _CursorNavigationCode:
    @staticmethod
    def up(i: int):
        return f"\u001b[{i}A"

    @staticmethod
    def down(i):
        return f"\u001b[{i}B"

    @staticmethod
    def right(i):
        return f"\u001b[{i}C"

    @staticmethod
    def left(i):
        return f"\u001b[{i}D"


class _PositionCode:
    @staticmethod
    def next_line(i):
        return f"\u001b[{i}E"

    @staticmethod
    def prev_line(i):
        return f"\u001b[{i}F"

    @staticmethod
    def set_column(i):
        return f"\u001b[{i}G"

    @staticmethod
    def set_position(i, j):
        return f"\u001b[{i};{j}H"

    @staticmethod
    def save_position(flag):
        if flag == "s":
            return "\u001b[{s}"
        elif flag == "u":
            return "\u001b[{u}"


class _ClearCode:
    @staticmethod
    def clear_screen(i: [0, 1, 2]):
        return f"\u001b[{i}J"

    @staticmethod
    def clear_line(i: [0, 1, 2]):
        return f"\u001b[{i}K"
