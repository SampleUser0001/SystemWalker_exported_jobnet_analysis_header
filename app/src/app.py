# -*- coding: utf-8 -*-
from logging import getLogger, config, DEBUG
import os

import sys
import glob
from logutil import LogUtil
from enums import TypeEnum

from controller import CSVReadController

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
LOG_CONFIG_FILE = ['config', 'log_config.json']

logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(os.path.join(PYTHON_APP_HOME, *LOG_CONFIG_FILE))
config.dictConfig(log_conf)
logger.setLevel(DEBUG)
logger.propagate = False

def exec():
    # 起動引数の取得
    # args = sys.argv
    # args[0]はpythonのファイル名。
    # 実際の引数はargs[1]から。

    args = sys.argv
    csv_home = args[1]
    export_home = args[2]

    logger.info(f'csv_home: {csv_home}')
    logger.info(f'export_home: {export_home}')

    NET_list = []
    JOB_list = []
    for csv in glob.glob(csv_home + '/**/*.csv', recursive=True):
        tmp_dict = CSVReadController.read(csv)
        NET_list.append(tmp_dict[TypeEnum.NET.value])
        JOB_list.append(tmp_dict[TypeEnum.JOB.value])
        logger.debug(f'csv: {csv}, header: {tmp_dict[TypeEnum.NET.value]}, JOB: {tmp_dict}')
    
    export(export_home + '/NET.txt', NET_list)
    export(export_home + '/JOB.txt', JOB_list)

def export(export_path: str, data: list):
    with open(export_path, 'w') as f:
        for d in set(data):
            f.write(d + '\n')
    
if __name__ == '__main__':
    logger.info('Start')
    exec()
    logger.info('Finish')
