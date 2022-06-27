import yadisk
import os
import my_token


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str) -> None:
        disk = yadisk.YaDisk(token=self.token)
        if os.path.exists(file_path):
            disk.upload(file_path, file_path.split('/')[-1])
        else:
            print('No such file')


if __name__ == '__main__':
    work_dir = os.getcwd()
    path_to_file = os.path.join(work_dir, 'files/yad.txt')
    uploader = YaUploader(my_token.token)
    uploader.upload(path_to_file)
