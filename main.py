from tkinter import *
from tkinter import ttk
from drawing_function import plot_function

def get_data_and_plot():
    equation = the_equation.get()
    try:
        start_range = float(start_entered_range.get())
        end_range = float(end_entered_range.get())
        plot_function(equation, (start_range, end_range))
    except ValueError:
        print("Ошибка: введите числовые значения для диапазонов")

root = Tk()
root.title("working with charts")

greetings = Label(root, width=30, height=10, bg="black", fg="white", font="30", text="Привет, я считаю графики")
greetings.pack()

enter_equation = Label(root, text="Введите свое уравнение: ")
enter_equation.pack()

the_equation = Entry(root)
the_equation.pack()

start_range_of_values = Label(root, text="Введите свое начало диапозона: ")
start_range_of_values.pack()

start_entered_range = Entry(root)
start_entered_range.pack()

end_range_of_values = Label(root, text="Введите свой конец диапозона: ")
end_range_of_values.pack()

end_entered_range = Entry(root)
end_entered_range.pack()

drawing = Button(root, text="Посчитать функцию!", command=get_data_and_plot)
drawing.pack()

root.mainloop()

