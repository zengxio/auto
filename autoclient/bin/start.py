#!/usr/bin/env python
#encoding:utf-8
import os
os.environ['USER_SETTINGS']="config.settings"
from lib.conf.config import settings
# print(settings.USER)
# print(settings.EMAIL)
from src.plugins import PluginManager
import sys
BASEDIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
from src import script
if __name__ == '__main__':
    script.run()
    # server_info=PluginManager().exec_plugin()
    # print(server_info)
    # server_info=PluginManager('192.168.1.199').exec_plugin()

