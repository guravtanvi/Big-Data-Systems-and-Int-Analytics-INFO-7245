# Pytorch official image with Python 3.7 as base
FROM pytorch/pytorch:1.7.0-cuda11.0-cudnn8-runtime

# Maintainer info
LABEL maintainer="guravtan@gmail.com"

# Upgrade pip with no cache and install base components for FastAPI App.
RUN pip install --no-cache-dir -U pip

#RUN pip install FastAPI
RUN pip install fastapi[all]

#Expose port 8000
EXPOSE 80

# Copy all the contents of the projects into the working directory
COPY  . .

# Install application dependencies from the requirements file
RUN pip install -r requirements.txt

# Run the FastAPI app on port 8000
CMD ["uvicorn", "fast_api:app", "--reload", "--host", "0.0.0.0", "--port", "80"]