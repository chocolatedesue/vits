import os
import shutil

file_path = r"D:\gg\get\floral\__Unpack__\floral\kano\audio"
dir = os.listdir(file_path)
idx = 0
txt = "./kano_train.txt.d.fix"
out_put = 'output'
mark = set()

def rename_audio(src):
    for i in os.listdir(src):
        src_path = os.path.join(src,i)
        i = "_".join(i.split('.')[:-1])+".ogg"
        out_path = os.path.join(src,i)
        os.rename(src_path,out_path)


def add_mark ():
    with open (txt,'r') as f1:
        for i in f1:
            idx = i.strip().split('|')[0].split('/')[-1]
            idx = idx[:-4]+".ogg"
            mark.add(idx)
            print (idx)


add_mark()


for i in dir:

    if not os.path.exists(out_put):
        os.mkdir(out_put)
    if i  in mark:
        shutil.copyfile(os.path.join(file_path,i),os.path.join(out_put,i))
    
        

print (idx)
