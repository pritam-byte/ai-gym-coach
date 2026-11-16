import streamlit as st
from services.persistence.exercise_repository import get_or_create_user


def render_login_wall():
    if st.session_state.get("username") is not None:
        return True

    st.markdown(
        """
        <div style="text-align: center; margin-top: 40px; margin-bottom: 24px;">
            <div style="display: inline-block; padding: 4px 14px; background: rgba(245,166,35,0.1); border: 1px solid rgba(245,166,35,0.3); border-radius: 0px; font-size: 11px; letter-spacing: 0.16em; color: #f5a623; margin-bottom: 16px;">
                // AI-POWERED · REAL-TIME · GYM COACH
            </div>
            <h1 style="margin-bottom: 8px;">( AI GYM COACH )</h1>
            <p style="color: #888; font-size: 15px; max-width: 460px; margin: 0 auto; line-height: 1.6;">
                Computer vision pose estimation and proactive voice coaching. Enter your username to begin training.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("login_form"):
        username = st.text_input(
            "Username",
            placeholder="Enter unique name (e.g. Pritam)",
            help="Your past workout logs and rep records will be saved under this name."
        )
        submit_button = st.form_submit_button("Start Session ⚡", width="stretch")

    if submit_button:
        if not username.strip():
            st.error("Please enter a valid username.")
            return False

        user = get_or_create_user(username.strip())
        st.session_state["user_id"] = user["id"]
        st.session_state["username"] = user["username"]
        st.rerun()

    return False
