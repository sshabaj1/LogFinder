from classes.handlers.log_handler import LogHandler

from classes.utilities.static_variables import StaticVariables

from ast import Set
import os, sys

class SearchHandler():


    def search_logs(path, searchword):
        is_error = False
        function_name = sys._getframe().f_code.co_name
        LogHandler.info_log('SearchHandler', function_name, '', '')
        
        try:
            os.chdir(path)
        except OSError as e:
            is_error = True
            LogHandler.critical_log('SearchHandler', function_name, 'OS Error', e)

        if is_error == True:
            return StaticVariables.ERROR_STRING
        else:
            search_words = list(searchword.split(','))
            matched_files = set()
            LogHandler.info_log('SearchHandler', function_name, 'Search Words', search_words)

        
        
            def read_text_file(file_path,search_word):
                function_name = sys._getframe().f_code.co_name
                LogHandler.info_log('SearchHandler', function_name, '', '')
                
                with open(file_path, encoding='utf8') as f:
                    f = f.readlines()
                    for line in f:
                        for search_word in search_words:
                            if search_word in line:
                                matched_files.add(str(file_path))
                                LogHandler.debug_log('SearchHandler', function_name, 'matched_files', matched_files)


                            
                                
            
            
            # iterate through all file
            for file in os.listdir():
                LogHandler.info_log('SearchHandler', function_name, 'enterd in loop/file: ', file)
                if file.endswith(StaticVariables.LOG_EXTENTION):
                    file_path = f"{path}\{file}"
                    LogHandler.debug_log('SearchHandler', function_name, 'file_path', file_path)

                    read_text_file(file_path, search_words)

            return matched_files