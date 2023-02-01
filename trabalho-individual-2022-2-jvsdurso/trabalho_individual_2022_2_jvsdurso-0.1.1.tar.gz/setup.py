# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src',
 'src.data_pipeline',
 'src.data_pipeline.feature_engineering',
 'src.data_pipeline.pre_processing',
 'src.parser']

package_data = \
{'': ['*'], 'src': ['yamls/*']}

install_requires = \
['altair==4.2.0',
 'attrs==22.2.0',
 'bpemb==0.3.4',
 'certifi==2022.12.7',
 'charset-normalizer==2.1.1',
 'contourpy==1.0.6',
 'coverage==7.0.2',
 'cycler==0.11.0',
 'entrypoints==0.4',
 'exceptiongroup==1.1.0',
 'fonttools==4.38.0',
 'gensim==3.8.3',
 'idna==3.4',
 'importlib-resources==5.10.2',
 'iniconfig==1.1.1',
 'jinja2==3.1.2',
 'joblib==1.2.0',
 'jsonschema==4.17.3',
 'kiwisolver==1.4.4',
 'markupsafe==2.1.1',
 'matplotlib==3.6.2',
 'numpy==1.24.1',
 'packaging==22.0',
 'pandas==1.5.2',
 'pillow==9.4.0',
 'pkgutil-resolve-name==1.3.10',
 'pluggy==1.0.0',
 'pylint>=2.15.10,<3.0.0',
 'pyparsing==3.0.9',
 'pyrsistent==0.19.3',
 'pytest-cov==4.0.0',
 'pytest==7.2.0',
 'python-dateutil==2.8.2',
 'pytz==2022.7',
 'pyyaml==6.0',
 'requests==2.28.1',
 'scikit-learn==1.2.0',
 'scipy==1.9.3',
 'sentencepiece==0.1.97',
 'six==1.16.0',
 'smart-open==6.3.0',
 'sphinx-autodoc-typehints==1.21.8',
 'threadpoolctl==3.1.0',
 'tomli==2.0.1',
 'toolz==0.12.0',
 'tqdm==4.64.1',
 'urllib3==1.26.13',
 'whatlies==0.7.0',
 'zipp==3.11.0']

