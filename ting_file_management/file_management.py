import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            sys.stderr.write('Formato inválido\n')

        with open(path_file) as archive:
            archive_content = archive.read().split("\n")
            return archive_content

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")