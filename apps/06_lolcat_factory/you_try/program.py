import platform
import subprocess
import os
import cat_service


def main():
    print_header()
    full_path = get_or_create_folder()
    download_cats(full_path)
    display_cats(full_path)


def print_header():
    print('--------------------------------------------')
    print('        LOLCAT FACTORY')
    print('--------------------------------------------')


def get_or_create_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    cat_count = 8

    for i in range(1, cat_count + 1):
        name = f'lolcat_{i}'
        print(f'downloading {name}')
        cat_service.get_cat(folder, name)
    print('done')

def display_cats(folder):
    print('Displaying cats')
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't support your os: " + platform.system())


if __name__ == '__main__':
    main()
