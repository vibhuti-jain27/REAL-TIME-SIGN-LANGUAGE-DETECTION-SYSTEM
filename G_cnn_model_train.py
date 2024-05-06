import numpy as np
import pickle
import cv2, os
from glob import glob
from keras import optimizers
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Conv2D, MaxPooling2D 
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint
from keras import backend as K
from keras.models import load_model
K.set_image_data_format('channels_last')
# import pydotplus
# import tensorflowjs as tfjs

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def get_image_size():
	img = cv2.imread('gestures/0/100.jpg', 0)
	return img.shape

def get_num_of_classes():
	return len(glob('gestures/*'))

image_x, image_y = get_image_size()

def cnn_model():
	num_of_classes = get_num_of_classes()
	model = Sequential()
	model.add(Conv2D(16, (2,2), input_shape=(image_x, image_y, 1), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='same'))
	model.add(Conv2D(32, (3,3), activation='relu'))
	model.add(MaxPooling2D(pool_size=(3, 3), strides=(3, 3), padding='same'))
	model.add(Conv2D(64, (5,5), activation='relu'))
	model.add(MaxPooling2D(pool_size=(5, 5), strides=(5, 5), padding='same'))
	model.add(Flatten())
	model.add(Dense(128, activation='relu'))
	model.add(Dropout(0.2))
	model.add(Dense(num_of_classes, activation='softmax'))
	sgd = optimizers.SGD(learning_rate=1e-2)
	model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
	filepath="cnn_model_keras2.keras"
	checkpoint1 = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
	callbacks_list = [checkpoint1]
	#from keras.utils import plot_model
	#plot_model(model, to_file='model.png', show_shapes=True)
	return model, callbacks_list

def train(epochs = 20):
	with open("train_images", "rb") as f:
		train_images = np.array(pickle.load(f))
	with open("train_labels", "rb") as f:
		train_labels = np.array(pickle.load(f), dtype=np.int32)

	with open("val_images", "rb") as f:
		val_images = np.array(pickle.load(f))
	with open("val_labels", "rb") as f:
		val_labels = np.array(pickle.load(f), dtype=np.int32)

	train_images = np.reshape(train_images, (train_images.shape[0], image_x, image_y, 1))
	val_images = np.reshape(val_images, (val_images.shape[0], image_x, image_y, 1))
	train_labels = to_categorical(train_labels)
	val_labels = to_categorical(val_labels)

	print(val_labels.shape)

	model, callbacks_list = cnn_model()
	model.summary()
	model.fit(train_images, train_labels, validation_data=(val_images, val_labels), epochs = epochs, batch_size=500, callbacks=callbacks_list)
	scores = model.evaluate(val_images, val_labels, verbose=0)
	print("CNN Error: %.2f%%" % (100-scores[1]*100))
	model.save('cnn_model_keras2.keras')
 
'''def validate():
	model, _ = cnn_model()
	if not os.path.exists("cnn_model_keras2.h"):
		print("No saved model found! Please train the model first.")
	else:
		model = load_model('cnn_model_keras2.keras')
		with open("val_images", "rb") as f:
			val_images = np.array(pickle.load(f))
		with open("val_labels", "rb") as f:
		    val_labels = np.array(pickle.load(f), dtype=np.int32)
		val_images = np.reshape(val_images, (val_images.shape[0], image_x, image_y, 1))
		val_labels = to_categorical(val_labels)
		score = model.evaluate(val_images,val_labels,verbose = 0)
		print("Loss = ", score[0])
		print("Accuracy = ", score[1])'''


train(epochs = 50)
#recurive feature extraction
#validate()
K.clear_session()






































'''import numpy as np
import pickle
import cv2, os
from glob import glob
from keras import optimizers
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Conv2D, MaxPooling2D 
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint
from keras import backend as K
K.set_image_data_format('channels_last')

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def get_image_size():
	img = cv2.imread('gestures/1/100.jpg', 0)
	return img.shape

def get_num_of_classes():
	return len(glob('gestures/*'))

image_x, image_y = get_image_size()

def cnn_model():
	num_of_classes = get_num_of_classes()
	model = Sequential()
	#model = UnpickleModelAndCallbacks('cnn_model_keras2.keras')
	#model = UnpickleModelOnly('cnn_model_keras2.keras')
	model.add(Conv2D(16, (2,2), input_shape=(image_x, image_y, 1), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='same'))
	model.add(Conv2D(32, (3,3), activation='relu'))
	model.add(MaxPooling2D(pool_size=(3, 3), strides=(3, 3), padding='same'))
	model.add(Conv2D(64, (5,5), activation='relu'))
	model.add(MaxPooling2D(pool_size=(5, 5), strides=(5, 5), padding='same'))
	model.add(Flatten())
	model.add(Dense(128, activation='relu'))
	model.add(Dropout(0.2))
	model.add(Dense(num_of_classes, activation='softmax'))
	sgd = optimizers.SGD(learning_rate=1e-2)
	model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
	#filepath="cnn_model_keras2.h5"
	filepath = "cnn_model_keras2.keras"
	checkpoint1 = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
	#checkpoint1 = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max', save_format='h5', save_weights_only=False)
	callbacks_list = [checkpoint1]
	#model.summary()
	#from keras.utils import plot_model
	#plot_model(model, to_file='model.png', show_shapes=True)
	return model, callbacks_list

def train():
	with open("train_images", "rb") as f:
		train_images = np.array(pickle.load(f))
	with open("train_labels", "rb") as f:
		train_labels = np.array(pickle.load(f), dtype=np.int32)

	with open("val_images", "rb") as f:
		val_images = np.array(pickle.load(f))
	with open("val_labels", "rb") as f:
		val_labels = np.array(pickle.load(f), dtype=np.int32)

	train_images = np.reshape(train_images, (train_images.shape[0], image_x, image_y, 1))
	val_images = np.reshape(val_images, (val_images.shape[0], image_x, image_y, 1))
	#train_labels = to_categorical(train_labels, num_classes=17)
	#val_labels = to_categorical(val_labels, num_classes=17)
	train_labels = to_categorical(train_labels)
	val_labels = to_categorical(val_labels)
     
	print(val_labels.shape)
	
	model, callbacks_list = cnn_model()
	#callbacks_list = []
	model.summary()
	model.fit(train_images, train_labels, validation_data=(val_images, val_labels), epochs=15, batch_size=500, callbacks=callbacks_list)
	scores = model.evaluate(val_images, val_labels, verbose=0)
	print("CNN Error: %.2f%%" % (100-scores[1]*100))
	model.save('cnn_model_keras2.keras')
	#checkpoint1 = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
	#callbacks_list.append(checkpoint1)
	
	#model.fit(train_images, train_labels, validation_data=(val_images, val_labels), epochs=15)
	#model.save('cnn_model_keras2.keras', save_format='keras')

train()
K.clear_session()'''