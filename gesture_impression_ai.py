import streamlit as st
import cv2
from gesture_recognizer import detect_gesture_from_frame
from llm_sentiment import interpret_gesture_with_llm
import time

# Page config
st.set_page_config(page_title="Gesture Impression AI", layout="centered")
st.title("🖐️ Gesture Impression AI")
st.markdown("Show a hand gesture to your webcam, and the AI will interpret its meaning!")

# Session state
if "camera_running" not in st.session_state:
    st.session_state.camera_running = False

# Buttons to start/stop camera
col1, col2 = st.columns(2)
with col1:
    if not st.session_state.camera_running:
        if st.button("📷 Start Camera"):
            st.session_state.camera_running = True
with col2:
    if st.session_state.camera_running:
        if st.button("🛑 Stop Camera"):
            st.session_state.camera_running = False

# Placeholders
frame_placeholder = st.empty()
gesture_placeholder = st.empty()
result_placeholder = st.empty()

# Camera loop
if st.session_state.camera_running:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("🚫 Could not access webcam.")
        st.session_state.camera_running = False
    else:
        st.success("✅ Camera started. Show your hand gesture!")

        prev_gesture = None
        last_sent_time = 0

        while st.session_state.camera_running:
            ret, frame = cap.read()
            if not ret:
                st.error("❌ Failed to grab frame.")
                break

            frame = cv2.flip(frame, 1)

            # Detect and annotate gesture
            gesture, frame = detect_gesture_from_frame(frame)
            frame_placeholder.image(frame, channels="BGR")

            # Show detected gesture (only one line)
            gesture_placeholder.markdown(f"### 🧠 Detected Gesture: **{gesture}**")

            # Call LLM if gesture changed and valid
            if gesture != prev_gesture and gesture != "No Hand":
                if time.time() - last_sent_time > 3:
                    interpretation = interpret_gesture_with_llm(gesture)
                    result_placeholder.info(f"💬 AI Interpretation: {interpretation}")
                    prev_gesture = gesture
                    last_sent_time = time.time()

            time.sleep(0.1)

        cap.release()
        st.success("📷 Camera stopped.")
