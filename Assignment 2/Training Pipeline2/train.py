import boto3
import pandas as pd
import os
import tensorflow as tf
import tensorflow_hub as hub
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from datetime import datetime
from tabulate import tabulate


def training_model(file):
    print("----------------------------------------")
    print("Executing Training Pipeline")
    print("----------------------------------------")

    print("Reading the labeled data")

    # Reading the the label data and refining the structure
    raw_data = pd.read_csv(file, header='infer')
    data = raw_data[['sentiment.targets.text', 'sentiment.targets.label']]
    data = data.rename(columns={'sentiment.targets.text': 'texts', 'sentiment.targets.label': 'label'})
    data = data[data.label != 'neutral']
    data = data.reset_index(drop=True)
    print("Labeled Data Refined!")

    # Encode the Label to convert it into numerical values [Negative = 0; Positive = 1]
    lab_enc = LabelEncoder()

    # Applying to the dataset
    data['label'] = lab_enc.fit_transform(data['label'])

    # Splitting
    x_train, x_test, y_train, y_test = train_test_split(data['texts'], data.label, test_size=0.1, random_state=42)

    Embed = 'https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1'
    Trainable_Module = True
    hub_layer = hub.KerasLayer(Embed, input_shape=[], dtype=tf.string, trainable=Trainable_Module)

    # Defining the model
    model = tf.keras.Sequential()
    model.add(hub_layer)  # pre-trained text embedding layer
    model.add(tf.keras.layers.Dense(16, activation='relu'))
    model.add(tf.keras.layers.Dense(32, activation='relu'))
    model.add(tf.keras.layers.Dense(1))

    print(model.summary())

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                  metrics=['accuracy']
                  )

    EPOCHS = 50  # can be changed
    BATCH_SIZE = 128  # can be changed

    history = model.fit(x_train, y_train, batch_size=BATCH_SIZE,
                        epochs=EPOCHS, validation_split=0.1,
                        verbose=1)

    accr = model.evaluate(x_test, y_test, verbose=0)
    tab_data = [["Model Trained on Original Title Text", '{:.2%}'.format(accr[0]), '{:.2%}'.format(accr[1])]]
    print(tabulate(tab_data, headers=['', 'LOSS', 'ACCURACY'], tablefmt='pretty'))

    # Saving the model
    model_name = 'sentiment_tf'
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'models'))
    save_path = os.path.join(path, f"{model_name}.keras")
    model.save(save_path)
    print(f"Saved keras pipeline model at {save_path}")


def upload_to_s3():
    # Connect to Boto3
    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-1')

    # Replace this with your S3 Bucket
    bucket_name = 'edgar-pipeline'

    model_files = [os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'models', 'sentiment_tf.keras')),
                   os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'processed_data', 'labeled_data.csv'))]

    for file in model_files:
        print(file)
        s3.Bucket(bucket_name).upload_file(Filename=file,
                                           Key='model/' + datetime.today().strftime(
                                               '%Y-%m-%d-%H:%M:%S') + '_' + os.path.basename(file))
        print('Upload Complete')

