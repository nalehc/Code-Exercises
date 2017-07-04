import image

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()


for col in range(img.getWidth()):                            
    for row in range(img.getHeight()):                          
        p = img.getPixel(col, row)
        grey = (p.getRed() + p.getGreen() + p.getBlue())/3
        newred = grey
        newgreen = grey
        newblue = grey

        newpixel = image.Pixel(newred, newgreen, newblue)

        newimg.setPixel(col, row, newpixel)

newimg.draw(win)
win.exitonclick()


wn.exitonclick()
    