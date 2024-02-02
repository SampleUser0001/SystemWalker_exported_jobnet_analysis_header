# -*- coding: utf-8 -*-
from logging import getLogger, config, DEBUG
import os

# import sys
from logutil import LogUtil

from enums import TypeEnum

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
LOG_CONFIG_FILE = ['config', 'log_config.json']

logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(os.path.join(PYTHON_APP_HOME, *LOG_CONFIG_FILE))
config.dictConfig(log_conf)
logger.setLevel(DEBUG)
logger.propagate = False

class CSVReadController():
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def read(filepath: str) -> dict:
        return_dict = {
            TypeEnum.NET.value: "",
            TypeEnum.JOB.value: ""
        }
        with open(filepath, 'r') as f:
            read_flag = {
                TypeEnum.NET.value: False,
                TypeEnum.JOB.value: False
            }
            for line in f.read().splitlines():
                if line == TypeEnum.NET.value or line == TypeEnum.JOB.value:
                    read_flag[line] = True
                    continue
                elif line == read_flag[TypeEnum.NET.value]:
                    return_dict[TypeEnum.NET.value] = line
                    read_flag[TypeEnum.NET.value] = False
                elif line == read_flag[TypeEnum.JOB.value]:
                    return_dict[TypeEnum.JOB.value] = line
                    read_flag[TypeEnum.JOB.value] = False
                else:
                    pass
        return return_dict
