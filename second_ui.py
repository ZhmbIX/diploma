# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'second.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1044, 578)
        MainWindow.setStyleSheet(u"background-color: #FAEEDD;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(560, 340, 481, 51))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.textEdit_4 = QTextEdit(self.centralwidget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(350, 290, 151, 31))
        self.textEdit_4.setStyleSheet(u"background-color:\"white\";")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(350, 420, 151, 41))
        self.comboBox.setStyleSheet(u"background-color:\"white\";")
        self.textEdit_3 = QTextEdit(self.centralwidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(350, 220, 151, 31))
        self.textEdit_3.setStyleSheet(u"background-color:\"white\";")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 80, 141, 31))
        self.label.setFont(font)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(560, 140, 481, 51))
        self.checkBox.setFont(font)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 420, 181, 31))
        self.label_6.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 210, 241, 41))
        self.label_3.setFont(font)
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(560, 230, 481, 71))
        self.checkBox_2.setFont(font)
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(350, 150, 151, 31))
        self.textEdit_2.setStyleSheet(u"background-color:\"white\";")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(570, 60, 431, 51))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_8.setFont(font1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 350, 251, 41))
        self.label_5.setFont(font)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(180, 20, 191, 41))
        self.label_10.setFont(font1)
        self.textEdit_5 = QTextEdit(self.centralwidget)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(350, 360, 151, 31))
        self.textEdit_5.setStyleSheet(u"background-color:\"white\";")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(350, 80, 151, 31))
        self.textEdit.setStyleSheet(u"background-color:\"white\";")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 280, 241, 41))
        self.label_4.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 140, 241, 41))
        self.label_2.setFont(font)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(800, 510, 181, 41))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"background-color: #FFE4C4;\n"
"")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(50, 510, 391, 41))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"background-color: #FFE4C4;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c \u043f\u0435\u0440\u0435\u0431\u043e\u0440\u0430 (n!)", None))
        self.textEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043e\u0442 1 \u0434\u043e n", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"F(\u043f) = max {0; tj-dj}", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"F(\u043f) = max {tj-dj}", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"F(\u043f) = max (tj-pj)", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"F(\u043f) = max (tj+pj)", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"F(\u043f) = max WjLj", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"F(\u043f) = max Wjzj", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"F(\u043f) = Wjtj", None))

        self.textEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043e\u0442 1 \u0434\u043e n", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440\u043d\u043e\u0441\u0442\u044c:", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0441\u043c\u0435\u0449\u0435\u043d\u0438\u044f ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0443\u043d\u043a\u0446\u0438\u044f \u0448\u0442\u0440\u0430\u0444\u0430:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b p<span style=\" vertical-align:sub;\">j</span>:</p></body></html>", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0448\u0442\u0440\u0430\u0444\u0430 \n"
" \u0441 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u043c\u0438 \u043d\u0435\u0443\u0431\u044b\u0432\u0430\u044e\u0449\u0438\u043c\u0438 \n"
" \u0448\u0442\u0440\u0430\u0444\u043d\u044b\u043c\u0438 \u0444\u0443\u043d\u043a\u0446\u0438\u044f\u043c\u0438 ", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043e\u0442 0 \u0434\u043e n", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0435 \u043c\u0435\u0442\u043e\u0434\u044b \u0440\u0435\u0448\u0435\u043d\u0438\u044f:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b W<span style=\" vertical-align:sub;\">j</span>:</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0442\u043e\u0447\u043d\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435:", None))
        self.textEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043e\u0442 1 \u0434\u043e n", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043e\u0442 1 \u0434\u043e n", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b d<span style=\" vertical-align:sub;\">j</span>:</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b r<span style=\" vertical-align:sub;\">j</span>:</p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0439 \u0448\u0430\u0433 ", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0441\u043b\u0443\u0447\u0430\u0439\u043d\u0443\u044e \u0444\u0443\u043d\u043a\u0438\u0446\u044e \u0448\u0442\u0440\u0430\u0444\u0430", None))
    # retranslateUi

