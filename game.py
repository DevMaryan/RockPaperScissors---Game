import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import QTimer
from random import randint

textFont = QFont('Helvetica', 12)
computerScore = 0
playerScore = 0

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Rock Paper Scissors Game - Developed my Marjan Shapkaroski')
        self.setFixedSize(570,370)
        self.setWindowIcon(QIcon('images\\game.png'))
        self.UI()

    def UI(self):
        # Computer & Player Score
        self.scoreComputer = QLabel('Computer score ', self)
        self.scoreComputer.move(30,20)
        self.scoreComputer.setFont(textFont)
        self.scoreComputer.adjustSize()

        self.scorePlayer = QLabel('Player score ', self)
        self.scorePlayer.move(400,20)
        self.scorePlayer.setFont(textFont)

        # Computer & Player Images
        self.imageComputer = QLabel(self)
        self.imageComputer.setPixmap(QPixmap('images\\paper.png'))
        self.imageComputer.move(10,100)

        self.imagePlayer = QLabel(self)
        self.imagePlayer.setPixmap(QPixmap('images\\paper.png'))
        self.imagePlayer.move(350,100)

        # VS images
        self.imageVS = QLabel(self)
        self.imageVS.setPixmap(QPixmap('images\\game.png'))
        self.imageVS.move(240,130)

        # Buttons
        self.btnStart = QPushButton('Start', self)
        self.btnStart.move(150, 330)
        self.btnStart.clicked.connect(self.start)
        self.btnStop = QPushButton('Stop', self)
        self.btnStop.move(235, 330)
        self.btnStop.clicked.connect(self.stop)

        self.btnNewGame = QPushButton('New Game', self)
        self.btnNewGame.move(320, 330)
        self.btnNewGame.clicked.connect(self.newGame)

        # Timer
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.playGame)

        self.show()

    def start(self):
        self.btnStop.setEnabled(True)
        self.timer.start()


    def playGame(self):
        self.rndComputer = randint(0,2)
        if self.rndComputer == 0:
            self.imageComputer.setPixmap(QPixmap('images\\rock.png'))
        elif self.rndComputer == 1:
            self.imageComputer.setPixmap(QPixmap('images\\paper.png'))
        else:
            self.imageComputer.setPixmap(QPixmap('images\\scissors.png'))
            
        self.rndPlayer = randint(0,2)
        if self.rndPlayer == 0:
            self.imagePlayer.setPixmap(QPixmap('images\\rock.png'))
        elif self.rndPlayer == 1:
            self.imagePlayer.setPixmap(QPixmap('images\\paper.png'))
        else:
            self.imagePlayer.setPixmap(QPixmap('images\\scissors.png'))
            
    def gameLogic(self):
        global computerScore
        global playerScore

        if self.rndComputer == 0 and self.rndPlayer == 0:
            mbox = QMessageBox.information(self, 'Result','Draw Game')
        elif self.rndComputer == 0 and self.rndPlayer == 1:
            mbox = QMessageBox.information(self, 'Result','You Won')
            playerScore += 1
            self.scorePlayer.setText('Your score {}'.format(playerScore))
        elif self.rndComputer == 0 and self.rndPlayer == 2:
            mbox = QMessageBox.information(self, 'Result','Computer Won')
            computerScore += 1
            self.scoreComputer.setText('Computer score {}'.format(computerScore))
            self.scoreComputer.adjustSize()
        elif self.rndComputer == 1 and self.rndPlayer == 0:
            mbox = QMessageBox.information(self, 'Result','Computer Won')
            computerScore += 1
            self.scoreComputer.setText('Computer score {}'.format(computerScore))
            self.scoreComputer.adjustSize()
        elif self.rndComputer == 1 and self.rndPlayer == 1:
            mbox = QMessageBox.information(self, 'Result','Draw Game')
        elif self.rndComputer == 1 and self.rndPlayer == 2:
            mbox = QMessageBox.information(self, 'Result','You Won')
            playerScore += 1
            self.scorePlayer.setText('Your score {}'.format(playerScore))
        elif self.rndComputer == 2 and self.rndPlayer == 0:
            mbox = QMessageBox.information(self, 'Result','You Won')
            playerScore += 1
            self.scorePlayer.setText('Your score {}'.format(playerScore))
        elif self.rndComputer == 2 and self.rndPlayer == 1:
            mbox = QMessageBox.information(self, 'Result','Computer Won')
            computerScore += 1
            self.scoreComputer.setText('Computer score {}'.format(computerScore))
            self.scoreComputer.adjustSize()
        elif self.rndComputer == 2 and self.rndPlayer == 2:
            mbox = QMessageBox.information(self, 'Result','Draw Game')

        if computerScore == 3 or playerScore == 3:
            mbox = QMessageBox.information(self, 'Info','Game Over. Computer Score is {}, Player Score is {}'.format(computerScore,playerScore))
            self.btnStart.setEnabled(False)
            self.btnStop.setEnabled(False)


    def stop(self):
        self.btnStop.setEnabled(False)
        self.timer.stop()
        self.gameLogic()
    
    def newGame(self):
        global computerScore
        global playerScore

        computerScore = 0
        playerScore = 0
        self.btnStart.setEnabled(True)
        self.btnStop.setEnabled(True)
        self.start()
        
        


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()