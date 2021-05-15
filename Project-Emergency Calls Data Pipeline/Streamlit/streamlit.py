import streamlit as st
import pandas as pd
import hashlib
import sqlite3
import services

# Security

# passlib,hashlib,bcrypt,scrypt


def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False


# DB Management

conn = sqlite3.connect('data.db')
c = conn.cursor()


# DB  Functions
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username, password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)', (username, password))
    conn.commit()


def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?', (username, password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data


def main():

    st.set_page_config(
        page_title="EmerygencyCallServices",
        page_icon=":phone:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("Emergency Call Services")

    # Sidebar
    st.sidebar.header(":gear: Navigation")
    menu = ["Home", "Login", "SignUp"]
    choice = st.sidebar.selectbox(label="Menu", options=menu, index=0, help="Main Navigation Menu")

    if choice == "Home":
        st.image("welcome.gif", use_column_width=True)

    elif choice == "Login":

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox("Login/Logout"):

            create_usertable()
            hashed_pswd = make_hashes(password)

            result = login_user(username, check_hashes(password, hashed_pswd))
            if result:

                a, b = st.beta_columns([0.6,10])
                a.image("support.png", width=60, caption=username)
                b.header("Welcome, {}!!".format(username))

                services.login_menu()
                # task = st.selectbox("Task", ["Add Post", "Analytics", "Profiles"])
                # if task == "Add Post":
                #     st.subheader("Add Your Post")
                #
                # elif task == "Analytics":
                #     st.subheader("Analytics")
                # elif task == "Profiles":
                #     st.subheader("User Profiles")
                #     user_result = view_all_users()
                #     clean_db = pd.DataFrame(user_result, columns=["Username", "Password"])
                #     st.dataframe(clean_db)
            else:
                st.sidebar.error("Incorrect Username/Password")

    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')

        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user, make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")


if __name__ == '__main__':
    main()
