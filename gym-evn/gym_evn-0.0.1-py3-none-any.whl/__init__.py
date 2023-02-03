from gym.envs.registration import register

register(
    id='gym_evn-v0',
    entry_point='gym_evn.envs:GymEnv',
)