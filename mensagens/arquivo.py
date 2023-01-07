# Abre o arquivo em modo de escrita
with open('mensagens.txt', 'a') as f:
  # Escreve a mensagem no arquivo
  f.write(body + '\n')
