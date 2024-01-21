from dotenv import dotenv_values

env = dotenv_values()


def getenv(name: str, ntype: str):
    value = env.get(name)
    if not value:
        return ""
    return ntype(value)


class Config:
    SESSION_NAME1 = getenv('SESSION_NAME1', str)
    API_ID1 = getenv('API_ID1', int)
    API_HASH1 = getenv('API_HASH1', str)

    SESSION_NAME2 = getenv('SESSION_NAME2', str)
    API_ID2 = getenv('API_ID2', int)
    API_HASH2 = getenv('API_HASH2', str)

    EDEN_API = getenv('EDEN_API', str)
    WEATHER_API = getenv('WEATHER_API', str)
