# import streamlit as st
# import pandas as pd
# from joblib import load 
# import os
# import numpy as np

# # from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm
# import pandas as pd
# import streamlit as st

# from sklearn.model_selection import train_test_split

# from lime import lime_tabular


# @st.cache(allow_output_mutation=True)
# def model_load():
#     loaded_models= load('gb_model_info (1).pkl')
#     return loaded_models



# def predict_model(data):
#     return {'prediction': [1], 'probability': [0.9]}  # Static return for testing


    
# # Create a button to download the model
# def download_objects(model_path):
    
#     with open(model_path, "rb") as f:
#         model_bytes = f.read()
#     st.sidebar.download_button(
#         label="Click to download",
#         data=model_bytes,
#         file_name=os.path.basename(model_path),
#         mime="application/octet-stream"
#     )
    
#     # Categorization function
# def model_category_using_y_preds(prediction):
#     if prediction > 60:
#         return 'High Demand'
#     else:
#         return 'Low Demand'
    

# def predict_fn(x):
#     loaded_models = model_load()
#     for model, result in zip(loaded_models):
#         if result['model_name']== 'XGBoosting':
#             model = model.predict_proba(x)
#     return model
