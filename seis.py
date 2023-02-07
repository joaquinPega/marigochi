import scipy.io.wavfile 
import numpy as np
import wave
import simpleaudio as sa

fs = 44100  # 44100 samples per second


# Start opening the file with wave
with wave.open('sound.wav') as f:
    # Read the whole file into a buffer. If you are dealing with a large file
    # then you should read it in blocks and process them separately.
	buffer = f.readframes(f.getnframes())
	# Convert the buffer to a numpy array by checking the size of the sample
	# with in bytes. The output will be a 1D array with interleaved channels.
	interleaved = np.frombuffer(buffer, dtype=f'int{f.getsampwidth()*8}')
	# Reshape it into a 2D array separating the channels in columns.
	data = np.reshape(interleaved, (-1, f.getnchannels()))

	print(data.size)
	x_output = open('outputx', 'wb')
	np.save(x_output, data)
	#for i in data:
	#	print(i)

	data2=np.load('outputx')

			
	play_obj = sa.play_buffer(data2, 1, 2, fs)

	# Wait for playback to finish before exiting
	play_obj.wait_done()


	#Al final vamos a usar esto despues que ande el modelo
	#scipy.io.wavfile.write('output.wav',44100, data)