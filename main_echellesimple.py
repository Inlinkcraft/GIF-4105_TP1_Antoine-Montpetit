import numpy as np

def align_canaux(canal_mobile, canal_ref, delta_max:tuple = (15, 15), mask:tuple = (100, 100)) -> tuple:
    min_score = float('inf')
    delta = (0, 0)
    i = 0
    for y in range(-delta_max[1], delta_max[1] + 1):
        for x in range(-delta_max[0], delta_max[0] + 1):
            score = calculate_score(canal_ref[mask[0]:-mask[0], mask[1]: -mask[1]], np.roll(np.roll(canal_mobile, x, axis = 0), y, axis = 1)[mask[0]:-mask[0], mask[1]: -mask[1]])
            if score < min_score:
                min_score = score
                delta = (x, y)
            i += 1
            print(str(i) + "\t" + str(np.floor((float(i) / 961.0)*100)) + " %\t (" +  str(x) + ", " + str(y) + ")\t" + str(score))
    return delta

def calculate_score(img_1, img_2):
    return np.sum((img_1 - img_2)**2)
