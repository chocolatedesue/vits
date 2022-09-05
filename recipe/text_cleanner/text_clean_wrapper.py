

from recipe.text_cleanner.text_cleanner import ex_brackets, exclude_H


class cleanner():
    
    def __init__(self) -> None:
        self.src_path = ''
        self.out_path = ''
        # self.content = ''
        

    def clean(self,src,out):
        self.src_path = src
        self.out_path = out
        # self.content
        with open (self.src_path,'r',encoding='utf-8') as f1:
            content = f1.readlines()

        content = ex_brackets(content)
        content = exclude_H(content)
        
        with open (self.out_path,'w',encoding='utf-8') as f2:
            for i in content:
                f2.write(i)
        print ("done")


    def exclude_H(self,content:str):
        import re
        i=0
        eh_content = []
        for line in content:
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
            # file.write(line)
            eh_content.append(line)
        print("exclude_H: ",i)
        return eh_content

# こにちわ、「あやせ」　-》 こにちわ、あやせ and 替换中文空格
    def ex_brackets(self,content):
        import re
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

        ex_mark_content = []
        for line in content:
            # 替换中文空格
            line = line.replace('\u3000','\u0020')
            line = line.replace(r'\\n','')
            line = line.replace(r'\n','')


            res = line.strip().split('|')
            content = res[-1]
            pre = "|".join(res[:-1])+"|"
            
            if len (content)<6 or sp_exist(content):
            # if len (content)<6:
                index += 1
                continue
            tmp = pat.search(content)
            # print ('sad')

            if not tmp:
                ex_mark_content.append(line)
            else:
                content = clean_brac (content)
                ex_mark_content.append(pre+content+'\n')

        print ("ex_brackets: ",index)
        return ex_mark_content



