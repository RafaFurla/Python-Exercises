#Reproduzindo um .mp3
from pygame import mixer
mixer.init()
mixer.music.load('topgun.mp3')
mixer.music.play()
input('Agora você escuta? ')
import winsound
