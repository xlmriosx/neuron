# Neuron

## Definition

A neuron is a fundamental part of a neural network.

These need to receive stimuli just as it happens with biological neurons. These "stimuli" are used to make a weighted sum within the function

Components of a Neuron:

![image](https://user-images.githubusercontent.com/78567418/148115904-510fbe1b-71b9-4ea5-a761-46b9006da540.png)

![image](https://user-images.githubusercontent.com/78567418/148115962-c8593848-424f-493b-9dfe-e262442c706e.png)

## Neuronal network

Neural networks are a class of models that are built with layers. Commonly used types of neural networks include convolutional and recurrent neural networks.

![image](https://user-images.githubusercontent.com/78567418/148116173-c722e3e7-03f4-4ae7-af73-c94bc75bdd39.png)
![image](https://user-images.githubusercontent.com/78567418/148116186-1aed8dfe-950d-4bcc-b08b-618399081977.png)

## Architecture

The vocabulary around neural networks architectures is described in the figure below:

![image](https://user-images.githubusercontent.com/78567418/148117765-0f50484a-78eb-401b-aafc-ffcd7a11bf2f.png)

By noting i the i^th layer of the network and j the j^th hidden unit of the layer, we have:

![image](https://user-images.githubusercontent.com/78567418/148117895-1c03596a-1b96-46a3-ac87-e83f0e338b7f.png)

where we note ww, bb, zz the weight, bias and output respectively.


## Activate neuron

We can activate a neuron with a function activation.

### Activation function

The activation functions are in charge of activating or deactivating neurons depending on the input value, for example if the value is very high or very low. These functions are represented by the letter φ(fi).

![image](https://user-images.githubusercontent.com/78567418/148116989-ad05c4e2-f349-4c5b-8420-2bb4a33130f6.png)

The input values are passed to the neuron and then the result of this is passed to the activation function. This returns a more normalized result (0 - 1, -1 - 1, etc) depending on the trigger function used.

If you look at it from the point of view of the graphs of the functions, the neuron returns a line graph which is then converted by the activation function into a non-linear graph. This is useful because in the real world the data is very unlikely to be linear, since it is common for it to be scattered.

Activation functions are used at the end of a hidden unit to introduce non-linear complexities to the model. Here are the most common ones:

####

![image](https://user-images.githubusercontent.com/78567418/148118158-59311123-7033-42e5-8244-4c2148a3d5ce.png)

#### Heaviside 

![image](https://user-images.githubusercontent.com/78567418/148117527-451930bf-de86-4863-8e2a-25311129cb5e.png)

### Mean square error

This show us how long we have for the function assigned.

![image](https://user-images.githubusercontent.com/78567418/148119993-ca435983-0577-4e99-a99b-50df2e02cfe5.png)

![image](https://user-images.githubusercontent.com/78567418/148120190-238c47e8-ecd3-4665-a2b6-56f700ca4b3e.png)








