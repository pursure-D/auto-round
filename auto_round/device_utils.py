
# Copyright (c) 2023 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def is_optimum_habana_available():
    import importlib
    from transformers.utils.import_utils import is_optimum_available

    return is_optimum_available() and importlib.util.find_spec("optimum.habana") != None

try:
    import habana_frameworks.torch.hpu as hthpu
    import habana_frameworks.torch.core as htcore
    if is_optimum_habana_available():
        is_hpu_available = True
    else:
        print("Should install optimum-habana when the environment has habana frameworks")
        is_hpu_available = False
except ImportError:
    is_hpu_available = False
