from gym.envs.registration import register

register(
    id='qianghua_evn-v0',
    entry_point='qianghua_evn.envs:QhEnv',
)