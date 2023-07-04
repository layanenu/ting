Projeto realizado durante o curso de Desenvolvimento Web Full Stack na Trybe

Neste projeto você deverá implementar um programa que simule um algoritmo de indexação de documentos similar ao do Google. Seu programa deverá ser capaz de identificar ocorrências de termos em arquivos TXT.

Para isso, o programa desenvolvido por você deverá ter dois módulos:

Módulo de gerenciamento de arquivos que permite anexar arquivos de texto (formato TXT) e;
Módulo de buscas que permite operar funções de busca sobre os arquivos anexados.
👀 Neste projeto não iremos focar na análise de significados ou busca por sinônimos.

🚵 Habilidades exercitadas:

Manipular Pilhas;

Manipular Deque;

Manipular Nó & Listas Ligadas e;

Manipular Listas Duplamente Ligadas.

Requisitos:
Pacote ting_file_management
1 - Implemente uma fila para armazenar os arquivos que serão lidos.
2 - Implemente uma função txt_importer dentro do módulo file_management capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador.
3 - Implemente a função process no módulo file_process. Essa função deverá ser capaz de transformar o conteúdo da lista gerada pela função txt_importer em um dicionário que será armazenado dentro da Queue.
4 - Implemente uma função remove dentro do módulo file_process capaz de remover o primeiro arquivo processado
5 - Implemente uma função file_metadata dentro do módulo file_process capaz de apresentar as informações superficiais de um arquivo processado.
6 - Implemente os testes para a classe PriorityQueue capaz de armazenar arquivos pequenos de forma prioritária
Pacote ting_word_searches
7 - Implemente uma função exists_word, dentro do módulo word_search, que verifique a existência de uma palavra em todos os arquivos processados.
8 - Implemente uma função search_by_word dentro do módulo word_search, que busque uma palavra em todos os arquivos processados.

