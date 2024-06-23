# PhonePe Pulse Data Visualization and Exploration

## Project Overview
This project visualizes PhonePe Pulse data using Streamlit and Plotly. It extracts data from the PhonePe Pulse GitHub repository, transforms it, stores it in a MySQL database, and displays it on an interactive dashboard.

## Technologies Used
- Python
- Pandas
- MySQL
- mysql-connector-python
- Streamlit
- Plotly
- GitPython

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone <your-repo-url>
    cd PhonePe_Pulse_Dashboard
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Clone the PhonePe Pulse GitHub repository and extract data:
    ```bash
    python data_extraction.py
    ```

4. Transform the data:
    ```bash
    python data_transformation.py
    ```

5. Insert the data into the MySQL database:
    ```bash
    python database_insertion.py
    ```

6. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage
- Open the Streamlit app in your browser.
- Use the dropdown menu to select different metrics and visualize the data on the map.
