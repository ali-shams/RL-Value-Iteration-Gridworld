from itertools import product
from typing import Dict, Tuple, List

import numpy as np

from game.game import Game


class World:
    """
    class World
    """

    def __init__(self,
                 config: Dict,
                 game: Game,
                 *args,
                 **kwargs) -> None:
        """
        Constructor
        Parameters
        ----------
        `config` : `Dict`
            game configuration setup
        `game` : `Game`
            an instance of the Game class
        """
        self.config: Dict = config
        self.world_height: int = game.height
        self.world_width: int = game.width
        self.volcano_state: Tuple = (game.x_volcano, game.y_volcano)
        self.goal_state: Tuple = (game.x_goal, game.y_goal)
        self.x: int = None
        self.y: int = None
        self.states_space: List = self.create_states_space()
        self.actions: List = ['up', 'right', 'down', 'left']
        self.actions_arrow: List = ['\u2191', '\u2192', '\u2193', '\u2190']

    def create_states_space(self) -> List:
        """
        create a states space based on world height and width
        example:
             ━━━ ━━━ ━━━ ━━━ ━━━
            │ V │   │   │   │   │
             ━━━ ━━━ ━━━ ━━━ ━━━
            │   │   │   │   │   │
             ━━━ ━━━ ━━━ ━━━ ━━━
            │   │   │   │   │   │
             ━━━ ━━━ ━━━ ━━━ ━━━
        V is (0, 0) to (game.height, game.width)
        Returns
        -------
        `List`
        """
        return list(product(range(self.world_height), range(self.world_width)))

    def initialize_values(self) -> None:
        """
        initialize states values to zero
        example:
        [[0. 0. 0. 0. 0.]
         [0. 0. 0. 0. 0.]
         [0. 0. 0. 0. 0.]
         [0. 0. 0. 0. 0.]
         [0. 0. 0. 0. 0.]]
        """
        self.states_value: np = \
            np.full(shape=(self.world_height, self.world_width),
                    fill_value=0, dtype=np.float64)

    def initialize_policy(self) -> None:
        """
        initialize policy to none
        example:
        [[None None None None None]
         [None None None None None]
         [None None None None None]
         [None None None None None]
         [None None None None None]]
        """
        self.policy: np = np.full(shape=(
            self.world_height, self.world_width),
            fill_value=None)

    def is_terminal_state(self,
                          state: Tuple) -> bool:
        """
        check if the state is a terminal state
        Parameters
        ----------
        `state`: `Tuple`
            a state from states space
        Returns
        -------
        `bool`: true if the state is a terminal state, otherwise false
        """
        return state in [self.volcano_state, self.goal_state]

    def find_next_state(self,
                        current_state: Tuple,
                        action: str) -> Tuple:
        """
        find the next state based on the current state and an action
        Parameters
        ----------
        `current_state`: `Tuple`
        `action`: `str`
        Returns
        -------
        `Tuple`: next state as tuple
        """
        (self.x, self.y) = current_state
        if action in ('up', 'down'):
            self.check_height_boundary(action)
        else:
            self.check_width_boundary(action)
        return (self.x, self.y)

    def check_height_boundary(self,
                              action: str) -> None:
        """
        check the north and south boundary of the grid world
        Parameters
        ----------
        `action`: `str`
        """
        if (self.x - 1 < 0 and action == 'up') or (
                self.x + 1 == self.world_height and action == 'down'):
            pass
        elif action == 'up':
            self.x -= 1
        else:
            self.x += 1

    def check_width_boundary(self,
                             action: str) -> None:
        """
        check the west and east boundary of the grid world
        Parameters
        ----------
        `action`: `str`
        """
        if (self.y - 1 < 0 and action == 'left') or (
                self.y + 1 == self.world_width and action == 'right'):
            pass
        elif action == 'left':
            self.y -= 1
        else:
            self.y += 1

    def find_next_state_reward(self,
                               next_state: Tuple) -> int:
        """
        find the reward of going to the next state
        Parameters
        ----------
        `next_state`: `Tuple`
        Returns
        -------
        `int`: the numerical amount of reward
        """
        if next_state == self.goal_state:
            reward: int = self.config['goal_reward']
        elif next_state == self.volcano_state:
            reward: int = self.config['volcano_penalty']
        else:
            reward: int = -1
        return reward

    def find_probaility(self,
                        action: str,
                        probabilistic_action: str) -> float:
        """
        find the probability of performing an action.
        the probability of each action is indicated by
        config['action_probability'].
        Parameters
        ----------
        `action`: `str`
        `probabilistic_action`: `str`
        Returns
        -------
        `float`: the probability of performing an action
        """
        prob = (1 - self.config['action_probability']) / 4
        if action == probabilistic_action:
            prob += self.config['action_probability']
        return prob
