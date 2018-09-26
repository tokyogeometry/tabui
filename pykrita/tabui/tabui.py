from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QGridLayout, QToolButton, QSizePolicy
import krita

class TabUI(krita.DockWidget):

    def __init__(self):
        super(TabUI, self).__init__()

        self.baseWidget = QWidget()
        self.layout = QGridLayout()

        self.btnundo = QToolButton()
        self.btnundo.setStyleSheet("background-color:#300000;")
        self.btnundo.setText("Undo")
        self.btnundo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btnundo.clicked.connect(lambda: Krita.instance().action("edit_undo").trigger())
        self.layout.addWidget(self.btnundo, 0, 0)

        self.btnsave = QToolButton()
        self.btnsave.setStyleSheet("background-color:#002800;")
        self.btnsave.setText("Save")
        self.btnsave.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btnsave.clicked.connect(lambda: Krita.instance().action("file_save").trigger())
        self.layout.addWidget(self.btnsave, 0, 1)

        self.btnmirror = QToolButton()
        self.btnmirror.setStyleSheet("background-color:#000000;")
        self.btnmirror.setText("Mir.\nCanv.")
        self.btnmirror.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btnmirror.clicked.connect(lambda: Krita.instance().action("mirror_canvas").trigger())
        self.layout.addWidget(self.btnmirror, 0, 2)

        self.btnclear = QToolButton()
        self.btnclear.setStyleSheet("background-color:#000000;")
        self.btnclear.setText("Clear")
        self.btnclear.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btnclear.clicked.connect(lambda: Krita.instance().action("clear").trigger())
        self.layout.addWidget(self.btnclear, 1, 0)

        self.btndeselect = QToolButton()
        self.btndeselect.setStyleSheet("background-color:#000000;")
        self.btndeselect.setText("Desel.")
        self.btndeselect.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btndeselect.clicked.connect(lambda: Krita.instance().action("deselect").trigger())
        self.layout.addWidget(self.btndeselect, 1, 1)

        self.btnbrush = QToolButton()
        self.btnbrush.setStyleSheet("background-color:#000000;")
        self.btnbrush.setText("Brush")
        self.btnbrush.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btnbrush.clicked.connect(lambda: Krita.instance().action("KritaShape/KisToolBrush").trigger())
        self.layout.addWidget(self.btnbrush, 1, 2)

        self.btntransform = QToolButton()
        self.btntransform.setStyleSheet("background-color:#000000;")
        self.btntransform.setText("Transf.")
        self.btntransform.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btntransform.clicked.connect(lambda: Krita.instance().action("KisToolTransform").trigger())
        self.layout.addWidget(self.btntransform, 2, 0)

        self.btnfill = QToolButton()
        self.btnfill.setStyleSheet("background-color:#000000;")
        self.btnfill.setText("Fill")
        self.btnfill.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btnfill.clicked.connect(lambda: Krita.instance().action("fill_selection_foreground_color").trigger())
        self.layout.addWidget(self.btnfill, 2, 1)

        self.btncolorpicker = QToolButton()
        self.btncolorpicker.setStyleSheet("background-color:#000000;")
        self.btncolorpicker.setText("Col.\nPckr")
        self.btncolorpicker.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btncolorpicker.clicked.connect(lambda: Krita.instance().action("KritaSelected/KisToolColorPicker").trigger())
        self.layout.addWidget(self.btncolorpicker, 2, 2)

        self.btnselectionol = QToolButton()
        self.btnselectionol.setStyleSheet("background-color:#000000;")
        self.btnselectionol.setText("Outl.\nSel.")
        self.btnselectionol.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btnselectionol.clicked.connect(lambda: Krita.instance().action("KisToolSelectOutline").trigger())
        self.layout.addWidget(self.btnselectionol, 3, 0)

        self.baseWidget.setLayout(self.layout)
        self.setWidget(self.baseWidget)

        self.setWindowTitle(i18n("TabUI"))

    def canvasChanged(self, canvas):
        pass

Application.addDockWidgetFactory(krita.DockWidgetFactory("tabui", krita.DockWidgetFactoryBase.DockRight, TabUI))
