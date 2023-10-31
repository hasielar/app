import streamlit as st
import pandas as pd

# Title
st.title('Weight Tracking App')

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
st.text('This app allows you to set a weight goal and track your progress over time.')

# Instructions and how to use the app
st.header('Instructions:')
st.markdown('1. Use the sidebar to enter your current weight and set your target weight goal.')
st.markdown('2. In the "Weight Tracking" section, input your weight data over time, separated by commas.')
st.markdown('3. Observe the line chart that displays your weight history and see your progress.')
st.markdown('4. Check the "Weight Goal Progress" section to see if you have achieved your goal.')

# Tips
st.markdown('Tips:')
st.markdown('- Consistency is key to achieving your weight goal.')
st.markdown('- Monitor your progress and stay motivated.')

# Enjoy using the app!


