class LastScoreSingleton:
    """ Singleton class to store the last score of ML training. """

    _instance = None
    _last_score = None
    _no_score_set = True

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LastScoreSingleton, cls).__new__(cls)
        return cls._instance

    def set(self, score):
        """ Set the last score of ML training. """
        assert isinstance(score, (int, float)), "Score must be a number!"
        assert not isinstance(score, bool), "Score must not be a boolean"
        self._last_score = score
        self._no_score_set = False

    def take(self):
        """ Take the last score of ML training. """
        if self._no_score_set:
            msg = "No score has been set yet! "
            raise ValueError(msg)
        return self._last_score

    def clear(self):
        """ Clear the last score of ML training. """
        self._last_score = None
        self._no_score_set = True
