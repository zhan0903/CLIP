import minedojo

env = minedojo.make(
    task_id="harvest_wool_with_shears_and_sheep",
    image_size=(288, 512)
)
obs = env.reset()
for i in range(1000):
    act = env.action_space.no_op()
    act[0] = 1    # forward/backward
    if i % 50 == 0:
        act[2] = 1    # jump
    obs, rwd, done, info = env.step(act)
env.close()