from PIL import Image

def rotate(path, save_path, deg):
    if type(deg) != int: # Deg type check
        raise Exception("Degress has to be of type int")
    try:
        img = Image.open(path)
        img = img.rotate(deg)
        img.save(save_path)
        print("Process Completed")
    except IOError:
        pass

i_path = input("Image Path: ")
i_save_path = input("Image Save Path: ")
i_degs = int(input("Image Degrees: "))

rotate(i_path, i_save_path, i_degs)