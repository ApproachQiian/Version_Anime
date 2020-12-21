import sys
import ctypes
from matplotlib.figure import Figure
from PyQt5.QtGui import QIcon, QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGroupBox, QTextEdit, QMessageBox, QSizePolicy, \
    QFileDialog, QLabel


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=4, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        pass


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowIcon(QIcon('../dataset/logo/ml.png'))
        self.setWindowTitle('ANIME DCGAN!')
        self.resize(1232, 859)
        self.image = QLabel(self)
        self.image.setGeometry(30, 30, 501, 351)
        self.image.setStyleSheet(""" border:1px solid #cceff5;background:#fafcfd""")

        self.btn1 = QPushButton('选择本地文件', self)
        self.btn1.setGeometry(190, 400, 151, 51)
        self.btn1.clicked.connect(self.openImage)
        self.btn1.setStyleSheet(""".QPushButton {
            box-shadow: 0px 1px 0px 0px #f0f7fa;
            background:linear-gradient(to bottom, #33bdef 5%, #019ad2 100%);
            background-color:#33bdef;
            border-radius:6px;
            border:1px solid #057fd0;
            display:inline-block;
            cursor:pointer;
            color:#ffffff;
            font-family:Arial;
            font-size:15px;
            font-weight:bold;
            padding:6px 24px;
            text-decoration:none;
            text-shadow:0px -1px 0px #5b6178;
        }
        .QPushButton:hover {
            background:linear-gradient(to bottom, #019ad2 5%, #33bdef 100%);
            background-color:#019ad2;
        }
        .QPushButton:active {
            position:relative;
            top:1px;
    }""")

        self.btn2 = QPushButton('保存到本地', self)
        self.btn2.setGeometry(808, 400, 151, 51)
        self.btn2.setStyleSheet("""
            .QPushButton {
                box-shadow:inset 0px 1px 0px 0px #f7c5c0;
                background:linear-gradient(to bottom, #fc8d83 5%, #e4685d 100%);
                background-color:#fc8d83;
                border-radius:6px;
                border:1px solid #d83526;
                display:inline-block;
                cursor:pointer;
                color:#ffffff;
                font-family:Arial;
                font-size:15px;
                font-weight:bold;
                padding:6px 24px;
                text-decoration:none;
                text-shadow:0px 1px 0px #b23e35;
            }
            .QPushButton:hover {
                background:linear-gradient(to bottom, #e4685d 5%, #fc8d83 100%);
                background-color:#e4685d;
            }
            .QPushButton:active {
                position:relative;
                top:1px;
            }
        """)
        self.btn2.clicked.connect(self.save_image)

        self.imageshower = QLabel(self)
        self.imageshower.setGeometry(620, 30, 501, 351)
        self.imageshower.setStyleSheet("""
             border:1px solid #bfd1eb;background:#f3faff
        """)

        self.groupbox = QGroupBox('图像处理信息', self)
        self.groupbox.setGeometry(30, 490, 1161, 277)

        self.textedit = QTextEdit(self)
        self.textedit.setGeometry(45, 511, 1131, 241)
        self.textedit.setStyleSheet(""" border:1px solid #ffcc00;background:#fffff7""")

    def openImage(self):
        try:
            imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;*.png;All Files(*)")
            self.image.setPixmap(QPixmap(str(imgName)))
            self.image.setScaledContents(True)
        except Exception as e:
            print(str(e))

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '退出程序', "真的要退出程序吗QAQ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def save_image(self):
        try:
            fileName = QFileDialog.getSaveFileName(self, '保存文件', '.', '图像文件(*.png *.jpg)')
            path = fileName[0]
            print(str(path))
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID()
    window = Window()
    window.show()
    sys.exit(app.exec_())
