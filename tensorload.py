import tensorflow as tf
from tensorflow import keras
import numpy as np
import scipy.io.wavfile
import random
from random import randrange

tf.get_logger().setLevel('ERROR')
new_model = tf.keras.models.load_model('saved_model/my_model2')

# Check its architecture
new_model.summary()


test=np.array([[296, 60]])
prediction = new_model.predict(test)
running =True
tick =0
data = np.empty(shape=[0, 2])
while running:
	prev_prediction= prediction
	pred = prediction[0].astype(int)


	data = np.append(data, [[pred[0][0],pred[1][0]]], axis=0)
	
	prediction = new_model.predict(prediction)
	print(prediction)
	print(prev_prediction)
	if np.array_equal(prediction, prev_prediction):
		test=np.array([[random.randint(-100000, 100000),random.randint(-100000, 100000) ]])
		prediction = new_model.predict(test)
		print('True')
	tf.keras.backend.clear_session()
	
	if tick >= 4410000:
		running=False
	tick +=1
	print(tick)

y_output = open('outputy', 'wb')
np.save(y_output, data)
y_output.close()
scipy.io.wavfile.write('output.wav',44100, data)