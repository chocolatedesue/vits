import os


file_path = "train_6_fix.txt.et"
idx = 0

# dir = os.path.join("data","dataset")
dir = ""
List = list (map(lambda x:x[:-4],os.listdir(dir)))
mark = set(List)


with open (file_path,'r') as f1:
    with open (file_path+'.et','w') as f2:
        for line in f1:
            res = line.split('|')[0].split('/')[-1][:-4]
            if res not in mark:
                idx+=1
                continue
            f2.write(line)         
                
print (idx)