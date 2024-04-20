import os
import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

import matplotlib.pyplot as plt
import seaborn as sns

# Clases y tamaño
classes = ['usb hembra', 'usb macho', 'hdmi hembra', 'hdmi macho', 'enchufe tipo a hembra', 'enchufe tipo a macho', 'enchufe tipo c macho', 'enchufe tipo c hembra', 'vga macho', 'vga hembra', 'ethernet hembra', 'ethernet macho']
num_classes = len(classes)
img_rows, img_cols = 64, 64


def load_data():
    data = []
    target = []

    for index, x in enumerate(classes):
        folder_path = os.path.join('training', x)
        for img in os.listdir(folder_path):
            img_path = os.path.join(folder_path, img)
            image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image, (img_rows, img_cols))
            data.append(np.array(image))
            target.append(index)

    data = np.array(data)
    data = data.reshape(data.shape[0], img_rows, img_cols, 1)
    target = np.array(target)
    #NUMERO DE CLASES A DECLARAR
    new_target = to_categorical(target, num_classes)
    return data, new_target

data, target = load_data()

x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2)

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(img_rows, img_cols, 1)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
# model.add(Conv2D(128, (3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0, 25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(x_train, y_train, batch_size=80, epochs=100, verbose=1, validation_data=(x_test, y_test))

model.save('modelo.h5')

if not os.path.exists('graficas'):
    os.makedirs('graficas')

y_pred = model.predict(x_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true = np.argmax(y_test, axis=1)
confusion_mtx = confusion_matrix(y_true, y_pred_classes)

plt.figure(figsize=(8, 6))
sns.heatmap(confusion_mtx, annot=True, fmt='g', cmap='Blues', xticklabels=classes, yticklabels=classes)
plt.xlabel('Prediccion')
plt.ylabel('Real')
plt.savefig('graficas/matriz_confusion.png')
plt.show()

plt.figure()
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Historial de error')
plt.ylabel('Error')
plt.xlabel('Epoca')
plt.legend(['Entrenamiento', 'Validacion'], loc='upper right')
plt.savefig('graficas/historial_error.png')
plt.show()
