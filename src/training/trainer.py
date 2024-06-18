from src.research.classes.research_attributes import (
    ResearchAttributes,
    insert_research_attributes,
)


class Trainer(ResearchAttributes):
    """ A class to train a Keras model using datasets from research_attributes. """

    def __init__(self, research_attributes):
        """
        Initializes the Trainer with a ResearchAttributes instance.

        Args:
            - research_attributes (ResearchAttributes): The
                ResearchAttributes instance.
        """
        self._model = None
        self._training_history = None
        self._predictions_container = {}
        self._dataset_container = {}
        insert_research_attributes(self, research_attributes)

    def set_compiled_model(self, model):
        """
        Sets the compiled Keras model for training.

        Args:
            - model (tf.keras.Model): Compiled Keras model.
        """
        self._model = model

    def fit_predict_evaluate(self, **kwargs):
        """
        Fits the model to the dataset, saves the training history, calculates
        predictions, and evaluates the model.

        Args:
            - **kwargs: Keyword arguments for the Keras model's fit method.
        """
        if self.model is None:
            msg = "A compiled model must be set before calling fit."
            raise ValueError(msg)

        train_dataset = self._dataset_container.get("train_dataset")
        val_dataset = self._dataset_container.get("val_dataset")
        complete_dataset = self._dataset_container.get("complete_dataset")
        test_dataset = self._dataset_container.get("test_dataset")

        if val_dataset:
            kwargs["validation_data"] = val_dataset  # Add to fit kwargs.

        if train_dataset:
            self._training_history = self.model.fit(train_dataset, **kwargs)
        elif complete_dataset:
            self._training_history = self.model.fit(complete_dataset, **kwargs)
        else:
            msg = "Neither 'train_dataset' nor 'complete_dataset' found in dataset container."
            raise ValueError(msg)

        if train_dataset:
            self._predictions_container["train_predictions"] = self.model.predict(
                train_dataset
            )
        if val_dataset:
            self._predictions_container["val_predictions"] = self.model.predict(
                val_dataset
            )
        if complete_dataset:
            self._predictions_container["complete_predictions"] = self.model.predict(
                complete_dataset
            )
        if test_dataset:
            self._predictions_container["test_predictions"] = self.model.predict(
                test_dataset
            )

        self._evaluate()

    def _evaluate(self):
        # TODO:  Link to evaluating module here.
        msg = "Method not implemented yet."
        raise NotImplementedError(msg)
