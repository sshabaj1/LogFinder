from classes.utilities.static_variables import StaticVariables
from classes.pages.main_page  import  MainPage


import tkinter as tk
import sys





class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._Canvas= None
        self.switch_Canvas(StaticVariables.MAIN_PAGE)

    
    def switch_Canvas(self, Canvas_class):
        # function_name = sys._getframe().f_code.co_name
        # LogHandler.info_log(self, function_name, '', '')
            
        template_canvas_class = getattr(sys.modules[__name__], Canvas_class)
        new_Canvas = template_canvas_class(self)
        if self._Canvas is not None:
            self._Canvas.destroy()
        self._Canvas = new_Canvas
        self._Canvas.pack()

    # def __init__(self):
    #     tk.Tk.__init__(self)
    #     self._Canvas= tk.Canvas(self , bg = 'red', width = 345,height = 518)
    #     self.canvas.pack(fill = "both", expand = True)
    #     tk.title('')
    #     tk.iconbitmap(r'./static/cobra_logo.ico')




if __name__ == '__main__':
    app = MainApp()
    app.mainloop()