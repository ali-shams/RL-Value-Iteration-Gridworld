import os
from math import ceil
from datetime import datetime
from typing import (Dict,
                    List,
                    Tuple
                    )

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from helper.utils import ConstantCharacters as CONSTANTS
from helper.myfunction import _print

from game.game import Game
from grid.world import World


def clear_screen() -> None:
    """
    clear terminal screen based on operating system type
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def find_values() -> None:
    """
    find states value based on the bellman equation
    """
    converged: bool = False
    iteration: int = 0
    while not converged:
        DELTA: int = 0
        for state in world.states_space:
            iteration += 1
            if world.is_terminal_state(state):
                world.states_value[state]: int = 0
            else:
                old_value_based_on_all_action: int = world.states_value[state]
                new_values_list_for_each_action: List = list()
                for action in world.actions:
                    new_values_list: List = list()
                    for probabilistic_action in world.actions:
                        next_state: Tuple = \
                            world.find_next_state(state, probabilistic_action)
                        reward: int = world.find_next_state_reward(next_state)
                        probability: float = \
                            world.find_probaility(action, probabilistic_action)
                        new_values_list.append(probability * (reward
                                                              + (config['discount_factor']
                                                                 * world.states_value[next_state])))

                    new_values_list_for_each_action.append(sum(new_values_list))

                world.states_value[state]: int = \
                    max(new_values_list_for_each_action)
                DELTA: int = max(DELTA,
                                 np.abs(old_value_based_on_all_action
                                        - world.states_value[state]))
                converged: bool = True if DELTA < config['theta'] else False
    _print(f'Number of iteration is {iteration}')


def find_policy() -> None:
    """
    find the optimal policy.
    the action with the highest value of total discount cost,
    among other actions, is the optimal action.
    """
    for state in world.states_space:
        new_values_list_for_each_action: List = []

        for action in world.actions:
            next_state: Tuple = world.find_next_state(state, action)
            reward: int = world.find_next_state_reward(next_state)
            new_values_list_for_each_action.append(reward
                                                   + config['discount_factor']
                                                   * world.states_value[next_state])
        best_action: str = \
            new_values_list_for_each_action.index(
                max(new_values_list_for_each_action)
            )
        world.policy[state]: str = world.actions_arrow[best_action]


def plot_policy() -> None:
    """
    plot policy as heatmap
    """
    max_discounted_value = ceil(np.amax(world.states_value))
    fig, ax = plt.subplots()
    ax.xaxis.tick_top()
    sns.heatmap(world.states_value,
                vmin=0,
                vmax=max_discounted_value, cmap="YlGnBu",
                annot=world.policy, fmt="", linewidths=.2,
                cbar_kws={'label': 'Discounted sum cost'})
    os.makedirs(world.config['dir_to_save'], exist_ok=True)
    plot_name = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    plt.savefig(f"{world.config['dir_to_save']}{plot_name}.pdf")
    plt.show()
    plt.close()
    _print('The plot was created successfully.')


if __name__ == '__main__':
    clear_screen()
    _print(CONSTANTS.WELCOME_MESSAGE.value)
    config: Dict = dict({
        'volcano_penalty': -10,
        'goal_reward': 10,
        'discount_factor': 1,
        'theta': 1e-10,
        'action_probability': 0.7,
        'dir_to_save': 'plot/'
    })
    game: Game = Game()
    world: World = World(config, game)
    world.initialize_values()
    world.initialize_policy()
    find_values()
    find_policy()
    plot_policy()
