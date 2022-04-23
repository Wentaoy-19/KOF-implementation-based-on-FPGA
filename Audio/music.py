import numpy as np
import wave

#music = wave.open("C:/Users/Lenovo/Desktop/2_1.wav", 'r')
music = wave.open("final_bgm2.wav", 'r')
signal = music.readframes(-1)

soundwave = np.frombuffer(signal, dtype="uint16")

with open("final_bgm2.txt","w") as f:
    for i in soundwave:
        f.write('{:04X}'.format(i))
        f.write("\n")