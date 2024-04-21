import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from data import *

# Set page config
st.set_page_config(page_title="Depot Demand Predictions", page_icon="🚚", layout="wide")

# Function to make predictions based on input features
def make_prediction(drivers, pickups_per_day, inventory_level, depot, quantity_delivered, distance_from_depot, number_of_stations, discounts, demand):
    # This is just a placeholder for demonstration purposes
    predicted_demand = np.random.randint(100, 1000)  # Replace this with your actual prediction logic
    return predicted_demand

# Sidebar for navigation
with st.sidebar:
    from streamlit_option_menu import option_menu
    selected = option_menu(None, ["Home", "Prediction"], 
        icons=['house', 'bar-chart-line'], 
        menu_icon="cast", default_index=0, orientation="vertical",
        styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},
        })

if selected == "Home":
    st.title('Welcome to Depot Demand Predictions')
    st.markdown("""
        Use this tool to predict daily demand at different depots based on various input features. 
        Navigate to the **Prediction** tab to input data and see predictions.
    """)

elif selected == "Prediction":
    st.title('Depot Demand Prediction')
    with st.form("prediction_form"):
        st.subheader('Input Features for Demand Prediction')
        col1, col2, col3 = st.columns(3)
        
        with col1:
            drivers = st.number_input('Number of Drivers', min_value=0)
            pickups_per_day = st.number_input('Number of Pickups per Day', min_value=0)
            inventory_level = st.number_input('Inventory Level', min_value=0)
        
        with col2:
            depot = st.selectbox('Depot', ['Depot A', 'Depot B'])
            quantity_delivered = st.number_input('Quantity Delivered (m3)', min_value=0.0, step=0.1)
            distance_from_depot = st.number_input('Distance from Depot (km)', min_value=0.0, step=0.1)
        
        with col3:
            number_of_stations = st.number_input('Number of Stations', min_value=0)
            discounts = st.number_input('Discounts', min_value=0)
            demand = st.number_input('Demand', min_value=0)

        submitted = st.form_submit_button('Predict Demand')

    if submitted:
        # Check if all parameters have been entered
        if not all([drivers, pickups_per_day, inventory_level, quantity_delivered, distance_from_depot, number_of_stations, discounts, demand]):
            st.warning('Please fill all the fields to make a prediction.')
        else:
            # Create a DataFrame for the model input
            input_df = pd.DataFrame([{
                'drivers': drivers,
                'pickups_per_day': pickups_per_day,
                'inventory_level': inventory_level,
                'depot': depot,
                'quantity_delivered': quantity_delivered,
                'distance_from_depot': distance_from_depot,
                'number_of_stations': number_of_stations,
                'discounts': discounts,
                'demand': demand
            }])

 ## Predictions
            
# st.write(predict_model(data))
# st.markdown("#### Predictions Results")
# col11, col12, col13 = st.columns(3)

# predict_results = predict_model(data)

# # Assuming the predict_model function returns predictions for different models
# for i, (model_name, result) in enumerate(predict_results.items()):
#     if i == 0:
#         col = col11
#     elif i == 1:
#         col = col12
#     else:
#         col = col13

#     col.warning(model_name)
#     # Assuming model_category_using_y_preds is a function to categorize predictions
#     col.success(model_category_using_y_preds(result['prediction'][0]))
#     col.markdown(':grey[Probability of Demand] ')
#     col.info(round((result['probability']) * 100, 2))