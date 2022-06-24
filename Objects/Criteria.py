from Abstracts.CriteriaTypes import CriteriaTypes
class Criteria:
    key = CriteriaTypes
    value = None
    def __init__(self, key:CriteriaTypes = None, value = None):
        self.key = key
        self.value = value

    def __str__(self):
        return "{" + str(self.key) + ":" + str(self.value) + "}"