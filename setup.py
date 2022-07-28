from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

packages = ["sys",
            "os",
            "tkinter",
            "classes.pages.result_list_page",
            "classes.pages.main_page",
            "classes.utilities.static_variables",
            "classes.handlers.debug_handler",
            "classes.handlers.log_handler",
            "classes.handlers.search_handler",
            "classes.pages.result_list_page",
            "typing",
            "datetime",
            "inspect",
            "logging",
            "ast"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="Log Finder",
    options=options,
    version="1.1.0",
    description='',
    executables=executables
)
