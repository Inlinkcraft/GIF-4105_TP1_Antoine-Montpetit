#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TP1, code python pour débuter

# quelques librairies suggérées
# vous pourriez aussi utiliser matplotlib et opencv pour lire, afficher et sauvegarder des images

import numpy as np
import skimage as sk
import skimage.io as skio

# nom du fichier d'image
imname = 'Assets/00029u.tif'

# lire l'image
im = skio.imread(imname)

# conversion en double
im = sk.img_as_float(im)
    
# calculer la hauteur de chaque partie (1/3 de la taille de l'image)
height = int(np.floor(im.shape[0] / 3.0))

# sÃ©parer les canaux de couleur
b = im[:height]
g = im[height: 2*height]
r = im[2*height: 3*height]

# aligner les images... c'est ici que vous commencez à coder!
# ces quelques fonctions pourraient vous être utiles:
# np.roll, np.sum, sk.transform.rescale (for multiscale)

### ag = align(g, b)
### ar = align(r, b)
# créer l'image couleur
im_out = np.dstack([r, g, b])
im_out = sk.img_as_ubyte(im_out)

# sauvegarder l'image
fname = 'out/out_fname.jpg'
skio.imsave(fname, im_out)

# afficher l'image
skio.imshow(im_out)
skio.show()