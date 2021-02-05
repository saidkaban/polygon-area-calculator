class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for _ in range(self.height):
            picture = picture + "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, other_shape):
        width_wise = self.width // other_shape.width
        height_wise = self.height // other_shape.height
        print(width_wise * height_wise)
        return width_wise * height_wise

    def __str__(self):
       return "Rectangle(width={}, height={})".format(self.width, self.height)


class Square(Rectangle):
    def __init__(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_width(self, new_side):
        self.width = new_side
        self.height = new_side

    def set_height(self, new_side):
        self.width = new_side
        self.height = new_side

    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side

    def __str__(self):
        return "Square(side={})".format(self.width)