class API():
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def creator(self):
        return self._creator
    @creator.setter
    def creator(self, creator):
        self._creator = creator
