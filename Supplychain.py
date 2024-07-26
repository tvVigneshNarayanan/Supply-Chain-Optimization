import streamlit as st
import pandas as pd
import os
import sys

# Define file paths
files = {
    'Historical Costs': 'HistoricalCosts.csv',
    'Capacity Utilization': 'CapacityUtilization.csv',
    'Freight Costs': 'FreightCosts.csv',
    'Optimization Results': 'OptimizationResults.csv'
}

# Function to load data with error handling
def load_data(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        st.error(f"File not found: {file_path}")
        return pd.DataFrame()  # Return an empty DataFrame if file is not found

# Load datasets
historical_costs = load_data(files['Historical Costs'])
capacity_utilization = load_data(files['Capacity Utilization'])
freight_costs = load_data(files['Freight Costs'])
optimization_results = load_data(files['Optimization Results'])

# Title
st.title('Supply Chain Optimization Dashboard')

# Historical Costs
st.header('Historical Costs')
if not historical_costs.empty:
    st.dataframe(historical_costs)
else:
    st.write("No data available for Historical Costs.")

# Capacity Utilization
st.header('Capacity Utilization')
if not capacity_utilization.empty:
    st.dataframe(capacity_utilization)
else:
    st.write("No data available for Capacity Utilization.")

# Freight Costs
st.header('Freight Costs')
if not freight_costs.empty:
    st.dataframe(freight_costs)
else:
    st.write("No data available for Freight Costs.")

# Optimization Results
st.header('Optimization Results')
if not optimization_results.empty:
    st.dataframe(optimization_results)
else:
    st.write("No data available for Optimization Results.")
