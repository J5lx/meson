# Copyright 2016 The Meson development team

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .. import coredata, build
from .. import mesonlib
import os

class Python3Module:

    def extension_module(self, state, args, kwargs):
        if 'name_prefix' in kwargs:
            raise mesonlib.MesonException('Name_prefix is set automatically, specifying it is forbidden.')
        if 'name_suffix' in kwargs:
            raise mesonlib.MesonException('Name_suffix is set automatically, specifying it is forbidden.')
        host_system = state.host_machine.system
        if host_system == 'darwin':
            # Default suffix is 'dylib' but Python does not use it for extensions.
            suffix = 'so'
        elif host_system == 'windows':
            # On Windows the extension is pyd for some unexplainable reason.
            suffix = 'pyd'
        else:
            suffix = []
        kwargs['name_prefix'] = ''
        kwargs['name_suffix'] = suffix
        return state.interpreter.func_shared_lib(None, args, kwargs)

def initialize():
    return Python3Module()
