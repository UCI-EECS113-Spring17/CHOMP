import pygame
import random
import math
import socket
import time

class Timer():
    def __init__(self, num, compscreen):
        # time measured in 1/60 of a second
        self.time = num * 60
        self.screen = compscreen
        self.font = pygame.font.Font(None, 32)
        self.text = self.font.render(str(int(self.time/60 + 1)), 1, (0,0,0))
    def step(self):
        self.time -= 1
        self.text = self.font.render(str(int(self.time/60 + 1)), 1, (0,0,0))
        self.screen.blit(self.text, (50, 50))
        if self.time == 0:
            return True
        else:
            return False
    def done(self):
        if self.time <= 0:
            return False
        else:
            return True

class Score():
    def __init__(self, compscreen, num):
        self.limit = num
        self.score = 0
        self.screen = compscreen
        self.font = pygame.font.Font(None, 32)
        self.text = self.font.render("Score: " + str(self.score), 1, (0,0,0))
        self.w, self.h = compscreen.get_size()
    def step(self):
        self.score+=1
        self.text = self.font.render("Score: " + str(self.score), 1, (0,0,0))
        self.screen.blit(self.text, (int(self.w-self.w/6), int(self.h - self.h/6)))
        if self.score >= self.limit:
            return True
        else:
            return False
    def display(self):
        self.screen.blit(self.text, (int(self.w-self.w/6), int(self.h - self.h/6)))

class client():
    def __init__(self):
        self.s = socket.socket()
        self.host = 'chomp_board'
        self.port = 8081
        self.s.connect((self.host, self.port))
        self.smessage = "get".encode()
        self.a = 0.0
        self.b = 0.0
        self.warmup()
    def updateCoords(self):
        self.s.send(self.smessage)
        message = self.s.recv(1024)
        message = message.decode()
        if message == "":
            print("Found nothing!")
            return(self.a, self.b)
        print(message + "#3")    
        x = message.split(" ")
        self.a = float(x[0])
        self.b = float(x[1])
        return (self.a, self.b)
    def close_client(self):
        self.s.send("Close".encode())
        message = self.s.recv(1024)
        self.s.close()
    def getCoords(self):
        return (self.a, self.b)
    def warmup(self):
        mess= "get"
        self.s.send(mess.encode())
        self.s.send(mess.encode())
        self.s.recv(1024)
        c = 0
        while True:
            self.s.send(mess.encode())
            message = self.s.recv(1024)        
            message = message.decode()            
            c += 1
            if(c == 50):
                break
            time.sleep(0.01667)
