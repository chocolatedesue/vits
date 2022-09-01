from random import random, shuffle
import re

src = "fix.txt"


def my_shuffer():
    with open (src+'.rd','w',encoding='utf-8') as o:
        with open (src ,'r',encoding='utf-8') as s:
            ans = s.readlines()
            shuffle(ans)
            o.writelines(ans)


if __name__=='__main__':
    # transform()
    my_shuffer()