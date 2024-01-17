from tkinter import *

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-do_list")
        self.root.geometry("650x410+300+150")
        self.root.config(bg="#f7d569")

        self.label = Label(self.root, text="TO-DO List App", font=("Arial", 30, "bold"), bd=5, bg="#f7d569", fg='white')
        self.label.pack(side="top", fill=X)

        self.label_2 = Label(self.root, text="ADD TASK", font=("Arial", 20, "bold"), bd=5, bg="#f7d569", fg='white') 
        self.label_2.place(x=40, y=54)

        self.label_3 = Label(self.root, text="TASKS", font=("Arial", 20, "bold"), bd=5, bg="#f7d569", fg='white')  
        self.label_3.place(x=500, y=54)

        self.main_text = Listbox(self.root, height=10, bd=5, width=40, font=("Arial", 12), selectbackground="#3498db", selectforeground='white', bg="#ecf0f1")
        self.main_text.place(x=420, y=100)

        self.text = Entry(self.root, bd=5, font=("Arial", 12), bg="#ecf0f1")
        self.text.place(x=20, y=120, width=350)

        self.button = Button(self.root, text="Add Task", font=("Arial", 14), bd=5, bg="#2ecc71", fg="white", command=self.add)
        self.button.place(x=30, y=170)

        self.button_1 = Button(self.root, text="Delete", font=("Arial", 14), bd=5, bg="#e74c3c", fg="white", command=self.delete)
        self.button_1.place(x=30, y=220)

        self.load_tasks()

    def add(self):
        content = self.text.get()
        if content:
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content + '\n')
            self.text.delete(0, END)

    def delete(self):
        selected_item = self.main_text.curselection()
        if selected_item:
            self.main_text.delete(selected_item)
            with open('data.txt', "r+") as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    if line.strip() not in self.main_text.get(0, END):
                        f.write(line)
                f.truncate()

    def load_tasks(self):
        try:
            with open('data.txt', 'r') as file:
                tasks = file.readlines()
                for task in tasks:
                    self.main_text.insert(END, task.strip())
        except FileNotFoundError:
            pass

    def main(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.resizable(False, False)
    ul = Todo(root)
    ul.main()
