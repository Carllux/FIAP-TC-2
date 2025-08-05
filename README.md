
# 📊 Postech Challenge - Projeto em Python

Este repositório contém um projeto desenvolvido em Python para análise de dados, modelagem preditiva e entrega via API. Ele aborda o ciclo completo de um projeto de Data Science, utilizando ferramentas modernas e robustas como:

- `pandas` para manipulação de dados
- `scikit-learn`, `LogisticRegression`, `XGBoom`, `LightGBM` e `tensorflow` para modelagem preditiva
- `Optuna` para otimização de hiperparâmetros

---

## ⚙️ Requisitos

- <a href="https://www.python.org/downloads/release/python-3119/">Python 3.11.9</a>
- `git` instalado  
- Acesso ao terminal ou prompt de comando

---

## 🚀 Instalação

> 💡 **Recomendado**: utilize um ambiente virtual (`venv`) para garantir o isolamento das dependências do projeto.

### 1. Clone o repositório de desenvolvimento

```bash
git clone --branch develop https://github.com/Carllux/FIAP-TC-2.git
cd FIAP-TC-2
code .
```

### 2. Crie o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual

**Windows:**

```bash
.\.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 📁 Estrutura do Projeto

```text
.
├── data/                  # Bases de dados originais e transformadas
├── notebooks/             # Jupyter Notebooks com experimentações
├── src/                   # Código-fonte modularizado
│   ├── data/              # Carregamento, transformação e limpeza
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo
```

---

## 🧪 Como Executar os Notebooks

> Todos os notebooks seguem convenções profissionais:
- Células organizadas em blocos funcionais (carregamento, EDA, modelagem etc.)
- Comentários explicativos

Você pode executar os notebooks via Jupyter ou diretamente em ambiente como Google Colab ou VSCode.

---

## 🧵 Boas Práticas Adotadas

- Validação temporal com `TimeSeriesSplit` para dados financeiros
- Pipeline modular com reuso de funções
- Otimização automatizada com `Optuna`
- Avaliação robusta: `classification_report`, `confusion_matrix`, `ROC AUC`

---

## 📌 Observações

- Este projeto é parte de um desafio técnico proposto pela FIAP-POSTECH
- A modelagem está focada em prever movimentos do índice **Ibovespa**, categorizados em **Alta Significativa**, **Neutra** ou **Baixa Significativa**.
