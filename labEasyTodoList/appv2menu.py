import streamlit as st
import pandas as pd

# -----------------------------
# Initial Data
# -----------------------------
def init_data():
    if "tasks" not in st.session_state:
        st.session_state.tasks = []


# -----------------------------
# Home Page
# -----------------------------
def home_page():
    st.header("🏠 Welcome")

# -----------------------------
# Add Task
# -----------------------------
def add_task():
    st.header("➕ Add Task")

# -----------------------------
# Show Tasks
# -----------------------------
def show_tasks():
    st.header("📄 Task List")

# -----------------------------
# Delete Task
# -----------------------------
def delete_task():
    st.header("🗑 Delete Task")





# -----------------------------
# Main Program
# -----------------------------
def main():

    st.set_page_config(
        page_title="Student Task Manager",
        page_icon="📋",
        layout="wide"
    )

    init_data()

    st.title("📋 Student Task Manager")

    menu = st.sidebar.selectbox(
        "📋 Menu",
        [
            "🏠 Home",
            "➕ Add Task",
            "📄 Show Tasks",
            "🗑 Delete Task"
        ]
    )

    if menu == "🏠 Home":
        home_page()

    elif menu == "➕ Add Task":
        add_task()

    elif menu == "📄 Show Tasks":
        show_tasks()

    elif menu == "🗑 Delete Task":
        delete_task()


# -----------------------------
# Start Program
# -----------------------------
if __name__ == "__main__":
    main()


# =====================================================
# DEBUG (ใช้สอน)
# =====================================================

with st.expander("📦 Session State (สำหรับการเรียนรู้)"):

    st.write(st.session_state)