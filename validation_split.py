import os, sys
from os.path import join
from os import listdir
import numpy as np

TRAIN_DIR  = "Train Images"
VALID_DIR  = "Validation Images"
VALID_LOCK = "valid_lock"

classes = [class_ for class_ in os.listdir(TRAIN_DIR) if os.path.isdir(join(TRAIN_DIR, class_))]
validation_split = 0.15

try:
    os.mkdir(VALID_DIR)
except FileExistsError:
    print("Folder already exists")

if os.path.exists(join(TRAIN_DIR, VALID_LOCK)):
    print("[!] validation already done ! Quitting ...")
    sys.exit(0)

total = sum([len(listdir(join(TRAIN_DIR, class_))) for class_ in classes])
print("[*] total images : {}".format(total))

for class_ in classes:
    images = os.listdir(join(TRAIN_DIR, class_))
    valid_folder = join(VALID_DIR, class_)
    valid_files_num = round(len(images) * validation_split)

    try:
        os.mkdir(join(VALID_DIR, class_))
    except FileExistsError:
        print("[!] class {} Folder already exists in validation directory ".format(class_))

    print("[*] total files of class {} : {}".format(class_, len(images)))
    print("[*] taking {} files from {} to validation set".format(valid_files_num, class_))

    # shuffle files
    np.random.shuffle(images)

    # get files
    valid_images = images[:valid_files_num]
    for file in valid_images:
        old_path = join(TRAIN_DIR, class_, file)
        new_path = join(VALID_DIR, class_, file)
        os.rename(old_path, new_path)

file = open(join(TRAIN_DIR, VALID_LOCK),'w')
file.close()