#!/usr/bin/env python

import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

notebooks = os.listdir('.')
notebooks = sorted(filter(lambda fn: fn.endswith('.ipynb') and fn[:2].isdigit(), notebooks))

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

for notebook_filename in notebooks:
    print(f'executing notebook {notebook_filename}')
    with open(notebook_filename) as f:
        nb = nbformat.read(f, as_version=4)
        ep.preprocess(nb, {'metadata': {'path': '.'}})
    with open(notebook_filename, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
