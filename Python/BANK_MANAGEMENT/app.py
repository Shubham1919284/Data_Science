import json
import random
import string
from pathlib import Path

import streamlit as st


# ============================================================
# CONFIGURATION
# ============================================================

DATABASE = Path(__file__).parent / "data.json"


# ============================================================
# BANK MANAGEMENT CLASS
# ============================================================

class Bank:

    def __init__(self):
        self.data = []
        self.load_data()

    # --------------------------------------------------------
    # DATABASE
    # --------------------------------------------------------

    def load_data(self):
        """Load accounts from JSON database."""

        try:
            if DATABASE.exists():

                with open(DATABASE, "r", encoding="utf-8") as file:
                    content = file.read().strip()

                    self.data = json.loads(content) if content else []

            else:
                self.data = []
                self.save_data()

        except (json.JSONDecodeError, OSError):
            self.data = []

    def save_data(self):
        """Save account data to JSON."""

        try:
            with open(DATABASE, "w", encoding="utf-8") as file:
                json.dump(self.data, file, indent=4)

        except OSError as error:
            raise RuntimeError(f"Unable to save database: {error}")

    # --------------------------------------------------------
    # ACCOUNT NUMBER
    # --------------------------------------------------------

    def generate_account_number(self):
        """Generate a unique account number."""

        while True:

            account_number = (
                "".join(random.choices(string.ascii_uppercase, k=3))
                + "".join(random.choices(string.digits, k=6))
            )

            if not self.find_account(account_number):
                return account_number

    # --------------------------------------------------------
    # FIND ACCOUNT
    # --------------------------------------------------------

    def find_account(self, account_number):
        """Find account using account number."""

        for account in self.data:

            if account["account_number"] == account_number:
                return account

        return None

    # --------------------------------------------------------
    # AUTHENTICATION
    # --------------------------------------------------------

    def authenticate(self, account_number, pin):
        """Authenticate account using account number and PIN."""

        account = self.find_account(account_number)

        if account and account["pin"] == pin:
            return account

        return None

    # --------------------------------------------------------
    # CREATE ACCOUNT
    # --------------------------------------------------------

    def create_account(self, name, age, email, pin):

        if not name.strip():
            return False, "Name cannot be empty."

        if age < 18:
            return False, "Account holder must be at least 18 years old."

        if not email.strip() or "@" not in email:
            return False, "Please enter a valid email address."

        if not (1000 <= pin <= 9999):
            return False, "PIN must contain exactly 4 digits."

        account = {
            "name": name.strip(),
            "age": age,
            "email": email.strip(),
            "account_number": self.generate_account_number(),
            "balance": 0,
            "pin": pin
        }

        self.data.append(account)
        self.save_data()

        return True, account

    # --------------------------------------------------------
    # DEPOSIT
    # --------------------------------------------------------

    def deposit(self, account_number, pin, amount):

        account = self.authenticate(account_number, pin)

        if not account:
            return False, "Invalid account number or PIN."

        if amount <= 0:
            return False, "Amount must be greater than ₹0."

        if amount > 10000:
            return False, "Maximum deposit per transaction is ₹10,000."

        account["balance"] += amount

        self.save_data()

        return True, account["balance"]

    # --------------------------------------------------------
    # WITHDRAW
    # --------------------------------------------------------

    def withdraw(self, account_number, pin, amount):

        account = self.authenticate(account_number, pin)

        if not account:
            return False, "Invalid account number or PIN."

        if amount <= 0:
            return False, "Amount must be greater than ₹0."

        if amount > account["balance"]:
            return False, "Insufficient balance."

        account["balance"] -= amount

        self.save_data()

        return True, account["balance"]

    # --------------------------------------------------------
    # UPDATE ACCOUNT
    # --------------------------------------------------------

    def update_account(
        self,
        account_number,
        pin,
        name=None,
        email=None
    ):

        account = self.authenticate(account_number, pin)

        if not account:
            return False, "Invalid account number or PIN."

        if name and name.strip():
            account["name"] = name.strip()

        if email and email.strip():

            if "@" not in email:
                return False, "Invalid email address."

            account["email"] = email.strip()

        self.save_data()

        return True, "Account details updated successfully."

    # --------------------------------------------------------
    # DELETE ACCOUNT
    # --------------------------------------------------------

    def delete_account(self, account_number, pin):

        account = self.authenticate(account_number, pin)

        if not account:
            return False, "Invalid account number or PIN."

        self.data.remove(account)

        self.save_data()

        return True, "Account deleted successfully."


# ============================================================
# STREAMLIT CONFIG
# ============================================================

