class CoordinateValidator:
    """
    class Base
    """

    @property
    def height(self) -> str:
        """
        getter for grid world height attribute
        """
        return self.__height

    @height.setter
    def height(self,
               height: int) -> None:
        """
        setter for grid world height attribute
        Parameters
        ----------
        `height` : `int`
            grid world height attribute
        Raises
        ----------
        TypeError: raise an exception if the data type is not an integer
        ValueError: raise an exception if the value is not a positive integer
        """
        if height.isdigit():
            if int(height) > 1:
                self.__height: int = int(height)
            else:
                raise ValueError(f'{height} is invalid. '
                                 f'height must be greater than 1.')
        else:
            raise TypeError(f'{height} is invalid. '
                            f'you must enter a positive integer number.')

    @property
    def width(self) -> str:
        """
        getter for grid world width attribute
        """
        return self.__width

    @width.setter
    def width(self,
              width: int) -> None:
        """
        setter for grid world width attribute
        Parameters
        ----------
        `width` : `int`
            grid world width attribute
        Raises
        ----------
        TypeError: raise an exception if the data type is not an integer
        ValueError: raise an exception if the value is not a positive integer
        """
        if width.isdigit():
            if int(width) > 1:
                self.__width: int = int(width)
            else:
                raise ValueError(f'{width} is invalid. '
                                 f'width must be greater than 1.')
        else:
            raise TypeError(f'{width} is invalid. '
                            f'you must enter a positive integer number.')

    @property
    def x_volcano(self) -> str:
        """
        getter for x location of volcano attribute
        """
        return self.__x_volcano

    @x_volcano.setter
    def x_volcano(self,
                  x_volcano: int) -> None:
        """
        setter for x location of volcano attribute
        Parameters
        ----------
        `x_volcano` : `int`
            x location of volcano attribute
        Raises
        ----------
        TypeError: raise an exception if the data type is not an integer
        ValueError: raise an exception if the value is not a positive integer
        """
        if x_volcano.isdigit():
            if 0 <= int(x_volcano) < self.__height:
                self.__x_volcano: int = int(x_volcano)
            else:
                raise ValueError(f'{x_volcano} is invalid. '
                                 f'x location of the volcano '
                                 f'must be between 0 to {self.__height - 1}.')
        else:
            raise TypeError(f'{x_volcano} is invalid. '
                            f'you must enter a positive integer number.')

    @property
    def y_volcano(self) -> str:
        """
        getter for y location of volcano attribute
        """
        return self.__y_volcano

    @y_volcano.setter
    def y_volcano(self,
                  y_volcano: int) -> None:
        """
        setter for y location of volcano attribute
        Parameters
        ----------
        `y_volcano` : `int`
            y location of volcano attribute
        Raises
        ----------
        TypeError: raise an exception if the data type is not an integer
        ValueError: raise an exception if the value is not a positive integer
        """
        if y_volcano.isdigit():
            if 0 <= int(y_volcano) < self.__width:
                self.__y_volcano: int = int(y_volcano)
            else:
                raise ValueError(f'{y_volcano} is invalid. '
                                 f'y location of the volcano '
                                 f'must be between 0 to {self.__width - 1}.')
        else:
            raise TypeError(f'{y_volcano} is invalid. '
                            f'you must enter a positive integer number.')

    @property
    def x_goal(self) -> str:
        """
        getter for x location of goal attribute
        """
        return self.__x_goal

    @x_goal.setter
    def x_goal(self,
               x_goal: int) -> None:
        """
        setter for x location of goal attribute
        Parameters
        ----------
        `x_goal` : `int`
            x location of goal attribute
        Raises
        ----------
        TypeError: raise an exception if the data type is not an integer
        ValueError: raise an exception if the value is not a positive integer
        """
        if x_goal.isdigit():
            if 0 <= int(x_goal) < self.__height:
                self.__x_goal: int = int(x_goal)
            else:
                raise ValueError(f'{x_goal} is invalid. '
                                 f'x location of the goal '
                                 f'must be between 0 to {self.__height - 1}.')
        else:
            raise TypeError(f'{x_goal} is invalid. '
                            f'you must enter a positive integer number.')

    @property
    def y_goal(self) -> str:
        """
        getter for y location of goal attribute
        """
        return self.__y_goal

    @y_goal.setter
    def y_goal(self,
               y_goal: int) -> None:
        """
        setter for y location of goal attribute
        Parameters
        ----------
        `y_goal` : `int`
            y location of goal attribute
        Raises
        ----------
        TypeError: raise an exception if the data type is not an integer
        ValueError: raise an exception if the value is not a positive integer
        """
        if y_goal.isdigit():
            if 0 <= int(y_goal) < self.__width:
                self.__y_goal: int = int(y_goal)
            else:
                raise ValueError(f'{y_goal} is invalid. '
                                 f'y location of the goal '
                                 f'must be between 0 to {self.__width - 1}.')
        else:
            raise TypeError(f'{y_goal} is invalid. '
                            f'you must enter a positive integer number.')
