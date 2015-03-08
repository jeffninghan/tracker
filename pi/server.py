from flask import Flask
import pygame

app = Flask(__name__)

song_filename = 'song.mp3'
playing = False
song_list = ['song.mp3', 'song2.mp3', 'song3.mp3']


@app.route('/play')
def play():
    global playing
    if not playing:
        pygame.mixer.music.play()
        playing = True
    else:
        pygame.mixer.music.unpause()
    return 'playing'

@app.route('/pause')
def pause():
    pygame.mixer.music.pause()
    return 'pause'

@app.route('/rewind')
def rewind():
    global current
    if current > 0:
        current -= 1
        pygame.mixer.music.load(song_list[current])
        pygame.mixer.music.play()
    else:
        print "cannot rewind"
    return 'rewind'

@app.route('/forward')
def forward():
    global current
    if current < len(song_list)-1:
        current += 1
        pygame.mixer.music.load(song_list[current])
        pygame.mixer.music.play()
    else:
        print "cannot forward"
    return 'forward'

@app.route('/louder')
def louder():
    global sound_level
    sound_level += 0.1
    pygame.mixer.music.set_volume(sound_level)
    return 'louder'


@app.route('/quiet')
def quiet():
    global sound_level
    sound_level -= 0.1
    pygame.mixer.music.set_volume(sound_level)
    return 'quiet'

           
if __name__ == '__main__':
    app.debug = True
    playing = False
    current = 0
    sound_level = 0.5
    pygame.mixer.init()
    pygame.mixer.music.load(song_list[current])
    app.run(host='192.168.1.127', port=80)

