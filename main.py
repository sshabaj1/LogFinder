from classes.handlers.log_handler import LogHandler
from classes.handlers.debug_handler import DebugHandler

from classes.utilities.static_variables import StaticVariables
from classes.pages.main_page  import  MainPage
from classes.pages.result_list_page  import  ResultListPage

import tkinter as tk
import sys
import os





class MainApp(tk.Tk):


    def __init__(self):
        tk.Tk.__init__(self)
        self._Canvas= None
        self.switch_Canvas(StaticVariables.MAIN_PAGE_STRING)

    global path
    global files_list
    global main_dir

    main_dir = os.getcwd()
    path = ''
    files_list = []
    
    def switch_Canvas(self, Canvas_class):
        function_name = sys._getframe().f_code.co_name
        LogHandler.info_log(self, function_name, '', '')
        LogHandler.debug_log(self, function_name, 'Canvas: ', Canvas_class)

        template_canvas_class = getattr(sys.modules[__name__], Canvas_class)
        new_Canvas = template_canvas_class(self)
        if self._Canvas is not None:
            self._Canvas.destroy()
        self._Canvas = new_Canvas
        self._Canvas.pack()


    def get_path(self, path):
        function_name = sys._getframe().f_code.co_name
        LogHandler.info_log(self, function_name, '', '')

        self.path = path
        LogHandler.debug_log(self, function_name, 'path: ', self.path)

    def get_file_list(self, file_list):
        function_name = sys._getframe().f_code.co_name
        LogHandler.info_log(self, function_name, '', '')

        self.files_list = file_list
        LogHandler.debug_log(self, function_name, 'files_list', self.files_list)


    def set_path(self):
        function_name = sys._getframe().f_code.co_name
        LogHandler.info_log(self, function_name, '', '')
        return self.path

    def set_file_list(self):
        function_name = sys._getframe().f_code.co_name
        LogHandler.info_log(self, function_name, '', '')
        return self.files_list


    def open_file(self,fileName):
        function_name = sys._getframe().f_code.co_name
        LogHandler.info_log(self, function_name, '', '')

        os.system("start " + fileName)


    

    def set_dir(self):
        function_name = sys._getframe().f_code.co_name
        LogHandler.info_log(self, function_name, '', '')

        return main_dir
    




if __name__ == '__main__':
    app = MainApp()
    app.mainloop()