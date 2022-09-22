import os


# dir = ""
import shutil

# data = [('.scn','text'),('.ogg','audio')]
data = [('.scn','text')]


def get(src:str,out:str,name:str):
    index = 0
    for i in os.listdir(dir):
        if i.endswith(name):
            if name=='.ogg':
                if i.startswith('bgm') or i.startswith('hse') or i.startswith('se') or i.startswith('sys'):
                    continue
            src_path = os.path.join(src,i)
            out_path = os.path.join(out,i)
            shutil.copyfile(src_path,out_path)
            index+=1
    print (f"dump nums: {index}")


            
dir = r'D:\gg\get\ambitious_mission\unencrypted'

for i in data:
    out_dir,content = i[-1],i[0]
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    get (dir,out_dir,content)