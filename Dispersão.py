import csv

class TabelaDispersao:
    def __init__(self, tamanho, funcao_hash):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
        self.funcao_hash = funcao_hash

    def inserir(self, chave, dado):
        indice = self.funcao_hash(chave) % self.tamanho

        if self.tabela[indice] is None:
            self.tabela[indice] = [(chave, dado)]
        else:
            for item in self.tabela[indice]:
                if item[0] == chave:  # Verifica se é uma duplicata
                    return
            self.tabela[indice].append((chave, dado))

# Função de hash simples para exemplo
def funcao_hash(chave):
    return hash(chave)  # Função de hash nativa do Python

# Função para eliminar duplicatas do arquivo CSV
def eliminar_duplicatas_csv(nome_arquivo_entrada, nome_arquivo_saida):
    tabela_hash = TabelaDispersao(1000, funcao_hash)  # Ajuste o tamanho conforme necessário

    with open(nome_arquivo_entrada, 'r', newline='') as arquivo_entrada, \
            open(nome_arquivo_saida, 'w', newline='') as arquivo_saida:
        
        leitor = csv.reader(arquivo_entrada)
        escritor = csv.writer(arquivo_saida)

        for linha in leitor:
            chave = linha[0]  # A chave pode ser o primeiro elemento da linha, por exemplo
            tabela_hash.inserir(chave, linha)

        # Escrevendo os dados sem duplicatas no arquivo de saída
        for lista in tabela_hash.tabela:
            if lista is not None:
                for item in lista:
                    escritor.writerow(item[1])  # Escreve os dados sem a chave

# Exemplo de uso
nome_arquivo_entrada = 'seu_dataset.csv'
nome_arquivo_saida = 'sem_duplicatas.csv'
eliminar_duplicatas_csv(nome_arquivo_entrada, nome_arquivo_saida)
