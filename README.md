![Python 3.11.9](https://img.shields.io/badge/Python-3.11.9-blue.svg)![Libs](https://img.shields.io/badge/Libs-Scikit--learn%20|%20XGBoost%20|%20Optuna-orange)![Status](https://img.shields.io/badge/Status-Finalizado-green)


# 📊 Tech Challenge: Modelo Preditivo para o IBOVESPA

Este repositório contém o desenvolvimento do projeto final para a **Fase 02** do curso de Pós-Graduação em Data Analytics da **FIAP POS-TECH**.


## 🎯 O Problema

A missão consistiu em atuar como cientista de dados em um fundo de investimentos brasileiro, com o desafio de criar um modelo preditivo da tendência diária do IBOVESPA.  

Sendo o objetivo classificar os movimentos do índice em duas categorias:
- **Alta Significativa**
- **Neutra**/**Baixa Significativa**

Servindo como uma ferramenta de apoio à tomada de decisão para analistas quantitativos.

---
O projeto percorre todas as etapas do pipeline de Data Science:
- Aquisição e tratamento de dados
- Engenharia de atributos
- Modelagem preditiva com múltiplos algoritmos
- Seleção e validação rigorosa do modelo final

---


## ⚙️ Requisitos

- [Python 3.11.9](https://www.python.org/downloads/release/python-3119/)
- `git` instalado
- Acesso ao terminal ou prompt de comando

---

## 🚀 Instalação

> 💡 Recomendado: utilize um ambiente virtual (`venv`) para garantir o isolamento das dependências.

### 1. Clone o repositório

```bash
git clone --branch main https://github.com/Carllux/FIAP-TC-2.git
cd FIAP-TC-2
```

### 2. Crie o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual

- **Windows**:
  ```bash
  .\.venv\Scripts\activate
  ```

- **Linux/macOS**:
  ```bash
  source .venv/bin/activate
  ```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

> ⚠️ **Observação**: Caso encontre erros relacionados a compiladores C++ no Windows, pode ser necessário instalar o **Microsoft C++ Build Tools**.

---

## 🛠️ Metodologia Aplicada

### 1. Aquisição e Pré-processamento dos Dados

- Coleta dos dados históricos diários do IBOVESPA.
- Limpeza e padronização.
- Conversão para `DatetimeIndex`.
- Definição da variável-alvo (target).

### 2. Engenharia de Atributos

Criação de um conjunto diversificado de features:

- **Atributos Autoregressivos**: médias móveis, retornos defasados, etc.  
- **Volatilidade e Candlestick**: variações entre máximas/mínimas e proporções de sombras.  
- **Atributos Exógenos**: variações do Dólar (USD/BRL), S&P 500 e Petróleo Brent.  
- **Interações**: combinações entre volatilidade e tendência.

### 3. Estratégia de Modelagem e Validação

- **Modelagem por Regimes de Mercado**:  
  Segmentação da série temporal em períodos como:
  - "Boom das Commodities"
  - "Pandemia"
  - "Pós-Pandemia"

- **Modelos Testados**:
  - Regressão Logística
  - XGBoost
  - LSTM

- **Otimização de Hiperparâmetros**:
  - Utilização da biblioteca **Optuna**.

- **Validação Temporal Robusta**:
  - Divisão dos dados em conjuntos de **Treino**, **Validação** e **Teste** respeitando a ordem cronológica.

### 4. Modelo Final Selecionado

- **Modelo**: Regressão Logística  
- **Regime**: Pós-Pandemia (Juros Altos)  
- **Justificativa**:
  - Melhor desempenho na classe de maior interesse (Alta)
  - Após balanceamento com `class_weight='balanced'`
  - **Recall** de 41% e **F1-Score** de 0.39 para a classe 'Alta'

---

## 📁 Estrutura do Projeto

```plaintext
.
├── data/                  # Bases de dados originais e transformadas
├── docs/                  # PDF contendo o storytelling técnico do código
├── notebooks/             # Jupyter Notebooks com experimentações
├── src/                   # Código-fonte modularizado
│   └── data/              # Carregamento, transformação e limpeza
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo
```

---

## 🧪 Como Executar os Notebooks

Os notebooks seguem uma estrutura clara, com células organizadas em blocos funcionais e comentários explicativos.

Você pode executá-los em ambientes como:
- Jupyter Notebook
- Google Colab
- VSCode (com extensão Python ativa)

### Ordem recomendada:
- `Com exceção do notebook 00_data_investigation.ipynb, é recomendada a execução de todos os notebooks de forma linear`

1. `01_Exploracao_e_Feature_Engineering.ipynb`  
2. `02_Modelagem_e_Validacao.ipynb`

---

## 🧵 Boas Práticas Adotadas

- ✅ **Validação Temporal Robusta**
- ✅ **Modelagem por Regimes de Mercado**
- ✅ **Tratamento de Desbalanceamento com `class_weight`**
- ✅ **Otimização Automatizada com Optuna**
- ✅ **Pipeline Modular e Reutilizável**
- ✅ **Avaliação Holística com múltiplas métricas**:
  - `classification_report`
  - `confusion_matrix`
  - `ROC AUC`

---

## 📬 Contato

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/carlos-vinicius-nascimento-de-jesus/)
