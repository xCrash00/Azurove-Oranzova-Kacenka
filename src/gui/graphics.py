#!/usr/bin/python3

import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import (QWidget, QApplication, QGridLayout, QPushButton)

from src.ui import logic


class Graphics(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		grid = QGridLayout()
		self.label = QLabel(self)
		grid.addWidget(self.label)
		self.setLayout(grid)

		names = ['', '', '', 'Neg',
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
			if name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
				logic.num_pressed(name)
			elif name == 'Neg':
				logic.negate_pressed()
			elif name == 'Abs':
				logic.abs_pressed()
			elif name == 'Fact':
				logic.fact_pressed()
			elif name in ['+', '-', '*', '/']:
				logic.operator_pressed(name)
			elif name == '=':
				logic.get_res()
			elif name == 'Cls':
				logic.c_pressed()
			elif name == 'Bck':
				logic.ce_pressed()
			self.label.setText(logic.term)
		return handleButton

	def keyPressEvent(self, event):
		if event.key() == QtCore.Qt.Key_Escape:
			self.close()
		elif type(event) == QtGui.QKeyEvent:
			logic.num_pressed(chr(event.key()))
			self.label.setText(logic.term)
		else:
			event.ignore()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Graphics()
	sys.exit(app.exec_())