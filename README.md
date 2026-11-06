# 🏋️‍♂️ AI Real-Time Gym Coach (Multimodal Vision & Voice)

> **An intelligent, real-time fitness coach powered by Computer Vision and Generative AI. It tracks your workout form through your webcam, counts reps and sets, provides proactive spoken coaching cues, and permanently logs your workout history.**

---

## 📌 Project Overview

The **AI Real-Time Gym Coach** is a full-stack, multimodal fitness assistant designed to bring personal training to any browser without requiring wearable sensors or specialized hardware. 

By analyzing live video streams via **WebRTC**, the app uses **MediaPipe Pose Landmarker** to calculate 3D joint angles in real time, detecting form faults such as shallow squats, sagging hips in push-ups, or swinging during curls. An integrated **Groq-powered LLM Coach** dynamically generates concise, motivational voice feedback that is converted to speech (**gTTS**) and played aloud during your workout, while all workout performance metrics are saved to an **SQLite database**.

---

## 🚀 Key Features

* **Real-Time 33-Point Skeleton Tracking**: Ultra-fast body landmark estimation powered by Google MediaPipe's high-precision full pose model.
* **Biomechanic Form Evaluation**: Calculates real-time joint angles (knees, elbows, hips, torso) to assess depth, stability, arching, and alignment.
* **Proactive Spoken AI Coaching**: Detects incorrect form or completed sets and instantly delivers spoken cues through your speakers using Groq LLM + Text-to-Speech.
* **Low-Latency WebRTC Streaming**: Smooth live webcam video processing inside the browser using `streamlit-webrtc`.
* **5 Supported Compound & Isolation Exercises**:
  * 🦵 **Squats** (Knee angle, back angle, depth status)
  * 💪 **Push-ups** (Elbow angle, body alignment, hip sagging/piking)
  * 🏋️ **Biceps Curls** (Elbow angle, elbow drift, torso swing)
  * 🏋️‍♂️ **Shoulder Press** (Extension status, lower back arch)
  * 🏃 **Lunges** (Front knee angle, torso uprightness, balance offset)
* **Automated Workout History & Analytics**: Automatically records reps, sets, and active duration in a local SQLite database with daily aggregation tables.

---

## 🛠️ Tech Stack & Technologies Used

### 🖥️ Frontend & Interface
* **Streamlit (`1.54.0`)**: Powers the reactive web dashboard, sidebar exercise planning, and live state updates.
* **Custom CSS & Typography**: Modern dark-mode fitness UI styling.

### 👁️ Computer Vision & Video
* **Google MediaPipe (`0.10.14`)**: Extracts 33 3D body landmarks at high frame rates using `pose_landmarker_full.task`.
* **OpenCV (`opencv-python-headless`)**: Performs video frame transformation, color conversions, and on-screen metric overlay rendering.
* **Streamlit-WebRTC (`0.64.5`) & PyAV (`av`)**: Bridges real-time browser webcam streaming to Python with minimal latency.

### 🧠 Generative AI & Audio Feedback
* **Groq API**: High-speed LLM inference (`openai/gpt-oss-20b`) generating concise 10–15 word verbal coaching cues based on live biomechanical events.
* **gTTS (`2.5.3`)**: Converts AI coach text feedback into natural speech played automatically in the browser.

### 💾 Data & Persistence
* **SQLite3**: Lightweight, zero-config local relational database (`data.db`) storing user profiles and workout records.
* **Pandas (`2.2.3`)**: Aggregates exercise duration, reps, and sets grouped by workout date for progress tracking.

### ⚙️ Environment & Utilities
* **Python 3.11**: Primary runtime ensuring optimal binary wheel compatibility for MediaPipe and PyTorch/JAX ecosystems.
* **python-dotenv (`1.2.2`)**: Safe management of environment variables and API keys.

---

## 🏗️ Architecture Workflow

```
[Webcam Stream] 
       │
       ▼ (WebRTC SENDRECV)
[VideoProcessorClass] ──▶ [MediaPipe Pose Landmarker]
       │                                │
       ▼                                ▼
[Overlay Rendering]              [Joint Angle Math]
       │                                │
       ▼                                ▼
[Browser Display]           [Exercise Form Detector]
                                        │
                       ┌────────────────┴────────────────┐
                       ▼                                 ▼
            [SQLite Persistence]               [Voice Pipeline]
            - Reps & Sets saved                - Groq LLM Feedback
            - Workout time logged              - gTTS Audio Generation
            - History Table updated            - Auto-played in Browser
```

---

## 📂 Project Structure

```plaintext
AI-REALTIME-GYM-COACH-V2/
├── .streamlit/
│   └── config.toml             # Custom theme colors and configuration
├── core/
│   └── base_exercise.py        # Base abstract class for joint angle calculations
├── detectors/
│   ├── biceps_curl.py          # Biceps curl detector with swing & drift analysis
│   ├── lunges.py               # Lunge detector with balance & knee angle analysis
│   ├── pushup.py               # Push-up detector with hip sag & alignment checks
│   ├── shoulder_press.py       # Shoulder press detector with back arch tracking
│   └── squat.py                # Squat detector with depth & back angle checks
├── ml_models/
│   └── pose_landmarker_full.task # Official MediaPipe 33-point pose model
├── services/
│   ├── auth/login_wall.py      # User authentication & session management
│   ├── coaching/
│   │   ├── llm.py              # Groq LLM integration & prompt engineering
│   │   ├── tts.py              # Google Text-to-Speech audio synthesizer
│   │   └── voice_pipeline.py   # Event dispatcher connecting form flaws to audio
│   ├── config/workout_config.py# Thresholds, connection points & system prompts
│   ├── persistence/
│   │   └── exercise_repository.py # SQLite database connector & history queries
│   ├── state/session_defaults.py  # Streamlit session state initialization
│   ├── tracking/metrics.py     # Real-time state synchronizer between camera & UI
│   ├── ui/style_loader.py      # CSS injector and style manager
│   └── vision/
│       └── exercise_video_processor.py # WebRTC frame processor & annotation
├── static/
│   └── style.css               # Modern dark-mode stylesheet
├── .env.example                # Template for environment variables
├── data.db                     # Local SQLite database (auto-generated)
├── main.py                     # Primary Streamlit application entry point
├── requirements.txt            # Python dependencies
├── run.bat                     # Quick launcher for Windows Command Prompt
└── run.ps1                     # Quick launcher for Windows PowerShell
```

---

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/AI-REALTIME-GYM-COACH-V2.git
cd AI-REALTIME-GYM-COACH-V2
```

### 2. Set Up Environment
Create your virtual environment with **Python 3.11**:
```powershell
py -3.11 -m venv .venv311
.\.venv311\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 3. Add API Keys
Copy `.env.example` to `.env` and add your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run the Application
```powershell
.\run.bat
```
or
```powershell
streamlit run main.py
```
Open **`http://localhost:8501`** in your browser and start your workout!
