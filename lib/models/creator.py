class Creator():
    @property
    def name(self, name):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
