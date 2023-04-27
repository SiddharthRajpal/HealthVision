# HealthVision

This project uses deep learning algorithms and the Keras library to determine if a person has certain diseases or not from their chest x-rays and other scans. The trained model is displayed using Streamlit, which enables the user to upload an image and receive instant feedback.



## Requirements

The following libraries are required for running this project:

- TensorFlow
- Keras
- Pillow
- Streamlit


## Installation

If you have the requirements already installed, you can skip this section. If not, follow the steps below to install them:

1. Install TensorFlow:

    ```
    pip install tensorflow
    ```

2. Install Keras:

    ```
    pip install keras
    ```

3. Install Pillow:

    ```
    pip install pillow
    ```

4. Install Streamlit:

    ```
    pip install streamlit
    ```


## Usage
Our Site is hosted at this link :- [https://healthvisionai.streamlit.app/]
- Also here are some "Executors" for you to use while testing our software.. these are just references and you can use any image ou have :) :- [https://github.com/SiddharthRajpal/HealthVision/tree/main/Executors]

## Our Model
Below is the summary of our CNN model which we have made using python and keras.

### Model for Covid & Pneumonia Classification

| Layer (type)                  | Output Shape             | Param #     |
|-------------------------------|--------------------------|-------------|
| conv2d (Conv2D)               | (None, 222, 222, 32)     | 896         |
| max_pooling2d (MaxPooling2D)  | (None, 111, 111, 32)     | 0           |
| conv2d_1 (Conv2D)             | (None, 109, 109, 64)     | 18496       |
| max_pooling2d_1 (MaxPooling2D)| (None, 54, 54, 64)       | 0           |
| conv2d_2 (Conv2D)             | (None, 52, 52, 128)      | 73856       |
| max_pooling2d_2 (MaxPooling2D)| (None, 26, 26, 128)      | 0           |
| flatten (Flatten)             | (None, 86528)            | 0           |
| dense (Dense)                 | (None, 128)              | 11075712    |

As you can see this is a simple Neural Network with 8 layers.
This model has been copied and trained on several types of data (skin cancer, glaucoma, etc.)

