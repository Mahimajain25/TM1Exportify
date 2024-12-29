import streamlit as st
import pandas as pd
from utils import write_to_excel,write_to_excel_multiple_sheets

# Function to export dimensions with elements and attributes
def export_dimension_with_elements_and_attributes(tm1):
    st.markdown("""   
        <h1 style='text-align: center; font-family: Arial;'>
        <span style='color: #FFD700;'>Tm1</span><span style='color: #4682B4;'>Exportify</span>
        </h1>
        """, unsafe_allow_html=True)
     
    st.title("Export Dimension with Elements & Attributes")

    options = ['All Dimension with Attributes', 'All Dimension with Attributes Data']
    selected_option = st.selectbox('Select below options', options)
    
    if selected_option:
        st.write(f"Current selection is: {selected_option}")
        
        # Export "All Dimension with Attributes"
        if selected_option == "All Dimension with Attributes":
            if st.button("Export"):
                rows = []
                for dimension in tm1.dimensions.get_all_names():
                    for hierarchy in tm1.dimensions.hierarchies.get_all_names(dimension):
                        level_count = tm1.dimensions.hierarchies.elements.get_levels_count(dimension, hierarchy)
                        
                        elements_by_level = {}
                        for level in range(level_count):
                            elements_by_level[level] = tm1.dimensions.hierarchies.elements.get_elements_by_level(dimension, hierarchy, level)

                        edges = tm1.dimensions.hierarchies.elements.get_edges(dimension, hierarchy)
                        attributes = tm1.dimensions.hierarchies.elements.get_element_attributes(dimension, hierarchy)
                        
                        row = [dimension]
                        row.append(attributes if attributes else None)
                        row.append(edges if edges else None)
                        
                        for level in range(level_count):
                            elements = elements_by_level.get(level, [])
                            row.append(elements if elements else None)
                            
                        rows.append(row)

                columns = ['Dimension', 'Attributes', 'Edges']
                max_levels = max(
                    tm1.dimensions.hierarchies.elements.get_levels_count(dimension, hierarchy)
                    for dimension in tm1.dimensions.get_all_names()
                    for hierarchy in tm1.dimensions.hierarchies.get_all_names(dimension)
                )
                for level in range(max_levels):
                    columns.append(f'Level {level}')

                df = pd.DataFrame(rows, columns=columns)
                write_to_excel('All Dimension with Attributes.xlsx', df)
                st.success("All Dimension with Attributes exported successfully")
        
        # Export "All Dimension with Attributes Data"
        elif selected_option == "All Dimension with Attributes Data":
            if st.button("Export"):
                sheet_data = {}
                for dimension in tm1.dimensions.get_all_names():
                    for hierarchy in tm1.dimensions.hierarchies.get_all_names(dimension):
                        if tm1.dimensions.hierarchies.elements.attribute_cube_exists(dimension):
                            df = tm1.dimensions.hierarchies.elements.get_elements_dataframe(dimension, hierarchy)
                            sheet_name = f"{dimension}_{hierarchy}"
                            sheet_data[sheet_name] = df
                write_to_excel_multiple_sheets('All Dimension with Attributes Data.xlsx', sheet_data)
                st.success("All Dimension with Attributes Data exported successfully")
