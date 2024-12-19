Descrição do Projeto - Bootcamp CyberSecurity Santander #2
Este projeto, desenvolvido no contexto do Bootcamp CyberSecurity Santander #2, foca em explorar conceitos fundamentais de segurança cibernética, especificamente criptografia de dados, através de uma aplicação prática. O objetivo principal é proteger arquivos sensíveis contra acessos não autorizados, utilizando técnicas modernas de criptografia e descriptografia com o algoritmo AES no modo CTR (Counter Mode).

Objetivo
Demonstrar como aplicar algoritmos de criptografia para proteger informações confidenciais.
Garantir que os dados criptografados possam ser recuperados de forma segura, desde que a chave correta seja utilizada.
Explorar boas práticas de manipulação de arquivos e segurança de dados no contexto de cibersegurança.
Ferramentas e Tecnologias
Linguagem de Programação: Python
Biblioteca de Criptografia: cryptography
Algoritmo: AES (Advanced Encryption Standard) no modo CTR (Counter Mode)
Funcionalidades
Encriptação (encripter.py)

Lê o conteúdo de um arquivo (teste.txt) e utiliza uma chave de criptografia fixa para protegê-lo.
Gera um nonce (valor único e aleatório) para cada operação de criptografia, garantindo a segurança e evitando repetições de padrões.
Remove o arquivo original após criptografá-lo, reduzindo riscos de exposição.
Cria um novo arquivo criptografado (teste.txt.ransomwaretroll) que inclui o nonce no início para auxiliar na descriptografia.
Decriptação (decripter.py)

Lê o arquivo criptografado gerado pelo script anterior.
Separa o nonce e os dados criptografados.
Usa a mesma chave de criptografia para decifrar os dados e restaurar o conteúdo original.
Remove o arquivo criptografado e cria o arquivo descriptografado (teste.txt).
Aplicações Práticas
Este projeto simula um cenário real de proteção e recuperação de dados, sendo aplicável em:

Desenvolvimento de sistemas de proteção de arquivos locais.
Educação em segurança cibernética, mostrando os fundamentos de criptografia simétrica.
Demonstração de como ransomware funciona, mas com foco educativo e ético.
Resultados Esperados
Ao executar os scripts, os participantes poderão:

Entender os passos necessários para proteger dados de forma eficaz.
Aprender a importância do gerenciamento seguro de chaves e nonce.
Observar como uma implementação prática de criptografia pode ser incorporada em soluções reais.
Este projeto é uma introdução essencial ao universo da segurança de dados e um exemplo prático de como aplicar conceitos fundamentais de cibersegurança em Python.
