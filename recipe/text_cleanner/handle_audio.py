import os
import shutil
idx = 0


def audio_handler(src,output):
    if not os.path.exists(output):
        os.mkdir(output)
    for file in os.listdir(src):
        res = file.split('.')
        src_path = os.path.join(src,file)
        if res[-1]=='wav':
            shutil.copyfile(src_path,os.path.join(output,file))
            
        else:
            file_without_postfix = res[0]
            os.system(f"ffmpeg -i {f'{src}/{file}'} -ar 22050 -acodec pcm_s16le -ac 1 {f'{output}/{file_without_postfix}.wav'}")
            global idx
            idx+=1


if __name__ == "__main__":
    audio_handler('atn2','dataset')
    print (idx)