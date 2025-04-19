"""Projeto Portifólio nlp
Bibliotecas usadas:
Python              3.11.5
nltk	            3.8.1   (Processamento de linguagem natural)

Tive um problema com a biblioteca Tokenize,especificamente com o "punkt",
exigindo que intalasse toda a biblioteca manualmente no pc,recorri e achei
essa alternativa.

"""
#Importando bibliotecas
import os
import nltk
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist

# Recursos de linguagem do NLTK
#nltk.download('stopwords')


# Tokeniza um texto

def mensagem(txt):
#Função que irá receber um texto e procura-ló para ver se é arquivo de texto
#Caso positivo irá transcreve-lo,caso negativo irá repassar a mensagem.  
    
    if os.path.isfile(txt):
        with open(txt, 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read()
        return texto
    else:
        return txt

tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(mensagem (input(str("Digite seu arquivo ou menssagem: "))))
print(f"\033[1;32m Tokens:\033[0m {tokens}")

#Removendo Stop Words

stop_words = set(stopwords.words('portuguese'))
tokens_sem_stopwords = [palavra for palavra in tokens if palavra.lower()
not in stop_words]
print(f"\033[1;32m Sem Stop Words:\033[0m {tokens_sem_stopwords}")

# Análise de frequência

frequencia = FreqDist(tokens_sem_stopwords)
print(f"\033[1;32m Frequência:\033[0m{frequencia.most_common(10)}")

