# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 612)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.stackedWidget.setObjectName("stackedWidget")

        self.GameScreen = QtWidgets.QWidget()
        self.GameScreen.setObjectName("GameScreen")
        self.GameScreenProgressBar = QtWidgets.QProgressBar(self.GameScreen)
        self.GameScreenProgressBar.setGeometry(QtCore.QRect(660, 10, 118, 23))
        self.GameScreenProgressBar.setProperty("value", 24)
        self.GameScreenProgressBar.setObjectName("GameScreenProgressBar")
        self.GameScreenButton1 = QtWidgets.QPushButton(self.GameScreen)
        self.GameScreenButton1.setGeometry(QtCore.QRect(20, 500, 111, 41))
        self.GameScreenButton1.setObjectName("GameScreenButton1")
        self.stackedWidget.addWidget(self.GameScreen)

        self.DifficultyScreen = QtWidgets.QWidget()
        self.DifficultyScreen.setObjectName("DifficultyScreen")
        self.DifficultySlider = QtWidgets.QSlider(self.DifficultyScreen)
        self.DifficultySlider.setGeometry(QtCore.QRect(90, 140, 621, 41))
        self.DifficultySlider.setMaximum(2)
        self.DifficultySlider.setOrientation(QtCore.Qt.Horizontal)
        self.DifficultySlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.DifficultySlider.setObjectName("DifficultySlider")
        self.PullingCheckBox = QtWidgets.QCheckBox(self.DifficultyScreen)
        self.PullingCheckBox.setGeometry(QtCore.QRect(80, 260, 70, 17))
        self.PullingCheckBox.setChecked(True)
        self.PullingCheckBox.setObjectName("PullingCheckBox")
        self.PushingCheckBox = QtWidgets.QCheckBox(self.DifficultyScreen)
        self.PushingCheckBox.setGeometry(QtCore.QRect(80, 300, 70, 17))
        self.PushingCheckBox.setChecked(True)
        self.PushingCheckBox.setObjectName("PushingCheckBox")
        self.GrabbingCheckBox = QtWidgets.QCheckBox(self.DifficultyScreen)
        self.GrabbingCheckBox.setGeometry(QtCore.QRect(80, 340, 70, 17))
        self.GrabbingCheckBox.setChecked(True)
        self.GrabbingCheckBox.setObjectName("GrabbingCheckBox")
        self.ReachingCheckBox = QtWidgets.QCheckBox(self.DifficultyScreen)
        self.ReachingCheckBox.setGeometry(QtCore.QRect(80, 380, 70, 17))
        self.ReachingCheckBox.setChecked(True)
        self.ReachingCheckBox.setObjectName("ReachingCheckBox")
        self.DifficultyHeader = QtWidgets.QLabel(self.DifficultyScreen)
        self.DifficultyHeader.setGeometry(QtCore.QRect(90, 70, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.DifficultyHeader.setFont(font)
        self.DifficultyHeader.setObjectName("DifficultyHeader")
        self.BilateralHeader = QtWidgets.QLabel(self.DifficultyScreen)
        self.BilateralHeader.setGeometry(QtCore.QRect(90, 200, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.BilateralHeader.setFont(font)
        self.BilateralHeader.setObjectName("BilateralHeader")
        self.BackButtonSettingsScreen = QtWidgets.QPushButton(self.DifficultyScreen)
        self.BackButtonSettingsScreen.setGeometry(QtCore.QRect(360, 480, 111, 41))
        self.BackButtonSettingsScreen.setObjectName("BackButtonSettingsScreen")
        self.stackedWidget.addWidget(self.DifficultyScreen)
        self.InstructionsScreen = QtWidgets.QWidget()
        self.InstructionsScreen.setObjectName("InstructionsScreen")
        self.InstructionsText = QtWidgets.QTextBrowser(self.InstructionsScreen)
        self.InstructionsText.setGeometry(QtCore.QRect(50, 70, 701, 411))
        self.InstructionsText.setObjectName("InstructionsText")
        self.InstructionsHeader = QtWidgets.QLabel(self.InstructionsScreen)
        self.InstructionsHeader.setGeometry(QtCore.QRect(310, 20, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.InstructionsHeader.setFont(font)
        self.InstructionsHeader.setObjectName("InstructionsHeader")
        self.pushButton_3 = QtWidgets.QPushButton(self.InstructionsScreen)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 500, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.InstructionsScreen)
        self.StartScreen = QtWidgets.QWidget()
        self.StartScreen.setObjectName("StartScreen")
        self.BilaturtleText = QtWidgets.QLabel(self.StartScreen)
        self.BilaturtleText.setGeometry(QtCore.QRect(300, 40, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.BilaturtleText.setFont(font)
        self.BilaturtleText.setObjectName("BilaturtleText")
        self.StartButton = QtWidgets.QPushButton(self.StartScreen)
        self.StartButton.setGeometry(QtCore.QRect(330, 160, 111, 51))
        self.StartButton.setObjectName("StartButton")
        self.SettingsButton = QtWidgets.QPushButton(self.StartScreen)
        self.SettingsButton.setGeometry(QtCore.QRect(330, 230, 111, 51))
        self.SettingsButton.setObjectName("SettingsButton")
        self.PersonalTable = QtWidgets.QTableWidget(self.StartScreen)
        self.PersonalTable.setGeometry(QtCore.QRect(120, 150, 121, 191))
        self.PersonalTable.setObjectName("PersonalTable")
        self.PersonalTable.setColumnCount(1)
        self.PersonalTable.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.PersonalTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PersonalTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.PersonalTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.PersonalTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.PersonalTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.PersonalTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PersonalTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PersonalTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PersonalTable.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PersonalTable.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PersonalTable.setItem(4, 0, item)
        self.GroupTable = QtWidgets.QTableWidget(self.StartScreen)
        self.GroupTable.setGeometry(QtCore.QRect(550, 150, 121, 191))
        self.GroupTable.setObjectName("GroupTable")
        self.GroupTable.setColumnCount(1)
        self.GroupTable.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.GroupTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.GroupTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.GroupTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.GroupTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.GroupTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.GroupTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.GroupTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.GroupTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.GroupTable.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.GroupTable.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.GroupTable.setItem(4, 0, item)
        self.stackedWidget.addWidget(self.StartScreen)

        self.QuitScreen = QtWidgets.QWidget()
        self.QuitScreen.setObjectName("QuitScreen")
        self.QuitText = QtWidgets.QLabel(self.QuitScreen)
        self.QuitText.setGeometry(QtCore.QRect(290, 60, 261, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QuitText.setFont(font)
        self.QuitText.setObjectName("QuitText")
        self.QuitYesButton = QtWidgets.QPushButton(self.QuitScreen)
        self.QuitYesButton.setGeometry(QtCore.QRect(230, 240, 141, 91))
        self.QuitYesButton.setObjectName("QuitYesButton")
        self.QuitNoButton = QtWidgets.QPushButton(self.QuitScreen)
        self.QuitNoButton.setGeometry(QtCore.QRect(420, 240, 141, 91))
        self.QuitNoButton.setObjectName("QuitNoButton")
        self.stackedWidget.addWidget(self.QuitScreen)

        self.ProgressScreen = QtWidgets.QWidget()
        self.ProgressScreen.setObjectName("ProgressScreen")
        self.GoodJobText = QtWidgets.QLabel(self.ProgressScreen)
        self.GoodJobText.setGeometry(QtCore.QRect(330, 90, 261, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.GoodJobText.setFont(font)
        self.GoodJobText.setObjectName("GoodJobText")
        self.ProgressScreenProgressBar = QtWidgets.QProgressBar(self.ProgressScreen)
        self.ProgressScreenProgressBar.setGeometry(QtCore.QRect(270, 220, 231, 61))
        self.ProgressScreenProgressBar.setProperty("value", 24)
        self.ProgressScreenProgressBar.setObjectName("ProgressScreenProgressBar")
        self.PointsLabel = QtWidgets.QLabel(self.ProgressScreen)
        self.PointsLabel.setGeometry(QtCore.QRect(270, 300, 221, 31))
        self.PointsLabel.setObjectName("PointsLabel")
        self.TimeLabel = QtWidgets.QLabel(self.ProgressScreen)
        self.TimeLabel.setGeometry(QtCore.QRect(270, 330, 161, 31))
        self.TimeLabel.setObjectName("TimeLabel")
        self.StreakLabel = QtWidgets.QLabel(self.ProgressScreen)
        self.StreakLabel.setGeometry(QtCore.QRect(270, 360, 181, 31))
        self.StreakLabel.setObjectName("StreakLabel")
        self.ProgressContinueButton = QtWidgets.QPushButton(self.ProgressScreen)
        self.ProgressContinueButton.setGeometry(QtCore.QRect(320, 430, 111, 41))
        self.ProgressContinueButton.setObjectName("ProgressContinueButton")
        self.stackedWidget.addWidget(self.ProgressScreen)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GameScreenButton1.setText(_translate("MainWindow", "Instructions"))
        self.PullingCheckBox.setText(_translate("MainWindow", "Pulling"))
        self.PushingCheckBox.setText(_translate("MainWindow", "Pushing"))
        self.GrabbingCheckBox.setText(_translate("MainWindow", "Grabbing"))
        self.ReachingCheckBox.setText(_translate("MainWindow", "Reaching"))
        self.DifficultyHeader.setText(_translate("MainWindow", "Difficulty"))
        self.BilateralHeader.setText(_translate("MainWindow", "Bilateral Movements"))
        self.BackButtonSettingsScreen.setText(_translate("MainWindow", "Back"))
        self.InstructionsText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">We need some art here</p></body></html>"))
        self.InstructionsHeader.setText(_translate("MainWindow", "Instructions"))
        self.pushButton_3.setText(_translate("MainWindow", "Back"))
        self.BilaturtleText.setText(_translate("MainWindow", "BILATURTLE"))
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.SettingsButton.setText(_translate("MainWindow", "Settings"))
        item = self.PersonalTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1."))
        item = self.PersonalTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2."))
        item = self.PersonalTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3."))
        item = self.PersonalTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4."))
        item = self.PersonalTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5."))
        item = self.PersonalTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Personal"))
        __sortingEnabled = self.PersonalTable.isSortingEnabled()
        self.PersonalTable.setSortingEnabled(False)
        item = self.PersonalTable.item(0, 0)
        item.setText(_translate("MainWindow", "John"))
        item = self.PersonalTable.item(1, 0)
        item.setText(_translate("MainWindow", "Mary"))
        item = self.PersonalTable.item(2, 0)
        item.setText(_translate("MainWindow", "You"))
        item = self.PersonalTable.item(3, 0)
        item.setText(_translate("MainWindow", "Peter"))
        item = self.PersonalTable.item(4, 0)
        item.setText(_translate("MainWindow", "Sue"))
        self.PersonalTable.setSortingEnabled(__sortingEnabled)
        item = self.GroupTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1."))
        item = self.GroupTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2. "))
        item = self.GroupTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3."))
        item = self.GroupTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4."))
        item = self.GroupTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5."))
        item = self.GroupTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Group"))
        __sortingEnabled = self.GroupTable.isSortingEnabled()
        self.GroupTable.setSortingEnabled(False)
        item = self.GroupTable.item(0, 0)
        item.setText(_translate("MainWindow", "Team 1"))
        item = self.GroupTable.item(1, 0)
        item.setText(_translate("MainWindow", "Team 2"))
        item = self.GroupTable.item(2, 0)
        item.setText(_translate("MainWindow", "Team 4"))
        item = self.GroupTable.item(3, 0)
        item.setText(_translate("MainWindow", "Team 5"))
        item = self.GroupTable.item(4, 0)
        item.setText(_translate("MainWindow", "Team 3"))
        self.GroupTable.setSortingEnabled(__sortingEnabled)
        self.QuitText.setText(_translate("MainWindow", "Do you want to quit?"))
        self.QuitYesButton.setText(_translate("MainWindow", "Yes"))
        self.QuitNoButton.setText(_translate("MainWindow", "No"))
        self.GoodJobText.setText(_translate("MainWindow", "Good job!"))
        self.PointsLabel.setText(_translate("MainWindow", "Points: Insert points instead"))
        self.TimeLabel.setText(_translate("MainWindow", "Time: Insert time instead"))
        self.StreakLabel.setText(_translate("MainWindow", "Streak: Insert streak instead"))
        self.ProgressContinueButton.setText(_translate("MainWindow", "Continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

