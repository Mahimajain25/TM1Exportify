import streamlit as st
from export_list_of_objects import export_list_of_objects
from export_dimension import export_dimension_with_elements_and_attributes
from export_cubes import export_cubes_with_dimensions
from utils import get_tm1_service  # Import get_tm1_service from utils.py
import configparser

# Read configuration file
#config = configparser.ConfigParser()
#config.read('config.ini')

# Use st.cache_resource to cache the TM1 connection
@st.cache_resource
def get_tm1_service_cached():
    return get_tm1_service()  # Get the TM1 service from utils.py

# Connect to TM1 (cached)
tm1 = get_tm1_service_cached()

# Sidebar for radio buttons to navigate between pages
st.sidebar.title("Navigation")
page = st.sidebar.radio("", ["Export Objects", "Export Dimension with Elements & Attributes", "Export Cubes with Dimensions"])

# Display the selected page
if page == "Export Objects":
    export_list_of_objects(tm1)
elif page == "Export Dimension with Elements & Attributes":
    export_dimension_with_elements_and_attributes(tm1)
elif page == "Export Cubes with Dimensions":
    export_cubes_with_dimensions(tm1)
