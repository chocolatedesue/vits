import os
from pickle import TRUE
import logging

logging.basicConfig(filename='not_found.log',filemode='w',level=logging.INFO)

SCRIPT = '/root/workspace/test_data/tr_19'
POST_FIX=['.ogg','.opus','.wav']

# mark = set()vali

def validate(script:str):
    cnt=0
    with open (script,'r') as f1:
        for i in f1:
            res = i.strip().split('|')[0].split('.')[0]
            FLAG = False
            for j in POST_FIX:
                path = res+j
                # print (res)
                if os.path.isfile(path):
                    FLAG=TRUE
                    break
            if not FLAG:
                cnt+=1
                logging.info(i.strip())
        
    print ("not found nums: {}".format(cnt))


if __name__ == "__main__":
    validate(SCRIPT)