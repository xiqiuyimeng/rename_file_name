# -*- coding: utf-8 -*-
from pymediainfo import MediaInfo
import os
_author_ = 'luwt'
_date_ = '2019/5/20 11:07'


def get_file_info(filename):
    if os.path.isfile(filename):
        info = MediaInfo.parse(filename)
        data = info.to_data()
        file_title = data.get('tracks')[0].get('title')
        file_ext = data.get('tracks')[0].get('file_extension')
        print(file_title, file_ext)
        return file_title, file_ext
    else:
        print("非法路径")


if __name__ == '__main__':
    path = 'D:\\Test'
    fos = os.listdir(path)
    for f in fos:
        title, ext = get_file_info(os.path.join(path, f))
        os.rename(os.path.join(path, f), '.'.join([os.path.join(path, title), ext]))
