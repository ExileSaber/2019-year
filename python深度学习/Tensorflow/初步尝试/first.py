import tensorflow as tf
a = tf.placeholder(dtype=tf.int32, shape=[])
b = tf.placeholder(dtype=tf.int32, shape=[])
mul = tf.multiply(a, b)
add1 = tf.add(a, b)
add2 = tf.add(add1, mul)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())  # 初始化所有节点
    add2 = sess.run(add2, feed_dict={a: 4, b: 2})  # 实现并计算mul节点
    print(add2)