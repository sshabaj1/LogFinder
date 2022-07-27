from classes.utilities.static_variables import StaticVariables
from classes.handlers.search_handler import SearchHandler
from tkinter import filedialog


import  os
import tkinter as tk
import sys
from typing import TYPE_CHECKING

class MainPage(tk.Frame):

    if TYPE_CHECKING:
        from main import MainApp
        app = MainApp()

    def __init__(self, master, *args, **kwargs):

        # self is now an istance of tk.Frame
        tk.Frame.__init__(self,master, *args, **kwargs)
        # make a new Canvas whose parent is self.
        self.canvas = tk.Canvas(self, bg = 'white' ,width = 520,height = 520)
        self.canvas.pack(fill = "both", expand = True)
        master.title('Log Finder')



        self.blue_obj = tk.PhotoImage(file ='static/png/blue_obj.png')
        blue_obj_image = self.canvas.create_image(5, 50, image = self.blue_obj, anchor=tk.NW)

        self.qatar_logo = tk.PhotoImage(file ='static/png/qatar_logo.png')
        qatar_logo_image = self.canvas.create_image(20, 450, image = self.qatar_logo, anchor=tk.NW)

        self.open_folder = tk.PhotoImage(file ='static/png/open_folder.png')
        self.search_logo = tk.PhotoImage(file ='static/png/search_logo.png')





        global result_window
        global path
        global files_list
        global entry_search_word
        entry_search_word = tk.Entry(self.canvas)

        self.canvas.create_window(250,200, window=entry_search_word)

        def open_result_window():
            result_window  = tk.Toplevel(self.canvas)
            result_window.title('Results')
            result_window.geometry('400x400')
            result_window_canvas = tk.Canvas(result_window , width = 250,height = 250, bg='white')
            result_window_canvas.pack(fill = "both", expand = True)
            row = 0
            column = 10
            buttons = 0
            if len(self.files_list) > 0:
                for path in self.files_list:
                    row += 40
                    button_name_raw  = (path.rsplit('/',1))[1]
                    button_name = (button_name_raw.split("\\"))[1]

                    path_button = tk.Button(result_window, text=button_name, borderwidth=2, bg='white', command = lambda: openFile(path))
                    path_button_canvas = result_window_canvas.create_window( column, row, anchor = "nw",window = path_button)
            else:
                no_result_label = tk.Label(result_window, text='No Result', foreground='black', bg='white')
                no_result_canvas = result_window_canvas.create_window( 10, 50, anchor = "nw",window = no_result_label)

        def browse_button_handler():
            filename = filedialog.askopenfilename()
            print('filename: ', filename)
            path_list = filename.rsplit('/',1)
            self.path = path_list[0]
            print('path: ', self.path)
            

        def openFile(fileName):
            os.system("start " + fileName)
            
        def search_button_handler():
            logs_path = self.path
            search_words = entry_search_word.get()
            self.files_list  =  SearchHandler.search_logs(logs_path, search_words)
            open_result_window()

            print('files: ', self.files_list)


            


        browse_button = tk.Button( self, image=self.open_folder, borderwidth=0,  bg='white', command=browse_button_handler)
        browse_button_canvas = self.canvas.create_window( 170, 250, anchor = "nw",window = browse_button)

        search_button = tk.Button( self, image=self.search_logo, borderwidth=0,  bg='white', command=search_button_handler)
        search_button_canvas = self.canvas.create_window( 270, 235, anchor = "nw",window =search_button)