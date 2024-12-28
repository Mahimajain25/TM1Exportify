import streamlit as st
from utils import write_to_csv

# Function to export cubes with their respective dimensions
def export_cubes_with_dimensions(tm1):
    st.title("Export All Cubes with its Dimensions")
    cubes_name = st.selectbox("List of all Cubes click Export button to download", tm1.cubes.get_all_names())
    
    if st.button("Export"):
        data = [[cube.name, cube._dimensions] for cube in tm1.cubes.get_all()]
        write_to_csv('Cubes_with_Dimensions.csv', ['Cube Name', 'Dimension Name'], data)
        st.success("Cubes with their Dimensions exported to Cubes_with_Dimensions.csv")
