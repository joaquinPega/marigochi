import tensorflow as tf
from tensorflow import keras
import numpy as np

model = keras.Sequential([
    keras.layers.Dense(units=1, input_shape=(2,1))
    ])

model.compile(optimizer='sgd', loss='mean_squared_error')

xs=np.array([[1,1], [2,2], [3, 3]], dtype=float)
ys=np.array([[1,1], [2,2], [3, 3]], dtype=float)

print(xs)
model.fit(xs, ys, epochs=500)

test=np.array([[4,4]])

print(model.predict(test))