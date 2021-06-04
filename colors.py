def color_choice(color):
    # default
    if color == 0:
        return [
            '#375E97',
            '#FB6542',
            '#FFBB00',
            '#3F681C'
            ]

    #blues
    elif color == 1:
        return [
            '#6930C3',
            '#5390D9',
            '#48BFE3',
            '#64DFDF',
            '#80FFDB'
            ]

    # balanced
    elif color == 2:
        return [
            '#264653',
            '#2a9d8f',
            '#e9c46a',
            '#f4a261',
            '#e76f51'
            ]
    # palewave
    elif color == 3:
        return [
            '#d8e2dc',
            '#ffe5d9',
            '#ffcad4',
            '#f4acb7',
            '#9d8189'
            ]
    # Custom, user selected colors
    elif color == 4:
        return "custom"