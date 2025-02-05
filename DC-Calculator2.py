import streamlit as st
import pandas as pd

def calculate_credits(usage):
    # Define multipliers
    multipliers = {
        "Batch Data Pipeline": 2000,
        "Batch Data Transforms": 400,
        "Unstructured Data Processed": 60,
        "Streaming Data Pipeline": 5000,
        "Streaming Data Transforms": 5000,
        "Data Federation": 70,
        "Real-Time Profile API": 900,
        "Batch Profile Unification": 100000,
        "Sub-second Real-Time Events": 70000,
        "Batch Calculated Insights": 15,
        "Streaming Calculated Insights": 800,
        "Inferences": 3500,
        "Data Share Rows Shared": 800,
        "Data Queries": 2,
        "Accelerated Data Queries": 2,
        "Streaming Actions": 800,
        "Segment Rows Processed": 20,
        "Batch Activation": 10
    }
    
    # Calculate credit usage
    credit_usage = {k: usage[k] * multipliers[k] for k in multipliers}
    total_service_credits = sum(credit_usage[k] for k in multipliers if k not in ["Segment Rows Processed", "Batch Activation"])
    total_segmentation_credits = sum(credit_usage[k] for k in ["Segment Rows Processed", "Batch Activation"])
    
    credit_df = pd.DataFrame.from_dict(credit_usage, orient='index', columns=['Credits Used'])
    credit_df["Credits Used"] = credit_df["Credits Used"].apply(lambda x: f"{x:,.0f}")  # Format as comma-separated integers
    
    return credit_df, total_service_credits, total_segmentation_credits

# Streamlit UI
st.title("Salesforce Data Cloud Credit Calculator")

st.write("Enter the number of records processed (in millions) for each category.")

usage = {}
for key in [
    "Batch Data Pipeline", "Batch Data Transforms", "Unstructured Data Processed",
    "Streaming Data Pipeline", "Streaming Data Transforms", "Data Federation", "Real-Time Profile API",
    "Batch Profile Unification", "Sub-second Real-Time Events", "Batch Calculated Insights",
    "Streaming Calculated Insights", "Inferences", "Data Share Rows Shared", "Data Queries",
    "Accelerated Data Queries", "Streaming Actions", "Segment Rows Processed", "Batch Activation"
]:
    usage[key] = st.number_input(f"{key} (in million rows)", min_value=0.0, step=0.1)

if st.button("Calculate Credits"):
    credit_df, total_service_credits, total_segmentation_credits = calculate_credits(usage)
    st.write("## Credit Usage Breakdown")
    st.dataframe(credit_df)
    st.write(f"### Total Service Credits Used: {total_service_credits:,.0f}")
    st.write(f"### Total Segmentation & Activation Credits Used: {total_segmentation_credits:,.0f}")
