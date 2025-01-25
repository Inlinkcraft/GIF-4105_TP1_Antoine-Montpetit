#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TP1, code python pour débuter
from main_echellesimple import align_canaux
from manipulation_img import *
import numpy as np
import skimage as sk
import skimage.io as skio

# nom du fichier d'image
img_path = 'Assets/00106v.jpg'

# Loader l'image
img = img_load(img_path)

# Couper l'image
b, g, r = img_slice(img, 3)

# aligner les images... c'est ici que vous commencez à coder!
# ces quelques fonctions pourraient vous être utiles:
# np.roll, np.sum, sk.transform.rescale (for multiscale)

### ag = align(g, b)
### ar = align(r, b)

pos_r = align_canaux(r, b, (15, 15), (50, 50))
pos_g = align_canaux(g, b, (15, 15), (50, 50))

r = np.roll(np.roll(r, pos_r[0], axis = 0), pos_r[1], axis = 1)
g = np.roll(np.roll(g, pos_g[0], axis = 0), pos_g[1], axis = 1)

print("===================COMPLETE===================")
print("Position r", pos_r, "Position g", pos_g)
print("==============================================")

# Regénère l'image
img_out = generate_img_from_rgb(r, g, b)

# sauvegarder l'image
fname = 'out/out_fname.jpg'
skio.imsave(fname, img_out)

# afficher l'image
skio.imshow(img_out)
skio.show()