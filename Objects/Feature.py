class Feature:
    key: str
    value: str

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def __eq__(self, other) ->bool:
        if(self.key == other.key and self.value == other.value):
            return True
        return False

    def __str__(self):
        return "{\"key\":\"" + str(self.key) + "\",\"value\":\"" + str(self.value) + "\"}"