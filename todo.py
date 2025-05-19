from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QListWidget, QListWidgetItem,
    QComboBox, QDateEdit, QLabel
)
from PyQt5.QtCore import QDate
import sys

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yapılacaklar Listesi - Öncelik & Tarih")
        self.resize(550, 550)

        # Stil
        style = """
        QWidget {
            background-color: #f0f4fb;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 14px;
            color: #1a1a1a;
        }

        QLineEdit, QComboBox, QDateEdit {
            border: 1.5px solid #097dea;
            border-radius: 6px;
            padding: 6px;
            background-color: white;
            color: #333333;
        }

        QPushButton {
            background-color: #097dea;
            border: none;
            color: white;
            padding: 10px 18px;
            font-weight: bold;
            border-radius: 8px;
            margin: 4px 2px;
        }

        QPushButton:hover {
            background-color: #065bb5;
        }

        QListWidget {
            background-color: white;
            border: 1.5px solid #097dea;
            border-radius: 8px;
            padding: 8px;
        }

        QListWidget::item {
            padding: 8px 10px;
            border-bottom: 1px solid #cde1fb;
        }

        QListWidget::item:selected {
            background-color: #b3d4fc;
            color: #000000;
        }

        QLabel {
            font-weight: bold;
        }

        QDateEdit {
            min-width: 120px;
        }
        """
        self.setStyleSheet(style)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Görev girişi yatay düzen
        input_layout = QHBoxLayout()

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Görev yazınız...")
        input_layout.addWidget(self.task_input)

        self.priority_select = QComboBox()
        self.priority_select.addItems(["Düşük", "Orta", "Yüksek"])
        input_layout.addWidget(self.priority_select)

        self.date_input = QDateEdit()
        self.date_input.setDate(QDate.currentDate())
        self.date_input.setCalendarPopup(True)
        input_layout.addWidget(self.date_input)

        self.add_button = QPushButton("Ekle")
        self.add_button.clicked.connect(self.add_task)
        input_layout.addWidget(self.add_button)

        self.layout.addLayout(input_layout)

        # Liste widget
        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        # Silme butonu
        self.delete_button = QPushButton("Seçili Görevi Sil")
        self.delete_button.clicked.connect(self.delete_task)
        self.layout.addWidget(self.delete_button)

    def add_task(self):
        task_text = self.task_input.text().strip()
        if not task_text:
            return  # boşsa ekleme

        priority = self.priority_select.currentText()
        date = self.date_input.date().toString("dd.MM.yyyy")

        item_text = f"{task_text} - Öncelik: {priority} - Tarih: {date}"
        item = QListWidgetItem(item_text)
        self.task_list.addItem(item)

        self.task_input.clear()
        self.priority_select.setCurrentIndex(0)
        self.date_input.setDate(QDate.currentDate())

    def delete_task(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            self.task_list.takeItem(self.task_list.row(item))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())
