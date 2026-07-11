import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# -----------------------------
# CSS Design
# -----------------------------
def load_css():

    st.markdown("""
    <style>
    /* Sidebar Background Image */
    section[data-testid="stSidebar"] {

        background-image: url(
        "https://images.unsplash.com/photo-1516321318423-f06f85e504b3"
        );

        background-size: cover;

        background-position: center;

    }


    /* ทำให้ข้อความ Sidebar อ่านง่าย */
    section[data-testid="stSidebar"] * {

        color: white;

    }

    /* หัวข้อหลัก */
    h1 {
        color: #1f77b4;
        text-align: center;
    }


    /* หัวข้อย่อย */
    h2 {
        color: #2e8b57;
    }


    /* ปุ่ม */
    .stButton button {

        background-color: #1f77b4;

        color: white;

        border-radius: 10px;

        height: 40px;

        font-size: 16px;

    }


    /* ตอนเอาเมาส์ชี้ปุ่ม */
    .stButton button:hover {

        background-color: #0b5394;

        color: yellow;

    }


    /* ช่องกรอกข้อมูล */
    .stTextInput input {

        border-radius: 10px;

    }


    /* Sidebar */
    section[data-testid="stSidebar"] {

        background-color: #eaf4ff;

    }


    /* ตาราง */
    div[data-testid="stDataFrame"] {

        border-radius: 10px;

    }


    </style>
    """,
    unsafe_allow_html=True)


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
# -----------------------------
# Add Task
# -----------------------------
def add_task():

    st.header("➕ Add Task")

    # -------------------------
    # JavaScript Example
    # -------------------------
    st.info("JavaScript Example : แสดงจำนวนตัวอักษรที่พิมพ์")

    components.html("""

    <div style="
        border:1px solid #dddddd;
        padding:15px;
        border-radius:10px;
        background:#f8f9fa;
    ">

    <label><b>Task Preview (JavaScript)</b></label>

    <input
        id="taskInput"
        type="text"
        placeholder="Type task here..."
        style="
            width:95%;
            padding:8px;
            margin-top:8px;
        "
        onkeyup="countText()"
    >

    <p id="count">
        Characters : 0
    </p>

    <script>

    function countText(){

        let txt =
            document.getElementById("taskInput").value;

        document.getElementById("count").innerHTML =
            "Characters : " + txt.length;

    }

    </script>

    </div>

    """, height=170)

    st.divider()

    # -------------------------
    # Streamlit Form
    # -------------------------

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
# Footer
# -----------------------------
def footer():

    st.markdown("""
    <hr>

    <div style="
        text-align:center;
        color:gray;
        font-size:14px;
    ">

        Powered by 
        Team name :
        
        Student Development Team

    </div>

    """,
    unsafe_allow_html=True)

# -----------------------------
# Main Program
# -----------------------------
def main():

    st.set_page_config(
        page_title="Student Task Manager",
        page_icon="📋",
        layout="wide"
    )


    # โหลด CSS
    load_css()

    init_data()

    st.title("📋 Student Task Manager")

    st.sidebar.image(
        "https://static.vecteezy.com/system/resources/thumbnails/022/418/057/small_2x/project-task-management-and-effective-time-planning-tools-project-development-icon-3d-vector-illustration-png.png",
        width=250
    )

    st.sidebar.title(
        "Student Manager"
    )


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

# แสดง Footer ทุกหน้า
footer()

# =====================================================
# DEBUG (ใช้สอน)
# =====================================================

with st.expander("📦 Session State (สำหรับการเรียนรู้)"):

    st.write(st.session_state)