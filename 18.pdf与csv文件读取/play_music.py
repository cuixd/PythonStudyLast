import time
import pygame

# 有些音乐播放不了，没声音，甚至有些会报错
music = "/Users/cuixiaodong/Music/QQ音乐/中国娃娃-发财发福中国年.mp3"


#pygame.init()
pygame.mixer.init()

# screen = pygame.display.set_mode([640,480])
pygame.mixer.music.load(music)

pygame.mixer.music.play()

time.sleep(60)

pygame.mixer.music.stop()