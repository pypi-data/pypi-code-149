from gym.envs.registration import register

register(
    id='lt_env-v0',
    entry_point='lt_evn.envs:LtEnv',
)