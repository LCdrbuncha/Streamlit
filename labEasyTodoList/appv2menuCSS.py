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
    st.write("""
    โปรแกรมตัวอย่างสำหรับฝึก

    - Function
    - CRUD
    - Session State
    - Streamlit
    """)





# -----------------------------
# Add Task
# -----------------------------
def add_task():
    st.header("➕ Add Task")

    task = st.text_input("Task Name")

    status = st.selectbox(
        "Status",
        ["Pending", "Done"]
    )

    if st.button("Save"):

        if task.strip() == "":
            st.warning("Please enter task")
            return

        st.session_state.tasks.append({
            "Task": task,
            "Status": status
        })

        st.success("Add Success")








# -----------------------------
# Show Tasks
# -----------------------------
def show_tasks():
    st.header("📄 Task List")
    if len(st.session_state.tasks) == 0:
        st.info("No Data")
        return

    df = pd.DataFrame(st.session_state.tasks)

    df.index = df.index + 1
    df.index.name = "ID"

    st.dataframe(
        df,
        use_container_width=True
    )


# -----------------------------
# Delete Task
# -----------------------------
def delete_task():
    st.header("🗑 Delete Task")

    if len(st.session_state.tasks) == 0:
        st.info("No Data")
        return

    options = [
        f"{i+1}. {t['Task']} ({t['Status']})"
        for i, t in enumerate(st.session_state.tasks)
    ]

    index = st.selectbox(
        "Select Task",
        range(len(options)),
        format_func=lambda x: options[x]
    )

    if st.button("Delete"):

        st.session_state.tasks.pop(index)

        st.success("Delete Success")
        st.rerun()




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