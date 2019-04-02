#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Mar 21, 2018

.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

RL environment for story-telling from WikiData
based on https://github.com/openai/gym-wikinav/blob/master/gym_wikinav/envs/wikinav_env/environment.py
'''

import gym
from gym import error, spaces, utils
from gym.utils import seeding


class WikiDataEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, beam_size=32, goal_reward=10.0):
        """
        Args:
            beam_size: Number of candidates to present as actions at each
                timestep
            graph:
        """
        self.graph = 
        self.beam_size = beam_size
        self.goal_reward = goal_reward
        self._action_space = spaces.Discrete(self.beam_size)

    def step(self, action):
        """
        Parameters
        ----------
        action :

        Returns
        -------
        ob, reward, episode_over, info : tuple
            ob (object) :
                an environment-specific object representing your observation of
                the environment.
            reward (float) :
                amount of reward achieved by the previous action. The scale
                varies between environments, but the goal is always to increase
                your total reward.
            episode_over (bool) :
                whether it's time to reset the environment again. Most (but not
                all) tasks are divided up into well-defined episodes, and done
                being True indicates the episode has terminated. (For example,
                perhaps the pole tipped too far, or you lost your last life.)
            info (dict) :
                 diagnostic information useful for debugging. It can sometimes
                 be useful for learning (for example, it might contain the raw
                 probabilities behind the environment's last state change).
                 However, official evaluations of your agent are not allowed to
                 use this for learning.
        """
        self._take_action(action)
        self.status = self.env.step()
        reward = self._get_reward()
        ob = self.env.getState()
        episode_over = self.status != hfo_py.IN_GAME
        return ob, reward, episode_over, {}

    def reset(self):
        pass

    def render(self, mode='human', close=False):
        pass

    def _take_action(self, action):
        pass

    def _get_reward(self):
        """ Reward is given for ... """
        return 0

    def close(self):
        pass
