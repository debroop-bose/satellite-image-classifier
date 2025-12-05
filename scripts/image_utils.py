from PIL import Image
import numpy as np


def load_image(path):
    
    return Image.open(path)
    
def resize_image(image, size=(128, 128)):
    
    return image.resize(size)

def img_to_array(image):
    
    return np.asarray(image)
    
def normalise(image_array):
    
    return image_array.astype("float32") / 255.0
    
def compute_avg_rgb(image_array):
    
    avgR = np.mean(image_array[0, 0, 2])
    avgG = np.mean(image_array[0, 0, 1])
    avgB = np.mean(image_array[0, 0, 0])


    return {
        
        "avgR" : float(avgR),
        "avgG" : float(avgG),
        "avgB" : float(avgB)
    }

def compute_bright(image_arr):
    
    return float(image_arr.mean())