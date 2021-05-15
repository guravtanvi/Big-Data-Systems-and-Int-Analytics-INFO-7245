import boto3

# Downloading the pre trained model from s3 bucket
s3 = boto3.resource('s3')

# Replace the below with your s3 bucket where the model is stored
bucket = 'assignment4-model-store'

print("Downloading model from {} bucket...\n".format(bucket))
s3.Bucket(bucket).download_file('model_state_dict.bin', './model/model_state_dict.bin')

print("Model successfully downloaded!")
