# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blog_gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import test_log

class Ui_Dialog(object):
	def print_something(self):
		test_log.main()

	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(400, 300)
		self.btnRun = QtWidgets.QPushButton(Dialog)
		self.btnRun.setGeometry(QtCore.QRect(150, 100, 75, 23))
		self.btnRun.setObjectName("btnRun")
		self.btnRun.clicked.connect(self.print_something)

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
		self.btnRun.setText(_translate("Dialog", "Click me"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Dialog = QtWidgets.QDialog()
	ui = Ui_Dialog()
	ui.setupUi(Dialog)
	Dialog.show()
	sys.exit(app.exec_())

