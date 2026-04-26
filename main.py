import sys
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QComboBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class SurveyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Survey Form")
        self.setMinimumWidth(420)
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                font-family: Segoe UI, Arial, sans-serif;
            }
            QLabel#title {
                font-size: 20px;
                font-weight: bold;
                color: #2c3e50;
            }
            QLabel#subtitle {
                font-size: 12px;
                color: #7f8c8d;
            }
            QLabel.field-label {
                font-size: 13px;
                font-weight: bold;
                color: #34495e;
            }
            QLineEdit {
                border: 1px solid #bdc3c7;
                border-radius: 6px;
                padding: 8px 10px;
                font-size: 13px;
                background-color: #ffffff;
                color: #2c3e50;
            }
            QLineEdit:focus {
                border: 1px solid #3498db;
            }
            QPushButton#submit-btn {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 24px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton#submit-btn:hover {
                background-color: #2980b9;
            }
            QPushButton#submit-btn:pressed {
                background-color: #1f6fa0;
            }
            QComboBox {
                border: 1px solid #bdc3c7;
                border-radius: 6px;
                padding: 8px 10px;
                font-size: 13px;
                background-color: #ffffff;
                color: #2c3e50;
            }
            QComboBox:focus {
                border: 1px solid #3498db;
            }
            QComboBox::drop-down {
                border: none;
                width: 24px;
            }
        """)
        self._build_ui()

    def _build_ui(self):
        root = QVBoxLayout()
        root.setContentsMargins(30, 28, 30, 28)
        root.setSpacing(14)

        # --- Header ---
        title = QLabel("Student Survey")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle = QLabel("Please fill in all fields and press Submit.")
        subtitle.setObjectName("subtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        root.addWidget(title)
        root.addWidget(subtitle)
        root.addSpacing(6)

        # --- Fields ---
        self.input_name = self._add_field(root, "Full Name", "e.g. Jane Doe")
        self.input_age = self._add_field(root, "Age (1–120)", "e.g. 21")

        # Language — editable combo box
        lang_label = QLabel("Favorite Programming Language")
        lang_label.setStyleSheet("font-size: 13px; font-weight: bold; color: #34495e;")
        self.input_lang = QComboBox()
        self.input_lang.setEditable(True)
        self.input_lang.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.input_lang.addItems([
            "", "Python", "C++", "C", "Java", "JavaScript",
            "TypeScript", "C#", "Go", "Rust", "Kotlin", "Swift", "PHP", "Ruby"
        ])
        self.input_lang.setCurrentIndex(0)
        self.input_lang.lineEdit().setPlaceholderText("Select or type a language")
        root.addWidget(lang_label)
        root.addWidget(self.input_lang)

        root.addSpacing(8)

        # --- Submit button (right-aligned) ---
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        self.btn_submit = QPushButton("Submit")
        self.btn_submit.setObjectName("submit-btn")
        self.btn_submit.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_submit.clicked.connect(self._on_submit)
        btn_row.addWidget(self.btn_submit)
        root.addLayout(btn_row)

        self.setLayout(root)

    def _add_field(self, parent_layout: QVBoxLayout, label_text: str, placeholder: str) -> QLineEdit:
        label = QLabel(label_text)
        label.setProperty("class", "field-label")
        # Re-apply style for dynamic property
        label.setStyleSheet("font-size: 13px; font-weight: bold; color: #34495e;")
        line_edit = QLineEdit()
        line_edit.setPlaceholderText(placeholder)
        parent_layout.addWidget(label)
        parent_layout.addWidget(line_edit)
        return line_edit

    def _on_submit(self):
        name = self.input_name.text().strip()
        age = self.input_age.text().strip()
        lang = self.input_lang.currentText().strip()

        # --- Empty check ---
        if not name or not age or not lang:
            QMessageBox.warning(self, "Incomplete Form", "Please fill in all fields before submitting.")
            return

        # --- Age validation ---
        try:
            age_int = int(age)
            if not (1 <= age_int <= 120):
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Invalid Age", "Age must be a whole number between 1 and 120.")
            self.input_age.setFocus()
            self.input_age.selectAll()
            return

        self._save_to_file(name, age, lang)

        QMessageBox.information(
            self,
            "Success",
            "Your answers have been saved to survey_answers.txt."
        )

        self.input_name.clear()
        self.input_age.clear()
        self.input_lang.setCurrentIndex(0)
        self.input_lang.lineEdit().clear()
        self.input_name.setFocus()

    def _save_to_file(self, name: str, age: str, lang: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = (
            f"--- Submission [{timestamp}] ---\n"
            f"Full Name : {name}\n"
            f"Age       : {age}\n"
            f"Fav. Lang : {lang}\n\n"
        )
        with open("survey_answers.txt", "a", encoding="utf-8") as f:
            f.write(entry)


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = SurveyForm()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
