import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam

# Configurações do gerador de dados
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
train_generator = train_datagen.flow_from_directory(
    '.\img_trainning',
    target_size=(150, 150),
    batch_size=2,
    class_mode='binary',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    '.\img_trainning',
    target_size=(150, 150),
    batch_size=2,
    class_mode='binary',
    subset='validation'
)

print(f'Training samples: {train_generator.samples}')
print(f'Validation samples: {validation_generator.samples}')


batch = next(train_generator)
print(f'Batch shape: {batch[0].shape}')
print(f'Labels: {batch[1]}')

# Construindo o modelo
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'], run_eagerly=True)

# Treinando o modelo
model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // validation_generator.batch_size,
    epochs=10
)

# Salvando o modelo
model.save('cinto_seguranca_model.h5')
