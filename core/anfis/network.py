import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


class AnfisNetwork:
    """Creates ANFIS neural network"""

    def __init__(self, n_inputs: int, n_rules: int, learning_rate: float = 1e-2):
        """
        ?

        :type n_inputs: int
        :param n_inputs:
        :type n_rules: int
        :param n_rules:
        :type learning_rate: float
        :param learning_rate:
        """
        self.n = n_inputs
        self.m = n_rules
        # Input
        self.inputs = tf.placeholder(tf.float32, shape=(None, n_inputs))
        # Desired output
        self.targets = tf.placeholder(tf.float32, shape=None)
        # Means of Gaussian MFS
        mu = tf.get_variable("mu", [n_rules * n_inputs], initializer=tf.random_normal_initializer(0, 1))
        # Standard deviations of Gaussian MFS
        sigma = mu = tf.get_variable("sigma", [n_rules * n_inputs], initializer=tf.random_normal_initializer(0, 1))
        # Sequent centers
        y = tf.get_variable("y", [1, n_rules], initializer=tf.random_normal_initializer(0, 1))

        self.params = tf.trainable_variables()
        self.rul = tf.reduce_prod(
            tf.reshape(tf.exp(-0.5 * tf.square(tf.subtract(tf.tile(self.inputs, (1, n_rules)), mu)) / tf.square(sigma)),
                       (-1, n_rules, n_inputs)), axis=2
        )

        # Fuzzy base expansion function
        num = tf.reduce_sum(tf.multiply(self.rul, y), axis=1)
        den = tf.clip_by_value(tf.reduce_sum(self.rul, axis=1), 1e-12, 1e12)
        self.out = tf.divide(num, den)

        # Loss function computation
        self.loss = tf.losses.huber_loss(self.targets, self.out)

        # Optimization step
        self.optimize = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(self.loss)
        # Variables initializer
        self.init_variables = tf.global_variables_initializer()

    def infer(self, sess, x, targets=None):
        """
        ?

        :type sess: tf.Session
        :param sess: ?
        :param x: ?
        :param targets: ?
        :return: ?
        """
        if targets is None:
            return sess.run(self.out, feed_dict={self.inputs: x})
        else:
            return sess.run([self.out, self.loss], feed_dict={self.inputs: x, self.targets: targets})

    def train(self, sess, x, targets):
        """
        ?

        :param sess: ?
        :param x: ?
        :param targets: ?
        :return: ?
        """
        yp, l, _ = sess.run([self.out, self.loss, self.optimize], feed_dict={self.inputs: x, self.targets: targets})
        return l, yp

    def plot_mfs(self, sess):
        """
        ?

        :param sess:
        :return:
        """
        mus = sess.run(self.params[0])
        mus = np.reshape(mus, (self.m, self.n))
        sigmas = sess.run(self.params[1])
        sigmas = np.reshape(sigmas, (self.m, self.n))
        y = sess.run(self.params[2])
        xn = np.linspace(-1.5, 1.5, 1000)
        for r in range(self.m):
            if r % 4 == 0:
                plt.figure(figsize=(11, 6), dpi=80)
            plt.subplot(2, 2, (r % 4) + 1)
            ax = plt.subplot(2, 2, (r % 4) + 1)
            ax.set_title("Rule %d, sequent center: %f" % ((r + 1), y[0, r]))
            for i in range(self.n):
                plt.plot(xn, np.exp(-0.5 * ((xn - mus[r, i]) ** 2) / (sigmas[r, i] ** 2)))
