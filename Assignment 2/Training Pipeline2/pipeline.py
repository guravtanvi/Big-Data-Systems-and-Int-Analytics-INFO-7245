import os
import train
from sklearn.pipeline import Pipeline
import warnings
warnings.filterwarnings("ignore")

# Path of the labeled data file
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'processed_data', 'labeled_data.csv'))

# Defining the steps for pipeline
pipe = Pipeline(steps=[
        ('ReadData-TrainingModel', train.training_model(file_path)),
        ('SavingModelToS3', train.upload_to_s3())
        ])

# Triggering the sklearn pipeline
pipe
