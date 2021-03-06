import sys

import tensorflow as tf

if __name__ == "__main__":
    tensorboard_directory = sys.argv[1]

    graph = tf.Graph()
    sess = tf.Session(graph=graph)


    with graph.as_default():
        t_input = tf.placeholder(tf.float32, shape=())
        t_metric = tf.summary.scalar("my_metric", t_input)
        writer = tf.summary.FileWriter(tensorboard_directory, graph)

    for i in range(10):
        val_to_log = i
        step = i % 5
        my_metric = sess.run(
            t_metric,
            feed_dict={
                t_input: val_to_log,
            })
        print("Logging value: `{val}` at step: `{step}`".format(
            val=val_to_log, step=step))
        writer.add_summary(my_metric, step)
        writer.flush()


