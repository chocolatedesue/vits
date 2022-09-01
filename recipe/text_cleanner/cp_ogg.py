import os
import shutil

file_path = r"C:\Users\ccds\Desktop\code\gal\senbaka\audio"
dir = os.listdir(file_path)
idx = 0
# txt = "fix.txt"
out_put = 'output'
mark = set()


def add_mark (txt):
    with open (txt,'r',encoding='utf-8') as f1:
        for i in f1:
            idx = i.strip().split('|')[0].split('/')[-1]
            idx = idx[:-4]+".ogg"
            mark.add(idx)
            


add_mark(r"C:\Users\ccds\Desktop\code\gal\senbaka\text\senbaka_train_filelist.txt")
add_mark(r'C:\Users\ccds\Desktop\code\gal\senbaka\text\senbaka_val_filelist.txt')


for i in dir:
    if not os.path.exists(out_put):
        os.mkdir(out_put)
    if i in mark:
        shutil.copyfile(os.path.join(file_path,i),os.path.join(out_put,i))
        idx+=1
        

print (idx)
