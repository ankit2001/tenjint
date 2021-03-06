# tenjint - VMI Python Library
#
# Copyright (C) 2020 Bedrock Systems, Inc
# Authors: Jonas Pfoh <jonas@bedrocksystems.com>
#          Sebastian Vogl <sebastian@bedrocksystems.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from enum import Enum
import platform
import logging

_arch = platform.machine()

class Arch(Enum):
    UNSUPPORTED = 0
    X86_64 = 1
    AARCH64 = 2
    X86 = 3
    AARCH32 = 4

from .api import *
if _arch == "x86_64":
    arch = Arch.X86_64
    from .api_x86_64 import *
elif _arch == "aarch64":
    arch = Arch.AARCH64
    from .api_aarch64 import *
else:
    raise RuntimeError("Unrecognized Architecture")

try:
    from .tenjintapi import *
except ImportError as e:
    initialized = False
    logging.warning("Unable to import tenjintapi ({})".format(e))
else:
    initialized = True
    if _arch == "x86_64":
        from .tenjintapi_x86_64 import *
    elif _arch == "aarch64":
        from .tenjintapi_aarch64 import *
    else:
        raise RuntimeError("Unrecognized Architecture")
