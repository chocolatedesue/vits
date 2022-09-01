
import torch
src = ""



stat_dic = torch.load(src)['model']

name = src.split('.')[0]+"_demo"+'.pth'

torch.save({'model': stat_dic,
              'iteration': None,
              'optimizer': None,
              'learning_rate': None}, src)