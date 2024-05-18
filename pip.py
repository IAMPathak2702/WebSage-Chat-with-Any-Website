import os

def print_tree(root, padding, print_files=False, is_last=False):
    # Print the current directory or file
    print(padding, '└── ' if is_last else '├── ', os.path.basename(root), sep='')
    
    padding = padding + ('    ' if is_last else '│   ')

    files = []
    dirs = []
    
    # Separate directories and files
    for item in os.listdir(root):
        if os.path.isdir(os.path.join(root, item)):
            dirs.append(item)
        else:
            files.append(item)
    
    # Print directories
    for index, directory in enumerate(dirs):
        is_last = (index == len(dirs) - 1) and (not print_files or not files)
        print_tree(os.path.join(root, directory), padding, print_files, is_last)
    
    # Print files if requested
    if print_files:
        for index, file in enumerate(files):
            is_last = (index == len(files) - 1)
            print(padding, '└── ' if is_last else '├── ', file, sep='')

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Print a directory tree.')
    parser.add_argument('directory', metavar='D', type=str, nargs='?', default='.',
                        help='the root directory (default: current directory)')
    parser.add_argument('-f', '--files', action='store_true',
                        help='print files as well as directories')

    args = parser.parse_args()
    print_tree(args.directory, '', args.files)
