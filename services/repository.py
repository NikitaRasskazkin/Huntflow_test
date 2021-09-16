import os
from openpyxl import load_workbook


def _open_file_decorator(function):  # ToDo add logger 'file not open'
    """
    :param function:
    :return: file or 'file_error'
    """
    def environment(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except OSError:
            return 'file_error'
    return environment


class DataBase:
    def __init__(self, path):
        self.path = path
        self.cvs = self._get_cvs()

    @_open_file_decorator
    def get_database(self, name='Тестовая база.xlsx', sheet='Лист1'):   # ToDo add logger 'sheet not found'
        """
        :param name: db file name
        :param sheet: sheet name
        :return: opened db or 'sheet error' if sheet not found
        """
        try:
            return load_workbook(os.path.join(self.path, name))[sheet]
        except KeyError:
            return 'sheet error'

    @_open_file_decorator
    def get_cv_file(self, vacancy: str, applicant: str):
        """
        :param vacancy:
        :param applicant:
        :return: bite file or None if the cv is not provided
        """
        try:
            path = os.path.join(self.path, vacancy, f'{applicant}.{self.cvs[vacancy][applicant]}')
        except KeyError:
            return None
        with open(path, 'rb') as file:
            return file

    def _get_cvs(self):
        cvs = dict()
        for dir_or_file in os.listdir(self.path):
            cur_dir_path = os.path.join(self.path, dir_or_file)
            if not os.path.isdir(cur_dir_path):
                continue
            cvs[dir_or_file] = dict()
            for cv_file in os.listdir(cur_dir_path):
                cv_path = os.path.join(cur_dir_path, cv_file)
                if not os.path.isfile(cv_path):
                    continue
                name, file_format = cv_file.split('.')
                cvs[dir_or_file].update({name: file_format})
            if not cvs[dir_or_file]:
                cvs.pop(dir_or_file)
        return cvs
