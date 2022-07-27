


class RecordReturn():

    def get_path(self, path):
        self.path = path
        print('RecordReturn/path: ', self.path)

    def get_file_list(self, file_list):
        self.file_list = file_list
        print('RecordReturn/file_list: ', self.file_list)

    def set_path(self):
        return self.path

    def set_file_list(self):
        return self.file_list