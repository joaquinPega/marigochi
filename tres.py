import wave
import numpy
import simpleaudio as sa

frequency = 440  # Our played note will be 440 Hz
fs = 44100  # 44100 samples per second
seconds = 3  # Note duration of 3 seconds

# Read file to get buffer                                                                                               
ifile = wave.open("sound.wav")
samples = ifile.getnframes()
audio = ifile.readframes(samples)

# Convert buffer to float32 using NumPy                                                                                 
audio_as_np_int16 = numpy.frombuffer(audio, dtype=numpy.int16)

print(audio_as_np_int16.size)

audio_as_np_int16= audio_as_np_int16[532300:1032300]

play_obj = sa.play_buffer(audio_as_np_int16, 1, 2, fs)

# Wait for playback to finish before exiting
play_obj.wait_done()