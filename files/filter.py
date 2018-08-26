from PIL import ImageFilter
from PIL import Image

def main():
    im = Image.open("kent800.jpg")
    
    for i in range(im.width):
        for j in range(im.height):
            r,g,b = im.getpixel((i,j))
            
            avg = (r+g+b)//3
            im.putpixel((i,j),(avg,avg,avg))
            
    im.show()
    
main()