from PColorLogging.Drawer.color.color_code import _ColorModeCode, _TextModeCode, _ForegroundCode, _BackgroundCode


class ColorMode:
    RESET = _ColorModeCode.RESET
    BOLD = _ColorModeCode.BOLD
    DARK = _ColorModeCode.DARK


class TextMode:
    ITALIC = _TextModeCode.ITALIC
    UNDERLINE = _TextModeCode.UNDERLINE
    SLOW_BLINK = _TextModeCode.SLOW_BLINK
    FAST_BLINK = _TextModeCode.FAST_BLINK
    REVERSE = _TextModeCode.REVERSE
    HIDE = _TextModeCode.HIDE
    CROSS = _TextModeCode.CROSS


class PColor:
    BLACK = _ForegroundCode.BLACK
    RED = _ForegroundCode.RED
    GREEN = _ForegroundCode.GREEN
    YELLOW = _ForegroundCode.YELLOW
    BLUE = _ForegroundCode.BLUE
    PURPLE = _ForegroundCode.PURPLE
    CYAN = _ForegroundCode.CYAN
    WHITE = _ForegroundCode.WHITE
    B_BLACK = _BackgroundCode.BLACK
    B_RED = _BackgroundCode.RED
    B_GREEN = _BackgroundCode.GREEN
    B_YELLOW = _BackgroundCode.YELLOW
    B_BLUE = _BackgroundCode.BLUE
    B_PURPLE = _BackgroundCode.PURPLE
    B_CYAN = _BackgroundCode.CYAN
    B_WHITE = _BackgroundCode.WHITE

    @staticmethod
    def get_extra_color(i, j):
        code = str(i * 16 + j)
        return "\u001b[38;5;" + code + "m " + code.ljust(4)

    @staticmethod
    def get_extra_background_color(i, j):
        code = str(i * 16 + j)
        return "\u001b[48;5;" + code + "m " + code.ljust(4)
