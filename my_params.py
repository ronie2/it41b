import pwd
import os
import mimetypes
from datetime import datetime


def get_file_type(full_path):
    file_type, encoding = mimetypes.guess_type(full_path)
    return file_type


def parse_arguments():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs='+', help='Paths to list')
    return parser.parse_args()


def get_paths_content(paths):
    return (os.walk(path) for path in paths)


def owner_name(full_path):
    file_stats = get_file_stats(full_path)
    user_id = file_stats.st_uid
    return pwd.getpwuid(user_id).pw_name


def get_full_path(root, file):
    return root + "/" + file


def get_file_stats(full_path):
    return os.stat(full_path)


def get_access_time(full_path):
    file_stats = get_file_stats(full_path)
    access_time = datetime.fromtimestamp(file_stats.st_atime)
    return access_time


def get_permissions(full_path):
    file_stats = get_file_stats(full_path)
    return oct(file_stats.st_mode)[-3:]

def path_nice_content(paths_content):
    for content_by_path in paths_content:
        for root, dirs, files in content_by_path:
            path = root.split("/")
            tabs_index = len(path)
            print((tabs_index - 1) * "──", os.path.basename(root))
            for file in files:
                full_path = get_full_path(root, file)
                print(tabs_index * "──" +
                      "{file}\t\t "
                      "Owner: {owner}\t File Type: {file_type}\t "
                      "Access Time: {access_time}\t Permissions: {permissions}"
                      .format(file=file,
                              owner=owner_name(full_path),
                              file_type=get_file_type(full_path),
                              access_time=get_access_time(full_path),
                              permissions=get_permissions(full_path)))


if __name__ == "__main__":
    paths = parse_arguments().path
    paths_content_list = list(get_paths_content(paths))
    paths_content = get_paths_content(paths)
    path_nice_content(paths_content)
