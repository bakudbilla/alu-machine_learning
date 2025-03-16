#!/usr/bin/env python3
""" Shear image """
import tensorflow as tf


def shear_image(image, intensity):
    """randomly shears image"""
    img = tf.keras.preprocessing.image.img_to_array(image)
    sheared_img = tf.keras.preprocessing.image.random_shear(img, intensity,
                                                            row_axis=0,
                                                            col_axis=1,
                                                            channel_axis=2
                                                            )
    shearimage_out = tf.keras.preprocessing.image.array_to_img(sheared_img)
    return shearimage_out
