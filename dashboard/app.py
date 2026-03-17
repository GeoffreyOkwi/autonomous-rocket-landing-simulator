import streamlit as st
import pandas as pd
import subprocess
import os
import time
import matplotlib.pyplot as plt
import sys

# -------------------------
# Add project root to path
# -------------------------

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from config.settings import PLANET_GRAVITY, DEFAULT_PLANET

# -------------------------
# Project paths
# -------------------------

exe_path = os.path.join(
    project_root,
    "cmake-build-debug",
    "rocket_sim.exe"
)

telemetry_path = os.path.join(
    project_root,
    "telemetry.csv"
)

# -------------------------
# Dashboard title
# -------------------------

st.title("🚀 AI Controlled Rocket Landing Simulator")

# -------------------------
# Planet Selection
# -------------------------

planet = st.sidebar.selectbox(
    "Select Planet",
    list(PLANET_GRAVITY.keys()),
    index=list(PLANET_GRAVITY.keys()).index(DEFAULT_PLANET))


gravity = PLANET_GRAVITY[planet]

st.sidebar.metric(
    label="Surface Gravity (m/s²)",
    value=f"{gravity:.2f}"
)

#if st.button("Run Simulation"):
   # subprocess.run(
      #  [exe_path, str(gravity)],
      #  cwd=os.path.dirname(exe_path)
  #  )


# -------------------------
# Mission Summary
# -------------------------

st.subheader("🛰 Mission Summary")

summary_col1, summary_col2, summary_col3, summary_col4 = st.columns(4)

if os.path.exists(telemetry_path):

    df_summary = pd.read_csv(telemetry_path)

    final_velocity = df_summary["velocity"].iloc[-1]
    final_fuel = df_summary["fuel"].iloc[-1]

    if abs(final_velocity) < 3:
        status = "SAFE LANDING"
    else:
        status = "HARD LANDING"

    summary_col1.metric("Planet", planet)
    summary_col2.metric("Landing Velocity (m/s)", f"{final_velocity:.2f}")
    summary_col3.metric("Fuel Remaining", f"{final_fuel:.1f}")
    summary_col4.metric("Status", status)

else:

    summary_col1.metric("Planet", planet)
    summary_col2.metric("Landing Velocity", "N/A")
    summary_col3.metric("Fuel Remaining", "N/A")
    summary_col4.metric("Status", "Run Simulation")


st.subheader("📊 Telemetry")

if os.path.exists(telemetry_path):

    df = pd.read_csv(telemetry_path).tail(400)
    df = df.set_index("time")

    st.write("Velocity(m/s) vs Time (s)")
    st.line_chart(df[["velocity"]])

    st.write("Throttle vs Time")
    st.line_chart(df[["throttle"]])



    df = None

# -------------------------
# Load Telemetry
# -------------------------

if os.path.exists(telemetry_path):

    df_full = pd.read_csv(telemetry_path)

    # Sample across the whole flight
    sample_step = max(len(df_full) // 2000, 1)

    df = df_full.iloc[::sample_step]

    st.subheader("🚀 Rocket Telemetry")

    # Altitude vs Time
    st.markdown("**Altitude(m) vs Time (s)**")
    st.line_chart(df.set_index("time")[["altitude"]])

    # Velocity vs Time
    st.markdown("**Velocity(m/s) vs Time (s)**")
    st.line_chart(df.set_index("time")[["velocity"]])

    # Fuel vs Time
    st.markdown("**Fuel(kg) vs Time (s)**")
    st.line_chart(df.set_index("time")[["fuel"]])

    # -------------------------
# Load Telemetry
# -------------------------

if os.path.exists(telemetry_path):

    df_full = pd.read_csv(telemetry_path)

    # Sample across the whole flight
    sample_step = max(len(df_full) // 2000, 1)

    df = df_full.iloc[::sample_step]

    st.markdown("**Altitude vs Fuel Consumption**")

    df_af = df_full[df_full["fuel"] > 0]

    if len(df_af) > 0:

     fig, ax = plt.subplots()

     ax.plot(df_af["fuel"], df_af["altitude"])

    # Reverse fuel axis so it shows 1000 → 0
     ax.set_xlim(1000, 0)

     ax.set_xlabel("Fuel (kg)")
     ax.set_ylabel("Altitude (m)")
     ax.set_title("Rocket Descent: Altitude vs Fuel")

     st.pyplot(fig)


    # Final descent speed
    velocity = df_full["velocity"].iloc[-1]

    st.metric(
        label="🚀 Final Descent Speed (m/s)",
        value=f"{velocity:.2f}"
    )

    # Only ONE telemetry table
    st.subheader("📡 Latest Telemetry (Last 10 Rows)")
    st.dataframe(df_full.tail(10))