import logging
LOG_FILE = 'test.log'

def getlogger(file_name):
    logger = logging.getLogger("asyncio")
    # logger.setLevel(logging.INFO)
    logging.basicConfig(level=logging.INFO #设置日志输出格式
                    ,filename=file_name #log日志输出的文件位置和文件名
                    ,filemode="w" #文件的写入格式，w为重新写入文件，默认是追加
                    ,format="%(asctime)s-%(filename)-8s: %(message)s" #日志输出的格式
                    # -8表示占位符，让输出左对齐，输出长度都为8位
                    ,datefmt="%Y-%m-%d %H:%M:%S" #时间输出的格式
                    )
    return logger

def test_basic():
    logging.basicConfig(level=logging.INFO)
    logging.info('sad')

log = getlogger(LOG_FILE)
log.info("sad")