st.set_page_config(
    page_title="NovaBank",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main background */

    .stApp {
        background: linear-gradient(
            135deg,
            #0f172a 0%,
            #111827 50%,
            #020617 100%
        );
        color: white;
    }

    /* Sidebar */

    section[data-testid="stSidebar"] {
        background: #020617;
        border-right: 1px solid #1e293b;
    }

    /* Headers */

    h1, h2, h3 {
        color: #f8fafc;
    }

    /* Cards */

    .bank-card {
        background: rgba(30, 41, 59, 0.75);
        border: 1px solid #334155;
        border-radius: 18px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.25);
    }

    .metric-card {
        background: linear-gradient(
            135deg,
            #1e293b,
            #0f172a
        );

        border: 1px solid #334155;
        border-radius: 18px;
        padding: 22px;
        text-align: center;
    }

    .metric-title {
        color: #94a3b8;
        font-size: 14px;
    }

    .metric-value {
        color: #f8fafc;
        font-size: 28px;
        font-weight: 700;
    }

    /* Buttons */

    .stButton > button {
        width: 100%;
        border-radius: 10px;
        border: 1px solid #475569;
        background: #1e293b;
        color: white;
        font-weight: 600;
        padding: 10px;
        transition: 0.2s;
    }

    .stButton > button:hover {
        border-color: #60a5fa;
        background: #334155;
    }

    /* Inputs */

    .stTextInput input,
    .stNumberInput input {
        background: #0f172a;
        color: white;
        border-radius: 10px;
    }

    /* Success / error */

    div[data-testid="stAlert"] {
        border-radius: 12px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# INITIALIZE BANK
# ============================================================

if "bank" not in st.session_state:
    st.session_state.bank = Bank()

bank = st.session_state.bank


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center">

        <h1>🏦 NovaBank</h1>

        <p style="color:#94a3b8">
        Smart Banking System
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    menu = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "➕ Create Account",
            "💰 Deposit Money",
            "💸 Withdraw Money",
            "👤 Account Details",
            "✏️ Update Account",
            "🗑️ Delete Account"
        ]
    )

    st.divider()

    st.caption("JSON-based Banking System")
    st.caption("Built with Python + Streamlit")


# ============================================================
# DASHBOARD
# ============================================================

