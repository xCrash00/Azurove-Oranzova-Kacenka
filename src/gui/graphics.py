#!/usr/bin/python3

import sys

from PyQt5.QtWidgets import (QWidget, QLCDNumber, QApplication, QGridLayout, QPushButton)

from src.ui import logic


class Graphics(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		grid = QGridLayout()
		self.lcd = QLCDNumber(self)
		self.setLayout(grid)

		names = ['', '', '', 'a',
				 'Cls', 'Bck', '', 'Close',
				 '7', '8', '9', '/',
				 '4', '5', '6', '*',
				 '1', '2', '3', '-',
				 '0', '.', '=', '+']

		positions = [(i, j) for i in range(6) for j in range(4)]

		for position, name in zip(positions, names):
			if name == '':
				continue
			button = QPushButton(name, self)
			grid.addWidget(button, *position)
			button.clicked.connect(self.make_handleButton(name))
		self.move(300, 150)
		self.setWindowTitle('Calculator')
		self.show()

	def make_handleButton(self, name):
		def handleButton():
			logic.num_pressed(name)
			self.lcd.display(logic.term)

		return handleButton


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Graphics()
	sys.exit(app.exec_())