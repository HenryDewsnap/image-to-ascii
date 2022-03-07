from PIL import Image
import math

def get_pixels(path):
    ##Png's are wierd );
    if not path.endswith(".png"):
        im = Image.open(path)
        rgb_im = im.convert("RGB")
        rgb_im.save(path)
    image = Image.open(path)
    return image.load(), image.size

def sum_tuple(tuple):
    out = 0
    for num in tuple: out += num
    return out

pixels  = list(" .:-=+*#%@")
#pixels  = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'. ")
max_val = sum_tuple((255,255,255))
divider = math.ceil(max_val/len(pixels))

if __name__ == "__main__":
    image, size = get_pixels(input(f"[Image name/Image path]-> "))

    print(f"Image Dimensions: {size}")
    out_width = int(input("Enter Image Width-> "))
    if input("Auto Aspect Ratio (y/n): ") == "n":
        out_size = [out_width, int(input("Enter Image Height-> "))]
    else: out_size = [out_width,math.floor(size[1]/(size[0]/out_width))-1]
    multipliers = [size[0]/out_size[0], size[1]/out_size[1]]
    for y in range(out_size[1]):
        for x in range(out_size[0]):
            print(pixels[ int(sum_tuple(image[x*multipliers[0],y*multipliers[1]])/divider) ], end=" ")
        print()
