import os

def raw_to_json(tool_path,raw_dir_path):

    for i in os.listdir(raw_dir_path):
        token = i.split('.')
        if token[-1]=='scn' and token[-2]=='txt':
            os.system(f"{tool_path} {raw_dir_path}/{i}")


    for i in os.listdir (raw_dir_path):
        token = i.split('.')

        if token[-1]=='json' and token[-2]=='txt':
            try:
                os.rename(os.path.join(raw_dir_path,i),'json/'+i)
            except:
                continue
        if token[-1]=='json' and token[-2]=='resx':
            os.remove(os.path.join(raw_dir_path,i))


tool_path = r"C:\Users\ccds\Desktop\code\gal\util\Ulysses-FreeMoteToolkit-v3.2.0\FreeMoteToolkit\PsbDecompile.exe"

raw_to_json(tool_path,"raw")