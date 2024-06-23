import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# Database configuration
db_config = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'port': '3306',
    'database': 'phonepe_pulse'
}

def fetch_data():
    # Construct database connection URL
    db_url = f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

    # Create SQLAlchemy engine
    engine = create_engine(db_url)

    # Execute SQL query and return DataFrame
    query = "SELECT * FROM pulse_data"
    data = pd.read_sql(query, engine)

    return data

def main():
    st.title('PhonePe Pulse Data Visualization Dashboard')

    # Fetch data
    data = fetch_data()

    if data.empty:
        st.write('No data available. Please ensure that the database is populated.')
        return

    st.write('Data loaded successfully')

    # Display dropdown for selecting metric
    metrics = data['metric_name'].unique()
    selected_metric = st.selectbox('Select a metric to display', metrics)

    # Filter data based on selected metric
    filtered_data = data[data['metric_name'] == selected_metric]

    if filtered_data.empty:
        st.write('No data available for the selected metric. Please choose another metric.')
        return

    # Display data visualization
    st.write('Data visualization:')
    fig = px.scatter_geo(
        filtered_data,
        lat='latitude',
        lon='longitude',
        color='metric_value',
        hover_name='metric_name',
        size='metric_value',
        projection='natural earth'
    )
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
