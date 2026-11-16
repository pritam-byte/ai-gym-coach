import streamlit as st
import textwrap
from services.persistence.exercise_repository import get_or_create_user


def render_login_wall():
    if st.session_state.get("username") is not None:
        return True

    # Check if username was passed from the Front Page (index.html) via URL query params
    query_params = getattr(st, "query_params", None)
    if query_params is not None and "username" in query_params:
        param_user = query_params.get("username")
        if param_user and str(param_user).strip():
            user = get_or_create_user(str(param_user).strip())
            st.session_state["user_id"] = user["id"]
            st.session_state["username"] = user["username"]
            st.rerun()

    # Match the front page luxury dark typography & layout using st.html (never treated as code)
    hero_html = """<div style="text-align: center; margin-top: 15px; margin-bottom: 24px;">
<div style="display: inline-block; padding: 4px 14px; background: rgba(245,166,35,0.08); border: 1px solid rgba(245,166,35,0.3); font-size: 11px; letter-spacing: 0.16em; color: #f5a623; margin-bottom: 20px;">// AI-POWERED · REAL-TIME · GYM COACH</div>
<h1 style="font-family: 'Instrument Serif', Georgia, serif; font-size: clamp(60px, 9vw, 96px); line-height: 0.88; margin: 0 0 18px 0; letter-spacing: 0.02em; font-weight: 400;"><span style="background: linear-gradient(135deg, #ffffff 25%, #f5a623 65%, #00d4ff 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">AI GYM<br/>COACH</span></h1>
<p style="color: #888888; font-size: 15px; max-width: 520px; margin: 0 auto 28px auto; line-height: 1.7; font-weight: 300;">Your form. Analyzed. Corrected. In milliseconds.<br/>Computer vision that watches every rep and tells you exactly what to fix.</p>
<div style="display: flex; justify-content: center; align-items: center; max-width: 540px; margin: 0 auto 32px auto; border: 1px solid rgba(255,255,255,0.08); background: rgba(255,255,255,0.02);">
<div style="flex: 1; padding: 16px 12px; text-align: center;"><div style="font-family: 'Instrument Serif', serif; font-size: 32px; color: #fff; line-height: 1;">100<span style="font-size: 13px; color: #f5a623;">ms</span></div><div style="font-size: 10px; color: #666; letter-spacing: 0.1em; text-transform: uppercase; margin-top: 4px;">Avg Latency</div></div>
<div style="width: 1px; height: 36px; background: rgba(255,255,255,0.08);"></div>
<div style="flex: 1; padding: 16px 12px; text-align: center;"><div style="font-family: 'Instrument Serif', serif; font-size: 32px; color: #fff; line-height: 1;">5<span style="font-size: 13px; color: #f5a623;">+</span></div><div style="font-size: 10px; color: #666; letter-spacing: 0.1em; text-transform: uppercase; margin-top: 4px;">Exercises</div></div>
<div style="width: 1px; height: 36px; background: rgba(255,255,255,0.08);"></div>
<div style="flex: 1; padding: 16px 12px; text-align: center;"><div style="font-family: 'Instrument Serif', serif; font-size: 32px; color: #fff; line-height: 1;">95<span style="font-size: 13px; color: #00d4ff;">%</span></div><div style="font-size: 10px; color: #666; letter-spacing: 0.1em; text-transform: uppercase; margin-top: 4px;">Form Accuracy</div></div>
</div>
</div>"""

    if hasattr(st, "html"):
        st.html(hero_html)
    else:
        st.markdown(hero_html, unsafe_allow_html=True)

    with st.form("login_form"):
        username = st.text_input(
            "Athlete Identification",
            placeholder="Enter unique name (e.g. Pritam)",
            help="Your workouts, sets, and rep logs will be saved to your local database under this name."
        )
        submit_button = st.form_submit_button("TRY IT LIVE →", width="stretch")

    if submit_button:
        if not username.strip():
            st.error("Please enter your name to proceed.")
            return False

        user = get_or_create_user(username.strip())
        st.session_state["user_id"] = user["id"]
        st.session_state["username"] = user["username"]
        st.rerun()

    return False
