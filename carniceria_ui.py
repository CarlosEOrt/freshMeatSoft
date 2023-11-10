# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'carniceria.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFormLayout,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import Resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1156, 686)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_17 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(253, 240, 213);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 42))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"background-color:rgb(0, 48, 73);\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:rgb(0, 48, 73);\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(102, 155, 188);\n"
"border-radius:20px;\n"
"}")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.btn_menu = QPushButton(self.frame_superior)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setMinimumSize(QSize(300, 40))
        icon = QIcon()
        icon.addFile(u"Imagenes/menu-burger.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.btn_menu)

        self.horizontalSpacer = QSpacerItem(442, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_minimizar = QPushButton(self.frame_superior)
        self.btn_minimizar.setObjectName(u"btn_minimizar")
        self.btn_minimizar.setMinimumSize(QSize(80, 40))
        icon1 = QIcon()
        icon1.addFile(u"Imagenes/horizontal-rule.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimizar.setIcon(icon1)
        self.btn_minimizar.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.btn_minimizar)

        self.btn_pestana = QPushButton(self.frame_superior)
        self.btn_pestana.setObjectName(u"btn_pestana")
        self.btn_pestana.setMinimumSize(QSize(80, 40))
        icon2 = QIcon()
        icon2.addFile(u"Imagenes/window-restore.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pestana.setIcon(icon2)
        self.btn_pestana.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.btn_pestana)

        self.btn_maximizar = QPushButton(self.frame_superior)
        self.btn_maximizar.setObjectName(u"btn_maximizar")
        self.btn_maximizar.setMinimumSize(QSize(80, 40))
        icon3 = QIcon()
        icon3.addFile(u"Imagenes/window-maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximizar.setIcon(icon3)
        self.btn_maximizar.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.btn_maximizar)

        self.btn_cerrar = QPushButton(self.frame_superior)
        self.btn_cerrar.setObjectName(u"btn_cerrar")
        self.btn_cerrar.setMinimumSize(QSize(80, 40))
        icon4 = QIcon()
        icon4.addFile(u"Imagenes/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cerrar.setIcon(icon4)
        self.btn_cerrar.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.btn_cerrar)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_main = QFrame(self.frame)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_main)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_control = QFrame(self.frame_main)
        self.frame_control.setObjectName(u"frame_control")
        self.frame_control.setMinimumSize(QSize(300, 0))
        self.frame_control.setMaximumSize(QSize(0, 16777215))
        self.frame_control.setStyleSheet(u"QFrame{\n"
"background-color:rgb(0, 48, 73);\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:rgb(102, 155, 188);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"border-radius:20px;\n"
"color:rgb(253, 240, 213);\n"
"font: 77 10pt \"Arial Black\";\n"
"border-color:rgb(253, 240, 213);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 255, 255);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"border-radius:20px;\n"
"color:rgb(0, 48, 73);\n"
"font: 77 10pt \"Arial Black\";\n"
"}")
        self.frame_control.setFrameShape(QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_control)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_inventario = QPushButton(self.frame_control)
        self.btn_inventario.setObjectName(u"btn_inventario")
        self.btn_inventario.setMinimumSize(QSize(0, 50))
        icon5 = QIcon()
        icon5.addFile(u"Imagenes/list-check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_inventario.setIcon(icon5)
        self.btn_inventario.setIconSize(QSize(35, 35))

        self.verticalLayout_4.addWidget(self.btn_inventario)

        self.btn_ventas = QPushButton(self.frame_control)
        self.btn_ventas.setObjectName(u"btn_ventas")
        self.btn_ventas.setMinimumSize(QSize(0, 50))
        icon6 = QIcon()
        icon6.addFile(u"Imagenes/comment-dollar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ventas.setIcon(icon6)
        self.btn_ventas.setIconSize(QSize(35, 35))

        self.verticalLayout_4.addWidget(self.btn_ventas)

        self.btn_cote_de_caja = QPushButton(self.frame_control)
        self.btn_cote_de_caja.setObjectName(u"btn_cote_de_caja")
        self.btn_cote_de_caja.setMinimumSize(QSize(0, 50))
        icon7 = QIcon()
        icon7.addFile(u"Imagenes/cash-register.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cote_de_caja.setIcon(icon7)
        self.btn_cote_de_caja.setIconSize(QSize(35, 35))

        self.verticalLayout_4.addWidget(self.btn_cote_de_caja)

        self.btn_estadisticas = QPushButton(self.frame_control)
        self.btn_estadisticas.setObjectName(u"btn_estadisticas")
        self.btn_estadisticas.setMinimumSize(QSize(0, 50))
        icon8 = QIcon()
        icon8.addFile(u"Imagenes/chart-histogram.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_estadisticas.setIcon(icon8)
        self.btn_estadisticas.setIconSize(QSize(35, 35))

        self.verticalLayout_4.addWidget(self.btn_estadisticas)

        self.btn_temperaturas = QPushButton(self.frame_control)
        self.btn_temperaturas.setObjectName(u"btn_temperaturas")
        self.btn_temperaturas.setMinimumSize(QSize(0, 50))
        icon9 = QIcon()
        icon9.addFile(u"Imagenes/snowflake.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_temperaturas.setIcon(icon9)
        self.btn_temperaturas.setIconSize(QSize(35, 35))

        self.verticalLayout_4.addWidget(self.btn_temperaturas)


        self.horizontalLayout_2.addWidget(self.frame_control)

        self.frame_paginas = QFrame(self.frame_main)
        self.frame_paginas.setObjectName(u"frame_paginas")
        self.frame_paginas.setStyleSheet(u"")
        self.frame_paginas.setFrameShape(QFrame.StyledPanel)
        self.frame_paginas.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_paginas)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_temperaturas = QFrame(self.frame_paginas)
        self.frame_temperaturas.setObjectName(u"frame_temperaturas")
        self.frame_temperaturas.setStyleSheet(u"QLabel{\n"
"color:rgb(0, 48, 73);\n"
"font: 77 16pt \"Arial Black\";\n"
"}")
        self.frame_temperaturas.setFrameShape(QFrame.StyledPanel)
        self.frame_temperaturas.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_temperaturas)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_titulo_empresa = QLabel(self.frame_temperaturas)
        self.lbl_titulo_empresa.setObjectName(u"lbl_titulo_empresa")

        self.horizontalLayout_3.addWidget(self.lbl_titulo_empresa)

        self.lbl_logo_empresa = QLabel(self.frame_temperaturas)
        self.lbl_logo_empresa.setObjectName(u"lbl_logo_empresa")
        self.lbl_logo_empresa.setMinimumSize(QSize(60, 60))
        self.lbl_logo_empresa.setMaximumSize(QSize(60, 60))
        self.lbl_logo_empresa.setPixmap(QPixmap(u"Imagenes/Logo.png"))
        self.lbl_logo_empresa.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.lbl_logo_empresa)

        self.horizontalSpacer_2 = QSpacerItem(332, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.lbl_imagen_termometro = QLabel(self.frame_temperaturas)
        self.lbl_imagen_termometro.setObjectName(u"lbl_imagen_termometro")
        self.lbl_imagen_termometro.setMinimumSize(QSize(50, 50))
        self.lbl_imagen_termometro.setMaximumSize(QSize(50, 50))
        self.lbl_imagen_termometro.setPixmap(QPixmap(u"Imagenes/temperature-high.svg"))
        self.lbl_imagen_termometro.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.lbl_imagen_termometro)

        self.lbl_temperatura_actual = QLabel(self.frame_temperaturas)
        self.lbl_temperatura_actual.setObjectName(u"lbl_temperatura_actual")

        self.horizontalLayout_3.addWidget(self.lbl_temperatura_actual)

        self.comboBox_temperaturas = QComboBox(self.frame_temperaturas)
        self.comboBox_temperaturas.addItem("")
        self.comboBox_temperaturas.addItem("")
        self.comboBox_temperaturas.addItem("")
        self.comboBox_temperaturas.setObjectName(u"comboBox_temperaturas")
        self.comboBox_temperaturas.setMinimumSize(QSize(60, 0))
        self.comboBox_temperaturas.setStyleSheet(u"QComboBox{\n"
"border: 1px solid rgb(0, 48, 73);\n"
"border-radius:4px;\n"
"padding-left:10px;\n"
"font:75 12pt \"Arial Black\";\n"
"color: rgb(0, 48, 73);\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"width:12px;\n"
"height:12px;\n"
"margin-right:15px;\n"
"}\n"
"\n"
"QComboBox::on{\n"
"border: 4px solid rgb(102, 155, 188);\n"
"}")

        self.horizontalLayout_3.addWidget(self.comboBox_temperaturas)

        self.lbl_titulo_empresa.raise_()
        self.lbl_temperatura_actual.raise_()
        self.lbl_imagen_termometro.raise_()
        self.lbl_logo_empresa.raise_()
        self.comboBox_temperaturas.raise_()

        self.verticalLayout_3.addWidget(self.frame_temperaturas)

        self.frame_contenido = QFrame(self.frame_paginas)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setStyleSheet(u"QComboBox{\n"
"border: 1px solid rgb(0, 48, 73);\n"
"border-radius:4px;\n"
"padding-left:10px;\n"
"font:75 12pt \"Times New Roman\";\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"width:12px;\n"
"height:12px;\n"
"margin-right:15px;\n"
"}\n"
"\n"
"QComboBox::on{\n"
"border: 4px solid rgb(102, 155, 188);\n"
"}\n"
"\n"
"\n"
"\n"
"QFrame{\n"
"background-color:rgb(253, 240, 213);\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QLabel{\n"
"font: 87 12pt \"Arial Black\";\n"
"background-color:rgb();\n"
"color:rgb(0, 48, 73);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border:0px;\n"
"color:rgb(0, 48, 73);\n"
"border-bottom:2px solid rgb(61,61,61);\n"
"font: 75 12pt \"Times New Roman\";\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:rgb(0, 48, 73);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"border-radius:20px;\n"
"color:rgb(253, 240, 213);\n"
"font: 77 10pt \"Arial Black\";\n"
"border-color:rgb(253, 240, 213);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-col"
                        "or:rgb(102, 155, 188);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"border-radius:20px;\n"
"color:rgb(0, 48, 73);\n"
"font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 48, 73);\n"
"gridline-color:rgb(0, 48, 73);\n"
"font-size:(12pt);\n"
"color:#000000;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"background-color: rgb(0, 48, 73);\n"
"border: 1px solid rgb(0,0,0);\n"
"font-size: 12pt;\n"
"color:rgb(253, 240, 213);\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::Section{\n"
"background-color:rgb(0,0,0);\n"
"border: 1px: solid: rgb(0, 206, 152);\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::Items{\n"
"background-color:rgb(0,0,0);\n"
"border: 1px: solid: rgb(0, 206, 152);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame_contenido.setFrameShape(QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_contenido)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(1, 1, 1, 1)
        self.stackedWidget_menu = QStackedWidget(self.frame_contenido)
        self.stackedWidget_menu.setObjectName(u"stackedWidget_menu")
        self.stackedWidget_menu.setEnabled(True)
        self.page_temperaturas = QWidget()
        self.page_temperaturas.setObjectName(u"page_temperaturas")
        self.verticalLayout_22 = QVBoxLayout(self.page_temperaturas)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_11 = QLabel(self.page_temperaturas)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_11)

        self.tabla_temperaturas = QTableWidget(self.page_temperaturas)
        if (self.tabla_temperaturas.columnCount() < 5):
            self.tabla_temperaturas.setColumnCount(5)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.Dense2Pattern)
        font = QFont()
        font.setFamilies([u"Arial Black"])
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setForeground(brush);
        self.tabla_temperaturas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_temperaturas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_temperaturas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_temperaturas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_temperaturas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabla_temperaturas.setObjectName(u"tabla_temperaturas")
        self.tabla_temperaturas.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabla_temperaturas.sizePolicy().hasHeightForWidth())
        self.tabla_temperaturas.setSizePolicy(sizePolicy)
        self.tabla_temperaturas.setMinimumSize(QSize(0, 0))
        self.tabla_temperaturas.setLayoutDirection(Qt.LeftToRight)
        self.tabla_temperaturas.setAutoFillBackground(False)
        self.tabla_temperaturas.setFrameShape(QFrame.StyledPanel)
        self.tabla_temperaturas.setMidLineWidth(0)
        self.tabla_temperaturas.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tabla_temperaturas.setAlternatingRowColors(False)
        self.tabla_temperaturas.setShowGrid(True)
        self.tabla_temperaturas.setGridStyle(Qt.SolidLine)
        self.tabla_temperaturas.setSortingEnabled(False)
        self.tabla_temperaturas.horizontalHeader().setVisible(True)
        self.tabla_temperaturas.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_temperaturas.horizontalHeader().setDefaultSectionSize(152)
        self.tabla_temperaturas.horizontalHeader().setHighlightSections(True)
        self.tabla_temperaturas.verticalHeader().setVisible(False)
        self.tabla_temperaturas.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_temperaturas.verticalHeader().setHighlightSections(True)

        self.verticalLayout_13.addWidget(self.tabla_temperaturas)


        self.verticalLayout_22.addLayout(self.verticalLayout_13)

        self.stackedWidget_menu.addWidget(self.page_temperaturas)
        self.page_credenciales_eliminar_temperatura = QWidget()
        self.page_credenciales_eliminar_temperatura.setObjectName(u"page_credenciales_eliminar_temperatura")
        self.verticalLayout_21 = QVBoxLayout(self.page_credenciales_eliminar_temperatura)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_18 = QLabel(self.page_credenciales_eliminar_temperatura)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_18)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_21.addItem(self.verticalSpacer_11)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_4)

        self.lbl_logo_empresa_5 = QLabel(self.page_credenciales_eliminar_temperatura)
        self.lbl_logo_empresa_5.setObjectName(u"lbl_logo_empresa_5")
        self.lbl_logo_empresa_5.setMinimumSize(QSize(120, 120))
        self.lbl_logo_empresa_5.setMaximumSize(QSize(120, 120))
        self.lbl_logo_empresa_5.setPixmap(QPixmap(u"../../Carniceria/freshMeatSoft/Imagenes/portrait.svg"))
        self.lbl_logo_empresa_5.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.lbl_logo_empresa_5)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_18)


        self.verticalLayout_21.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, -1, 5)
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_19)

        self.lbl_contrasena_eliminar_temperatura = QLineEdit(self.page_credenciales_eliminar_temperatura)
        self.lbl_contrasena_eliminar_temperatura.setObjectName(u"lbl_contrasena_eliminar_temperatura")
        self.lbl_contrasena_eliminar_temperatura.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_15.addWidget(self.lbl_contrasena_eliminar_temperatura)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_20)


        self.verticalLayout_21.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, -1, -1, 60)
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_23)

        self.btn_validar_contrasena_eliminar_temperatura = QPushButton(self.page_credenciales_eliminar_temperatura)
        self.btn_validar_contrasena_eliminar_temperatura.setObjectName(u"btn_validar_contrasena_eliminar_temperatura")
        self.btn_validar_contrasena_eliminar_temperatura.setMinimumSize(QSize(120, 40))

        self.horizontalLayout_16.addWidget(self.btn_validar_contrasena_eliminar_temperatura)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_24)


        self.verticalLayout_21.addLayout(self.horizontalLayout_16)

        self.stackedWidget_menu.addWidget(self.page_credenciales_eliminar_temperatura)
        self.page_estadisticas = QWidget()
        self.page_estadisticas.setObjectName(u"page_estadisticas")
        self.verticalLayout_14 = QVBoxLayout(self.page_estadisticas)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.lbl_titulo_estadisticas = QLabel(self.page_estadisticas)
        self.lbl_titulo_estadisticas.setObjectName(u"lbl_titulo_estadisticas")
        self.lbl_titulo_estadisticas.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.lbl_titulo_estadisticas)

        self.stackedWidget_menu.addWidget(self.page_estadisticas)
        self.page_corte_de_caja = QWidget()
        self.page_corte_de_caja.setObjectName(u"page_corte_de_caja")
        self.verticalLayout_15 = QVBoxLayout(self.page_corte_de_caja)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.lbl_titulo_corte_de_caja = QLabel(self.page_corte_de_caja)
        self.lbl_titulo_corte_de_caja.setObjectName(u"lbl_titulo_corte_de_caja")
        self.lbl_titulo_corte_de_caja.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.lbl_titulo_corte_de_caja)

        self.btn_anadir_gasto = QPushButton(self.page_corte_de_caja)
        self.btn_anadir_gasto.setObjectName(u"btn_anadir_gasto")
        self.btn_anadir_gasto.setMinimumSize(QSize(120, 40))

        self.verticalLayout_15.addWidget(self.btn_anadir_gasto)

        self.stackedWidget_menu.addWidget(self.page_corte_de_caja)
        self.page_agregar_inventario = QWidget()
        self.page_agregar_inventario.setObjectName(u"page_agregar_inventario")
        self.verticalLayout_11 = QVBoxLayout(self.page_agregar_inventario)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_7 = QLabel(self.page_agregar_inventario)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(30)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(30)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.page_agregar_inventario)
        self.label.setObjectName(u"label")

        self.verticalLayout_7.addWidget(self.label)

        self.label_2 = QLabel(self.page_agregar_inventario)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_7.addWidget(self.label_2)

        self.label_5 = QLabel(self.page_agregar_inventario)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.page_agregar_inventario)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.label_4 = QLabel(self.page_agregar_inventario)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)

        self.label_3 = QLabel(self.page_agregar_inventario)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_7.addWidget(self.label_3)


        self.horizontalLayout_7.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lineEdit = QLineEdit(self.page_agregar_inventario)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 0))

        self.verticalLayout_6.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.page_agregar_inventario)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_6.addWidget(self.lineEdit_2)

        self.comboBox = QComboBox(self.page_agregar_inventario)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.verticalLayout_6.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.page_agregar_inventario)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_6.addWidget(self.comboBox_2)

        self.lineEdit_4 = QLineEdit(self.page_agregar_inventario)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 0))

        self.verticalLayout_6.addWidget(self.lineEdit_4)

        self.lineEdit_3 = QLineEdit(self.page_agregar_inventario)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 0))

        self.verticalLayout_6.addWidget(self.lineEdit_3)


        self.horizontalLayout_7.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.btn_agregar_producto = QPushButton(self.page_agregar_inventario)
        self.btn_agregar_producto.setObjectName(u"btn_agregar_producto")
        self.btn_agregar_producto.setMinimumSize(QSize(120, 40))
        self.btn_agregar_producto.setIconSize(QSize(40, 40))

        self.horizontalLayout_9.addWidget(self.btn_agregar_producto)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.stackedWidget_menu.addWidget(self.page_agregar_inventario)
        self.page_editar_inventario = QWidget()
        self.page_editar_inventario.setObjectName(u"page_editar_inventario")
        self.verticalLayout_29 = QVBoxLayout(self.page_editar_inventario)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_45 = QLabel(self.page_editar_inventario)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font1)
        self.label_45.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_45)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_14)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(30)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_49 = QLabel(self.page_editar_inventario)
        self.label_49.setObjectName(u"label_49")

        self.verticalLayout_27.addWidget(self.label_49)

        self.label_48 = QLabel(self.page_editar_inventario)
        self.label_48.setObjectName(u"label_48")

        self.verticalLayout_27.addWidget(self.label_48)

        self.label_47 = QLabel(self.page_editar_inventario)
        self.label_47.setObjectName(u"label_47")

        self.verticalLayout_27.addWidget(self.label_47)

        self.label_46 = QLabel(self.page_editar_inventario)
        self.label_46.setObjectName(u"label_46")

        self.verticalLayout_27.addWidget(self.label_46)

        self.label_43 = QLabel(self.page_editar_inventario)
        self.label_43.setObjectName(u"label_43")

        self.verticalLayout_27.addWidget(self.label_43)

        self.label_44 = QLabel(self.page_editar_inventario)
        self.label_44.setObjectName(u"label_44")

        self.verticalLayout_27.addWidget(self.label_44)


        self.horizontalLayout_22.addLayout(self.verticalLayout_27)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setSpacing(30)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(25, -1, -1, -1)
        self.lineEdit_26 = QLineEdit(self.page_editar_inventario)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setMinimumSize(QSize(0, 0))

        self.verticalLayout_28.addWidget(self.lineEdit_26)

        self.lineEdit_27 = QLineEdit(self.page_editar_inventario)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setMinimumSize(QSize(0, 0))

        self.verticalLayout_28.addWidget(self.lineEdit_27)

        self.comboBox_13 = QComboBox(self.page_editar_inventario)
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.setObjectName(u"comboBox_13")
        self.comboBox_13.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.verticalLayout_28.addWidget(self.comboBox_13)

        self.comboBox_14 = QComboBox(self.page_editar_inventario)
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.setObjectName(u"comboBox_14")

        self.verticalLayout_28.addWidget(self.comboBox_14)

        self.lineEdit_28 = QLineEdit(self.page_editar_inventario)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setMinimumSize(QSize(0, 0))

        self.verticalLayout_28.addWidget(self.lineEdit_28)

        self.lineEdit_25 = QLineEdit(self.page_editar_inventario)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setMinimumSize(QSize(0, 0))

        self.verticalLayout_28.addWidget(self.lineEdit_25)


        self.horizontalLayout_22.addLayout(self.verticalLayout_28)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_22)


        self.verticalLayout_29.addLayout(self.horizontalLayout_22)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_13)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_21)

        self.btn_agregar_producto_7 = QPushButton(self.page_editar_inventario)
        self.btn_agregar_producto_7.setObjectName(u"btn_agregar_producto_7")
        self.btn_agregar_producto_7.setMinimumSize(QSize(120, 40))
        self.btn_agregar_producto_7.setIconSize(QSize(40, 40))

        self.horizontalLayout_21.addWidget(self.btn_agregar_producto_7)


        self.verticalLayout_29.addLayout(self.horizontalLayout_21)

        self.stackedWidget_menu.addWidget(self.page_editar_inventario)
        self.page_agregar_gasto = QWidget()
        self.page_agregar_gasto.setObjectName(u"page_agregar_gasto")
        self.verticalLayout_18 = QVBoxLayout(self.page_agregar_gasto)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.lbl_titulo_gastos = QLabel(self.page_agregar_gasto)
        self.lbl_titulo_gastos.setObjectName(u"lbl_titulo_gastos")
        self.lbl_titulo_gastos.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.lbl_titulo_gastos)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(23)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_9 = QLabel(self.page_agregar_gasto)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_16.addWidget(self.label_9)

        self.label_10 = QLabel(self.page_agregar_gasto)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_16.addWidget(self.label_10)


        self.horizontalLayout_4.addLayout(self.verticalLayout_16)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(50)
        self.lineEdit_concepto_gasto = QLineEdit(self.page_agregar_gasto)
        self.lineEdit_concepto_gasto.setObjectName(u"lineEdit_concepto_gasto")

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.lineEdit_concepto_gasto)

        self.lineEdit_monto_gasto = QLineEdit(self.page_agregar_gasto)
        self.lineEdit_monto_gasto.setObjectName(u"lineEdit_monto_gasto")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_monto_gasto)


        self.horizontalLayout_4.addLayout(self.formLayout_2)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_16)


        self.verticalLayout_18.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_10)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_8)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_5)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_17)

        self.btn_agregar_gasto = QPushButton(self.page_agregar_gasto)
        self.btn_agregar_gasto.setObjectName(u"btn_agregar_gasto")
        self.btn_agregar_gasto.setMinimumSize(QSize(120, 40))
        self.btn_agregar_gasto.setIconSize(QSize(40, 40))

        self.horizontalLayout_13.addWidget(self.btn_agregar_gasto)


        self.verticalLayout_18.addLayout(self.horizontalLayout_13)

        self.stackedWidget_menu.addWidget(self.page_agregar_gasto)
        self.page_credenciales_editar = QWidget()
        self.page_credenciales_editar.setObjectName(u"page_credenciales_editar")
        self.verticalLayout_9 = QVBoxLayout(self.page_credenciales_editar)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.page_credenciales_editar)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_12)

        self.lbl_logo_empresa_2 = QLabel(self.page_credenciales_editar)
        self.lbl_logo_empresa_2.setObjectName(u"lbl_logo_empresa_2")
        self.lbl_logo_empresa_2.setMinimumSize(QSize(120, 120))
        self.lbl_logo_empresa_2.setMaximumSize(QSize(120, 120))
        self.lbl_logo_empresa_2.setPixmap(QPixmap(u"Imagenes/portrait.svg"))
        self.lbl_logo_empresa_2.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.lbl_logo_empresa_2)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 5)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.lbl_contrasena_editar = QLineEdit(self.page_credenciales_editar)
        self.lbl_contrasena_editar.setObjectName(u"lbl_contrasena_editar")
        self.lbl_contrasena_editar.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_10.addWidget(self.lbl_contrasena_editar)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_11)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 60)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.btn_validar_contrasena_editar = QPushButton(self.page_credenciales_editar)
        self.btn_validar_contrasena_editar.setObjectName(u"btn_validar_contrasena_editar")
        self.btn_validar_contrasena_editar.setMinimumSize(QSize(120, 40))

        self.horizontalLayout_8.addWidget(self.btn_validar_contrasena_editar)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.stackedWidget_menu.addWidget(self.page_credenciales_editar)
        self.page_credenciales_eliminar = QWidget()
        self.page_credenciales_eliminar.setObjectName(u"page_credenciales_eliminar")
        self.verticalLayout_20 = QVBoxLayout(self.page_credenciales_eliminar)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_17 = QLabel(self.page_credenciales_eliminar)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_17)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_19.addItem(self.verticalSpacer_7)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_29)

        self.lbl_logo_empresa_4 = QLabel(self.page_credenciales_eliminar)
        self.lbl_logo_empresa_4.setObjectName(u"lbl_logo_empresa_4")
        self.lbl_logo_empresa_4.setMinimumSize(QSize(120, 120))
        self.lbl_logo_empresa_4.setMaximumSize(QSize(120, 120))
        self.lbl_logo_empresa_4.setPixmap(QPixmap(u"Imagenes/portrait.svg"))
        self.lbl_logo_empresa_4.setScaledContents(True)

        self.horizontalLayout_19.addWidget(self.lbl_logo_empresa_4)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_30)


        self.verticalLayout_19.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, -1, -1, 5)
        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_31)

        self.lbl_contrasena_eliminar = QLineEdit(self.page_credenciales_eliminar)
        self.lbl_contrasena_eliminar.setObjectName(u"lbl_contrasena_eliminar")
        self.lbl_contrasena_eliminar.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_20.addWidget(self.lbl_contrasena_eliminar)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_32)


        self.verticalLayout_19.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, -1, -1, 60)
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_33)

        self.btn_validar_contrasena_eliminar = QPushButton(self.page_credenciales_eliminar)
        self.btn_validar_contrasena_eliminar.setObjectName(u"btn_validar_contrasena_eliminar")
        self.btn_validar_contrasena_eliminar.setMinimumSize(QSize(120, 40))

        self.horizontalLayout_25.addWidget(self.btn_validar_contrasena_eliminar)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_34)


        self.verticalLayout_19.addLayout(self.horizontalLayout_25)


        self.verticalLayout_20.addLayout(self.verticalLayout_19)

        self.stackedWidget_menu.addWidget(self.page_credenciales_eliminar)
        self.page_inventario = QWidget()
        self.page_inventario.setObjectName(u"page_inventario")
        self.verticalLayout_5 = QVBoxLayout(self.page_inventario)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_titulo_inventario = QLabel(self.page_inventario)
        self.lbl_titulo_inventario.setObjectName(u"lbl_titulo_inventario")
        self.lbl_titulo_inventario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbl_titulo_inventario)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tabla_inventario = QTableWidget(self.page_inventario)
        if (self.tabla_inventario.columnCount() < 7):
            self.tabla_inventario.setColumnCount(7)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.Dense2Pattern)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        __qtablewidgetitem5.setForeground(brush1);
        self.tabla_inventario.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_inventario.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_inventario.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_inventario.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_inventario.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_inventario.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_inventario.setHorizontalHeaderItem(6, __qtablewidgetitem11)
        self.tabla_inventario.setObjectName(u"tabla_inventario")
        self.tabla_inventario.setEnabled(True)
        sizePolicy.setHeightForWidth(self.tabla_inventario.sizePolicy().hasHeightForWidth())
        self.tabla_inventario.setSizePolicy(sizePolicy)
        self.tabla_inventario.setMinimumSize(QSize(0, 0))
        self.tabla_inventario.setLayoutDirection(Qt.LeftToRight)
        self.tabla_inventario.setAutoFillBackground(False)
        self.tabla_inventario.setFrameShape(QFrame.StyledPanel)
        self.tabla_inventario.setMidLineWidth(0)
        self.tabla_inventario.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tabla_inventario.setAlternatingRowColors(False)
        self.tabla_inventario.setShowGrid(True)
        self.tabla_inventario.setGridStyle(Qt.SolidLine)
        self.tabla_inventario.setSortingEnabled(False)
        self.tabla_inventario.horizontalHeader().setVisible(True)
        self.tabla_inventario.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_inventario.horizontalHeader().setDefaultSectionSize(109)
        self.tabla_inventario.horizontalHeader().setHighlightSections(True)
        self.tabla_inventario.verticalHeader().setVisible(False)
        self.tabla_inventario.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_inventario.verticalHeader().setHighlightSections(True)

        self.horizontalLayout_6.addWidget(self.tabla_inventario)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.btn_agregar_inventario = QPushButton(self.page_inventario)
        self.btn_agregar_inventario.setObjectName(u"btn_agregar_inventario")
        self.btn_agregar_inventario.setMinimumSize(QSize(120, 40))

        self.horizontalLayout_5.addWidget(self.btn_agregar_inventario)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.stackedWidget_menu.addWidget(self.page_inventario)
        self.page_mostrar_seleccion = QWidget()
        self.page_mostrar_seleccion.setObjectName(u"page_mostrar_seleccion")
        self.verticalLayout_12 = QVBoxLayout(self.page_mostrar_seleccion)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lbl_id = QLabel(self.page_mostrar_seleccion)
        self.lbl_id.setObjectName(u"lbl_id")
        self.lbl_id.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lbl_id)

        self.lbl_nombre = QLabel(self.page_mostrar_seleccion)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lbl_nombre)

        self.lbl_descripcion = QLabel(self.page_mostrar_seleccion)
        self.lbl_descripcion.setObjectName(u"lbl_descripcion")
        self.lbl_descripcion.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lbl_descripcion)

        self.lbl_categoria = QLabel(self.page_mostrar_seleccion)
        self.lbl_categoria.setObjectName(u"lbl_categoria")
        self.lbl_categoria.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lbl_categoria)

        self.lbl_subcategoria = QLabel(self.page_mostrar_seleccion)
        self.lbl_subcategoria.setObjectName(u"lbl_subcategoria")
        self.lbl_subcategoria.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lbl_subcategoria)

        self.lbl_precio = QLabel(self.page_mostrar_seleccion)
        self.lbl_precio.setObjectName(u"lbl_precio")
        self.lbl_precio.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lbl_precio)

        self.lbl_cantidad = QLabel(self.page_mostrar_seleccion)
        self.lbl_cantidad.setObjectName(u"lbl_cantidad")
        self.lbl_cantidad.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lbl_cantidad)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_12.addItem(self.verticalSpacer_4)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)

        self.btn_editar_inventario = QPushButton(self.page_mostrar_seleccion)
        self.btn_editar_inventario.setObjectName(u"btn_editar_inventario")
        self.btn_editar_inventario.setMinimumSize(QSize(120, 40))
        self.btn_editar_inventario.setIconSize(QSize(16, 16))

        self.horizontalLayout_12.addWidget(self.btn_editar_inventario)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_14)

        self.btn_eliminar_inventario = QPushButton(self.page_mostrar_seleccion)
        self.btn_eliminar_inventario.setObjectName(u"btn_eliminar_inventario")
        self.btn_eliminar_inventario.setMinimumSize(QSize(120, 40))

        self.horizontalLayout_12.addWidget(self.btn_eliminar_inventario)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_15)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.stackedWidget_menu.addWidget(self.page_mostrar_seleccion)
        self.page_ventas = QWidget()
        self.page_ventas.setObjectName(u"page_ventas")
        self.verticalLayout = QVBoxLayout(self.page_ventas)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_titulo_ventas = QLabel(self.page_ventas)
        self.lbl_titulo_ventas.setObjectName(u"lbl_titulo_ventas")
        self.lbl_titulo_ventas.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_titulo_ventas)

        self.lineEdit_busqueda_ventas = QLineEdit(self.page_ventas)
        self.lineEdit_busqueda_ventas.setObjectName(u"lineEdit_busqueda_ventas")
        self.lineEdit_busqueda_ventas.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_busqueda_ventas)

        self.tabla_ventas = QTableWidget(self.page_ventas)
        if (self.tabla_ventas.columnCount() < 4):
            self.tabla_ventas.setColumnCount(4)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_ventas.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_ventas.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabla_ventas.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabla_ventas.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        self.tabla_ventas.setObjectName(u"tabla_ventas")
        self.tabla_ventas.setProperty("showDropIndicator", True)
        self.tabla_ventas.horizontalHeader().setDefaultSectionSize(195)

        self.verticalLayout.addWidget(self.tabla_ventas)

        self.stackedWidget_menu.addWidget(self.page_ventas)

        self.verticalLayout_17.addWidget(self.stackedWidget_menu)


        self.verticalLayout_3.addWidget(self.frame_contenido)


        self.horizontalLayout_2.addWidget(self.frame_paginas)


        self.verticalLayout_2.addWidget(self.frame_main)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)

        self.horizontalLayout_17.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_menu.setCurrentIndex(9)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText("")
        self.btn_minimizar.setText("")
        self.btn_pestana.setText("")
        self.btn_maximizar.setText("")
        self.btn_cerrar.setText("")
        self.btn_inventario.setText(QCoreApplication.translate("MainWindow", u"    INVENTARIO", None))
        self.btn_ventas.setText(QCoreApplication.translate("MainWindow", u"   VENTAS", None))
        self.btn_cote_de_caja.setText(QCoreApplication.translate("MainWindow", u"    CORTE DE CAJA", None))
        self.btn_estadisticas.setText(QCoreApplication.translate("MainWindow", u"    ESTADISTICAS", None))
        self.btn_temperaturas.setText(QCoreApplication.translate("MainWindow", u"    TEMPERATURAS", None))
        self.lbl_titulo_empresa.setText(QCoreApplication.translate("MainWindow", u"FRESH MEAT SOFT", None))
        self.lbl_logo_empresa.setText("")
        self.lbl_imagen_termometro.setText("")
        self.lbl_temperatura_actual.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.comboBox_temperaturas.setItemText(0, QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.comboBox_temperaturas.setItemText(1, QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.comboBox_temperaturas.setItemText(2, QCoreApplication.translate("MainWindow", u"%", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Control de temperaturas", None))
        ___qtablewidgetitem = self.tabla_temperaturas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem1 = self.tabla_temperaturas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Temp Promedio", None));
        ___qtablewidgetitem2 = self.tabla_temperaturas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Temp Maxima", None));
        ___qtablewidgetitem3 = self.tabla_temperaturas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Temp Minima", None));
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"INGRESA LA CONTRASE\u00d1A", None))
        self.lbl_logo_empresa_5.setText("")
        self.btn_validar_contrasena_eliminar_temperatura.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.lbl_titulo_estadisticas.setText(QCoreApplication.translate("MainWindow", u"ESTADISTICAS", None))
        self.lbl_titulo_corte_de_caja.setText(QCoreApplication.translate("MainWindow", u"CORTE DE CAJA", None))
        self.btn_anadir_gasto.setText(QCoreApplication.translate("MainWindow", u"A\u00d1ADIR GASTO", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"AGREGAR PRODUCTO", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Descripcion:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Categoria:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"SubCategoria:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Precio:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Cantidad:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Carne", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Despensa", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Carne", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Pollo", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Res", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Cerdo", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Pescado", None))

        self.btn_agregar_producto.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"EDITAR PRODUCTO", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Descripcion:", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Categoria:", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"SubCategoria:", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Precio:", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Cantidad:", None))
        self.comboBox_13.setItemText(0, QCoreApplication.translate("MainWindow", u"Carne", None))
        self.comboBox_13.setItemText(1, QCoreApplication.translate("MainWindow", u"Despensa", None))

        self.comboBox_13.setCurrentText(QCoreApplication.translate("MainWindow", u"Carne", None))
        self.comboBox_14.setItemText(0, QCoreApplication.translate("MainWindow", u"Pollo", None))
        self.comboBox_14.setItemText(1, QCoreApplication.translate("MainWindow", u"Res", None))
        self.comboBox_14.setItemText(2, QCoreApplication.translate("MainWindow", u"Cerdo", None))
        self.comboBox_14.setItemText(3, QCoreApplication.translate("MainWindow", u"Pescado", None))
        self.comboBox_14.setItemText(4, QCoreApplication.translate("MainWindow", u"Fruta", None))
        self.comboBox_14.setItemText(5, QCoreApplication.translate("MainWindow", u"Verdura", None))
        self.comboBox_14.setItemText(6, QCoreApplication.translate("MainWindow", u"Abarrote", None))
        self.comboBox_14.setItemText(7, QCoreApplication.translate("MainWindow", u"Limpieza", None))
        self.comboBox_14.setItemText(8, QCoreApplication.translate("MainWindow", u"Cremer\u00eda", None))

        self.btn_agregar_producto_7.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.lbl_titulo_gastos.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR GASTOS", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"CONCEPTO:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"MONTO:", None))
        self.btn_agregar_gasto.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"INGRESA LA CONTRASE\u00d1A", None))
        self.lbl_logo_empresa_2.setText("")
        self.btn_validar_contrasena_editar.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"INGRESA LA CONTRASE\u00d1A", None))
        self.lbl_logo_empresa_4.setText("")
        self.btn_validar_contrasena_eliminar.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.lbl_titulo_inventario.setText(QCoreApplication.translate("MainWindow", u"INVENTARIO", None))
        ___qtablewidgetitem4 = self.tabla_inventario.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem5 = self.tabla_inventario.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem6 = self.tabla_inventario.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None));
        ___qtablewidgetitem7 = self.tabla_inventario.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Categoria", None));
        ___qtablewidgetitem8 = self.tabla_inventario.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"SubCategoria", None));
        ___qtablewidgetitem9 = self.tabla_inventario.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Precio", None));
        ___qtablewidgetitem10 = self.tabla_inventario.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        self.btn_agregar_inventario.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.lbl_id.setText(QCoreApplication.translate("MainWindow", u"Tu hermana :D", None))
        self.lbl_nombre.setText(QCoreApplication.translate("MainWindow", u"Nombre Producto", None))
        self.lbl_descripcion.setText(QCoreApplication.translate("MainWindow", u"Descripcion Producto", None))
        self.lbl_categoria.setText(QCoreApplication.translate("MainWindow", u"Categoria Producto", None))
        self.lbl_subcategoria.setText(QCoreApplication.translate("MainWindow", u"SubCategoria Producto", None))
        self.lbl_precio.setText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.lbl_cantidad.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
        self.btn_editar_inventario.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_eliminar_inventario.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.lbl_titulo_ventas.setText(QCoreApplication.translate("MainWindow", u"VENTAS", None))
        self.lineEdit_busqueda_ventas.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el producto a buscar", None))
        ___qtablewidgetitem11 = self.tabla_ventas.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem12 = self.tabla_ventas.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem13 = self.tabla_ventas.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Precio", None));
        ___qtablewidgetitem14 = self.tabla_ventas.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
    # retranslateUi

