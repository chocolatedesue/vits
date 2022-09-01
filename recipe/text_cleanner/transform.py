def transform(src):
    with open (src,'r',encoding='utf-8') as f1:
        with open (src+'.cg','w',encoding='utf-8') as f2:
            for line in f1:
                mid = line.strip().split('|')
                mid[1] =  str(int(mid[1])+8)
                # print (mid)
                ans = '|'.join(mid)+'\n'
                f2.write(ans)
                
transform("train_6_fix.txt.et")