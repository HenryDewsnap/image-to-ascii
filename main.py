from PIL import Image
import math

def get_pixels(path):
    image = Image.open(path)
    return image.load(), image.size

def sum_tuple(tuple):
    out = 0
    for num in tuple: out += num
    return out

pixels  = list(" .:-=+*#%@")
max_val = sum_tuple((255,255,255))
divider = math.ceil(max_val/len(pixels))

if __name__ == "__main__":
    image, size = get_pixels(input(f"[Image name/Image path]-> "))
    out_width = int(input("Enter Image Width-> "))
    out_size = [out_width,math.floor(size[1]/(size[0]/out_width))]
    dimensional_multiplers = [0,0]; dimensional_multiplers[0] = math.floor(size[0]/out_size[0]); dimensional_multiplers[1] = math.floor(size[1]/out_size[1])
    out_matrix = [[0 for x in range(out_size[0])] for y in range(out_size[1])]
    for y in range(out_size[1]):
        for x in range(out_size[0]):
            print(pixels[int(sum_tuple(image[x*dimensional_multiplers[0],y*dimensional_multiplers[1]])/divider)],end=" ")
        print()
