import numpy as np
import scipy.io.wavfile
import simpleaudio as sa

fs = 44100  # 44100 samples per second


data=np.load('outputx')

print(data[10000:11000])
play_obj = sa.play_buffer(data, 1, 2, fs)

# Wait for playback to finish before exiting
play_obj.wait_done()

scipy.io.wavfile.write('output.wav',44100, data)
