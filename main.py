import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
import requests

# List of Time Zones
TIME_ZONE = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]
# Streamlit Title
st.title("Time Zone App")

# Select Time Zones
selected_timezone = st.multiselect("Select Timezones", TIME_ZONE, default=['Asia/Karachi'])

# Display the selected timezones and current time for each
st.subheader("Selected Timezones")
for tz in selected_timezone:
    # get  and format current time for each selected timezone with AM and PM
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**{tz}**: {current_time}")



# Time Conversion Section
st.subheader("Convert time between timezones")
current_time = st.time_input("Current Time", value=datetime.now().time())
from_tz = st.selectbox("From Timezone", TIME_ZONE, index=0)
to_tz = st.selectbox("To timezone", TIME_ZONE, index=1)

if st.button(" convert timezone"):
# Perform the conversion                         
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")

# Display converted time
    st.success(f"Converted Time in {to_tz}: {converted_time}")
