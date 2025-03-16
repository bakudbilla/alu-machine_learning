#!/usr/bin/env python3
""" rotate_image"""
import tensorflow as tf


def rotate_image(image):
    """rotates image by 90 degrees
    """
    rotate_90 = tf.image.rot90(image, k=1)
    return rotate_90
