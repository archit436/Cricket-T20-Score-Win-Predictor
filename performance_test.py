# This file will serve to test the performance of the model over the course of multiple T20 World Cup 2024 matches.
# The model will be tested on the basis of the accuracy of its predictions and the overall performance of the model.

# Stary by importing the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

# Load the model
pipe1 = pickle.load(open('pipe_first_innings.pkl', 'rb'))
pipe2 = pickle.load(open('pipe_second_innings.pkl', 'rb'))

# Load the dataset