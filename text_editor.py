from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Main(QMainWindow):
    def __init__(self, parent= None):
        QMainWindow.__init__(self, parent)
        self.InitUi()
        self.filename = ''
        
        
    def menubar(self):
        menubar = self.menuBar()
        File = menubar.addMenu('File')
        Edit = menubar.addMenu('Edit')
        View = menubar.addMenu('View')

        File.addAction(self.newAction)
        File.addAction(self.openAction)
        File.addAction(self.save)
        
    def ToolBar(self):
        self.newAction = QAction('New')
        self.newAction.setShortcut('ctrl+n')
        self.newAction.triggered.connect(self.new)

        self.openAction = QAction('Open')
        self.openAction.setShortcut('ctrl+o')
        self.openAction.triggered.connect(self.open)

        self.save = QAction('Save')
        self.save.setShortcut('ctrl+s')
        self.save.triggered.connect(self.savee)

    def FormatBar(self):
        fontbox = QFontComboBox(self)
        fontbox.currentFontChanged.connect(lambda font: self.text.setCurrentFont(font))
        fontsize = QSpinBox(self)
        fontsize.setSuffix(' Pts')
        fontsize.valueChanged.connect(lambda size: self.text.setFontPointSize(size))
        fontsize.setValue(14)

        bold = QAction(QIcon(r"C:\Users\subed\Desktop\Qt\Practice\Text_Editor\bold.png"), 'Bold', self)
        italic = QAction(QIcon(r'C:\Users\subed\Desktop\Qt\Practice\Text_Editor\italic.png'), 'Italic', self)
        underline = QAction(QIcon(r'C:\Users\subed\Desktop\Qt\Practice\Text_Editor\underline.png'), 'Underline', self)

        alignJustify = QAction(QIcon(r'C:\Users\subed\Desktop\Qt\Practice\Text_Editor\align-justify.png'), 'Align-Justify', self)
        alignCenter = QAction(QIcon(r'C:\Users\subed\Desktop\Qt\Practice\Text_Editor\align-center.png'), 'Align-Center', self)
        alignLeft = QAction(QIcon(r'C:\Users\subed\Desktop\Qt\Practice\Text_Editor\align-left.png'), 'Align-Left', self)
        alignRight = QAction(QIcon(r'C:\Users\subed\Desktop\Qt\Practice\Text_Editor\align-right.png'), 'Align-Right', self)

        self.formatbar = self.addToolBar('Format')
        self.formatbar.addWidget(fontbox)
        self.formatbar.addWidget(fontsize)
        self.formatbar.addSeparator()

        self.formatbar.addAction(bold)
        bold.triggered.connect(self.Bold)

        self.formatbar.addAction(italic)
        italic.triggered.connect(self.Italic)

        self.formatbar.addAction(underline)
        underline.triggered.connect(self.Underline)

        self.formatbar.addSeparator()
        
        self.formatbar.addAction(alignJustify)
        alignJustify.triggered.connect(self.alignJustify)

        self.formatbar.addAction(alignCenter)
        alignCenter.triggered.connect(self.alignCenter)

        self.formatbar.addAction(alignLeft)
        alignLeft.triggered.connect(self.alignLeft)

        self.formatbar.addAction(alignRight)
        alignRight.triggered.connect(self.alignRight)

        self.formatbar.addSeparator()
        

    def new(self):
        window = Main(self)
        window.show()

    def savee(self):
        if not self.filename:
            self.filename = QFileDialog.getSaveFileName(self, ' Save File ')[0].split('/')[-1]

        if not self.filename.endswith(".txt") :
            self.filename += ".txt"
       
        with open(self.filename, 'wt') as file:
            file.write(self.text.toPlainText())

    def open(self):
        self.filename = QFileDialog.getOpenFileName(self, ' Open File ', '.', '(*.txt)')[0].split('/')[-1]

        if self.filename:
            with open(self.filename, 'rt') as file:
                self.text.setText(file.read())

    def Bold(self):
        if self.text.fontWeight() == QFont.Bold:
            self.text.setFontWeight(QFont.Normal)
        else:
            self.text.setFontWeight(QFont.Bold)


    def Italic(self):
        state = self.text.fontItalic()
        self.text.setFontItalic(not state)

    def Underline(self):
        state = self.text.fontUnderline()
        self.text.setFontUnderline(not state)

    def Strike(self):
        words = self.text.currentCharFormat()
        words.setFontStrikeOut(not words.setFontStrikeOut())
        self.text.setCurrentCharFormat(words)

    def alignCenter(self):
        self.text.setAlignment(Qt.AlignCenter)

    def alignLeft(self):
        self.text.setAlignment(Qt.AlignLeft)

    def alignRight(self):
        self.text.setAlignment(Qt.AlignRight)

    def alignJustify(self):
        self.text.setAlignment(Qt.AlignJustify)

    def InitUi(self):

        self.ToolBar()
        self.menubar()
        self.text = QTextEdit()
        self.FormatBar()
        self.setWindowTitle('Text Editor (Development in Progress)')
        self.setWindowIcon(QIcon(r'C:\Users\subed\Desktop\Qt\Practice\Text_Editor\text_editor.png'))
        self.setCentralWidget(self.text)
        self.setGeometry(100, 100, 900, 600)

    

def main():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    app.exec_()

if __name__ == "__main__":
    main()