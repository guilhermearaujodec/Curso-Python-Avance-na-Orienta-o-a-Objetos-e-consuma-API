
-----

# 📚 Projeto: API de Restaurantes - Python com Orientação a Objetos

## 🚀 Sobre o Projeto

Este projeto foi desenvolvido como parte do curso **"Python: avance na Orientação a Objetos e consuma API"** da Alura. O objetivo principal foi aplicar os conceitos de **Orientação a Objetos (OO)** em Python, ao mesmo tempo em que se aprende a **consumir uma API externa** e a **criar uma API local** utilizando o *framework* **FastAPI**.

A aplicação realiza as seguintes funções:

1.  **Consome Dados:** Utiliza a biblioteca `requests` para obter dados de restaurantes a partir de uma API externa.
2.  **Modelagem OO:** Os dados de restaurantes são estruturados e manipulados através de classes Python (Orientação a Objetos).
3.  **Criação de API Local:** Uma API local é criada com **FastAPI** e executada com **Uvicorn**, expondo *endpoints* que retornam os dados de restaurantes tratados.

-----

## 🛠️ Tecnologias Utilizadas

As seguintes tecnologias e bibliotecas foram essenciais para o desenvolvimento e execução deste projeto:

| Categoria | Tecnologia | Descrição |
| :--- | :--- | :--- |
| **Linguagem** | Python | Linguagem de programação principal. |
| **Ambiente** | venv | Módulo padrão do Python para criar ambientes virtuais isolados. |
| **Web Framework** | FastAPI | Framework moderno e rápido para criar APIs em Python. |
| **Servidor** | Uvicorn | Servidor ASGI (Asynchronous Server Gateway Interface) para executar o FastAPI. |
| **Requisições HTTP** | Requests | Biblioteca simples e elegante para fazer requisições HTTP (consumir a API externa). |
| **Dependências** | `requirements.txt` | Arquivo contendo todas as dependências do projeto. |

-----

## ⚙️ Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

### 1\. Clonar o Repositório

```bash
# Clone o repositório para a sua máquina
git clone https://github.com/guilhermearaujodec/Curso-Python-Avance-na-Orienta-o-a-Objetos-e-consuma-API.git

# Navegue até o diretório do projeto
cd Curso-Python-Avance-na-Orienta-o-a-Objetos-e-consuma-API
```

### 2\. Configurar o Ambiente Virtual (`venv`)

É altamente recomendado usar um ambiente virtual para isolar as dependências do projeto.

1.  **Criar o Ambiente Virtual:**
    ```bash
    python -m venv venv
    ```
2.  **Ativar o Ambiente Virtual:**
      * **Windows (Command Prompt/PowerShell):**
        ```bash
        .\venv\Scripts\activate
        ```
      * **Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```

### 3\. Instalar as Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas necessárias listadas no arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

As bibliotecas instaladas incluem: `fastapi`, `uvicorn`, `requests`.

-----

### 4\. Executar a API Local (`Uvicorn`)

O projeto utiliza o **Uvicorn** para rodar a API local construída com **FastAPI**.

1.  **Certifique-se de que o ambiente virtual está ativado.**

2.  **Execute o servidor:**

    ```bash
    uvicorn main:app --reload
    ```

      * `main:app`: Indica que a aplicação principal (`app`) está definida no arquivo `main.py`.
      * `--reload`: Habilita o modo de *reload*, que reinicia o servidor automaticamente a cada alteração no código.

3.  **Acesse a API:**
    Após a execução, a API estará acessível em:

      * 🔗 **URL Base:** `http://127.0.0.1:8000`
      * 📄 **Documentação Interativa (Swagger UI):** `http://127.0.0.1:8000/docs`

-----

## 🌎 API Externa Consumida

Este projeto consome uma API externa para obter a lista inicial de restaurantes.

  * **URL da API Externa:** `https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json`

O código utiliza a biblioteca `requests` para fazer a requisição a este *endpoint*.

-----

## 🛣️ Endpoints da API Local

A API local expõe os dados tratados dos restaurantes nos seguintes *endpoints* (acesse via `http://127.0.0.1:8000/docs` para testar):

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| **GET** | `/api/hello` | Endpoint que exibe uma mensagem incrível do mundo da programação!  |
| **GET** | `/api/restaurantes` | Endpoint que retorna uma lista com todos os itens de menu de **todos** os restaurantes. |
| **GET** | `/api/restaurantes/?restaurante={nome_do_restaurante}` | Retorna os dados de um restaurante específico pelo seu nome. |

-----

## 🛑 Desativar o Ambiente Virtual

Para sair do ambiente virtual e retornar ao seu terminal normal, use o comando:

```bash
deactivate
```
