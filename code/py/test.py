
# https://lab.constellate.org

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
# dataset_id = ""

# Pull in the sampled (1500 items) dataset CSV using
# The .get_metadata() method downloads the CSV file for our metadata
# to the /data folder and returns a string for the file name and location
# dataset_metadata will be a string containing that file name and location
dataset_metadata = constellate.get_metadata("data/bvb-jsonl.jsonl")

# Download the full dataset (up to a limit of 25,000 documents),
# request it first in the builder environment. See the Constellate Client
# documentation at: https://constellate.org/docs/constellate-client
# Then use the `constellate.download` method show below.
#dataset_metadata = constellate.download(dataset_id, 'metadata')
