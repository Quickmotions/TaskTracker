import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from functools import partial


class TrackerUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('To-Do Tracker')
        self.setFixedSize(250, 250)
        self.task_manager = Tasks()

    def list_tasks(self):
        for task in self.task_manager.tasks:
            ...


class Tasks:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        with open('tasks.data') as f:
            for line in f.readlines():
                self.tasks.append(line.strip())

    def create_task(self):
        ...


def main():
    app = QApplication(sys.argv)
    ui = TrackerUI()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
