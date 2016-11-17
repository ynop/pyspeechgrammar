*****
Integrated in https://github.com/ynop/spych. No changes will be made to this repository anymore.
*****


*****
pyspeechgrammar
*****

PySpeechGrammar can be used to parse and convert speech grammar formats.

Currently the following formats are supported:

* JSGF (parsing)
* SRGS XML (serializing)

Usage
########

**Import:**

.. code-block:: python

    import pyspeechgrammar

**Convert JSGF to SRGS XML**

.. code-block:: python

    import pyspeechgrammar
    
    jsgf_value = '#JSGF V1.0; ...'
    srgs_xml_value = pyspeechgrammar.convert_jsgf_string_to_srgs_xml_string(jsgf_value)

.. code-block:: python

    import pyspeechgrammar
    
    jsgf_file_path = 'file.jsgf'
    srgs_xml_target_path = 'srgs.xml'
    
    srgs_xml_value = pyspeechgrammar.convert_jsgf_to_srgs_xml(jsgf_file, srgs_xml_target_path)



Installation
########

.. code-block:: bash

    python setup.py install

Requirements
########

* modgrammar

Compatibility
########

* Python 3

Licence
########

The MIT License (MIT)

Copyright (c) 2015 Matthias

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
