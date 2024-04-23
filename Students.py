from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QFont, QPalette, QColor
from PyQt6.QtCore import Qt

import sqlite3

class Students(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Students Database")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.FN_input = QLineEdit()
        self.ln_input = QLineEdit()
        self.term_input = QLineEdit()
        self.gpa_input = QLineEdit()
        self.ID_input = QLineEdit()

        self.INS_button = QPushButton("Add")
        self.viw_button = QPushButton("View")
        self.srch_button = QPushButton("Search")
        self.del_button = QPushButton("Delete")
        self.upd_button = QPushButton("Update")
        self.sif_button = QPushButton("Check if student failed or succeeded")
        self.clear_button = QPushButton("Clear")
        self.exit_button = QPushButton("Exit")

        self.layout.addWidget(QLabel("First Name:"))
        self.layout.addWidget(self.FN_input)
        self.layout.addWidget(QLabel("Last Name:"))
        self.layout.addWidget(self.ln_input)
        self.layout.addWidget(QLabel("Term:"))
        self.layout.addWidget(self.term_input)
        self.layout.addWidget(QLabel("GPA:"))
        self.layout.addWidget(self.gpa_input)
        self.layout.addWidget(self.INS_button)
        self.layout.addWidget(self.viw_button)
        self.layout.addWidget(self.srch_button)
        self.layout.addWidget(QLabel("ID to Delete or Update or Search or Check if student failed or Succeeded:"))
        self.layout.addWidget(self.ID_input)
        self.layout.addWidget(self.del_button)
        self.layout.addWidget(self.upd_button)
        self.layout.addWidget(self.sif_button)
        self.layout.addWidget(self.clear_button)
        self.layout.addWidget(self.exit_button)

        self.connect()

        self.INS_button.clicked.connect(self.insert)
        self.viw_button.clicked.connect(self.vpop)
        self.srch_button.clicked.connect(self.spop)
        self.del_button.clicked.connect(self.delete)
        self.upd_button.clicked.connect(self.upop)
        self.sif_button.clicked.connect(self.successorfail)
        self.clear_button.clicked.connect(self.clear)
        self.exit_button.clicked.connect(self.close)

        self.apply_stylesheet()

    def apply_stylesheet(self):
        style_sheet = """
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 14px;
            }
            QLineEdit {
                font-size: 14px;
                padding: 6px;
                border: 1px solid #ccc;
            }
            QPushButton {
                font-size: 14px;
                padding: 8px;
                border: none;
                background-color: #4caf50;
                color: white;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3c893d;
            }
        """
        self.setStyleSheet(style_sheet)

    def connect(self):
        conn = sqlite3.connect("students.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS data1 (id INTEGER PRIMARY KEY, fn TEXT, ln TEXT, term INTEGER, gpa REAL)")
        conn.commit()
        conn.close()

    def insert(self):
        fn = self.FN_input.text()
        ln = self.ln_input.text()
        term = self.term_input.text()
        gpa = self.gpa_input.text()
        conn = sqlite3.connect("students.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO data1 VALUES (NULL,?,?,?,?)", (fn, ln, term, gpa))
        conn.commit()
        conn.close()
        QMessageBox.information(self, "Info", f"{fn} has been added")
        self.clear()

    def view(self):
        conn = sqlite3.connect("students.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM data1")
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(self):
        fn = self.FN_input.text()
        ln = self.ln_input.text()
        term = self.term_input.text()
        gpa = self.gpa_input.text()
        id = self.ID_input.text()
        conn = sqlite3.connect("students.db")
        cur = conn.cursor()

        if fn and ln:
            cur.execute("SELECT * FROM data1 WHERE fn=? AND ln=?", (fn, ln))
        elif fn:
            if term:
                if gpa:
                    cur.execute("SELECT * FROM data1 WHERE fn=? AND term=? AND gpa=?", (fn, term,gpa))
                cur.execute("SELECT * FROM data1 WHERE fn=? AND term=?", (fn, term))
            elif gpa:
                if gpa:
                    cur.execute("SELECT * FROM data1 WHERE fn=? AND gpa=?", (fn, gpa))
            else:
                cur.execute("SELECT * FROM data1 WHERE fn=?", (fn,))
        elif ln:
            if term:
                if gpa:
                    cur.execute("SELECT * FROM data1 WHERE ln=? AND term=? AND gpa=?", (ln, term,gpa))
                else:
                    cur.execute("SELECT * FROM data1 WHERE ln=? AND term=?", (ln, term))
            elif gpa:
                if gpa:
                    cur.execute("SELECT * FROM data1 WHERE ln=? AND gpa=?", (ln, gpa))
            else:
                cur.execute("SELECT * FROM data1 WHERE ln=?", (ln,))
        elif term:
            cur.execute("SELECT * FROM data1 WHERE term=?", (term,))
        elif gpa:
            cur.execute("SELECT * FROM data1 WHERE gpa=?", (gpa,))
        elif id:
            cur.execute("SELECT * FROM data1 WHERE id=?", (id,))
        else:
            QMessageBox.information(self, "Info", "Please enter search criteria")
            return []

        rows = cur.fetchall()
        conn.close()
        return rows



    def delete(self):
        id = self.ID_input.text()
        conn = sqlite3.connect("students.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM data1 WHERE id=?", (id,))
        conn.commit()
        conn.close()
        QMessageBox.information(self, "Deleted", f"ID: {id} was deleted")
        self.ID_input.clear()

    def clear(self):
        self.ID_input.clear()
        self.FN_input.clear()
        self.ln_input.clear()
        self.term_input.clear()
        self.gpa_input.clear()

    def update(self):
        id = self.ID_input.text()
        fn = self.FN_input.text()
        ln = self.ln_input.text()
        term = self.term_input.text()
        gpa = self.gpa_input.text()
        conn = sqlite3.connect("students.db")
        cur = conn.cursor()
        cur.execute("UPDATE data1 SET fn=?, ln=?, term=?, gpa=? WHERE id=?", (fn, ln, term, gpa, id))
        conn.commit()
        conn.close()
        QMessageBox.information(self, "Info", f"{id} has been updated")
        self.ID_input.clear()
        self.FN_input.clear()
        self.ln_input.clear()
        self.term_input.clear()
        self.gpa_input.clear()

    def vpop(self):
        pop = self.view()
        if not pop:
            pop = "No students"
        QMessageBox.information(self, "Info", str(pop))

    def spop(self):
        sp = self.search()
        if not sp:
            sp = "Not found in database"
        QMessageBox.information(self, "Info", str(sp))

    def successorfail(self):
        fn = self.FN_input.text()
        ln = self.ln_input.text()
        term = self.term_input.text()
        gpa = self.gpa_input.text()
        sp = None

        id = self.ID_input.text()
        if not id:
            QMessageBox.information(self, "Info", "Please enter ID")
            return
        conn = sqlite3.connect("students.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM data1 WHERE id=?", (id,))
        sp = cur.fetchone()
        conn.close()
        if not sp:
            QMessageBox.information(self, "Info", "Not found in database")
            return

        try:
            fn, ln, term, gpa = sp[1:5]
            if float(gpa) >= 2 and int(term) == 4:
                QMessageBox.information(self, "Info", f"{fn} has passed the grade")
            elif float(gpa) >= 2 and int(term) != 4:
                QMessageBox.information(self, "Info", f"{fn} has passed the quarter")
            elif float(gpa) < 2:
                QMessageBox.information(self, "Info", f"Sorry {fn} has failed the quarter")
        except ValueError:
            pass


    def upop(self):
        id = self.ID_input.text()
        if not id:
            QMessageBox.information(self, "Info", "Please enter the ID")
            return
        self.update()
        QMessageBox.information(self, "Info", f"{id} has been updated")
        self.ID_input.clear()

app = QApplication([])
students = Students()

# Apply a theme (e.g., Fusion)
app.setStyle("Fusion")

# Modify the palette to customize the theme colors
palette = QPalette()
palette.setColor(QPalette.ColorRole.Window, QColor("#f0f0f0"))  # Set background color
palette.setColor(QPalette.ColorRole.WindowText, QColor("#333333"))  # Set text color
app.setPalette(palette)

# Set a custom font
font = QFont("Arial", 12)
app.setFont(font)

students.show()
app.exec()
