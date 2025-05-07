# Python
=== GUIA PARA AMBIENTES VIRTUAIS PYTHON ===

1. CRIAR O AMBIENTE VIRTUAL:
---------------------------------------
Execute no terminal (dentro da pasta do seu projeto):

# Linux/Mac:
python3 -m venv .venv

# Windows:
python -m venv .venv

(Isto cria uma pasta oculta '.venv' com o ambiente isolado)

2. ATIVAR O AMBIENTE:
---------------------------------------
# Linux/Mac:
source .venv/bin/activate

# Windows:
.\.venv\Scripts\activate

(Seu terminal mostrará (.venv) no início da linha quando ativado)

3. INSTALAR BIBLIOTECAS:
---------------------------------------
Com o ambiente ativado, instale o que precisar:
pip install pandas numpy matplotlib  # (exemplo)

4. SALVAR AS DEPENDÊNCIAS (requirements.txt):
---------------------------------------
Gere o arquivo que "congela" as bibliotecas instaladas:
pip freeze > requirements.txt

(O arquivo será criado na pasta atual)

5. DESATIVAR O AMBIENTE:
---------------------------------------
Simplesmente digite:
deactivate

6. RECRIAR O AMBIENTE EM OUTRA MÁQUINA:
---------------------------------------
Basta copiar a pasta do projeto COM o requirements.txt e executar:
python3 -m venv .venv           # Cria o ambiente
source .venv/bin/activate       # Ativa (Linux/Mac)
pip install -r requirements.txt # Instala todas as dependências

=== DICAS IMPORTANTES ===
• Sempre ative o ambiente antes de trabalhar no projeto
• O VS Code detecta automaticamente ambientes na pasta .venv
• Nunca commit a pasta .venv no Git - apenas o requirements.txt
• Atualize o requirements.txt sempre que instalar novas bibliotecas

=== EXEMPLO DE requirements.txt ===
numpy==1.23.5
pandas==1.5.2
matplotlib==3.6.2
