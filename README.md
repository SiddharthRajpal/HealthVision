![Health (1)](https://user-images.githubusercontent.com/77538244/234961507-c6969ae8-4647-4899-853d-17e6b3c46315.png)

# HealthVision
This project uses deep learning algorithms and the Keras library to determine if a person has certain diseases or not from their chest x-rays and other scans. The trained model is displayed using Streamlit, which enables the user to upload an image and receive instant feedback.

Essentially it uses 6 different CNN models to diagnose 6 different diseases :- Covid, Glaucoma, Skin Cancer, Pneumonia, Tuberculosis and Brain Tumor classification
Covid and Pnemonia are detected using chest X-ray scans of the patient while Gluacoma uses an internal scan of the eye and Skin Cancer is detected
using external pictures

# Trailer
Watch our Trailer here :- [https://drive.google.com/file/d/1rsuZLO70enTyi4aTBziKADpSQ04UE9KP/view?usp=sharing]



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

As you can see this is a simple Neural Network with 8 layers. (this had an accuracy of approx 0.93 on average)
Each Layer has a specific job in order to get the desired output, they are :-

- Convolutional layer (conv2d): This layer takes an input image and applies a set of 32 filters to produce 32 output feature maps. Each filter extracts a particular feature from the image. The output of this layer has a shape of (None, 222, 222, 32).

- Max pooling layer (max_pooling2d): This layer reduces the dimensionality of the output of the previous layer by taking the maximum value in each 2x2 region. The output of this layer has a shape of (None, 111, 111, 32).

- Convolutional layer (conv2d_1): This layer applies a set of 64 filters to the output of the previous layer to produce 64 output feature maps. The output of this layer has a shape of (None, 109, 109, 64).

- Max pooling layer (max_pooling2d_1): This layer reduces the dimensionality of the output of the previous layer by taking the maximum value in each 2x2 region. The output of this layer has a shape of (None, 54, 54, 64).

- Convolutional layer (conv2d_2): This layer applies a set of 128 filters to the output of the previous layer to produce 128 output feature maps. The output of this layer has a shape of (None, 52, 52, 128).

- Max pooling layer (max_pooling2d_2): This layer reduces the dimensionality of the output of the previous layer by taking the maximum value in each 2x2 region. The output of this layer has a shape of (None, 26, 26, 128).

 - Flatten layer (flatten): This layer flattens the output of the previous layer into a 1D vector. The output of this layer has a shape of (None, 86528).

- Fully connected layer (dense): This layer takes the flattened vector from the previous layer and applies 128 neurons to it, producing a 128-dimensional output. The output of this layer has a shape of (None, 128).



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
 ![PNEUMONIA(4268)](https://user-images.githubusercontent.com/77538244/234957766-d2c1d207-6719-43bb-9865-9202b9d3f136.jpg)

#### Negative
![NORMAL(1559)](https://user-images.githubusercontent.com/77538244/234957860-709f2738-7acf-4dfb-b9f6-3d3bb3688986.jpg)

### Skin Cancer
#### Positive (Malignant)
 ![90](https://user-images.githubusercontent.com/77538244/234957957-e0c19cbe-9988-45c8-9d4f-84382ea40014.jpg)

#### Negative (Benign)
  ![69](https://user-images.githubusercontent.com/77538244/234958000-bae1b9bf-c3bb-4af2-b55b-2f8bed152daf.jpg)


## Usage
Our Site is hosted at this link :- [https://healthvisionai.streamlit.app/]
- Also here are some "Executors" for you to use while testing our software.. these are just references and you can use any image you have :- [https://github.com/SiddharthRajpal/HealthVision/tree/main/Executors]
