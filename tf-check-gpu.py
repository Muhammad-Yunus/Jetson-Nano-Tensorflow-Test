import tensorflow as tf

# tensorflow  2.x 
print("Check Available GPU device :")
print(tf.config.list_physical_devices('GPU'))