# HealthVision

This project uses deep learning algorithms and the Keras library to determine if a person has certain diseases or not from their chest x-rays and other scans. The trained model is displayed using Streamlit, which enables the user to upload an image and receive instant feedback.

Essentially it uses 4 different CNN models to diagnose 4 different diseases :- Covid, Glaucoma, Skin Cancer and Pneumonia
Covid and Pnemonia are detected using chest X-ray scans of the patient while Gluacoma uses an internal scan of the eye and Skin Cancer is detected
using external pictures




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


## Examples

### Covid-19
#### Positive
- ![COVID19(569)](https://user-images.githubusercontent.com/77538244/234957420-ad389276-cac4-4952-bd38-9a4d6b655e32.jpg)
#### Negative 
- ![NORMAL(1532)](https://user-images.githubusercontent.com/77538244/234957476-0d0e4e01-9244-443d-aab8-768a5190b4ea.jpg)

### Glaucoma
#### Positive
- ![sjchoi86-HRF-5](https://user-images.githubusercontent.com/77538244/234957597-bffec98d-71c5-40b3-aaca-e2a895e92e94.png)
itive 
#### Negative
- ![625](https://user-images.githubusercontent.com/77538244/234957672-62af00ee-7a98-425b-9620-1fb5c52121d7.jpg)

### Pneumonia
#### Positive
- ![PNEUMONIA(4268)](https://user-images.githubusercontent.com/77538244/234957766-d2c1d207-6719-43bb-9865-9202b9d3f136.jpg)

#### Negative
- ![NORMAL(1559)](https://user-images.githubusercontent.com/77538244/234957860-709f2738-7acf-4dfb-b9f6-3d3bb3688986.jpg)

### Skin Cancer
#### Positive (Malignant)
- ![90](https://user-images.githubusercontent.com/77538244/234957957-e0c19cbe-9988-45c8-9d4f-84382ea40014.jpg)

#### Negative (Benign)
-  ![69](https://user-images.githubusercontent.com/77538244/234958000-bae1b9bf-c3bb-4af2-b55b-2f8bed152daf.jpg)
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
- Also here are some "Executors" for you to use while testing our software.. these are just references and you can use any image you have :- [https://github.com/SiddharthRajpal/HealthVision/tree/main/Executors]
