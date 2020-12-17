import os
# os.system('cd C:\Users\pc\Documents\Python Personal\Fruit_Counting\yolov5')
# os.system('pip install -qr requirements.txt')

import torch
import browseFileGUI as bfg
from IPython.display import Image, clear_output  # to display images

# source = bfg.askdirectory()
# path = bfg.askdirectory()
# print(bfg.askopenfile())
# os.system("cd Fruit_Counting/yolov5")
os.system(f'python yolov5/detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source yolov5/data/images --save-txt --project results')

for image in os.listdir("yolov5/data/images"):
  # print(image[:-3])
  x = len(os.listdir("results"))
  l = x if x != 0 else ''
#   print(l)
  with open(f"results/exp{l}/labels/{image[:-3]+'txt'}", "r+") as f:
    # print(f)
    # print(f.read())

    # content = f.read()
    # print("number of fruits", len(content.split("\n")))
    n = 0
    for _ in f.readlines():
      # print(_[:2])
      if int(_[:2]) in [46, 47, 49]:
        n += 1

    print(f"number of fruits in {image}:", n)
