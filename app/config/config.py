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

    # NotCoin
    MIN_CLICKS_COUNT: int = 1
    AUTO_BUY_ENERGY_BOOST: bool = False
    AUTO_BUY_SPEED_BOOST: bool = True
    AUTO_BUY_CLICK_BOOST: bool = True
    USE_PROXY_FROM_FILE: bool = False
    SLEEP_BETWEEN_CLICK: list[int] = [10, 15]
    SLEEP_BEFORE_BUY_MERGE: list[int] = [10, 15]
    SLEEP_BEFORE_ACTIVATE_FREE_BUFFS: list[int] = [10, 15]
    SLEEP_BEFORE_ACTIVATE_TURBO: list[int] = [10, 15]
