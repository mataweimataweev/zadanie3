def ploshad(width, height):
    if width <= 0 or height <= 0:
        return "Ширина и высота прямоугольника должны быть положительными числами."
    else:
        area = width * height
        return area

print(ploshad(65,45))