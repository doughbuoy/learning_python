"""" Module for detecting a key press """

try:
    # If windows platform
    import msvcrt

    def getkey():
        # wait for it
        return msvcrt.getch()

except ImportError:
# If Linux or IOS
    import sys
    import tty
    import termios

    def getkey():
        fd = sys.stdin.fileno()
        orig_attr = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, orig_attr)
        return ch

# if its somethin else the exceptio will go unhandled


