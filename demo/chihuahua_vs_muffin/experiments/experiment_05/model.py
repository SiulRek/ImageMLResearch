import tensorflow as tf

def make_model(hyperparameters):
    """
    Creates and compiles a model using a pretrained MobileNetV2 base with
    custom dense layers on top.

    Args:
        - hyperparameters (dict): A dictionary containing model hyperparameters.

    Returns:
        - model: A compiled tf.keras model.
    """
    # Load the pretrained MobileNetV2 model without the top layer
    base_model = tf.keras.applications.MobileNetV2(
        input_shape=(128, 128, 3),
        include_top=False,
        weights="imagenet"
    )
    
    # Freeze the base model to prevent its weights from being updated during training
    base_model.trainable = False

    # Build the new model on top of the pretrained base
    model = tf.keras.models.Sequential([
        base_model,
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(hyperparameters["dense_units"], activation="relu"),
        tf.keras.layers.Dropout(hyperparameters["dropout_rate"]),
        tf.keras.layers.Dense(2, activation="softmax")
    ])

    # Compile the model
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=hyperparameters["learning_rate"]),
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )
    
    return model
