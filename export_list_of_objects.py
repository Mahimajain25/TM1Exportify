import streamlit as st
from utils import write_to_csv

# Function to export list of objects (Dim, Cubes, Process)
def export_list_of_objects(tm1):
    st.markdown("""   
        <h1 style='text-align: center; font-family: Arial;'>
            <span style='color: #FFD700;'>Tm1</span><span style='color: #4682B4;'>Exportify</span>
            </h1>
        """, unsafe_allow_html=True)

    st.title("Export in Excel List of Objects")
    
    # Add selectbox 
    options = ["Dimension", "Cube", "Process"]  # You can add more options as needed
    selected_option = st.selectbox("Select an object from the dropdown", options)

    # Display export button only after an option is selected
    if selected_option:
        st.write(f"Current selection is: {selected_option}")
        
        # Export "Dimension" option
        if selected_option == "Dimension":
            if st.button("Export"):
                data = [[dimension] for dimension in tm1.dimensions.get_all_names()]
                write_to_csv('Dimensions.csv', ['Dimension'], data)
                st.success("Dimensions exported to Dimensions.csv")

        # Export "Cube" option
        elif selected_option == "Cube":
            if st.button("Export"):
                data = [[cube] for cube in tm1.cubes.get_all_names()]
                write_to_csv('Cubes.csv', ['Cube'], data)
                st.success("Cubes exported to Cubes.csv")

        # Export "Process" option
        elif selected_option == "Process":
            if st.button("Export"):
                data = [[process] for process in tm1.processes.get_all_names()]
                write_to_csv('Processes.csv', ['Process'], data)
                st.success("Processes exported to Processes.csv")
