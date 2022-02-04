import gym
import time

ENV_NAME = "Acrobot-v1"

env = gym.make(ENV_NAME)

num_episodes = 20
timesteps = 1000

for episode in range(num_episodes):
    observe = env.reset()
    for _ in range(timesteps):
        env.render()
        time.sleep(0.01)
        observe, reward, done, info = env.step(env.action_space.sample())
        print(f"Observe: {observe}\nReward: {reward}\nDone: {done}\nInfo: {info}")
        if done:
            print(f"Episode {episode} is done")
            break
env.close()
