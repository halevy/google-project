from tkinter import *
from SRC.auto_complete import get_best_k_completions

root = Tk()
root.geometry("380x350")
root.title(" Auto Completion ")


def Take_input():

    Output.delete(1.0,END)
    INPUT = inputtxt.get("1.0", "end-1c")
    flag = 0

    if INPUT[-1] == '#':
        inputtxt.delete(1.0,END)
        Output.delete(1.0, END)
        flag = 1

    if not flag:
        auto_complete_data = get_best_k_completions(INPUT)

        if len(auto_complete_data) == 0:
            Output.insert(END, "No results")

        for i in range(len(auto_complete_data)):
            sentence = f"\n{i+1}. {auto_complete_data[i].completed_sentence}," \
                       f" ({auto_complete_data[i].source_text})\n"
            Output.insert(END, sentence)


inputtxt = Text(root, height=2,
                width=50)

Output = Text(root, height=15,
              width=50)

Display = Button(root, height=1,
                 width=20,
                 text="Search",
                 command=lambda: Take_input())

inputtxt.pack()
Display.pack()
Output.pack()


mainloop()