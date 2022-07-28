import os
from datetime import date


class DirectoryHandler():

    def mkdir_today(self, path):
        main_dir = os.getcwd()
        dir_list =main_dir.split('\\')
        documents_dir = f'{dir_list[0]}/{dir_list[1]}/{dir_list[2]}/Documents/{path}'
        today = date.today()
        dir_name = today.strftime("%d-%m-%Y")
        if_exitsts_logs = os.path.exists(f'{dir_list[0]}/{dir_list[1]}/{dir_list[2]}/Documents/{path}')
        if_exitsts = os.path.exists(f'{dir_list[0]}/{dir_list[1]}/{dir_list[2]}/Documents/{path}/{dir_name}')

        if not if_exitsts_logs:
            os.mkdir(f'{dir_list[0]}/{dir_list[1]}/{dir_list[2]}/Documents/{path}')

        if not if_exitsts:
            os.mkdir(f'{dir_list[0]}/{dir_list[1]}/{dir_list[2]}/Documents/{path}/{dir_name}')