setup_kwargs = {
    'name': 'trabalho-individual-2022-2-jvsdurso',
    'version': '0.1.1',
    'description': 'Dependências deste projeto.',
    'long_description': '# Trabalho individual de GCES 2022-2\n|Aluno|Matrícula|\n|--|--|\n|João Vitor de Souza Durso|180123459|\n\n## Observação\nPara tornar o repositório privado, tive que deletar o fork do trabalho e refazer tudo no meu próprio GitHub. Por isso, posso ter esquecido alguma informação ou passo no caminho.\n\n| Item | Peso |\n|---|---|\n| 1. Containerização do Banco                      | 1.0 |\n| 2. Containerização da biblioteca + Banco          | 1.5 |\n| 3. Publicação da biblioteca  | 1.5 |\n| 4. Documentação automatizada | 1.5 |\n| 5. Integração Contínua (Build, Test, Lint, Documentação)       | 3.0 |\n| 6. Deploy Contínuo                               | 1.5 |\n\n\n## 1. Containerização do Banco\n\nCriação do [docker-compose.yaml](docker-compose.yaml) com a definição do container do MongoDB.\n\n### docker-compose.yaml\n```yaml\nversion: \'3.5\'\n\nservices:\n  postgres:\n    image: postgres\n    restart: always\n    container_name: postgres\n    env_file:\n      - metabase/config/postgres_exemple.env\n\n  metabase:\n    image: metabase/metabase\n    ports:\n      - 3001:3000\n    env_file:\n      - metabase/config/metabase_database_exemple.env\n    depends_on:\n      - postgres\n```\n\nPara comprovar o funcionamento, basta executar:\n\n```\nsudo docker-compose up --remove-orphans\n```\n```\ndocker exec -it $(docker ps -f "name=mongo" -q) mongosh\n```\n```\nuse admin\n```\n```\ndb.auth(\'lappis\',\'l4pp1s\')\n```\n\n## 2. Containerização da biblioteca + Banco\n\nNessa etapa, criou-se o [Dockerfile](Dockerfile). Depois adicionou-se alterações ao [docker-compose.yaml](docker-compose.yaml) para adicionar a biblioteca quando rodar o Docker.\n\n### docker-compose.yaml\n```yaml\nversion: \'3.5\'\n\nservices:\n  postgres:\n    image: postgres\n    restart: always\n    container_name: postgres\n    env_file:\n      - metabase/config/postgres_exemple.env\n\n  metabase:\n    image: metabase/metabase\n    ports:\n      - 3001:3000\n    env_file:\n      - metabase/config/metabase_database_exemple.env\n    depends_on:\n      - postgres\n\n  lib:\n    build: .\n```\n\n### Dockerfile\n```Dockerfile\nFROM python:3.8 AS python\n\nRUN mkdir /app\n\nCOPY . /app\n\nWORKDIR /app\n\nRUN python -m pip install --upgrade pip \\\n    pip install poetry\n\nRUN poetry install\n\nRUN apt update -y\nRUN apt-get install python3-sphinx -y\nRUN apt-get install doxygen sphinx-common -y\n\nRUN doxygen doxygen.conf -y\nRUN sphinx-build -b html docs/source docs/build\n```\n\nPara ratificar o funcionamento, basta executar:\n\n```\nsudo docker-compose up --remove-orphans\n```\n\n## 3. Publicação da biblioteca\n\nNesta etapa, inicializou-se o poetry:\n\n```\npoetry init\n```\n\nO comando abaixo serve para adicionar todas as dependências do projeto no arquivo [poetry.lock](poetry.lock).\n```\npoetry add $(cat requirements.txt)\n```\n\nO comando abaixo gera a biblioteca das dependências.\n```\npoetry build\n```\n\nOs dois comandos abaixo são para configurar o token do PyPi e publicar a biblioteca no Pypi.\n```\npoetry config pypi-token.pypi <TOKEN>\n```\n\n```\npoetry publish --skip-existing\n```\n\nPara ratificar o sucesso, acesse o link abaixo para ver a biblioteca publicada:\n\n### Link da Biblioteca Publicada\nhttps://pypi.org/project/trabalho-individual-2022-2-jvsdurso/\n\nOu utilize o comando:\n\n```\npip3 install https://pypi.org/project/trabalho-individual-2022-2-jvsdurso/\n```\n\n## 4. Documentação automatizada\n\nNesta etapa, inicializou-se o Doxygen e o Sphinx:\n\nPrimeiro, é preciso instalar o Doxygen:\n\nEm seguida, gera-se um arquivo [Doxyfile](doxygen.conf), colocando as configurações desejadas.\n\n```\ndoxygen -g doxygen.conf\n```\n\n### doxygen.conf\n\n```\n# Doxyfile 1.9.1\n\n# This file describes the settings to be used by the documentation system\n# doxygen (www.doxygen.org) for a project.\n#\n# All text after a double hash (##) is considered a comment and is placed in\n# front of the TAG it is preceding.\n#\n# All text after a single hash (#) is considered a comment and will be ignored.\n# The format is:\n# TAG = value [value, ...]\n# For lists, items can also be appended using:\n# TAG += value [value, ...]\n# Values that contain spaces should be placed between quotes (\\" \\").\n\n#---------------------------------------------------------------------------\n# Project related configuration options\n#---------------------------------------------------------------------------\n\n# The PROJECT_NAME tag is a single word (or a sequence of words surrounded by\n# double-quotes, unless you are using Doxywizard) that should identify the\n# project for which the documentation is generated. This name is used in the\n# title of most generated pages and in a few other places.\n# The default value is: My Project.\n\nPROJECT_NAME           = "trabalho-individual-2022-2-jvsdurso"\n\n# The OUTPUT_DIRECTORY tag is used to specify the (relative or absolute) path\n# into which the generated documentation will be written. If a relative path is\n# entered, it will be relative to the location where doxygen was started. If\n# left blank the current directory will be used.\n\nOUTPUT_DIRECTORY       = "doxygen_output"\n\n#---------------------------------------------------------------------------\n# Configuration options related to the input files\n#---------------------------------------------------------------------------\n\n# The INPUT tag is used to specify the files and/or directories that contain\n# documented source files. You may enter file names like myfile.cpp or\n# directories like /usr/src/myproject. Separate the files or directories with\n# spaces. See also FILE_PATTERNS and EXTENSION_MAPPING\n# Note: If this tag is empty the current directory is searched.\n\nINPUT                  = "src"\n\n#---------------------------------------------------------------------------\n# Configuration options related to the XML output\n#---------------------------------------------------------------------------\n\n# If the GENERATE_XML tag is set to YES, doxygen will generate an XML file that\n# captures the structure of the code including all documentation.\n# The default value is: NO.\n\nGENERATE_XML           = YES\n```\n\nPor fim, gerou-se a documentação em XML executando:\n\n```\ndoxygen doxygen.conf\n```\n\nEm seguida, inicia-se o Sphinx, utilizando os comandos:\n\n```\nmkdir docs\ncd docs\nsphinx-quickstart\n```\n\nAdiciona-se as configurações desejadas:\n\n### conf.py\n```py\n# Configuration file for the Sphinx documentation builder.\n#\n# This file only contains a selection of the most common options. For a full\n# list see the documentation:\n# https://www.sphinx-doc.org/en/master/usage/configuration.html\n\n# -- Path setup --------------------------------------------------------------\n\n# If extensions (or modules to document with autodoc) are in another directory,\n# add these directories to sys.path here. If the directory is relative to the\n# documentation root, use os.path.abspath to make it absolute, like shown here.\n#\nimport os\nimport sys\nsys.path.insert(0, os.path.abspath(\'../../src\'))\n\n\n# -- Project information -----------------------------------------------------\n\nproject = \'trabalho-individual-2022-2-jvsdurso\'\ncopyright = \'2023, João Durso\'\nauthor = \'João Durso\'\n\n\n# -- General configuration ---------------------------------------------------\n\n# Add any Sphinx extension module names here, as strings. They can be\n# extensions coming with Sphinx (named \'sphinx.ext.*\') or your custom\n# ones.\n\nextensions = [\'sphinx.ext.autodoc\',\n    \'sphinx.ext.doctest\',\n    \'sphinx.ext.intersphinx\',\n    \'sphinx.ext.todo\',\n    \'sphinx.ext.coverage\',\n    \'sphinx.ext.mathjax\',\n    \'sphinx.ext.ifconfig\',\n    \'sphinx.ext.viewcode\',\n    \'sphinx.ext.githubpages\']\n\n# Add any paths that contain templates here, relative to this directory.\ntemplates_path = [\'_templates\']\n\n# The suffix(es) of source filenames.\n# You can specify multiple suffix as a list of string:\n#\n# source_suffix = [\'.rst\', \'.md\']\nsource_suffix = \'.rst\'\n\n# The master toctree document.\nmaster_doc = \'index\'\n\n```\n\n## 5. Integração Contínua (Build, Test, Lint, Documentação)\n\nPara criar a integração contínua, criou-se o arquivo [ci-cd.yml](.github/workflows/ci-cd.yml) que acionará o GitHub Actions a cada atualização da master.\n\n### ci-cd.yml\n```yml\nname: GCES CI/CD\n\non:\n  push:\n    branches:\n      - main\n    pull_request:\n      - main\n\nenv:\n  ACTIONS_ALLOW_UNSECURE_COMMANDS: "true"\n\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n    - name: Copy master...\n      uses: actions/checkout@v2\n\n    - name: Config python...\n      uses: actions/setup-python@v2\n      with:\n        python-version: 3.8\n\n    - name: Installing poetry...\n      run: python -m pip install poetry\n\n    - name: Installing sphinx...\n      run: sudo apt install --allow-unauthenticated python3-sphinx -y\n\n    - name: Check for new Python version...\n      run: |\n        NEW_VERSION=$(curl --silent https://www.python.org/ftp/python/ | grep -Eo \'python-[0-9\\.]+\' | sort -V | tail -1)\n        INSTALLED_VERSION=$(python3 --version | awk \'{print $2}\')\n        if [ "$NEW_VERSION" != "$INSTALLED_VERSION" ]; then\n          echo "Updating Python from $INSTALLED_VERSION to $NEW_VERSION"\n          sudo apt-get update\n          sudo apt-get install -y $NEW_VERSION\n        else\n          echo "Python is up-to-date ($INSTALLED_VERSION)"\n        fi\n\n    - name: Installing requirements...\n      run: |\n        python -m pip install --upgrade pip\n        pip install -r requirements.txt \n\n    - name: Watching lint...\n      run: |\n        pip install pylint\n        pylint src\n      continue-on-error: true\n\n    - name: Testing...\n      run: poetry run pytest --cov \n\n    - name: Generate documentation...\n      run: sphinx-build -b html docs/source docs/build\n\n    - name: Publishing in poetry...\n      run: |\n        poetry version patch\n        poetry build -v\n        poetry install\n        poetry config pypi-token.pypi ${{ secrets.PYPI_TOKEN }}\n        poetry publish --skip-existing\n\n```\n\nÉ possível ver o GitHub Actions funcionando no [link](https://github.com/jvsdurso/Trabalho-Individual-2022-2/actions).\n\n## 6. Deploy Contínuo\n\nO deploy contínuo foi feito no mesmo arquivo [ci-cd.yml](.github/workflows/ci-cd.yml) supracitado.\n\n',
    'author': 'jvsdurso',
    'author_email': 'jvsdurso@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
