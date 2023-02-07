import tensorflow as tf
from tensorflow import keras
import numpy as np
import os



model = keras.Sequential([
    keras.layers.Dense(units=1, input_shape=(2,1))
   ])

model.compile(optimizer='Adadelta', loss='mse',
              metrics=['Accuracy'])

xoutput=np.load('outputx').astype(float)
print(xoutput)
xoutput=  np.delete(xoutput, np.where(xoutput == [0,0]),axis=0)
print(xoutput)

xs = np.delete(xoutput, 0, axis=0)
print(xs.size)
print(xs[0])
print(xoutput.size)
ys = np.delete(xoutput, -1, axis=0)
print(ys.size)
print(ys[0])

print(xs)

model.fit(xs, ys, epochs=3)

# Save the entire model as a SavedModel.

model.save('saved_model/my_model2')


test=np.array([[-262,482]])

print(model.predict(test))

