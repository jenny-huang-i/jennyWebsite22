from fileinput import filename
import os
from shutil import move
def rename(startingNumber, path):
    i = startingNumber

    for file in os.listdir(path):
        if not file.startswith("gallery_"):
            move(f'{path}\\{file}', f'{path}\\gallery_{i}.jpeg')
            i += 1
if __name__ == '__main__':
    rename(1, "C:\\Users\\Jenny Huang\\Documents\\GitHub\\webtwopointo\\imgForWeb\\galleryImg")