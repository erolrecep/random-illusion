import numpy as np
import cv2

def generate(seed_idx):
    np.random.seed(seed_idx)
    new_img = np.random.randint(0, 255, (480, 640))
    return new_img

img_array = []
for seed_idx in range(1024):
    new_img = generate(seed_idx)
    new_img = new_img.astype(np.uint8)
    height, width = new_img.shape
    size = (width,height)
    img_array.append(cv2.merge((new_img, new_img, new_img)))
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
