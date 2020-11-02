import cv2
import os
from imutils import paths
import shutil

pasta = 'Mae'
id = 4

def listNegImagem():
    imagemPath = list(paths.list_images(pasta))
    numero = 1
    if not os.path.exists('Fotos'):
        os.makedirs('Fotos')

    for i in imagemPath:
        rename = i.replace(i, "Fotos/" + "pessoa." + str(id) + "." + str(numero) + ".jpg")
        fotoName = rename.split("/")[1]
        shutil.copy(i, rename)
        img = cv2.imread("Fotos/" + fotoName, cv2.IMREAD_GRAYSCALE)
        resized_image = cv2.resize(img, (220, 220))
        cv2.imwrite("Fotos/" + fotoName, resized_image)

        print(fotoName)

        numero += 1

listNegImagem()