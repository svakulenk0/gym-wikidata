from gym.envs.registration import register

register(
    id='wikidata-v0',
    entry_point='gym_wikidata.envs:WikiDataEnv',
)
