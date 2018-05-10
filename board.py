#!/usr/bin/env python3

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *
import time
from random import randint

class Board():
    def __init__(self):
        self.my_move = False
        self.decision = ""
        self.window = Tk()
        self.Menu_init()

    def Menu_init(self):
        self.window.title("Game Platform")
        self.result = Label(self.window, width=33, height=2, text="Welcome on Game Platform!\n Please send your name:")
        self.result.grid(row=1, column=1, columnspan=3)
        self.my_msg = StringVar()
        self.entry_field = Entry(self.window, textvariable=self.my_msg, width=33)
        self.entry_field.grid(row=5, column=1, columnspan=3)
        self.send_button = Button(self.window, text="Send", command=self.sendName, width=16, height=3, bg="grey")
        self.send_button.grid(row=6, column=1, columnspan=2)
        self.quit_button = Button(self.window, text="Quit Game Room", command=self.quitGame, width=16, height=3, bg="grey")
        self.quit_button.grid(row=6, column=3, columnspan=2)

    def showGames(self):
        self.TTT_button = Button(self.window, text="Tic Tac Toe", command=self.chooseTTT, width=33, height=3, bg="grey")
        self.TTT_button.grid(row=3, column=1, columnspan=3)
        self.GN_button = Button(self.window, text="Guess the Number", command=self.chooseGN, width=33, height=3, bg="grey")
        self.GN_button.grid(row=4, column=1, columnspan=3)

    def chooseTTT(self):
        self.decision = "TicTacToe"
        self.sendDecision()

    def chooseGN(self):
        self.decision = "GuessNumber"
        self.sendDecision()

    def GN_init(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.title("Guess the Number")
        self.randomNumber = 0;
        self.info = Label(self.window, width=33, height=2, text="Guess the Number between 0 and 100!")
        self.info.grid(row=1, column=1, columnspan=3)
        self.my_guess = StringVar()
        self.entry_guess = Entry(self.window, textvariable=self.my_guess, width=21)
        self.entry_guess.grid(row=2, column=1, columnspan=2)
        self.guess_button = Button(self.window, text="Have a guess!", width=10, height=3, command=self.guessNumber, bg="grey")
        self.guess_button.grid(row=2, column=3)
        self.result = Label(self.window, width=33, height=2, text="")
        self.result.grid(row=4, column=1, columnspan=3)
        self.entry_field = Entry(self.window, textvariable=self.my_msg, width=33)
        self.entry_field.grid(row=5, column=1, columnspan=3)
        self.send_button = Button(self.window, text="Send", command=self.sendMessage, width=10, height=3, bg="grey")
        self.send_button.grid(row=6, column=1)
        self.restartButton = Button(self.window, text="ReStart", command=self.chooseGN, width=10, height=3, bg="grey")
        self.restartButton.grid(row=6, column=2)
        self.back_button = Button(self.window, text="Back", command=self.chooseBack, width=10, height=3, bg="grey")
        self.back_button.grid(row=6, column=3)
        if (self.my_move):
            self.randomNumber = randint(0, 100)
            self.decision = "Number: " + str(self.randomNumber)
            self.sendDecision()

    def TTT_init(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.title("Tic Tac Toe")
        self.who_move = "X"
        self.move_cell = ""
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.b1 = Button(self.window, text=self.cells[1], width=10, height=5, command=self.b1_pressed, bg="white")
        self.b1.grid(row=1, column=1)
        self.b2 = Button(self.window, text=self.cells[2], width=10, height=5, command=self.b2_pressed, bg="white")
        self.b2.grid(row=1, column=2)
        self.b3 = Button(self.window, text=self.cells[3], width=10, height=5, command=self.b3_pressed, bg="white")
        self.b3.grid(row=1, column=3)
        self.b4 = Button(self.window, text=self.cells[4], width=10, height=5, command=self.b4_pressed, bg="white")
        self.b4.grid(row=2, column=1)
        self.b5 = Button(self.window, text=self.cells[5], width=10, height=5, command=self.b5_pressed, bg="white")
        self.b5.grid(row=2, column=2)
        self.b6 = Button(self.window, text=self.cells[6], width=10, height=5, command=self.b6_pressed, bg="white")
        self.b6.grid(row=2, column=3)
        self.b7 = Button(self.window, text=self.cells[7], width=10, height=5, command=self.b7_pressed, bg="white")
        self.b7.grid(row=3, column=1)
        self.b8 = Button(self.window, text=self.cells[8], width=10, height=5, command=self.b8_pressed, bg="white")
        self.b8.grid(row=3, column=2)
        self.b9 = Button(self.window, text=self.cells[9], width=10, height=5, command=self.b9_pressed, bg="white")
        self.b9.grid(row=3, column=3)
        self.result = Label(self.window, width=33, height=2, text="")
        self.result.grid(row=4, column=1, columnspan=3)
        self.entry_field = Entry(self.window, textvariable=self.my_msg, width=33)
        self.entry_field.grid(row=5, column=1, columnspan=3)
        self.send_button = Button(self.window, text="Send", command=self.sendMessage, width=10, height=3, bg="grey")
        self.send_button.grid(row=6, column=1)
        self.restartButton = Button(self.window, text="ReStart", command=self.restartButton_pressed, width=10, height=3, bg="grey")
        self.restartButton.grid(row=6, column=2)
        self.back_button = Button(self.window, text="Back", command=self.chooseBack, width=10, height=3, bg="grey")
        self.back_button.grid(row=6, column=3)

    def chooseBack(self):
        self.decision = "Back"
        self.sendDecision()

    def backToMenu(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.Menu_init()
        self.showGames()
        self.result.config(text="Choose the game:")

    def guessNumber(self):
        if self.my_move:
            self.msg = self.my_guess.get()
            self.my_guess.set("")  # Clears input field.
            self.decision = "Guess: " + str(self.msg)
            self.sendDecision()

    def checkResultGN(self, new_guess):
        self.my_move = not self.my_move
        if (new_guess.isdigit() == False):
            self.info.config(text=new_guess + " is not a positive integer!")
        elif (int(new_guess) == self.randomNumber):
            if (self.my_move):
                self.info.config(text=new_guess + " is what we were looking for! You lose ;(")
            else:
                self.info.config(text=new_guess + " is what we were looking for! You win!")
            self.guess_button.config(state=DISABLED)
        elif (int(new_guess) > self.randomNumber):
            self.info.config(text=new_guess + " is too much!")
        elif (int(new_guess) < self.randomNumber):
            self.info.config(text=new_guess + " is too less!")
        self.writeWhoMoves()


    def quitGame(self):
        client_socket.send(bytes("{quit}", "utf8"))
        client_socket.close()
        self.window.quit()

    def sendName(self):
        """Handles sending of messages."""
        self.msg = self.my_msg.get()
        self.my_msg.set("")  # Clears input field.
        client_socket.send(bytes(self.msg, "utf8"))
        self.showGames()
        if self.msg == "{quit}":
            client_socket.close()
            self.window.quit()

    def sendMessage(self):
        """Handles sending of messages."""
        self.msg = self.my_msg.get()
        self.my_msg.set("")  # Clears input field.
        client_socket.send(bytes(self.msg, "utf8"))
        if self.msg == "{quit}":
            client_socket.close()
            self.window.quit()

    def sendBoard(self):
        """Handles sending of messages."""
        self.msg = "New move: " + self.move_cell
        client_socket.send(bytes(self.msg, "utf8"))
        if self.msg == "{quit}":
            client_socket.close()
            self.window.quit()

    def sendDecision(self):
        """Handles sending of messages."""
        self.msg = "New decision: " + self.decision
        client_socket.send(bytes(self.msg, "utf8"))
        if self.msg == "{quit}":
            client_socket.close()
            self.window.quit()


    def receive(self):
        """Handles receiving of messages."""
        while True:
            try:
                self.msg = client_socket.recv(BUFSIZ).decode("utf8")
                if ("New move" in self.msg):
                    message = self.msg
                    self.my_move = not self.my_move
                    self.writeWhoMoves()
                    self.updateBoard(message[-1:])
                elif ("New decision" in self.msg):
                    if ("TicTacToe" in self.msg):
                        self.TTT_init()
                        self.writeWhoMoves()
                    elif ("GuessNumber" in self.msg):
                        self.GN_init()
                        self.writeWhoMoves()
                    elif ("Back" in self.msg):
                        self.backToMenu()
                    elif ("Guess" in self.msg):
                        message = self.msg.split()
                        self.checkResultGN(message[len(message)-1])
                    elif ("Number" in self.msg):
                        message = self.msg.split()
                        self.randomNumber = int(message[len(message)-1])

                else:
                    self.result.config(text=self.msg)
                if ("has joined the game" in self.msg):
                    self.my_move = True
            except OSError:  # Possibly client has left the chat.
                break

    def updateBoard(self, new_cells):
        if new_cells == "1":
            self.cells[1] = self.who_move
            self.b1.config(text=self.cells[1], state=DISABLED)

        elif new_cells == "2":
            self.cells[2] = self.who_move
            self.b2.config(text=self.cells[2], state=DISABLED)

        elif new_cells == "3":
            self.cells[3] = self.who_move
            self.b3.config(text=self.cells[3], state=DISABLED)

        elif new_cells == "4":
            self.cells[4] = self.who_move
            self.b4.config(text=self.cells[4], state=DISABLED)

        elif new_cells == "5":
            self.cells[5] = self.who_move
            self.b5.config(text=self.cells[5], state=DISABLED)

        elif new_cells == "6":
            self.cells[6] = self.who_move
            self.b6.config(text=self.cells[6], state=DISABLED)

        elif new_cells == "7":
            self.cells[7] = self.who_move
            self.b7.config(text=self.cells[7], state=DISABLED)

        elif new_cells == "8":
            self.cells[8] = self.who_move
            self.b8.config(text=self.cells[8], state=DISABLED)

        elif new_cells == "9":
            self.cells[9] = self.who_move
            self.b9.config(text=self.cells[9], state=DISABLED)

        elif new_cells == "0":
            self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            self.b1.config(text=self.cells[1], state=NORMAL, bg="white")
            self.b2.config(text=self.cells[2], state=NORMAL, bg="white")
            self.b3.config(text=self.cells[3], state=NORMAL, bg="white")
            self.b4.config(text=self.cells[4], state=NORMAL, bg="white")
            self.b5.config(text=self.cells[5], state=NORMAL, bg="white")
            self.b6.config(text=self.cells[6], state=NORMAL, bg="white")
            self.b7.config(text=self.cells[7], state=NORMAL, bg="white")
            self.b8.config(text=self.cells[8], state=NORMAL, bg="white")
            self.b9.config(text=self.cells[9], state=NORMAL, bg="white")

        if self.who_move == "X":
            self.who_move = "O"
        else:
            self.who_move = "X"
        winner_exist = self.isWinner()
        if winner_exist:
            self.finish_game()


    def writeWhoMoves(self):
        if self.my_move:
            self.result.config(text="Your move!")
        else:
            self.result.config(text="Opponent move!")

    def isWinner(self):
        if self.cells[1] == self.cells[2] == self.cells[3] != " ":
            self.b1.config(bg="blue")
            self.b2.config(bg="blue")
            self.b3.config(bg="blue")
            return True
        elif self.cells[4] == self.cells[5] == self.cells[6] != " ":
            self.b4.config(bg="blue")
            self.b5.config(bg="blue")
            self.b6.config(bg="blue")
            return True
        elif self.cells[7] == self.cells[8] == self.cells[9] != " ":
            self.b7.config(bg="blue")
            self.b8.config(bg="blue")
            self.b9.config(bg="blue")
            return True
        elif self.cells[1] == self.cells[4] == self.cells[7] != " ":
            self.b1.config(bg="blue")
            self.b4.config(bg="blue")
            self.b7.config(bg="blue")
            return True
        elif self.cells[2] == self.cells[5] == self.cells[8] != " ":
            self.b2.config(bg="blue")
            self.b5.config(bg="blue")
            self.b8.config(bg="blue")
            return True
        elif self.cells[3] == self.cells[6] == self.cells[9] != " ":
            self.b3.config(bg="blue")
            self.b6.config(bg="blue")
            self.b9.config(bg="blue")
            return True
        elif self.cells[1] == self.cells[5] == self.cells[9] != " ":
            self.b1.config(bg="blue")
            self.b5.config(bg="blue")
            self.b9.config(bg="blue")
            return True
        elif self.cells[3] == self.cells[5] == self.cells[7] != " ":
            self.b3.config(bg="blue")
            self.b5.config(bg="blue")
            self.b7.config(bg="blue")
            return True
        else:
            return False

    def finish_game(self):
        self.b1.config(state=DISABLED)
        self.b2.config(state=DISABLED)
        self.b3.config(state=DISABLED)
        self.b4.config(state=DISABLED)
        self.b5.config(state=DISABLED)
        self.b6.config(state=DISABLED)
        self.b7.config(state=DISABLED)
        self.b8.config(state=DISABLED)
        self.b9.config(state=DISABLED)
        if self.who_move == "X":
            self.who_move = "O"
        else:
            self.who_move = "X"
        if self.my_move:
            self.result.config(text="You lose ;(")
        else:
            self.result.config(text="You win!")

    def b1_pressed(self):
        if self.my_move:
            self.move_cell = "1"
            self.sendBoard()


    def b2_pressed(self):
        if self.my_move:
            self.move_cell = "2"
            self.sendBoard()

    def b3_pressed(self):
        if self.my_move:
            self.move_cell = "3"
            self.sendBoard()

    def b4_pressed(self):
        if self.my_move:
            self.move_cell = "4"
            self.sendBoard()

    def b5_pressed(self):
        if self.my_move:
            self.move_cell = "5"
            self.sendBoard()

    def b6_pressed(self):
        if self.my_move:
            self.move_cell = "6"
            self.sendBoard()

    def b7_pressed(self):
        if self.my_move:
            self.move_cell = "7"
            self.sendBoard()

    def b8_pressed(self):
        if self.my_move:
            self.move_cell = "8"
            self.sendBoard()

    def b9_pressed(self):
        if self.my_move:
            self.move_cell = "9"
            self.sendBoard()

    def restartButton_pressed(self):
        self.move_cell = "0"
        self.sendBoard()


    def getBoard(self):
        return self.cells

board=Board()

HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=board.receive)
receive_thread.start()

mainloop()
