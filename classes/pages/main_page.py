from classes.utilities.static_variables import StaticVariables

from classes.handlers.search_handler import SearchHandler
from classes.handlers.log_handler import LogHandler
from classes.handlers.debug_handler import DebugHandler

from classes.pages.result_list_page import ResultListPage

from tkinter import filedialog


import  os
import tkinter as tk
import sys
from typing import TYPE_CHECKING

class MainPage(tk.Frame):

    path = None
    page_number = 1

    if TYPE_CHECKING:
        from main import MainApp
        app = MainApp()

    def __init__(self, master, *args, **kwargs):

        tk.Frame.__init__(self,master, *args, **kwargs)
        self.canvas = tk.Canvas(self, bg = 'white' ,width = 520,height = 520)
        self.canvas.pack(fill = "both", expand = True)
        master.iconbitmap(StaticVariables.APP_ICON)
        master.title(StaticVariables.LOG_FINDER)

        dir =  os.getcwd()

        global debug_image
        global result_window
        global files_list
        global entry_search_word
        

           
        self.debug_image = tk.PhotoImage(file =f'static/png/debug/{DebugHandler.debug_status}.png')

        self.help_image = tk.PhotoImage(file =StaticVariables.HELP_LOGO)

        self.main_page_logo = tk.PhotoImage(file=StaticVariables.MAIN_PAGE_LOGO)
        main_page_logo_image = self.canvas.create_image(180, 70, image = self.main_page_logo, anchor=tk.NW)

        self.open_folder = tk.PhotoImage(file =StaticVariables.OPEN_FOLDER_PATH)
        self.search_logo = tk.PhotoImage(file =StaticVariables.SEARCH_LOGO_PATH)

        entry_search_word = tk.Entry(self.canvas)

        self.canvas.create_window(250,200, window=entry_search_word)



        def handle_no_results():
            function_name = sys._getframe().f_code.co_name
            LogHandler.info_log(self, function_name, '', '')

            result_window  = tk.Toplevel(self.canvas)
            result_window.title(StaticVariables.NO_RESULT_STRING)
            result_window.geometry('200x200')
            result_window_canvas = tk.Canvas(result_window , width = 250,height = 250, bg='white')
            result_window_canvas.pack(fill = "both", expand = True)
            no_result_label = tk.Label(result_window, text=StaticVariables.NO_RESULTS_RETURNED, foreground='black', bg='white')
            no_result_canvas = result_window_canvas.create_window( 40, 50, anchor = "nw",window = no_result_label)


        
        def handle_no_path_selected():
            function_name = sys._getframe().f_code.co_name
            LogHandler.info_log(self, function_name, '', '')

            result_window  = tk.Toplevel(self.canvas)
            result_window.iconbitmap(StaticVariables.APP_ICON)
            result_window.title(StaticVariables.PATH_ERROR_STRING)
            result_window.geometry('200x200')
            result_window_canvas = tk.Canvas(result_window , width = 250,height = 250, bg='white')
            result_window_canvas.pack(fill = "both", expand = True)
            no_result_label = tk.Label(result_window, text=StaticVariables.NO_PATH_SELECTED_STRING, foreground='black', bg='white')
            no_result_canvas = result_window_canvas.create_window( 10, 50, anchor = "nw",window = no_result_label)


        def handle_no_word_writen():
            function_name = sys._getframe().f_code.co_name
            LogHandler.info_log(self, function_name, '', '')

            result_window  = tk.Toplevel(self.canvas)
            result_window.iconbitmap(StaticVariables.APP_ICON)
            result_window.title(StaticVariables.SEARCH_ERROR_STRING)
            result_window.geometry('200x200')
            result_window_canvas = tk.Canvas(result_window , width = 250,height = 250, bg='white')
            result_window_canvas.pack(fill = "both", expand = True)
            no_result_label = tk.Label(result_window, text=StaticVariables.NO_KEYWORD_WRITEN_STRING, foreground='black', bg='white')
            no_result_canvas = result_window_canvas.create_window( 50, 50, anchor = "nw",window = no_result_label)


        def handle_help_button():
            function_name = sys._getframe().f_code.co_name
            LogHandler.info_log(self, function_name, '', '')

            self.page_number = 1

            result_window  = tk.Toplevel(self.canvas)
            result_window.iconbitmap(StaticVariables.APP_ICON)
            result_window.title(StaticVariables.HELP_STRING)
            result_window.geometry('520x400')
            result_window_canvas = tk.Canvas(result_window , width = 250,height = 250, bg='white')
            result_window_canvas.pack(fill = "both", expand = True)

            result_window.help_png = tk.PhotoImage(file=f'{StaticVariables.HELP_PHOTOS_PATH}/{self.page_number}.png')
            help_png_images = result_window_canvas.create_image(0, 0, image = result_window.help_png, anchor=tk.NW)


            

            def handle_next_button():
                if self.page_number < 7:
                    self.page_number += 1
                    result_window.help_png.config(file=f'{StaticVariables.HELP_PHOTOS_PATH}/{self.page_number}.png')

            def handle_back_button():
                if self.page_number > 1:
                    self.page_number -= 1
                    result_window.help_png.config(file=f'{StaticVariables.HELP_PHOTOS_PATH}/{self.page_number}.png')

            self.back_button_img = tk.PhotoImage(file =StaticVariables.SMALL_BACK_BUTTON)
            self.next_button_img = tk.PhotoImage(file =StaticVariables.SMALL_NEXT_BUTTON)

            back_button = tk.Button( result_window, image=self.back_button_img, borderwidth=0,  bg='white', command=handle_back_button)
            back_button_canvas = result_window_canvas.create_window( 30, 350, anchor = "nw",window = back_button)

            next_button = tk.Button( result_window, image=self.next_button_img, borderwidth=0,  bg='white', command=handle_next_button)
            next_button_canvas = result_window_canvas.create_window( 460, 350, anchor = "nw",window = next_button)
            


        def browse_button_handler():
            function_name = sys._getframe().f_code.co_name
            LogHandler.info_log(self, function_name, '', '')

            filename = filedialog.askopenfilename()
            path_list = filename.rsplit('/',1)
            self.path = path_list[0]
            master.get_path(self.path)

            

        
            
        def search_button_handler():
            function_name = sys._getframe().f_code.co_name
            LogHandler.info_log(self, function_name, '', '')
            if self.path == None:
                handle_no_path_selected()
            else:
                logs_path = self.path
                search_words = entry_search_word.get()
                if len(search_words) > 0:
                    files_list  =  SearchHandler.search_logs(logs_path, search_words)
                    if files_list == StaticVariables.ERROR_STRING:
                        handle_no_path_selected()
                    else:
                        LogHandler.debug_log(self, function_name, 'files_list', files_list)
                        if len(files_list) > 1:
                            master.get_file_list(files_list)
                            master.switch_Canvas(StaticVariables.RESULT_LIST_STRING)
                        else:
                            handle_no_results()
                else:
                    handle_no_word_writen()
            

        
        def handle_debug_button():
            function_name = sys._getframe().f_code.co_name
            LogHandler.info_log(self, function_name, '', '')

            if DebugHandler.debug_status ==StaticVariables.OFF_STRING:
                DebugHandler.debug_status =StaticVariables.ON_STRING
                self.debug_image.config(file=StaticVariables.ON_DEBUG_PATH)
                LogHandler.create_log_file(self)
            else:
                DebugHandler.debug_status == StaticVariables.ON_STRING
                DebugHandler.debug_status =StaticVariables.OFF_STRING
                self.debug_image.config(file=StaticVariables.OFF_DEBUG_PATH)
                
            


        browse_button = tk.Button( self, image=self.open_folder, borderwidth=0,  bg='white', command=browse_button_handler)
        browse_button_canvas = self.canvas.create_window( 170, 250, anchor = "nw",window = browse_button)

        search_button = tk.Button( self, image=self.search_logo, borderwidth=0,  bg='white', command= search_button_handler)
        search_button_canvas = self.canvas.create_window( 270, 235, anchor = "nw",window =search_button)

        debug_button = tk.Button( self, image=self.debug_image, borderwidth=0,  bg='white', command=handle_debug_button)
        debug_button_canvas = self.canvas.create_window( 10, 10, anchor = "nw",window = debug_button)

        help_button = tk.Button( self, image=self.help_image, borderwidth=0,  bg='white', command=handle_help_button)
        help_button_canvas = self.canvas.create_window( 10, 480, anchor = "nw",window = help_button)