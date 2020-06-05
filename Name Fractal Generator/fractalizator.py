"""
This code makes a Julia set out of your name.
"""
from PIL import Image
from typing import List, Tuple


def first_and_last(name) -> Tuple[str, str]:
    """
    Separate a name into first and last
    """

    first, last, *_ = name.split()
    return list(first), list(last)


def numberator(word: str) -> int:
    """
    Assign a value to each letter in a name. Does not use standard
    alphabetical ordering, rather it uses an assignment based on how
    numbers were written in Ancient Greek.
    More on the way letters are encoded can be found at:
    https://greeknumber.weebly.com/uploads/3/8/9/4/38945097/498534559.gif?425

    Encoded for English, German and BKS
    """
    letter_values = {
        "a": 1,
        "b": 2,
        "c": 500,
        "č": 508,
        "ć": 310,
        "d": 4,
        "đ": 14,
        "e": 5,
        "f": 500,
        "g": 3,
        "h": 8,
        "i": 10,
        "j": 10,
        "k": 20,
        "l": 30,
        "m": 40,
        "n": 50,
        "o": 70,
        "p": 80,
        "q": 420,
        "r": 100,
        "s": 200,
        "š": 208,
        "t": 300,
        "u": 400,
        "v": 400,
        "w": 800,
        "x": 600,
        "y": 400,
        "z": 7,
        "ž": 15,
        "ä": 6,
        "ö": 75,
        "ü": 405,
        "ß": 400
    }
    return sum(letter_values.get(letter.lower(), 0) for letter in word)


def draw_julia(name, a, b,resolution):
    
    #Choosing a resolution
    #0 for quick code tests
     if resolution==0:
          width,height=100,100
     elif resolution==1:
          width,height=800,600
     elif resolution==2:
          width,height=1360,768
     elif resolution==3:
          width,height=1920,1080
     elif resolution==4:
          width,height=2048,1556
     elif resolution==5:
          width,height=3840,2160
     elif resolution==6:
          width,height=7680,4320

    
     
    #Making the fractal  
     aval = a / (10 ** ((len(str(a)) + 1))) + 0.6
     bval = ((b / (10 ** len(str(b)))) / 2) + 0.2
     w, h, zoom = width, height, 1
     bitmap = Image.new("RGB", (w, h), "white")
     pix = bitmap.load()
     cX = -aval
     cY = bval
     moveX, moveY = 0.0, 0.0
     maxIter = 255  
     for x in range(w):
        for y in range(h):
            zx = 1.5 * (x - w / 2) / (0.5 * zoom * w) + moveX
            zy = 1.0 * (y - h / 2) / (0.5 * zoom * h) + moveY
            i = maxIter
            while zx **2 + zy **2 < 4 and i > 1:
                tmp = zx **2 - zy **2 + cX
                zy, zx = 2.0 * zx * zy + cY, tmp
                i -= 1

            pix[x, y] = (i << 21) + (i << 10) + (i * 8)
     bitmap.show()
     bitmap.save("{0}.jpg".format(name))
	 


if __name__ == "__main__":
	name = input("Please enter your first and last name: ")
	if len(name.split(' '))!=2:
		print('Invalid input. Please try again!')
	else:
		resolution=int(input('\nPlease select the resolution\n'
			'1) VGA       (800  x 600)\n'
			'2) HD        (1360 x 768)\n'
			'3) Full HD   (1920 x 1080)\n'
			'4) 2K        (2048 × 1556)\n'
			'5) 4K        (3840 x 2160)\n'
			'6) 8K        (7680 × 4320)\n'
			'Enter [number] to select: '))
		if resolution not in range(0,7):
			print('Invalid input')
		else:    
			first, last = first_and_last(name)
			first_value = numberator(first)
			last_value = numberator(last)
			draw_julia(name, first_value, last_value,resolution)