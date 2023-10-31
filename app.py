import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Title
st.title('Weight Goal Setter App')

#Sub Header
st.subheader("Hi.I'm Huslen and this is my app :wave:")
st.write("soooooo")

# Sidebar
st.sidebar.header('User Input')
user_weight = st.sidebar.number_input('Enter your weight (in kg)', min_value=1.0, max_value=500.0, value=70.0)
target_weight = st.sidebar.number_input('Set your target weight (in kg)', min_value=1.0, max_value=500.0, value=65.0)

# Weight history
st.header('Weight Tracking')
weight_data = st.text_area('Enter your weight data (comma-separated, e.g., 70,69,68)', '')

if weight_data:
    weight_list = [float(weight) for weight in weight_data.split(',')]
    weight_list.append(user_weight)  # Add the most recent weight

    # Create a DataFrame to store weight data
    df = pd.DataFrame({'Date': range(1, len(weight_list) + 1), 'Weight': weight_list})

    # Line chart for weight tracking
    st.line_chart(df.set_index('Date'))

    # Progress visualization
    progress = (user_weight - target_weight) / (weight_list[0] - target_weight)
    if progress > 0:
        st.success(f'You have made {progress*100:.2f}% progress towards your weight goal!')
    else:
        st.warning(f'You are {abs(progress*100):.2f}% away from your weight goal.')

# Goal progress
st.header('Weight Goal Progress')
if user_weight < target_weight:
    st.success('Congratulations! You have achieved your weight goal.')
else:
    st.warning('Keep working towards your weight goal.')

# App description
import streamlit as st

# Introduction
st.title("Welcome to the Weight Tracking App")
st.text("This is a simple tool to help you monitor your weight over time and work towards your weight goal. "
        "Whether you're aiming to lose, gain, or maintain your weight, this app can assist you in visualizing your progress.")

# How to Use
st.header("How to Use:")
st.text("1. **User Input**:")
st.text("   - On the left-hand side, you'll find a sidebar labeled 'User Input.' Here, you can set your weight-related parameters:")
st.text("     - **Current Weight**: Input your current weight (in kilograms) by typing it into the 'Enter your weight' field.")
st.text("     - **Target Weight**: Set your desired target weight by entering the value in the 'Set your target weight' field.")

st.text("2. **Weight Data Entry**:")
st.text("   - Below the 'User Input' section, you'll see a text area labeled 'Weight Tracking.' Here, you can input your weight data over time.")
st.text("   - Enter your weight readings, separated by commas, in chronological order. For example, if you have recorded your weight for three days, you can input it as '70, 69, 68,' with the most recent weight as the last entry.")

st.text("3. **Visualization**:")
st.text("   - Once you've entered your weight data, the app will generate a line chart that displays your weight changes over time. The x-axis represents the number of data points (1, 2, 3, ...) and the y-axis represents the corresponding weight values.")

st.text("4. **Goal Progress**:")
st.text("   - The app calculates and displays your progress toward your target weight goal.")
st.text("   - If your current weight is less than your target weight, you'll see a success message indicating that you've achieved your goal.")
st.text("   - If your current weight is higher than your target weight, you'll receive a warning to keep working toward your goal.")

st.text("Use this app to keep track of your weight, stay motivated, and achieve your weight goals. "
        "Remember that consistency and dedication are key to a healthier you!")


