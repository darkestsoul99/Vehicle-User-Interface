#!/usr/bin/python3
#Reference code obtained from "https://www.raspberrypi.org/forums/viewtopic.php?t=53680" by user: LinuxCircle

from PyQt5.QtWidgets import QWidget
from radio_interface import *

class RadioWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.ui = Ui_radio_widget()
        self.ui.setupUi(self)

"""if __name__ == '__main__':
    init_radio(i2c_address)
    frequency = 101.1 # sample starting frequency
    # terminal user input infinite loop
    stdscr = curses.initscr()
    curses.noecho()
    try:
        while True:
            c = stdscr.getch()
            if c == ord('f'): # set to 101.1
                frequency = 101.1
                set_freq(i2c_address, frequency)
                time.sleep(1)
            elif c == ord('v'): # set to 102.1
                frequency = 102.1
                set_freq(i2c_address, frequency)
                time.sleep(1)
            elif c == ord('w'): # increment by 1
                frequency += 1
                set_freq(i2c_address, frequency)
                time.sleep(1)
            elif c == ord('s'): # decrement by 1
                frequency -= 1
                set_freq(i2c_address, frequency)
                time.sleep(1)
            elif c == ord('e'): # increment by 0.1
                frequency += 0.1
                set_freq(i2c_address, frequency)
                time.sleep(1)
            elif c == ord('d'): # decrement by 0.1
                frequency -= 0.1
                set_freq(i2c_address, frequency)
                time.sleep(1)
            elif c == ord('m'): # mute
                mute(i2c_address)
                time.sleep(1)
            elif c == ord('u'): # unmute
                set_freq(i2c_address, frequency)
                time.sleep(1)
            elif c == ord('q'): # exit script and cleanup
                mute(i2c_address)
                curses.endwin()
                break
    except KeyboardInterrupt:
        mute(i2c_address)
        curses.endwin()"""