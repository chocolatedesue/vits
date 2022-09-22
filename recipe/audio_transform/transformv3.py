# from asyncio import tasks
# import multiprocessing
import os
import concurrent.futures
import logging
import asyncio
import time

LOG_INTERVAL= 150
LOG_FILE = '22k.log'
SAMPLE_RATE = 22050
SRC_DIR = 'data'
OUT_DIR = '22k'
task = []
AUDIO_TYPE = ['wav','ogg','opus']


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
getlogger(LOG_FILE)
  



def transform(src,out):
    cnt = 0
    logging.info(src+"|"+out+" started")
    for i in os.listdir(src):
        res = i.split('.')
        if res[-1] not in AUDIO_TYPE:
            continue
        else:
            audio_without_postfix = res[0]
            out_path = os.path.join(out,audio_without_postfix)+'.wav'
            src_path = os.path.join(src,i)
            
            if os.path.exists(out_path):
                continue
            if cnt%LOG_INTERVAL!=0:
                os.system(f"ffmpeg -i {src_path} -ar {SAMPLE_RATE} -acodec pcm_s16le -ac 1 {out_path} -y -v quiet")
            else:
                os.system(f"ffmpeg -i {src_path} -ar {SAMPLE_RATE} -acodec pcm_s16le -ac 1 {out_path} -y")
            cnt+=1
            
    return (src,cnt)



def walk_dir(src_dir:str,out_dir:str,excutor):
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    for i in os.listdir(src_dir):
        # try to recurse the step
        src = os.path.join(src_dir,i)
        out = os.path.join(out_dir,i)
        
        if os.path.isdir(src):
            walk_dir(src,out,excutor)
        else:
            if i.split('.')[-1] in AUDIO_TYPE:
                global task
                task.append(excutor.submit(transform,src_dir,out_dir))
                return 
            
            

if __name__=='__main__':
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        walk_dir(SRC_DIR,OUT_DIR,executor)
        for i in task:
            st = time.time()
            src,cnt = i.result()
            ed = time.time()

            logging.info("{}'s dump nums: {} ".format(src,cnt))
            logging.info("consume time: {:.2f}".format(ed-st))
            

    end_time = time.time()
    logging.info("total finished cost: {:.2f}".format(end_time-start_time))
    print ("total finished cost: {:.2f}".format(end_time-start_time))