from PIL import Image


def is_building(im):
    black = 0
    for pixel in im.getdata():
        black += pixel
    return black>256*256/2

for i,line in enumerate(open("buildings.tiles")):
    try:
        line_splt=line.split(",")
        #line_splt.reverse()
        line_splt[0], line_splt[2]=line_splt[2].strip('\n'), line_splt[0]
        line_splt[1], line_splt[2]=line_splt[2], line_splt[1]
        path="/".join(line_splt)
        im = Image.open("masks/"+path+".png")
        if(is_building(im)):
             Image.open("images/"+path+".webp").convert("RGB").save("buildings/"+str(i)+".png","png")
        else:
            Image.open("images/"+path+".webp").convert("RGB").save("not_buildings/"+str(i)+".png","png")
    except:
        pass

