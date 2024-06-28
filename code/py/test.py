### Import modules and libraries ###

import constellate
import pandas as pd
import os
import json
from pathlib import Path
import gzip

# For displaying plots inline with Jupyter Notebooks
%matplotlib inline

# Creating a variable `dataset_id` to hold our dataset ID
# The default dataset is Shakespeare Quarterly, 1950-present
dataset_id = "92c32bef-5e54-8741-1e64-a417053d18cd"
