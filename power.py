import sys
from time import sleep
from usb import core


class Power(object):
    def __init__(self):
        self.plug = core.find(idVendor=0x067b, idProduct=0x2303)
        if self.plug is None:
            raise ValueError("Device not found")

    def is_on(self):
        state = self.plug.ctrl_transfer(0xc0, 0x01, 0x0081, 0x0000, 0x0001)
        return state[0] == 0xa0

    def toggle(self, state_on):
        self.plug.ctrl_transfer(0x40, 0x01, 0x0001, 0xa0 if state_on else 0x20)


def main(args):
    commands = ["toggle", "cycle", "state"]
    try:
        cmd = args[1].lower()
        if cmd not in commands:
            print(f"available commands: {commands}")
            print("cycle takes an optional sleep (default 1 second)")
            return -1
    except IndexError:
        return -1

    power = Power()

    if cmd == "toggle":
        power.toggle(not power.is_on())
    elif cmd == "cycle":
        power.toggle(False)
        try:
            sleep(float(args[2]))
        except (IndexError, ValueError):
            sleep(1.0)
        power.toggle(True)
    elif cmd == "state":
        print(f"Plug power is {'on' if power.is_on() else 'off'}")
    else:
        return -1
    return 0


if __name__ == '__main__':
    ret = main(sys.argv)
    sys.exit(ret)
