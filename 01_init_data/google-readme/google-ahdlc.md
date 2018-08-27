# aHDLC Data Frame Layer
This is not an officially supported Google product

This repository contains a micro controller friendly implimentation of a
data framing layer, in C.


## How to use this library

CMake and Bazel build files have been included for your convenience.

 Lib only
 ```shell
  cmake CMakeLists.txt
  make all
 ```
Unit Tests
``` shell
  cmake CMakeLists.txt
  make unit_tests
  ./src/unit_tests/unit_tests
  ```

See unit tests for example usage.

## Source Code Headers

Every file containing source code must include copyright and license
information. This includes any JS/CSS files that you might be serving out to
browsers. (This is to help well-intentioned people avoid accidental copying that
doesn't comply with the license.)

Apache header:

    Copyright 2018 Google Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        https://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.