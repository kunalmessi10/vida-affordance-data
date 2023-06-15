import gzip
from typing import Any
import json
import glob
import os

import prior
from tqdm import tqdm


PATH = os.getcwd()


def load_dataset(config: Any = None, **kwargs) -> prior.DatasetDict:
    """Load the dataset."""
    data = {
        "train": prior.Dataset(
            data=[os.path.join(PATH, "data")], dataset="vida-affordance-data", split="train"
        )
    }

    return prior.DatasetDict(**data)
