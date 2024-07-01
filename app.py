# Start by importing the relevant libraries and classes.
import streamlit as st
import pickle
import pandas as pd
import numpy as np
import xgboost
from xgboost import XGBRegressor

# Import the ML model pipeline created under model_deployment.
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Define a list containing all team values.
teams = ['Australia',
         'India',
         'Bangladesh',
         'New Zealand',
         'South Africa',
         'England',
         'West Indies',
         'Afghanistan',
         'Pakistan',
         'Sri Lanka']

# Define a list of all possible venues.
cities = ['Colombo',
          'Mirpur',
          'Johannesburg',
          'Dubai',
          'Auckland',
          'Cape Town',
          'London',
          'Pallekele',
          'Barbados',
          'Sydney',
          'Melbourne',
          'Durban',
          'St Lucia',
          'Wellington',
          'Lauderhill',
          'Hamilton',
          'Centurion',
          'Manchester',
          'Abu Dhabi',
          'Mumbai',
          'Nottingham',
          'Southampton',
          'Mount Maunganui',
          'Chittagong',
          'Kolkata',
          'Lahore',
          'Delhi',
          'Nagpur',
          'Chandigarh',
          'Adelaide',
          'Bangalore',
          'St Kitts',
          'Cardiff',
          'Christchurch',
          'Trinidad']

# Define a title for the webapp.
st.title('T20 Cricket Score Predictor')

# We first design drop down list for team selection.
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

# Selection of Venue.
city = st.selectbox('Select city', sorted(cities))

# Input of current score, overs done, wickets out.
col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score', format="%d")
with col4:
    overs = st.number_input('Overs', min_value=5, max_value=20)
with col5:
    wickets = st.number_input('Wickets', min_value=0, max_value=10)

# Last five overs runs scored.
last_five = st.number_input('Runs scored in the last 5 overs', format="%d")

# Now we program the Predict Score button to use our trained model.
if st.button('Predict Score'):
    # Computation for entry to the model.
    balls_left = 120 - (overs*6)
    wickets_left = 10 - wickets
    crr = current_score/overs

    # Define a DataFrame for the input.
    input_df = pd.DataFrame({'batting_team': [batting_team],
                             'bowling_team': [bowling_team],
                             'city': [city],
                             'current_score': [current_score],
                             'balls_left': [balls_left],
                             'wickets_left': [wickets_left],
                             'crr': [crr],
                             'last_five': [last_five]})

    # Use the model to make a prediction on the input
    result = pipe.predict(input_df)

    # Output the predicted score.
    st.header("Predicted Score - " + str(int(result[0])))
