# Importing required libraries and functions
import model
from skills import *
from skills.functions import get_function
from model.training import TrainingModel

# Main function
if __name__ == '__main__':

    # Initializing data for training
    print("Model training started.")
    words = model.words
    classes = model.classes

    # Training model
    training_model = TrainingModel(words, classes, model.data_x, model.data_y)
    trained_model = training_model.train()
    print("Model training finished.")

    # Wish user according to current time
    wish()

    # Continous loop for AI to serve
    while True:

        # Getting voice command
        command = listen()

        # Check if command is not Empty
        if command != '':

            # Get predicted intent and response after processing command
            intent = training_model.get_intent(trained_model, command)
            response = TrainingModel.get_response(intent, model.data)
            print(f"Intent: {intent}")

            # Executing task of predicted intent 
            get_function(intent, command, response)

