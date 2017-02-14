#   Copyright 2017 Covata Limited or its affiliates
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import logging
import inspect

__all__ = ["LogMixin"]


class LogMixin(object):
    @property
    def logger(self):
        return logging.getLogger(self.__caller())

    def __caller(self):
        """
        Gets the name of the caller in {package}.{module}.{class} format

        :return: the name of the caller
        """
        # type: () -> str
        stack = inspect.stack()
        if len(stack) < 3:
            return ''

        caller_frame = stack[2][0]
        module = inspect.getmodule(caller_frame)
        name = filter(lambda x: x is not None, [
            module.__name__ if module else None,
            self.__class__.__name__])

        del caller_frame
        return ".".join(name)