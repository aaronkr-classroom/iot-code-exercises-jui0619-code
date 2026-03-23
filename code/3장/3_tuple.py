#3_tuple.py
#RGB 색상을 표현하는 튜플 예제
black=(0,0,0) #(r,g,b)
white=(255,255,255) #왜 255까지?
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
my_color=(24,75,189) #??? => blue-purple

#my_color[2]=0 #blue 삭제
my_color=(24,75,0)

my_colors=[
    black, white, red,
    green, blue, my_color
    ]

for color in my_colors:
    print(color)