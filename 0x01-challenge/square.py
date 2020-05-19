#!/usr/bin/python3
'''
Dumb comment
'''


class square():
    '''
    Square class
    '''

    width = 0

    def __init__(self, *args, **kwargs):
        '''
        Init
        '''
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def permiter_of_My_Square(self):
        '''
        Perimeter
        '''
        return (self.width * 4)

    def __str__(self):
        '''
        to string
        '''
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_My_Square())
