import sys

import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

tensorboard_directory = sys.argv[1]

# Fetch MNIST Dataset using the supplied Tensorflow Utility Function
mnist = input_data.read_data_sets("data/MNIST_data/", one_hot=True)

# Setup the Model Parameters
INPUT_SIZE, HIDDEN_SIZE, OUTPUT_SIZE = 784, 100, 10

### Start Building the Computation Graph ###

def get_model(features, labels, mode, params):
    # Initializer - initialize our variables from standard normal with stddev 0.1
    initializer = tf.random_normal_initializer(stddev=0.1)

    X = features["x"]

    # Hidden Layer Variables
    W_1 = tf.get_variable("Hidden_W", shape=[INPUT_SIZE, HIDDEN_SIZE], initializer=initializer, dtype=tf.float64)
    b_1 = tf.get_variable("Hidden_b", shape=[HIDDEN_SIZE], initializer=initializer, dtype=tf.float64)

    # Hidden Layer Transformation
    hidden = tf.nn.relu(tf.matmul(X, W_1) + b_1)

    # Output Layer Variables
    W_2 = tf.get_variable("Output_W", shape=[100, 10], initializer=initializer, dtype=tf.float64)
    b_2 = tf.get_variable("Output_b", shape=[10], initializer=initializer, dtype=tf.float64)

    # Output Layer Transformation
    output = tf.matmul(hidden, W_2) + b_2

    softmax_output = tf.nn.softmax(output)

    custom_mae_metric = tf.metrics.mean_absolute_error(
        predictions=softmax_output,
        labels=labels)
    tf.summary.scalar("custom_mae_metric", custom_mae_metric[1])
    loss = tf.losses.softmax_cross_entropy(labels, output)

    # train_op = tf.train.AdamOptimizer().minimize(loss)
    train_op = tf.train.AdamOptimizer().minimize(loss, global_step=tf.train.get_global_step())

    estimator_spec = tf.estimator.EstimatorSpec(
        mode=tf.estimator.ModeKeys.TRAIN,
        loss=loss,
        train_op=train_op)
    return estimator_spec

classifier = tf.estimator.Estimator(
    model_fn=get_model,
    model_dir=tensorboard_directory,
    config=tf.estimator.RunConfig(
        save_summary_steps=1))
        # log_step_count_steps=10))

classifier.train(
    input_fn=tf.estimator.inputs.numpy_input_fn(
        x={"x": mnist.train.images.astype(np.float64)},
        y=mnist.train.labels,
        shuffle=True),
    steps=201)

