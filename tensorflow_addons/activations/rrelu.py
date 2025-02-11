# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from tensorflow_addons.utils import keras_utils

@keras_utils.register_keras_custom_object
@tf.function
def rrelu(x,lower=0.125, upper=0.3333333333333333):
    """rrelu function.

    Computes rrelu function:
    `x if x > 0 else random(lower,upper)*x`.

    Args:
        x: A `Tensor`. Must be one of the following types:
            `float16`, `float32`, `float64`.
        lower: `float`, lower bound for random alpha.
        upper: `float`, upper bound for random alpha.
    Returns:
        A `Tensor`. Has the same type as `x`.
    """
    x = tf.convert_to_tensor(x)
    lower=tf.convert_to_tensor(x)
    upper=tf.convert_to_tensor(x,dtype=lower.dtype)
    alpha=tf.random.uniform([],lower,upper)
    return tf.nn.leaky_relu(x,alpha,name='rrelu')
