from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout ,QLabel , QHBoxLayout , QMessageBox , QRadioButton ,QSpinBox,QFormLayout,QLineEdit,QListWidget,QListWidgetItem,QTableView, QGroupBox,QButtonGroup,QItemEditorFactory,QTextEdit,QTextBrowser,QInputDialog        


import json


app = QApplication([])


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

btn_tag_add = QPushButton("Добавить тег")
btn_tag_del = QPushButton("Удалить тег")

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


def add_note():
    note_name,ok= QInputDialog.getText(notes_win,"Додати замітку","Назва замітки:")
    if ok and note_name!= "":
        notes[note_name] = {"текст": "","теги" : []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]["теги"])
        print(notes)

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[key]["теги"])

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open("notes_data.json","w") as file:
            json.dump(notes, file, sort_keys=True,ensire_ascii=False)
        print(notes)
    else:
        print("Замітка для вилучення не обрана!")

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["текст"] = field_text.toPlainText()
        with open("notes_data.json","w") as file:
            json.dimp(notes,file,sort_keys=True,ensure_ascii=False)
        print(notes)
    else:
        print("Замітка для збереження не вибрана")

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
            with open("notes_data.json", "w") as file:
                json.dump(notes, file,sort_keys=True,ensure_ascii=False)
            print(notes)
    else:
        print("Замітка для додавання тега не обрана!")
    
def del_tag():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]["tags"].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]["tags"])
        with open("notes_data.json","w") as file:
            json.dump(notes,file,sort_keys=True,ensure_ascii=False)
    else:
        print("Тег для вилучення не обраний!")
    
def search_tag():
    print(btn_note_search.text())    
    tag = field_tag.text()
    if btn_note_search.text() == "Шукати замітки по тегу" and tag:
        print(tag)
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]["tag"]:
                notes_filtered[note]=notes[note]
        btn_note_search.setText("скинути пошку")
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)        
        print(btn_note_search.text())
    elif btn_note_search.text() == "Скинути пошук":
        field_tag.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        btn_note_search.setText("Шукати замітки по тегу")
        print(btn_note_search.text())
    else:
        pass
        
list_notes.itemClicked.connect(show_note)

btn_note_create.clicked.connect(add_note)
list_notes.itemClicked.connect(show_note)
btn_note_save.clicked.connect(save_note)
btn_note_del.clicked.connect(del_note)
btn_tag_add.clicked.connect(add_tag)
btn_tag_del.clicked.connect(del_tag)
btn_note_search.clicked.connect(search_tag)




notes_win.show()

with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)




app.exec_()
