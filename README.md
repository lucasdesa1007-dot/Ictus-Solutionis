<table>
  <tr>
    <td>
      <img width="75" height="75" alt="Logo Ictus Solutionis" src="https://github.com/user-attachments/assets/13940d0b-4ce4-433b-bcb9-556a9e3ea316">
    </td>
    <td>
      <h1>Ictus Solutionis</h1>
      <b>💳 Maquininha de Cartão em Python</b>
    </td>
  </tr>
</table>

Simulação de uma **maquininha de cartão desenvolvida em Python**, criada para aplicar conceitos de lógica de programação em um sistema de pagamentos.

---

## 📌 Sobre o projeto

O **Ictus Solutionis** é um sistema desenvolvido em Python que simula as principais operações realizadas por uma maquininha de cartão.

O usuário informa o **valor da venda**, escolhe a **forma de pagamento**, seleciona a **bandeira do cartão** e, caso escolha crédito, pode definir a quantidade de parcelas.

Ao final da operação, o sistema gera um **comprovante de pagamento** contendo os dados da transação.

> 🎯 **Objetivo:** aplicar conhecimentos de Python e lógica de programação na construção de uma aplicação inspirada em sistemas de pagamento reais.

---

## ⚡ Funcionalidades

<table>
  <tr>
    <td>💰</td>
    <td><b>Registro de venda</b></td>
    <td>Permite informar o valor da transação.</td>
  </tr>
  <tr>
    <td>💳</td>
    <td><b>Débito e crédito</b></td>
    <td>Possibilidade de selecionar a forma de pagamento.</td>
  </tr>
  <tr>
    <td>🏦</td>
    <td><b>Bandeira do cartão</b></td>
    <td>Seleção entre diferentes bandeiras.</td>
  </tr>
  <tr>
    <td>🔢</td>
    <td><b>Parcelamento</b></td>
    <td>Compras no crédito podem ser parceladas.</td>
  </tr>
  <tr>
    <td>🧮</td>
    <td><b>Cálculo automático</b></td>
    <td>Calcula automaticamente o valor de cada parcela.</td>
  </tr>
  <tr>
    <td>📅</td>
    <td><b>Data e hora</b></td>
    <td>Registra o momento em que a compra foi realizada.</td>
  </tr>
  <tr>
    <td>🧾</td>
    <td><b>Comprovante</b></td>
    <td>Exibe os principais dados da transação.</td>
  </tr>
  <tr>
    <td>🔄</td>
    <td><b>Novas vendas</b></td>
    <td>Permite realizar várias vendas durante a execução.</td>
  </tr>
</table>

---

## 💳 Bandeiras disponíveis

<table>
  <tr>
    <th>Código</th>
    <th>Bandeira</th>
  </tr>
  <tr>
    <td><code>0</code></td>
    <td>Visa</td>
  </tr>
  <tr>
    <td><code>1</code></td>
    <td>Mastercard</td>
  </tr>
  <tr>
    <td><code>2</code></td>
    <td>Elo</td>
  </tr>
  <tr>
    <td><code>3</code></td>
    <td>American Express</td>
  </tr>
  <tr>
    <td><code>4</code></td>
    <td>Hipercard</td>
  </tr>
</table>

---

## 🖥️ Demonstração

### Iniciando uma venda

```text id="msuzxz"
==================================================
 Ictus Solutionis - MAQUININHA DE CARTÃO
==================================================

--- NOVA VENDA ---
Valor da venda: R$ 120.00

Tipo de pagamento:
[1] Débito
[2] Crédito
Escolha 1 ou 2: 2

Bandeira do cartão:
[0] visa
[1] mastercard
[2] elo
[3] amex
[4] hipercard

Escolha 0 ate 4: 0

Bandeira do cartao escolhida: visa

Quantas parcelas? (1 a 12) [padrão 1]: 3
```

### 🧾 Comprovante gerado

```text id="zht08g"
==================================================
 COMPROVANTE DE PAGAMENTO
==================================================
Data/Hora: 28/10/2026 18:30:00
Bandeira: visa
Tipo: Crédito parcelado
Valor gasto pela pessoa: R$ 120.00
Parcelas: 3x de R$ 40.00
Status: APROVADO
==================================================
```

---

## 🛠️ Tecnologias utilizadas

<table>
  <tr>
    <th>Tecnologia</th>
    <th>Utilização</th>
  </tr>
  <tr>
    <td>🐍 <b>Python 3</b></td>
    <td>Desenvolvimento da aplicação</td>
  </tr>
  <tr>
    <td>📅 <b>Datetime</b></td>
    <td>Registro da data e horário das transações</td>
  </tr>
  <tr>
    <td>🔧 <b>Git</b></td>
    <td>Controle de versão</td>
  </tr>
  <tr>
    <td>🐙 <b>GitHub</b></td>
    <td>Hospedagem e compartilhamento do código</td>
  </tr>
</table>

---

## 🧠 Conceitos aplicados

Durante o desenvolvimento do projeto foram utilizados:

`Variáveis` • `Input` • `Output` • `If / Elif / Else` • `While` • `Try / Except` • `Datetime` • `Formatação de Strings` • `Operações Matemáticas`

---

## 📂 Estrutura do projeto

```text id="ofclbi"
ictus-solutionis/
│
├── 📄 main.py
└── 📖 README.md
```

---

## ▶️ Como executar

### 1. Clone o repositório

```bash id="m2c08u"
git clone URL-DO-REPOSITORIO
```

### 2. Acesse a pasta

```bash id="8h97ny"
cd ictus-solutionis
```

### 3. Execute o programa

```bash id="xwyclz"
python main.py
```

> **Requisito:** é necessário ter o Python 3 instalado no computador.

---

## 🔄 Fluxo do sistema

```text id="oh1ngb"
Iniciar programa
      │
      ▼
Informar valor
      │
      ▼
Escolher pagamento
      │
      ├── Débito ──────────────┐
      │                        │
      └── Crédito              │
            │                  │
            ▼                  │
      Escolher parcelas        │
            │                  │
            └─────────┬────────┘
                      ▼
             Escolher bandeira
                      │
                      ▼
              Calcular valores
                      │
                      ▼
             Gerar comprovante
                      │
                      ▼
              Nova venda?
                 │        │
                Sim      Não
                 │        │
                 ▼        ▼
              Reinicia   Encerrar
```

---

## 🚧 Melhorias futuras

- [ ] Salvar vendas em um banco de dados
- [ ] Criar histórico de transações
- [ ] Adicionar taxas e juros
- [ ] Melhorar a validação das entradas
- [ ] Simular pagamentos recusados
- [ ] Desenvolver uma interface gráfica
- [ ] Gerar comprovantes em arquivos

---

## 🎓 Finalidade do projeto

O **Ictus Solutionis** foi desenvolvido com finalidade educacional, buscando colocar em prática conhecimentos de **Python, lógica de programação e desenvolvimento de software** através da criação de uma solução inspirada em sistemas utilizados no cotidiano.

---

<sub>💳 <b>Ictus Solutionis</b> — Tecnologia transformando ideias em soluções.</sub>
