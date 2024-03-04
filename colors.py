

def color(color_name):
    colors = {
        'white':(255, 255, 255),
        'black':(0, 0, 0),
        'red':(255, 0, 0),
        'blue':(0, 0, 255)
    }

    return colors.get(color_name, (0, 0, 0))