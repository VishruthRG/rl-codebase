import gym
import numpy as np
import matplotlib.pyplot as plt
import keras
import tensorflow as tf
import random
import cv2

env = gym.make('Pong-v4', render_mode = "human")

init_frame = env.reset()

def process_frame(frame):
    frame = frame[30:-12,5:-4]
    frame = np.average(frame,axis = 2)
    frame = cv2.resize(frame,(84,84),interpolation = cv2.INTER_NEAREST)
    frame = np.array(frame,dtype = np.uint8)
    return frame

for i in range(1):
    a = random.sample([0,1,2,3], 1)[0]
    next_obs, rw, done, _, info = env.step(a)
    next_obs = process_frame(next_obs)
    # plt.imshow(obs)
    plt.show()
    env.render()
    if done == True:
        env.reset()

