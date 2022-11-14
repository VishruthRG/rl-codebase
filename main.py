import gym
import numpy as np
import matplotlib.pyplot as plt
import keras
import tensorflow as tf
import random

env = gym.make('Pong-v4')

init_frame = env.reset()
plt.imshow(init_frame)

for i in range(10000):
    a = random.sample([0,1,2,3], 1)[0]
    ns, r, d, info = env.step(a)
    env.render()
    if d == True:
        env.reset()