if menu == "🏠 Dashboard":

    st.title("🏦 Welcome to NovaBank")

    st.markdown(
        """
        <p style="color:#94a3b8;font-size:18px">
        A simple and secure banking management system.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    total_accounts = len(bank.data)

    total_balance = sum(
        account["balance"]
        for account in bank.data
    )

    total_deposits = sum(
        account["balance"]
        for account in bank.data
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            f"""
            <div class="metric-card">

            <div class="metric-title">
            TOTAL ACCOUNTS
            </div>

            <div class="metric-value">
            {total_accounts}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="metric-card">

            <div class="metric-title">
            TOTAL BALANCE
            </div>

            <div class="metric-value">
            ₹{total_balance:,.2f}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
            <div class="metric-card">

            <div class="metric-title">
            SYSTEM STATUS
            </div>

            <div class="metric-value">
            🟢 ONLINE
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    st.markdown(
        """
        <div class="bank-card">

        <h3>✨ Banking Services</h3>

        <p style="color:#94a3b8">
        Use the sidebar to access banking services.
        </p>

        <ul style="color:#cbd5e1">

        <li>Create a new bank account</li>
        <li>Deposit money</li>
        <li>Withdraw money</li>
        <li>View account details</li>
        <li>Update account information</li>
        <li>Delete your account</li>

        </ul>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# CREATE ACCOUNT
# ============================================================

elif menu == "➕ Create Account":

    st.title("➕ Create New Account")

    with st.form("create_account"):

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
                "Full Name",
                placeholder="Enter your full name"
            )

            age = st.number_input(
                "Age",
                min_value=1,
                max_value=120,
                value=18
            )

        with col2:

            email = st.text_input(
                "Email",
                placeholder="example@gmail.com"
            )

            pin = st.number_input(
                "4-Digit PIN",
                min_value=0,
                max_value=9999,
                step=1,
                format="%04d"
            )

        submit = st.form_submit_button(
            "Create Account"
        )

    if submit:

        success, result = bank.create_account(
            name,
            age,
            email,
            pin
        )

        if success:

            st.success("🎉 Account created successfully!")

            st.markdown(
                f"""
                <div class="bank-card">

                <h3>Account Created</h3>

                <p>
                <b>Name:</b> {result["name"]}
                </p>

                <p>
                <b>Account Number:</b>
                <code>{result["account_number"]}</code>
                </p>

                <p>
                <b>Balance:</b> ₹0
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.warning(
                "⚠️ Please save your account number and PIN securely."
            )

        else:

            st.error(result)


# ============================================================
# DEPOSIT
# ============================================================

elif menu == "💰 Deposit Money":

    st.title("💰 Deposit Money")

    with st.form("deposit"):

        account_number = st.text_input(
            "Account Number"
        )

        pin = st.number_input(
            "PIN",
            min_value=0,
            max_value=9999,
            format="%04d"
        )

        amount = st.number_input(
            "Deposit Amount",
            min_value=1,
            max_value=10000,
            step=100
        )

        submit = st.form_submit_button(
            "Deposit Money"
        )

    if submit:

        success, result = bank.deposit(
            account_number,
            pin,
            amount
        )

        if success:

            st.success(
                f"✅ Deposit successful! "
                f"New balance: ₹{result:,.2f}"
            )

        else:

            st.error(result)


# ============================================================
# WITHDRAW
# ============================================================

elif menu == "💸 Withdraw Money":

    st.title("💸 Withdraw Money")

    with st.form("withdraw"):

        account_number = st.text_input(
            "Account Number"
        )

        pin = st.number_input(
            "PIN",
            min_value=0,
            max_value=9999,
            format="%04d"
        )

        amount = st.number_input(
            "Withdrawal Amount",
            min_value=1,
            step=100
        )

        submit = st.form_submit_button(
            "Withdraw Money"
        )

    if submit:

        success, result = bank.withdraw(
            account_number,
            pin,
            amount
        )

        if success:

            st.success(
                f"✅ Withdrawal successful! "
                f"Remaining balance: ₹{result:,.2f}"
            )

        else:

            st.error(result)


# ============================================================
# ACCOUNT DETAILS
# ============================================================

elif menu == "👤 Account Details":

    st.title("👤 Account Details")

    with st.form("details"):

        account_number = st.text_input(
            "Account Number"
        )

        pin = st.number_input(
            "PIN",
            min_value=0,
            max_value=9999,
            format="%04d"
        )

        submit = st.form_submit_button(
            "View Account"
        )

    if submit:

        account = bank.authenticate(
            account_number,
            pin
        )

        if account:

            st.success("Account verified successfully.")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Account Holder",
                    account["name"]
                )

            with col2:

                st.metric(
                    "Account Number",
                    account["account_number"]
                )

            with col3:

                st.metric(
                    "Balance",
                    f"₹{account['balance']:,.2f}"
                )

            st.divider()

            st.write("### Personal Information")

            st.write(
                f"**Name:** {account['name']}"
            )

            st.write(
                f"**Age:** {account['age']}"
            )

            st.write(
                f"**Email:** {account['email']}"
            )

        else:

            st.error(
                "Invalid account number or PIN."
            )


# ============================================================
# UPDATE ACCOUNT
# ============================================================

elif menu == "✏️ Update Account":

    st.title("✏️ Update Account")

    st.info(
        "You can update your name and email. "
        "Account number, age, balance and PIN cannot be changed."
    )

    with st.form("update"):

        account_number = st.text_input(
            "Account Number"
        )

        pin = st.number_input(
            "Current PIN",
            min_value=0,
            max_value=9999,
            format="%04d"
        )

        new_name = st.text_input(
            "New Name",
            placeholder="Leave blank to keep current name"
        )

        new_email = st.text_input(
            "New Email",
            placeholder="Leave blank to keep current email"
        )

        submit = st.form_submit_button(
            "Update Account"
        )

    if submit:

        success, result = bank.update_account(
            account_number,
            pin,
            new_name,
            new_email
        )

        if success:

            st.success(result)

        else:

            st.error(result)


# ============================================================
# DELETE ACCOUNT
# ============================================================

elif menu == "🗑️ Delete Account":

    st.title("🗑️ Delete Account")

    st.warning(
        "⚠️ Account deletion is permanent and cannot be undone."
    )

    with st.form("delete"):

        account_number = st.text_input(
            "Account Number"
        )

        pin = st.number_input(
            "PIN",
            min_value=0,
            max_value=9999,
            format="%04d"
        )

        confirmation = st.checkbox(
            "I understand that this account will be permanently deleted."
        )

        submit = st.form_submit_button(
            "Delete Account"
        )

    if submit:

        if not confirmation:

            st.error(
                "Please confirm account deletion."
            )

        else:

            success, result = bank.delete_account(
                account_number,
                pin
            )

            if success:

                st.success(result)

            else:

                st.error(result)