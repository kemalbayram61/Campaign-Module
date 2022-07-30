from enum import Enum
class DBObjectRole(Enum):
    DATABASE = 0
    REDIS = 1
    APPLICATION_CACHE = 2