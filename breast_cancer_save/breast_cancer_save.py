import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout

forecasters = pd.read_csv('entry_breast.csv')
division = pd.read_csv('out_breast.csv')

classifier = Sequential()
classifier.add(Dense(units = 8, activation = 'relu', 
                        kernel_initializer = 'normal', input_dim = 30))
classifier.add(Dropout(0.2))
classifier.add(Dense(units = 8, activation = 'relu', 
                        kernel_initializer = 'normal'))
classifier.add(Dropout(0.2))
classifier.add(Dense(units = 1, activation = 'sigmoid'))
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy',
                      metrics = ['binary_accuracy'])
classifier.fit(forecasters, division, batch_size = 10, epochs = 100)

classifier_json = classifier.to_json()
with open('classifier_breast.json', 'w') as json_file:
    json_file.write(classifier_json)
classifier.save_weights('classifier_breast.h5')