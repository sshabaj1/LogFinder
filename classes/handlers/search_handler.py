from ast import Set
import os

class SearchHandler():

    def search_logs(path, searchword):

        os.chdir(path)
        search_words = list(searchword.split(','))
        matched_files = set()
        print('search words: ', search_words)
        # Read text File
        
        
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