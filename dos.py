import numpy as np
import simpleaudio as sa
import wave, struct, math, random

fs = 44100  # 44100 samples per second

wave_read = wave.open('sound.wav', 'rb')
wave_obj = sa.WaveObject.from_wave_read(wave_read)
print(wave_obj)
# Start playback
play_obj = wave_obj.play()
# Wait for playback to finish before exiting
play_obj.wait_done()
