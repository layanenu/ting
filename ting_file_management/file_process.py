from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file, instance: Queue):
    if any(item['nome_do_arquivo'] == path_file for item in instance.queue):
        return None

    importer_txt = txt_importer(path_file)
    dictionary = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(importer_txt),
        "linhas_do_arquivo": importer_txt
    }

    instance.enqueue(dictionary)
    sys.stdout.write(str(dictionary))


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        deleted_file = instance.dequeue()
        name_file = deleted_file["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {name_file} removido com sucesso\n")


def file_metadata(instance: Queue, position):
    try:
        info = instance.search(position)
        info_string = (str(info))
        sys.stdout.write(info_string)
    except IndexError:
        sys.stderr.write('Posição inválida')
