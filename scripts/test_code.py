from grid_env import GridEnv

env = GridEnv(size=5, target=[2, 3], forbidden=[[2, 2]], render_mode="")
obs, info = env.reset()

done = False
while not done:
    action = 1
    obs, reward, done, truncated, info = env.step(action)
    print(obs, reward, done)

env.render()