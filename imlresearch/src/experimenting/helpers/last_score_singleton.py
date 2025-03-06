class LastScoreSingleton:
    """
    Singleton class to store the last score of ML training.

    This class ensures that only one instance exists and provides methods
    to set, retrieve, and clear the last recorded score.
    """

    _instance = None
    _last_score = None
    _no_score_set = True

    def __new__(cls):
        """
        Create or return the existing instance of the class.

        Returns
        -------
        LastScoreSingleton
            The singleton instance of the class.
        """
        if cls._instance is None:
            cls._instance = super(LastScoreSingleton, cls).__new__(cls)
        return cls._instance

    def set(self, score):
        """
        Set the last score of ML training.

        Parameters
        ----------
        score : int, float, or None
            The score value to store. Must be a numeric value or None.
        """
        assert isinstance(
            score, (int, float, type(None))
        ), "Score must be a number or None!"
        assert not isinstance(score, bool), "Score must not be a boolean"
        self._last_score = score
        self._no_score_set = False

    def take(self):
        """
        Retrieve the last stored score of ML training.

        Returns
        -------
        int, float, or None
            The last stored score.
        """
        if self._no_score_set:
            msg = "No score has been set yet! "
            raise ValueError(msg)
        return self._last_score

    def clear(self):
        """
        Clear the last stored score, resetting it to None.
        """
        self._last_score = None
        self._no_score_set = True
