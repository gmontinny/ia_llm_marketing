# 📝 Gerador de Conteúdo para Marketing com IA

Aplicação de geração automatizada de conteúdo para marketing digital, utilizando LLMs (Large Language Models) para criar textos adaptados ao público-alvo e canal de divulgação.

## 📋 Sobre o Projeto

Este projeto nasceu da necessidade de automatizar a criação de conteúdo para departamentos de marketing, permitindo gerar textos otimizados para diferentes plataformas (Instagram, LinkedIn, Blog, etc.) com controle sobre tom, tamanho, público-alvo e palavras-chave de SEO.

A aplicação suporta múltiplos provedores de IA:
- **Groq** com o modelo Llama 3.3 70B (gratuito, baixa latência)
- **OpenAI** com o modelo GPT-4o (pago, alta qualidade)

Ambos são integrados através do framework **LangChain**, com interface web construída em **Streamlit**.

## 🚀 Funcionalidades

- Seleção do provedor de IA (Groq ou OpenAI) diretamente na interface
- Geração de conteúdo para múltiplas plataformas (Instagram, Facebook, LinkedIn, Blog, E-mail)
- Controle do tom da mensagem (Normal, Informativo, Inspirador, Urgente, Informal)
- Ajuste do tamanho do texto (Curto, Médio, Longo, 1 parágrafo, 1 página)
- Segmentação por público-alvo (Geral, Jovens adultos, Famílias, Idosos, Adolescentes)
- Inclusão opcional de CTA (Call to Action)
- Geração automática de hashtags relevantes
- Inserção de palavras-chave para otimização SEO

## 🏗️ Arquitetura

```
ia_llm_marketing/
├── .env                 # Variáveis de ambiente (chaves de API, configurações)
├── .env.example         # Exemplo de .env para referência (sem dados sensíveis)
├── .gitignore           # Arquivos ignorados pelo Git
├── Dockerfile           # Imagem Docker da aplicação
├── docker-compose.yml   # Orquestração do container
├── requirements.txt     # Dependências do projeto
├── app.py               # Interface Streamlit (ponto de entrada)
├── notebook/            # Notebook original de desenvolvimento
│   └── LLMs para empresas e negócios - Marketing.ipynb
└── src/
    ├── __init__.py
    ├── config.py        # Configurações, constantes e carregamento do .env
    ├── prompts.py       # Dataclass de requisição e construção dinâmica do prompt
    └── chain.py         # Factory de LLMs e execução da chain LangChain
```

### Descrição dos Módulos

| Módulo | Responsabilidade |
|--------|-----------------|
| `config.py` | Carrega variáveis de ambiente (Groq e OpenAI) e define constantes da aplicação (provedores, plataformas, tons, tamanhos, públicos) |
| `prompts.py` | Define a estrutura de dados `ContentRequest` e monta o prompt dinâmico com base nos parâmetros do usuário |
| `chain.py` | Factory que instancia o modelo LLM (Groq ou OpenAI) e executa a chain LangChain (template → modelo → parser) |
| `app.py` | Interface web com formulário de entrada, seleção de provedor e exibição do resultado |

## ⚙️ Pré-requisitos

