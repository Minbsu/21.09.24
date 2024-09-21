from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout ,QLabel , QHBoxLayout , QMessageBox , QRadioButton ,QSpinBox,QFormLayout,QLineEdit,QListWidget,QListWidgetItem,QTableView, QGroupBox,QButtonGroup,QItemEditorFactory,QTextEdit,QTextBrowser,QInputDialog        


import json


app = QApplication([])

notes = {
    'Добро пожаловать!' : {
        "текст":"Это наилучшое приложение для записи заметок!",    
        "теги" : ["Добро","Инструкция"]
    }
}




notes_win = QWidget()
notes_win.resize(900,600)
notes_win.setWindowTitle("Smart Notes 0.0.1")

list_notes = QListWidget()
list_notes_label = QLabel("Список")
list_tags = QListWidget 
list_tags = QLabel("Список тегов")

btn_note_create = QPushButton("Создать заметку")
btn_note_del = QPushButton("Удалить заметку")
btn_note_save = QPushButton("Сохранить заметку")
btn_note_search = QPushButton("Искать заметку")
btn_note_add = QPushButton("Добавить заметку")

field_tag = QLineEdit()
field_tag.setPlaceholderText('Ведите заметки')
field_text = QTextEdit()

hlayout = QHBoxLayout()
vlayout = QVBoxLayout()
vlayout.addWidget(field_text)
hlayout.addWidget(btn_note_add)
hlayout.addWidget(btn_note_save)

h2layout = QHBoxLayout()
v2layout = QVBoxLayout()
v2layout.addWidget(list_notes)
v2layout.addWidget(list_notes_label)
h2layout.addWidget(btn_note_create)
h2layout.addWidget(btn_note_del)



h3layout = QHBoxLayout()
v3layout = QVBoxLayout()
h3layout.addWidget(btn_note_search)


v4layout = QVBoxLayout()



v2layout.addWidget(list_tags)
v2layout.addWidget(field_tag)
vlayout.addLayout(hlayout)
v2layout.addLayout(h2layout)
v2layout.addLayout(h3layout)

hlayout.addLayout(vlayout, stretch=2)
hlayout.addLayout(v2layout,stretch=1)




with open("notes_data.json","w") as file:
    json.dump(notes,file)



def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[key]["теги"])

list_notes.itemClicked.connect(show_note)

notes_win.show()

with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)

app.exec_()