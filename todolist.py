import sys
from PyQt5.QtWidgets import (QApplication,QWidget, QLabel,
                              QLineEdit, QPushButton, QVBoxLayout, 
                              QCheckBox,QTimeEdit, QListWidget, QListWidgetItem)
from PyQt5.QtCore import Qt

class todolist(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Nest")
        self.set_label= QLabel("----⭐Tasks⭐----",self)
        self.task= QLabel("Today's task: ",self)
        self.write_task= QLineEdit(self)
        self.errorlabel= QLabel(self)
        self.ask_timing= QLabel("Timing: ",self)
        self.time= QTimeEdit(self)
        self.add_task= QPushButton("Add task",self)
        self.task_layout= QListWidget(self)
        self.task_list=[]
        self.done_chores_button= QPushButton("Task Completed",self)
        self.initUI()


    def initUI(self):
        layout= QVBoxLayout()

        layout.addWidget(self.set_label)
        layout.addWidget(self.task)
        layout.addWidget(self.write_task)
        layout.addWidget(self.errorlabel)
        layout.addWidget(self.ask_timing)
        layout.addWidget(self.time)
        layout.addWidget(self.add_task)
        layout.addWidget(self.task_layout)
        layout.addWidget(self.done_chores_button)

        self.setLayout(layout)

        self.set_label.setAlignment(Qt.AlignCenter)
        self.set_label.setObjectName("set_label")
        self.task.setObjectName("task")
        self.write_task.setObjectName("write_task")
        self.errorlabel.setObjectName("errorlabel")
        self.ask_timing.setObjectName("ask_timing")
        self.time.setObjectName("time")
        self.add_task.setObjectName("add_task")
        self.task_layout.setObjectName("task_layout")
        self.done_chores_button.setObjectName("done_chores_button")

        self.setStyleSheet("""
            QLabel, QPushButton, QTimeEdit,QLineEdit{
                        font-family: Bell Mt;
                        }
            QLabel#set_label{
                        font-size: 40px;
                           }
            QLabel#task{
                        font-size : 30px;
                        }
            QLineEdit#write_task{
                        font-size : 25px;
                        }
            QLabel#errorlabel{
                        font-size : 15px;
                        color: red;
                        }
            QLabel#ask_timing{
                        font-size : 30px;
                        }
            QTimeEdit#time{
                        font-size : 25px;
                        }
            QPushButton#add_task{
                        font-size : 29px;
                        }
            QPushButton#done_chores_button{
                        font-size : 29px;
                        font-weight: bold;
                        }
            QListWidget#task_layout{
                        font-family: Bell MT;
                        font-size: 25px;
                        font-weight: bold;
                        background-color: #91decd;}
""")
        
        self.add_task.clicked.connect(self.adding_task)
        self.done_chores_button.clicked.connect(self.completed_task)

    def adding_task(self):
        task= self.write_task.text()
        time= self.time.time().toString("hh:mm AP")

        if task!="":
            self.task_list.append({
            "task": task, 
            "time": time
        })
            self.display_tasks()
            self.errorlabel.clear()
        else:
            self.display_error("Please enter a task to continue!") 
            

    def display_tasks(self):
        self.task_layout.clear()
        for data in self.task_list:
            tasks= data["task"]
            times= data["time"]

            item= QListWidgetItem(f"{tasks} ---- {times}")
            item.setCheckState(Qt.CheckState.Unchecked)
            self.task_layout.addItem(item)    
        self.write_task.clear()
        
    def display_error(self,message):
        self.errorlabel.setText(message)
        

    def completed_task(self):
        for i in range(self.task_layout.count()-1,-1,-1):
            item= self.task_layout.item(i)

            if item.checkState()== Qt.CheckState.Checked:
                self.task_layout.takeItem(i)
                self.task_list.pop(i)
        

if __name__ ==  "__main__":
    app= QApplication(sys.argv)
    window= todolist()
    window.show()
    sys.exit(app.exec_())
