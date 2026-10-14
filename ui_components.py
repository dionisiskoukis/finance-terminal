# ui_components.py
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QPlainTextEdit, QVBoxLayout, QWidget, QLineEdit

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Finance Terminal v1.2")
window.resize(980, 620)
window.setStyleSheet("""
    QWidget {
        background: #0a0f10;
        color: #dfe9e7;
        font-family: "Consolas", "SFMono-Regular", monospace;
    }

    QPlainTextEdit, QLineEdit {
        background-color: #0b1214;
        color: #b9f7d2;
        border: 1px solid #22383a;
        padding: 8px 10px;
        selection-background-color: #2d5d50;
        selection-color: #f4fff9;
        font-size: 12px;
    }

    QPlainTextEdit {
        min-height: 430px;
        background: #0c1416;
        border: 1px solid #2a3d3d;
    }

    QLineEdit {
        background: #0d1718;
        color: #dfe9e7;
        border: 1px solid #2d4244;
        padding-left: 12px;
    }

    QLabel {
        color: #b9f7d2;
        font-size: 11px;
        letter-spacing: 1.1px;
        text-transform: uppercase;
    }
""")

layout = QVBoxLayout(window)
layout.setContentsMargins(14, 14, 14, 14)
layout.setSpacing(10)

header_row = QHBoxLayout()
brand_label = QLabel("Finance Terminal")
brand_label.setStyleSheet("color: #dfe9e7; font-weight: 700; font-size: 11px; letter-spacing: 2px;")
status_label = QLabel("LIVE")
status_label.setAlignment(Qt.AlignCenter)
status_label.setStyleSheet("color: #d5d8d6; border: 1px solid #2f393b; padding: 3px 9px; min-width: 54px;")
header_row.addWidget(brand_label)
header_row.addStretch()
header_row.addWidget(status_label)
layout.addLayout(header_row)

display_screen = QPlainTextEdit()
display_screen.setReadOnly(True)
display_screen.setPlaceholderText("Awaiting market data...")
display_screen.setStyleSheet("border: 1px solid #2b3a3c; background: #0b1214; color: #b9f7d2; font-size: 12px;")
display_screen.setLineWrapMode(QPlainTextEdit.NoWrap)
layout.addWidget(display_screen)

input_row = QHBoxLayout()
prompt_label = QLabel(">_")
prompt_label.setStyleSheet("color: #dfe9e7; background: #101819; border: 1px solid #2a3d3d; padding: 8px 12px; min-width: 60px;")
prompt_label.setAlignment(Qt.AlignCenter)

typing_bar = QLineEdit()
typing_bar.setPlaceholderText("Enter command or ticker symbol...")
typing_bar.setStyleSheet("background: #0d1718; border: 1px solid #2d4244; color: #dfe9e7; padding: 8px 10px;")
input_row.addWidget(prompt_label)
input_row.addWidget(typing_bar)
layout.addLayout(input_row)

def to_screen(text):
    display_screen.appendPlainText(str(text))
    display_screen.ensureCursorVisible()

def show_terminal_banner():
    to_screen("")
    to_screen("Finance Terminal")
    to_screen("Type 'help' to see available commands.")
    to_screen("")