- Python 3.10+
- Conta na [Groq](https://console.groq.com/) com API key gerada
- (Opcional) Conta na [OpenAI](https://platform.openai.com/) com API key e créditos
- (Opcional) [Docker](https://www.docker.com/) e Docker Compose para execução via container

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd ia_llm_marketing
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Crie o arquivo `.env` a partir do exemplo:
```bash
cp .env.example .env
```

5. Edite o `.env` com suas chaves de API:
```env
# Groq (gratuito)
GROQ_API_KEY=sua_chave_groq_aqui
MODEL_NAME=llama-3.3-70b-versatile
TEMPERATURE=0.7

# OpenAI (pago)
OPENAI_API_KEY=sua_chave_openai_aqui
OPENAI_MODEL=gpt-4o
```

> - Para gerar sua API key da Groq, acesse: https://console.groq.com/keys
> - Para gerar sua API key da OpenAI, acesse: https://platform.openai.com/api-keys

## ▶️ Como Executar

### Localmente

```bash
streamlit run app.py
```

A aplicação será aberta automaticamente no navegador em `http://localhost:8501`.

### Com Docker

```bash
docker compose up --build
```

A aplicação estará disponível em `http://localhost:8501`.

Para rodar em segundo plano:
```bash
docker compose up --build -d
```

Para parar:
```bash
docker compose down
```

## 🖥️ Como Usar

1. Selecione o **Provedor de IA** desejado (Groq ou OpenAI)
2. Preencha o campo **Tema** com o assunto desejado (ex: "alimentação saudável")
3. Selecione a **Plataforma** de destino do conteúdo
4. Escolha o **Tom**, **Tamanho** e **Público-alvo**
5. Opcionalmente, marque as opções de **CTA** e **Hashtags**
6. Adicione **Palavras-chave** para SEO se necessário
7. Clique em **🚀 Gerar conteúdo**

O resultado será exibido logo abaixo do formulário, formatado em Markdown.

## 🧠 Tecnologias Utilizadas

| Tecnologia | Uso |
|-----------|-----|
| [LangChain](https://python.langchain.com/) | Orquestração de prompts e chains com LLMs |
| [Groq](https://groq.com/) | Provedor de inferência de modelos open source com baixa latência |
| [OpenAI](https://openai.com/) | Provedor de modelos proprietários de alta performance (GPT-4o) |
| [Llama 3.3 70B](https://huggingface.co/meta-llama) | Modelo open source utilizado via Groq |
| [Streamlit](https://streamlit.io/) | Framework para construção da interface web |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Gerenciamento de variáveis de ambiente |
| [Docker](https://www.docker.com/) | Containerização da aplicação |

## 🐳 Docker

O projeto inclui suporte completo a Docker para facilitar o deploy e a execução em qualquer ambiente.

| Arquivo | Descrição |
|---------|-----------|
| `Dockerfile` | Imagem baseada em Python 3.11 slim, instala dependências e executa o Streamlit |
| `docker-compose.yml` | Orquestra o container, carrega variáveis do `.env` e expõe a porta 8501 |

A imagem final é leve (~200MB) por utilizar `python:3.11-slim` e `--no-cache-dir` na instalação de pacotes.

## 🔄 Modelos Alternativos

### Groq (gratuito)

Suporta qualquer modelo disponível na Groq. Para trocar, altere `MODEL_NAME` no `.env`:

```env
MODEL_NAME=llama-3.3-70b-versatile
MODEL_NAME=llama3-70b-8192
MODEL_NAME=mixtral-8x7b-32768
```

Consulte os modelos disponíveis em: https://console.groq.com/docs/rate-limits

### OpenAI (pago)

Suporta qualquer modelo da OpenAI. Para trocar, altere `OPENAI_MODEL` no `.env`:

```env
OPENAI_MODEL=gpt-4o
OPENAI_MODEL=gpt-4o-mini
OPENAI_MODEL=gpt-4-turbo
```

Consulte modelos e preços em: https://platform.openai.com/docs/models

## 📌 Observações

- A temperatura controla a criatividade do modelo: valores mais altos (0.8–1.0) geram textos mais criativos, valores mais baixos (0.0–0.4) geram textos mais determinísticos
- O projeto foi desenvolvido inicialmente como notebook no Google Colab e posteriormente convertido para uma aplicação Streamlit profissional
- A arquitetura com factory pattern permite adicionar novos provedores facilmente sem alterar a lógica da chain
- As chaves de API nunca devem ser commitadas no repositório — o `.gitignore` já está configurado para ignorar o `.env`
- O arquivo `.env.example` serve como referência para configuração, sem expor dados sensíveis
- A OpenAI cobra por uso de tokens — consulte https://openai.com/api/pricing/ para estimativas de custo

## 📄 Licença

Este projeto é de uso educacional.
