import the_agent
import environ_pong as environment
#import matplotlib.pyplot as plt
import time
from collections import deque
import numpy as np
import csv
import os

name = 'PongDeterministic-v4'

agent = the_agent.Agent(possible_actions=[0,2,3],starting_mem_len=50000,max_mem_len=750000,starting_epsilon = 1, learn_rate = .00025)
env = environment.make_env(name,agent)

last_100_avg = [-21]
scores = deque(maxlen = 100)
max_score = -21

#If testing:
# agent.model.load_weights('recent_weights.hdf5')
# agent.model_target.load_weights('recent_weights.hdf5')
# agent.epsilon = 0.0

env.reset()

with open('three-layer-cpu-data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Episode', 'Steps', 'Duration', 'Score', 'Max Score', 'Epsilon'])

for i in range(10000):
    
    timesteps = agent.total_timesteps
    timee = time.time()
    score = environment.play_episode(name, env, agent, debug = False) #set debug to true for rendering
    scores.append(score)
    if score > max_score:
        max_score = score

    print('\nEpisode: ' + str(i))
    # print('Steps: ' + str(agent.total_timesteps - timesteps))
    # print('Duration: ' + str(time.time() - timee))
    # print('Score: ' + str(score))
    # print('Max Score: ' + str(max_score))
    # print('Epsilon: ' + str(agent.epsilon))



    data = [str(i), str(agent.total_timesteps - timesteps), str(time.time() - timee), str(score), str(max_score), str(agent.epsilon)] 
    if i % 10 == 0 and i != 0:
        with open('three-layer-cpu-data.csv', 'a') as f: 
            writer = csv.writer(f)   
            writer.writerow(data)

        # if i%100==0 and i!=0:
        #     last_100_avg.append(sum(scores)/len(scores))
        #     plt.plot(np.arange(0,i+1,100),last_100_avg)
        #     plt.show()