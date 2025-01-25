import numpy as np
import skimage as sk
import skimage.io as skio

# Lit l'image a une location "path"
# Retourne sont information sous forme d'array de float 
def img_load(path: str) -> any:
    im = skio.imread(path) # lire l'image
    return sk.img_as_float(im) # conversion en double

# Découpe une image dans le sens voulue
# Un nombre de fois voulue
# Retourne un tuple de tous les image découper
def img_slice(img: any, number_of_cuts: int, orientation: int = 0) -> tuple:
    length = int(np.floor(img.shape[orientation] / float(number_of_cuts))) # Calcul la longueur que doit avoir chacune des image
    
    # Selon l'orientation on coupe l'image original
    prev_length = 0
    curr_lenght = length
    cuts = []
    if orientation == 0:
        for i in range(number_of_cuts):
            cuts.append(img[prev_length: curr_lenght])
            prev_length = curr_lenght
            curr_lenght += length
    elif orientation == 1:
        for i in range(number_of_cuts):
            cuts.append(img[:,prev_length: curr_lenght])
            prev_length = curr_lenght
            curr_lenght += length
    else:
        raise IndexError("Orientation invalide")
    
    return tuple(cuts)

# Reconstruit l'image avec les canaux rgb
def generate_img_from_rgb(r, g, b,) -> any:
    im_out = np.dstack([r, g, b])
    return sk.img_as_ubyte(im_out)