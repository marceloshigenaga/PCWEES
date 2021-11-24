# PCWEES
Trata-se de um portal que catalogará e disponibilizará exemplos trabalhados de projetos de Engenharia de Software que possam ser usados por professores para apoiar o ensino da referida disciplina.

# Setup
Siga estas instruções para executar o projeto localmente. Isso requer Python 3 e o gerenciador de pacotes pip.

```bash
# Crie um ambiente virtual
python -m venv env

# Ative o ambiente virtual (Bash para Linux ou Mac)
. env/bin/activate

# Ative o ambiente virtual (cmd / PowerShell para Windows)
./env/Scripts/activate

# Instale requirements
pip install -r requirements.txt

# Vá para a pasta do aplicativo Django
cd pcwees

# Setup banco de dados.
./manage.py migrate

# Execute o servidor de desenvolvimento.
./manage.py runserver

# Agora você pode ver o projeto em http://localhost:8000
```
