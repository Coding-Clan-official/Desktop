from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QApplication, QGraphicsDropShadowEffect, QHBoxLayout, QTableWidget, QTableWidgetItem, QGridLayout, QMenuBar, QAction, QToolBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()  # Initialize the UI
        self.show()     # Show the window

    def init_ui(self):
        self.setWindowTitle("User Login")
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: white;")

        # Central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Title label
        title_label = QLabel("Welcome to the App", self)
        title_label.setStyleSheet("font-size: 28px; font-weight: bold; color: #003366;")
        layout.addWidget(title_label, alignment=Qt.AlignCenter)

        # Username input with shadow
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet("""
            padding: 10px; 
            border: 1px solid #003366; 
            border-radius: 5px; 
            background-color: white;
        """)
        layout.addWidget(self.username_input)
        self.add_shadow_effect(self.username_input)

        # Password input with shadow
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("""
            padding: 10px; 
            border: 1px solid #003366; 
            border-radius: 5px; 
            background-color: white;
        """)
        layout.addWidget(self.password_input)
        self.add_shadow_effect(self.password_input)

        # Login button with hover effect and shadow
        self.login_button = QPushButton("Login", self)
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #003366; 
                color: white; 
                border-radius: 5px; 
                padding: 10px; 
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #00509E; 
            }
        """)
        layout.addWidget(self.login_button)
        self.login_button.clicked.connect(self.authenticate_user)
        self.add_shadow_effect(self.login_button)

        # Adding a shadow effect to the main window
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        self.setGraphicsEffect(shadow)

        # Spacing adjustments
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Footer label
        footer_label = QLabel("© 2023 Your Company", self)
        footer_label.setStyleSheet("font-size: 12px; color: #003366;")
        layout.addWidget(footer_label, alignment=Qt.AlignCenter)

    def add_shadow_effect(self, widget):
        """Add shadow effect to a given widget."""
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        widget.setGraphicsEffect(shadow)

    def authenticate_user(self):
        # Placeholder for authentication logic
        print("Authentication logic goes here.")
        self.open_management_dashboard()  # Open accounting management on successful login

    def open_management_dashboard(self):
        self.management_dashboard = ManagementDashboard()
        self.management_dashboard.show()
        self.close()  # Close the login window

class ManagementDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.is_fullscreen = False  # Track fullscreen state
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Management Dashboard")
        self.setStyleSheet("background-color: #f0f0f0;")  # Light background

        # Create a menu bar
        menu_bar = self.menuBar()
        menu_bar.setStyleSheet("""
            QMenuBar {
                background-color: #003366;  /* Dark blue background */
                font-size: 16px;  /* Increased font size */
                color: white;  /* White text */
                padding: 5px;  /* Padding for menu bar */
            }
            QMenuBar::item {
                spacing: 15px;  /* Space between menu items */
                padding: 10px;  /* Padding for menu items */
                border-right: 1px solid #00509E;  /* Right border for separation */
            }
            QMenuBar::item:last-child {
                border-right: none;  /* Remove right border from last item */
            }
            QMenu {
                background-color: #00509E;  /* Lighter blue for dropdown */
                border: 1px solid #003366;  /* Border for dropdown */
                border-radius: 5px;  /* Rounded corners */
            }
            QMenu::item {
                padding: 10px;  /* Padding for menu items */
            }
            QMenu::item:selected {
                background-color: #007ACC;  /* Highlight color */
                color: white;  /* Text color on highlight */
            }
            QMenu::item:hover {
                background-color: #006699;  /* Change color on hover */
                color: #FFD700;  /* Change text color on hover */
            }
        """)

        # Create main menu items
        master_menu = menu_bar.addMenu("Master")
        transaction_menu = menu_bar.addMenu("Transaction")
        inventory_menu = menu_bar.addMenu("Inventory")
        reports_menu = menu_bar.addMenu("Reports")

        # Add submenu items with icons
        master_menu.addAction(QIcon("path/to/accounts_icon.png"), "Manage Accounts")
        master_menu.addAction(QIcon("path/to/users_icon.png"), "Manage Users")
        
        transaction_menu.addAction(QIcon("path/to/sales_icon.png"), "Sales")
        transaction_menu.addAction(QIcon("path/to/purchases_icon.png"), "Purchases")
        
        inventory_menu.addAction(QIcon("path/to/inventory_icon.png"), "Manage Inventory")
        
        reports_menu.addAction(QIcon("path/to/sales_report_icon.png"), "Sales Report")
        reports_menu.addAction(QIcon("path/to/inventory_report_icon.png"), "Inventory Report")

        # Central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Title label
        title_label = QLabel("Management Dashboard", self)
        title_label.setStyleSheet("font-size: 28px; font-weight: bold; color: #003366;")
        layout.addWidget(title_label, alignment=Qt.AlignCenter)

        # Add a placeholder for content
        content_label = QLabel("Select an option from the menu.", self)
        content_label.setStyleSheet("font-size: 18px; color: #555;")
        layout.addWidget(content_label, alignment=Qt.AlignCenter)

        # Show the window in full screen
        self.showFullScreen()

    def toggle_fullscreen(self):
        """Toggle between full-screen and windowed mode."""
        if self.is_fullscreen:
            self.showNormal()  # Show windowed
        else:
            self.showFullScreen()  # Show full screen
        self.is_fullscreen = not self.is_fullscreen  # Toggle state

    def add_shadow_effect(self, widget):
        """Add shadow effect to a given widget."""
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        widget.setGraphicsEffect(shadow)

    # Placeholder methods for button actions
    def manage_accounts(self):
        print("Managing accounts...")

    def manage_inventory(self):
        print("Managing inventory...")

    def manage_billings(self):
        print("Managing billings...")

    def manage_sales(self):
        print("Managing sales...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
