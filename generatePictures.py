def gp(startingNumber, endingNumber):


    for i in range(startingNumber, endingNumber + 1):
        s = f'<div class = "galleryContent">\n\t<img class = "galleryImage" src = "imgForWeb/galleryImg/gallery_{i}.jpeg" alt = "">\n</div>'
        print(s)


if __name__ == '__main__':
    gp(8,27)