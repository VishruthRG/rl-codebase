import gym
import numpy as np
import matplotlib.pyplot as plt
import keras
import tensorflow as tf
import random

env = gym.make('Pong-v4', render_mode='human')

init_frame = env.reset()
# plt.imshow(init_frame)

for i in range(10000):
    action = random.sample([0,1,2,3], 1)[0]
    obs, reward, terminated, truncated, info = env.step(action)
    env.render()
    if terminated == True:
        env.reset()
