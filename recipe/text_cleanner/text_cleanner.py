import re
# src = "res.txt.cl.es"



def exclude_H(src):
    with open(src+'.eh','w',encoding='utf-8') as file:
        with open(src,'r',encoding='utf-8') as origin:
            i=0
            for line in origin:
                dict={'kanji':0}
                scn=line.strip().split('|')[2]
                for chara in scn:
                    if re.search('[\u4e00-\u9fff]',chara):
                        dict['kanji']+=1
                    elif chara not in dict.keys():
                        dict[chara]=1
                    else:
                        dict[chara]+=1
                num=0
                for h_kana in ['ぁ','ぃ','ぅ','ぇ','ぉ','ゃ','ゅ','ょ','ァ','ィ','ゥ','ェ','ォ','ャ','ュ','ョ','っ','ッ','ん','ー','…','●']:
                    if h_kana in dict.keys():
                        num+=dict[h_kana]
                if num/len(scn)>0.35:
                    i+=1
                    continue
                file.write(line)
            print("exclude_H: ",i)
    return src+'.eh'

# こにちわ、「あやせ」　-》 こにちわ、あやせ and 替换中文空格
def ex_brackets(file_path):
    left = ['（','[','『','「', '【']
    right = ['）',']','』','」','】']
    tot = left + right
    specials = ["$f.word","精液"]
    pat = re.compile('(（(.*)）)|(\[(.*)\])|(『(.*)』)')
    
    def sp_exist(str:str):
        for i in specials:
            # print (i)
            if str.find(i)!=-1:
                return True
        return False

    def clean_brac(str:str):
        res = ""
        for i in str:
            if i in tot:
                continue
            # print (i)
            res = res+i
        return res

    with open(file_path,'r',encoding='utf-8') as f1:
        with open (file_path+".eb",'w',encoding='utf-8') as f2:
            for line in f1:
                # 全角空格换成半角  中 =》英
                line = line.replace('\u3000','\u0020')
                res = line.strip().split('|')
                content = res[-1]
                # print (content)
                pre = "|".join(res[:-1])+"|"
                if len (content)<6 or sp_exist(content):
                # if len (content)<6:
                    index += 1
                    continue
                tmp = pat.search(content)
                # print ('sad')

                if not tmp:
                    f2.write(line)
                else:
                    # print (tmp.groups())
                    # print (content)
                    content = clean_brac (content)
                    f2.write(pre+content+'\n')

    print ("ex_brackets: ",index)
    return file_path+".eb"


def remove_short_sentence(src_path):
    with open(src_path,'r',encoding = 'utf-8') as file:
        with open (src_path+'.rs','w',encoding='utf-8') as output:
            idx = 0
            for line in file:
                line = line.replace(r'\\n','')
                mid = line.strip().split('|')
                text  = mid[-1]

                if len(text)>5:
                    idx+=1
                    output.write(line)
            print ("remove_short_sentence: ",idx)
    return src_path+'.rs'


def unique(src):
    mark = set()
    idx = 0
    with open (src,'r') as f1:
        with open (src+'.u','w') as f2:
            for line in f1:
                res = line.split('|')[0].split('/')[-1][:-4]
                if res not in mark:
                    f2.write(line) 
                    mark.add(res)
                else:
                    idx+=1
    print (idx)
    return src+'.u'