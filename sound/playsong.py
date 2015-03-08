#import pygame
#
#pygame.init()
#pygame.mixer.init()
##pygame.mixer.music.load('song.mp3')
##pygame.mixer.music.play(1)
#
#input = 'p'
#
#events = pygame.event.get()
#while True:
#    for events in events:
#        if event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_LEFT:
#                pygame.mixer.music.load('song.mp3')
#                pygame.mixer.music.play(1)
#                continue
#            if event.key == pygame.K_RIGHT:
#                pygame.mixer.music.load('song.mp3')

        

# import pygame, sys, pycurl, os
 
# white = (255, 255, 255)
 
# pygame.init()
# pygame.display.set_caption('Basic Sound Example')
# size = [640, 480]
# screen = pygame.display.set_mode(size)
# clock = pygame.time.Clock()
 
# # load sound file
# #sound = pygame.mixer.music.load('song.mp3')
# #print 'the sound file is',sound.get_length(),'seconds long.'
 
# print 'press 1 - play sound'
# print 'press 2 - play sound continuously in a loop'
# print 'press 3 - play sound but start with 3 seconds fade-in effect'
# print 'press 4 - play sound for 5 seconds'
# print 'press 5 - play sound 3 more times'
# print 'press 9 - stop playing with 3 seconds fadeout effect'
# print 'press 0 - stop playing instantly'

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_1:
#                 os.system("curl 192.168.1.127/play")
#                 pygame.mixer.music.load('song.mp3')
#                 pygame.mixer.music.play()
#             if event.key == pygame.K_2:
#                 os.system("curl 192.168.1.127/pause")
#                 pygame.mixer.music.pause()
#             if event.key == pygame.K_3:
#                 #os.system("curl 192.168.1.127/switch")
#                 pygame.mixer.music.load('song2.mp3');
#                 pygame.mixer.music.play()
#             if event.key == pygame.K_4:
#                 pygame.mixer.music.load('song3.mp3');
#                 pygame.mixer.music.play()
#             if event.key == pygame.K_5:
#                 pygame.mixer.music.rewind()
#             if event.key == pygame.K_9:
#                 pygame.mixer.music.set_volume(0.3)
#             if event.key == pygame.K_0:
#                 pygame.mixer.music.stop()
#     screen.fill(white)
#     pygame.display.update()
#     clock.tick(20)

import os

def removeSpecialCharacters(s):
    return re.sub('[^A-Za-z0-9-`~!&/#%+=/\<>(){}]+', '', s).strip()

class ExecuteCommand:
    def __init__(self, ip):
        self.ip = ip

    def play(self):
        os.system("curl " + self.ip +"/play")

    def pause(self):
        os.system("curl " + self.ip +"/pause")

    def rewind(self):
        os.system("curl " + self.ip +"/rewind")

    def forward(self):
        os.system("curl " + self.ip +"/forward")

    def louder(self):
        os.system("curl " + self.ip +"/louder")

    def quiet(self):
        os.system("curl " + self.ip +"/quiet")

    def execute(self, text):
        text = removeSpecialCharacters(text)
        print text

