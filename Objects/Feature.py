class Feature:
    key: str
    value: str

    def __eq__(self, other) ->bool:
        if(self.key == other.key and self.value == other.value):
            return True
        return False