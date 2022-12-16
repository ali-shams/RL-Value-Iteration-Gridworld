from game.coordinate_validator import CoordinateValidator


class Game(CoordinateValidator):
    """
    class Game
    """

    # height = CoordinateValidator()
    # width = CoordinateValidator()

    def __init__(self) -> None:
        """
        Constructor
        """
        # self.height = input('Enter the height of the grid world: ')
        # self.width = input('Enter the width of the grid world: ')
        self.get_dimensions()
        self.get_volcano_loc()
        self.get_goal_loc()
        self.is_co_location_volcano_and_goal()

    def get_dimensions(self) -> None:
        """
        get height and width from the end user to create a grid world
        """
        self.height: int = input('Enter the height of the grid world: ')
        self.width: int = input('Enter the width of the grid world: ')

    def get_volcano_loc(self) -> None:
        """
        get the position of the volcano in terms of x and y
        """
        self.x_volcano: int = input(f'Enter X location of '
                                    f'volcano, between [0 {self.height - 1}]: ')
        self.y_volcano: int = input(f'Enter Y location of '
                                    f'volcano, between [0 {self.width - 1}]: ')

    def get_goal_loc(self) -> None:
        """
        get the position of the goal in terms of x and y
        """
        self.x_goal: int = input(f'Enter X location '
                                 f'of goal, between [0 {self.height - 1}]: ')
        self.y_goal: int = input(f'Enter Y location '
                                 f'of goal, between [0 {self.width - 1}]: ')

    def is_co_location_volcano_and_goal(self) -> None:
        """
        checking if the location of the goal and the volcano is the same
        """
        if self.x_volcano == self.x_goal and self.y_volcano == self.y_goal:
            raise Exception('The location of the volcano '
                            'and the goal should not be the same.')
