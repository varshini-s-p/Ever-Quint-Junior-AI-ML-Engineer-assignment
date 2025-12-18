import streamlit as st
from max_profit_logic import max_profit

st.set_page_config(page_title="Max Profit Optimizer")

st.title("Max Profit Property Planner")
st.write("Find the optimal mix of properties for maximum earnings.")

n = st.number_input(
    "Enter total available time units (n):",
    min_value=1,
    step=1
)

if st.button("Compute Optimal Mix"):
    result, earnings = max_profit(n)

    st.subheader("Optimal Mix")
    st.write(f"Theatre (T): {result['T']}")
    st.write(f"Pub (P): {result['P']}")
    st.write(f"Commercial Park (C): {result['C']}")

    st.subheader("Total Earnings")
    st.success(f"${earnings}")
