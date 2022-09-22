
import os
import re



# read by line
def get_scripts_v2(regex:str,src_dir,output_file,idx):
    with open (output_file,"a+",encoding='utf-8') as output:       
        for file_name in os.listdir(src_dir):
            with open (os.path.join(src_dir,file_name),"r",encoding='utf-8') as file:
                pattern = re.compile(regex)
                voice_name = re.compile(r'"voice": "(.*?)"')
                flag = True
                text = ""
                for line in file:
                    line = line.strip()
                    if flag:
                        res = pattern.search(line)
                        if res:
                            text = res.group(1)
                            flag = False if flag else True
                            

                    else:
                        res = voice_name.search(line)
                        if res:
                            audio = res.group(1)
                            ans = "dataset/"+audio+'.wav'+f"|{idx}|"+text+'\n'
                            output.write(ans)
                            flag = False if flag else True


def test():
    hm = r'\["虹夢",\[\[null,"「(.*?)」",[0-9]*'
    get_scripts_v2(hm,"test","hm.txt",1)


def main():
    # test()
    # holo = r'\["幌子",\[\[null,"「(.*?)」",[0-9]*'
    # kakuya= r'\["かぐや",\[\[null,"「(.*?)」",[0-9]*'
    # hm = r'\["虹夢",\[\[null,"「(.*?)」",[0-9]*'
    # yae = r'\["弥栄",\[\[null,"「(.*?)」",[0-9]*'
    # atn = r'\["あてな",\[\[null,"「(.*?)」",[0-9]*'
    # regexs = [kakuya,yae,hm,atn,holo]
    idx = 4
    if os.path.exists('json'):
        os.mkdir('json')
    regexs = [ r'\["あてな",\[\[null,"「(.*?)」",[0-9]*']
    for i in regexs:
        get_scripts_v2(i,"json",'res.txt',idx)
        idx+=1


if __name__=="__main__":
    main()