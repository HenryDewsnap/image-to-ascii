# image-to-ascii

## Usage
``` 
1.) main.py
2.) Enter Image Path (INCLUDING FILE EXTENSION)
3.) Enter the width of the output you want (the height will be worked out from this)
4.) Enjoy
```

## How It Works
```
1.) Opens image and gets data such as width,height as well as pixel RGB values.
2.) Iterates over each pixel summing the RGB values Value = R+G+B
3.) Value Divided by (255+255+255 / length of asciicharacters) to get the index of the ascii-character
4.) Prints this ascii-character
```
