#from candevice import CanDevice
import time
import sys

from debug import *
from engine import Engine
from wheel  import Wheel
from canbus import CanBus
from elm    import Elm

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QGridLayout)


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.init_config()
        self.init_debug()
        self.init_canbus()
        self.init_engine()
        self.init_wheel()
        self.init_elm()
        self.init_ui()

    def deinit(self):
        self.deinit_elm()
        self.deinit_engine()
        self.deinit_wheel()
        self.deinit_canbus()

    def init_ui(self):
        grid = QGridLayout()

        btn0 = QPushButton("key_0")
        btn0.clicked.connect(lambda:self.btn_clicked(0))
        grid.addWidget(btn0)

        btn1 = QPushButton("key_1")
        btn1.clicked.connect(lambda:self.btn_clicked(1))
        grid.addWidget(btn1)

        btn2 = QPushButton("key_2")
        btn2.clicked.connect(lambda:self.btn_clicked(2))
        grid.addWidget(btn2)

        btn3 = QPushButton("key_3")
        btn3.clicked.connect(lambda:self.btn_clicked(3))
        grid.addWidget(btn3)

        self.setLayout(grid)
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("pyelmemu")
        self.show()

    def btn_clicked(self, i):
        msg = "Button clicked: %d" % i
        self.wheel.key_press(i)

    def init_config(self):
        debug_print_mtcall("Applicaion", "init_config")

    def init_canbus(self):
        debug_print_mtcall("Application", "init_canbus")
        self.canbus = CanBus(11, "CanBusThread")

    def init_engine(self):
        debug_print_mtcall("Application", "init_engine")
        self.engine = Engine(self.canbus)

    def init_wheel(self):
        debug_print_mtcall("Application", "init_wheel")
        self.wheel = Wheel(self.canbus)

    def init_elm(self):
        debug_print_mtcall("Application", "init_elm")
        self.elm = Elm(self.canbus)

    def init_debug(self):
        debug_mask_set(DEBUG_LEVEL_ALL)
        debug_add_filter("Wheel")

    def deinit_engine(self):
        debug_print_mtcall("Application", "deinit_engine")
        self.engine.close()

    def deinit_wheel(self):
        debug_print_mtcall("Application", "deinit_wheel")
        self.wheel.close()

    def deinit_elm(self):
        debug_print_mtcall("Application", "deinit_elm")
        self.elm.close()

    def deinit_canbus(self):
        debug_print_mtcall("Application", "deinit_canbus")
        self.canbus.close()

if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    app_instance = Application()
    qapp.exec_()
    app_instance.deinit()
