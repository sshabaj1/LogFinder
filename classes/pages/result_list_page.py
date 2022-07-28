from classes.handlers.debug_handler import DebugHandler
from classes.handlers.log_handler import LogHandler

from classes.utilities.static_variables import StaticVariables




import tkinter as tk
from tkinter import E, StringVar, ttk
import sys
from typing import TYPE_CHECKING
import os

record_list = []

class ResultListPage(tk.Frame):
    if TYPE_CHECKING:
        from main import MainApp
        app = MainApp()


    def __init__(self, master, *args, **kwargs):
        dir = (master.set_dir()).replace('\\', '/')
        tk.Frame.__init__(self,master, *args, **kwargs)
        self.canvas = tk.Canvas(self, bg = 'DeepSky Blue2' ,width = 668,height = 550, relief="sunken")
        self.canvas.pack(fill = "both", expand = True)
        master.iconbitmap(f'{dir}/{StaticVariables.APP_ICON}')
        master.title('Results')

        dir = (master.set_dir()).replace('\\', '/')

        self.back_image = tk.PhotoImage(file =f'{dir}/{StaticVariables.BACK_LOGO}')

        search_frame = tk.LabelFrame(self.canvas, text='Search Data')
        search_frame.place(height=470, width=670)

        tv1 = ttk.Treeview(search_frame, columns=(1), show='headings', height='5')
        tv1.place(relheight=1, relwidth=1)
        tv1.heading(1, text='File Name')

        scroll_bar_y = tk.Scrollbar(search_frame, orient='vertical', command=tv1.yview)
        scroll_bar_x = tk.Scrollbar(search_frame, orient='horizontal', command=tv1.xview)
        tv1.configure(xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set)
        scroll_bar_x.pack(side='bottom', fill='x')
        scroll_bar_y.pack(side='right', fill='y')

        path = master.set_path()
        file_list = list(master.set_file_list())



        def on_double_click(event):
            function_name = sys._getframe().f_code.co_name
            LogHandler.info_log(self, function_name, '', '')

            LogHandler. debug_log(self, function_name, 'event', event)
            item = tv1.identify('item', event.x, event.y)
            item_nr = int(item[1:])
            item_nr -= 1
            clicked_record = file_list[item_nr]
            LogHandler. debug_log(self, function_name, 'clicked_record', clicked_record.replace('\\','/'))
            master.open_file(clicked_record)

        for file in file_list:
            LogHandler. debug_log(self, 'on_double_click/for loop/', 'file', file)
            correct_path = file.replace('\\', '/')
            LogHandler. debug_log(self, 'on_double_click/for loop/', 'correct_path', correct_path)
            file_name = correct_path.rsplit('/',1)[1]
            LogHandler. debug_log(self, 'on_double_click/for loop/', 'file_name', file_name)
            tv1.insert('', 'end', values=file_name)
        tv1.bind('<Double-1>', on_double_click)




        def handle_back():
            function_name = sys._getframe().f_code.co_name
            LogHandler.info_log(self, function_name, '', '')
            
            new_dir = master.set_dir()
            os.chdir(new_dir)
            master.switch_Canvas(StaticVariables.MAIN_PAGE_STRING)








        back_button = tk.Button( self, image=self.back_image, borderwidth=0, bg='DeepSky Blue2', command=handle_back)
        back_button_canvas = self.canvas.create_window( 30, 480, anchor = "nw",window = back_button)