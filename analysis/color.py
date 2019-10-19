# pase the intevral of color. The highter the number, the brighter the color
def genRGB(init,final,n):
    color_list = []
    if n-1==0: return(init)

    a = int(str(final[1:3]),16) - int(str(init[1:3]),16)
    b = int(str(final[3:5]),16) - int(str(init[3:5]),16)
    c = int(str(final[5:]),16) - int(str(init[5:]),16)
    dn = (int(a/n-1),int(b/n-1),int(c/n-1))
    
    for i in range(n-1,0,-1):
        s = '#'
        s += str(hex(int(str(init[1:3]),16)+i*dn[0]))
        s += str(hex(int(str(init[3:5]),16)+i*dn[1]))
        s += str(hex(int(str(init[5:]),16)+i*dn[2]))
        color_list.append(s)
    return(color_list)

# mix color with five kind of dataset
def indexRGB(data1,data2,data3,data4,data5):
    x = data1*8 + data3*8 + data4*4 + data5*8
    y = data4*14 + data5*14
    if x!=0 : 
       b = 255
    else :
       b = x
    if y!=0 : 
       r = 255
    else :
       r = y
    s1 = '#' + str(hex(r)[2:]) + str(hex(x+y)[2:]) + str(hex(b)[2:])
    return(s1)


def toRGB(r, g, b):
    s = '#'
    if r < 16:
        s += '0'
    s += hex(r)[2:]
    if g < 16:
        s += '0'
    s += hex(g)[2:]
    if b < 16:
        s += '0'
    s += hex(b)[2:]
    return s.upper()


def interpol(color1, color2, a):
    color = [0, 0, 0]
    for i in range(3):
        color[i] = int(color1[i] * (1-a) + color2[i] * a)

    return color