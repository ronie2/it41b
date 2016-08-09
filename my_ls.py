import os


def parse_arguments():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs='+', help='Paths to list')
    return parser.parse_args()


def get_paths_content(paths):
    return (os.walk(path) for path in paths)
    # return [get_full_paths(path) for path in paths]


def path_nice_content(paths_content_list):
    for content_list in paths_content_list:
        for root, dirs, files in content_list:
            path = root.split("/")
            tabs_index = len(path)
            print((tabs_index - 1) * "─", os.path.basename(root))
            for file in files:
                print(tabs_index * "─", file)


if __name__ == "__main__":
    paths = parse_arguments().path
    paths_content = get_paths_content(paths)
    path_nice_content(paths_content)
