import tensorflow as tf
import os
import numpy as np

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"


# Initialization of tensors
x= tf.constant(4, shape =(1,1,), dtype = tf.float32)
x= tf.constant([[1,2,3], [4,5,6]])

y  = tf.eye((4))  # I for identity matrix
y = tf.ones((2,4))

x= tf.random.normal((3,3), mean = 0, stddev= 1)
x= tf.range(start =1, limit = 10, delta = 2)

x= tf.cast(x, dtype = tf.float64)
# tf.float(16, 32, 64), tf.int(8, 16, 32, 64)



#Mathematical Operations
x= tf.constant((1,2,3))
y = tf.constant((3,4,5))
z = y + x  #  or z =tf.constant(y + x)  or z = tf.add(x,y)

z= tf.constant(y-x) 
z = tf.subtract(y,x)
z=y-x
# SAME CAN BE DONE FOR DIVISION AND MULTIPLICATION

z = tf.tensordot(x,y, axes =1)
z = tf.reduce_sum(x*y, axis =0)

z = x **5

#x= tf.random.normal((2,3))
#y= tf.random.normal((3,4))
#z = tf.matmul(x,y) 


# Indexing
x = tf.constant(range(1,10))
y = x[1:]
z = x[1:3]
w = x[::2]
p = x[::-1]


print(p)

