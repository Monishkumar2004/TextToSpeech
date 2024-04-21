
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTextEdit, QHBoxLayout, QVBoxLayout

from gtts import gTTS 

import os


# text = "my name is ayush kumar gupta."

# audio = gTTS(text= text, lang='hi', slow= False)
# audio.save('output.mp3')

# os.system("start output.mp3")

class TextToSpeech(QWidget):
    
    def converter(self, text):
                
        text = self.input_box.toPlainText()
        audio = gTTS(text= text, lang= 'en', slow= False)
        audio.save('output.mp3')

        os.system('output.mp3')
    
    def __init__(self) :
        super().__init__()
        
        self.resize(500, 600)
        self.setWindowTitle("Text To Speech")

        # creating objects
        self.input_box = QTextEdit()
        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.converter)

        masterLayout = QVBoxLayout()
        masterLayout.addWidget(self.input_box)
        masterLayout.addWidget(self.convert_button)
        
        self.setLayout(masterLayout)

        



if __name__ == "__main__":
    app = QApplication([])
    mainWindow = TextToSpeech()
    mainWindow.show()
    app.exec_()
    