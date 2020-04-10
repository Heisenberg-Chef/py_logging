import logging
import time
#   创建一个log对象
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)   #   log的总开关
#   创建一个handler，用于写入日志文件
rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
handle = logging.FileHandler("log_2.txt",encoding='utf-8',mode='w')
handle.setLevel(logging.DEBUG)
#   定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
handle.setFormatter(formatter)
#   logger对象添加handle
logger.addHandler(handle)
# 创建一个流打印的handle
ch_handle = logging.StreamHandler()
ch_handle.setLevel(logging.DEBUG)
ch_handle.setFormatter(formatter)
#   将流加入到logger的实例对象
logger.addHandler(ch_handle)
#   打印日志
logger.debug('this is a logger debug message')
logger.info('this is a logger info message')
logger.warning('this is a logger warning message')
logger.error('this is a logger error message')
logger.critical('this is a logger critical message')