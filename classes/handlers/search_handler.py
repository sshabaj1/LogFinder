from classes.handlers.log_handler import LogHandler

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
            return 'ERROR'
        else:
            search_words = list(searchword.split(','))
            matched_files = set()
            LogHandler.info_log('SearchHandler', function_name, 'Search Words', search_words)

        
        
            def read_text_file(file_path,search_word):
                with open(file_path, encoding='utf8') as f:
                    f = f.readlines()
                    for line in f:
                        for search_word in search_words:
                            if search_word in line:
                                print("word found in: ", file_path)
                                print(str(file_path))
                                matched_files.add(str(file_path))
                                print('-----------',matched_files)

                            
                                
            
            
            # iterate through all file
            for file in os.listdir():
                print('enterd in for loop file: ', file)
                # Check whether file is in text format or not
                if file.endswith(".log"):
                    file_path = f"{path}\{file}"
                    print('file_path: ', file_path)
            
                    # call read text file function
                    read_text_file(file_path, search_words)
            print('matched files: ', matched_files)

            return matched_files