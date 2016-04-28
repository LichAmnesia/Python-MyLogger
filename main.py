# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia  
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-04-28 13:43:58
# @Last Modified time: 2016-04-28 13:49:06
# @FileName: main.py

from logger.mylogger import Logger
log_main = Logger.get_logger(__file__)

def main():
    # 输出info
    log_main.info("It is information")
    # 输出error
    log_main.error("It is an error")


if __name__ == '__main__':
    main()
