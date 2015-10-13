import os
import logging.config
import toolbox
import yaml

from logging import *

from inspect import getsourcefile
from os.path import abspath
from os.path import dirname
from os.path import join

path = abspath(join(dirname(getsourcefile(lambda:0)),  "../../logging.yaml"))

def setup_logging(
    default_path=path, 
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

# kick it on import
setup_logging()
