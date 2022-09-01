mark = set()
idx = 0

def unique(src):
    global mark
    global idx
    with open (src,'r') as f1:
        with open (src+'.u','w') as f2:
            for line in f1:
                res = line.split('|')[0].split('/')[-1][:-4]
                if res not in mark:
                    f2.write(line) 
                    mark.add(res)
                else:
                    idx+=1
   

def add_mark(src):
    global mark
    global idx
    with open (src,'r') as f1:
        for line in f1:
            res = line.split('|')[0].split('/')[-1][:-4]
            if res not in mark:
                mark.add(res)
            else:
                idx+=1
    

add_mark(r"C:\Users\ccds\Desktop\code\gal\senbaka\text\senbaka_train_filelist.txt")
print (len(mark))
print (idx)
unique(r"C:\Users\ccds\Desktop\code\gal\senbaka\text\senbaka_val_filelist.txt")

print (len(mark))
print (idx)