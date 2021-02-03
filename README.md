# Jetson Nano - Tensorflow Test

L4T (Linux 4 Tegra) OS is not prebuild with Tensorflow. Luckily NVIDIA provides us with a Tensorflow binary which can be installed via pip (python package manager). 

## Official TensorFlow for Jetson Nano!
- Official TensorFlow release for Jetson Nano for JetPact 4.5/4.4/4.3 in Python 3.6 :
https://forums.developer.nvidia.com/t/official-tensorflow-for-jetson-nano/71770

## Test Tensorflow 2.x
- Run `tf-check-gpu.py` to check GPU is availabe to use,
```
python3 tf-check-gpu.py
```
- Run `keras-cnn-mnist.py` to train CNN model using MNIST dataset,
```
python3 keras-cnn-mnist.py
```
- Run `keras-lstm-bidirectional-imdb.py` to train LSTM Bidirectional model using IMDB dataset,
```
python3 keras-lstm-bidirectional-imdb.py
```

## Tutorial
- full tutorial is accessible in my medium,
