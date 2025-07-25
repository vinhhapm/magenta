# Copyright 2025 The Magenta Authors.
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

"""Tensor2Tensor trainer for Magenta problems."""

# Registers all Magenta problems with Tensor2Tensor.

from magenta.tensor2tensor import models  # pylint: disable=unused-import
from magenta.tensor2tensor import problems  # pylint: disable=unused-import
from tensor2tensor.bin import t2t_trainer
import tensorflow.compat.v1 as tf


def main(argv):
  t2t_trainer.main(argv)


def console_entry_point():
  tf.disable_v2_behavior()
  tf.logging.set_verbosity(tf.logging.INFO)
  tf.app.run(main)


if __name__ == '__main__':
  console_entry_point()
