<table>
  <tr>
    <td>
      <img width="75" height="75" alt="Logo Ictus Solutionis" src="https://github.com/user-attachments/assets/13940d0b-4ce4-433b-bcb9-556a9e3ea316">
    </td>
    <td>
      <h1>Ictus Solutionis PAY</h1>
      <b>💳 Maquininha de Cartão em Python com Interface Gráfica</b>
    </td>
  </tr>
</table>

Simulação de uma **maquininha de cartão desenvolvida em Python com CustomTkinter**, criada para aplicar conceitos de lógica de programação e interface gráfica em um sistema de pagamentos.

---

## 📌 Sobre o projeto

O **Ictus Solutionis PAY** é um sistema desenvolvido em Python que simula as principais operações realizadas por uma maquininha de cartão, agora com uma **interface gráfica** em tema escuro.

O usuário informa o **valor da venda**, escolhe o **tipo de pagamento** (débito ou crédito), seleciona a **bandeira do cartão** e, se quiser, define a **quantidade de parcelas**.

Ao aprovar a venda, o sistema exibe um **comprovante** com os dados da transação e guarda a venda em uma lista. Uma segunda janela mostra todas as **vendas de hoje** e o **total do dia**.

> 🎯 **Objetivo:** aplicar conhecimentos de Python, lógica de programação e criação de interfaces na construção de uma aplicação inspirada em sistemas de pagamento reais.

---

## ⚡ Funcionalidades

<table>
  <tr>
    <td>💰</td>
    <td><b>Registro de venda</b></td>
    <td>Campo para informar o valor da transação.</td>
  </tr>
  <tr>
    <td>💳</td>
    <td><b>Débito e crédito</b></td>
    <td>Seleção do tipo de pagamento por caixa de opções.</td>
  </tr>
  <tr>
    <td>🏦</td>
    <td><b>Bandeira do cartão</b></td>
    <td>Seleção entre Visa, Mastercard, Elo, Amex e Hipercard.</td>
  </tr>
  <tr>
    <td>🔢</td>
    <td><b>Parcelamento</b></td>
    <td>Campo opcional de parcelas. Se ficar vazio (ou for 0), assume 1x.</td>
  </tr>
  <tr>
    <td>📅</td>
    <td><b>Data e hora</b></td>
    <td>Registra o momento da venda no formato <code>dd/mm/aaaa hh:mm</code>.</td>
  </tr>
  <tr>
    <td>🧾</td>
    <td><b>Comprovante</b></td>
    <td>Exibe na tela o status <i>APROVADO</i>, data, bandeira, tipo e valor.</td>
  </tr>
  <tr>
    <td>🗂️</td>
    <td><b>Vendas de hoje</b></td>
    <td>Janela separada listando todas as vendas realizadas e o total do dia.</td>
  </tr>
  <tr>
    <td>⚠️</td>
    <td><b>Tratamento de erros</b></td>
    <td>Mostra uma mensagem de erro caso os dados informados sejam inválidos.</td>
  </tr>
</table>

---

## 💳 Bandeiras disponíveis

<table>
  <tr>
    <th>Bandeira</th>
  </tr>
  <tr><td>Visa</td></tr>
  <tr><td>Mastercard</td></tr>
  <tr><td>Elo</td></tr>
  <tr><td>American Express (amex)</td></tr>
  <tr><td>Hipercard</td></tr>
</table>

---

## 💻 Como funciona a interface

### Tela principal

```text
       Ictus Solutionis
┌─────────────────────────┐
│ Valor R$                │
├─────────────────────────┤
│ credito              ▼  │
├─────────────────────────┤
│ visa                 ▼  │
├─────────────────────────┤
│ Parcelas                │
└─────────────────────────┘

┌─────────────────────────┐
│         APROVAR         │
└─────────────────────────┘

┌─────────────────────────┐
│      VENDAS DE HOJE     │
└─────────────────────────┘
```

| Elemento | Tipo | Função |
|---|---|---|
| **Valor R$** | `CTkEntry` | Valor da venda |
| **Tipo** | `CTkComboBox` | `debito` ou `credito` (padrão: crédito) |
| **Bandeira** | `CTkComboBox` | Bandeira do cartão (padrão: visa) |
| **Parcelas** | `CTkEntry` | Número de parcelas (opcional) |
| **APROVAR** | `CTkButton` | Registra a venda e mostra o comprovante |
| **VENDAS DE HOJE** | `CTkButton` | Abre a janela com o histórico do dia |

### 🧾 Exemplo de comprovante

```text
APROVADO!
 29/10/2026 10:00
 mastercard ---- credito
 R$82.00
Salvo! Total hoje: 3
```

### 🗂️ Exemplo da janela "Vendas de Hoje"

```text
1. 29/10/2026 10:00 - R$ 35.00
   amex credito 3x
2. 29/10/2026 10:00 - R$ 135.00
   elo debito 1x
3. 29/10/2026 10:00 - R$ 82.00
   mastercard credito 2x

TOTAL DO DIA: R$ 252.00
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
    <td>🎨 <b>CustomTkinter</b></td>
    <td>Interface gráfica moderna (tema escuro, botões, campos e janelas)</td>
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

`Variáveis` • `Funções` • `Listas` • `Dicionários` • `For / Enumerate` • `If / Else` • `Try / Except` • `Datetime` • `Formatação de Strings (f-string)` • `Operações Matemáticas` • `Interface Gráfica (CustomTkinter)` • `Eventos de botão`

---

## 📂 Estrutura do projeto

```text
ictus-solutionis/
│
├── 📄 main.py
└── 📖 README.md
```

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone URL-DO-REPOSITORIO
```

### 2. Acesse a pasta

```bash
cd ictus-solutionis
```

### 3. Instale a dependência

```bash
pip install customtkinter
```

> 💡 No VS Code, se aparecer erro de importação, aperte `Ctrl + Shift + P`, digite **Install Missing Imports** e reinicie o editor.

### 4. Execute o programa

```bash
python main.py
```

> **Requisitos:** Python 3 e a biblioteca `customtkinter` instalados no computador.

---

## 🔄 Fluxo do sistema

```text
Abrir o programa
      │
      ▼
Informar valor, tipo, bandeira e parcelas
      │
      ▼
Clicar em APROVAR
      │
      ▼
Dados válidos? ── Não ──► Mostrar mensagem de erro
      │
     Sim
      │
      ▼
Salvar venda na lista
      │
      ▼
Exibir comprovante
      │
      ▼
Limpar campos (pronto para nova venda)

A qualquer momento:
VENDAS DE HOJE ──► abre janela com a lista e o total do dia
```

---

## 🚧 Melhorias futuras

- [ ] Salvar vendas em arquivo ou banco de dados (hoje o histórico some ao fechar o programa)
- [ ] Mostrar o valor de cada parcela no comprovante
- [ ] Bloquear parcelamento quando o pagamento for no débito
- [ ] Adicionar taxas e juros
- [ ] Melhorar a validação das entradas (valores negativos, parcelas acima de 12)
- [ ] Simular pagamentos recusados
- [ ] Aumentar a janela principal para melhorar a legibilidade
- [ ] Gerar comprovantes em arquivos

---

## 🎓 Finalidade do projeto

O **Ictus Solutionis PAY** foi desenvolvido com finalidade educacional, buscando colocar em prática conhecimentos de **Python, lógica de programação e desenvolvimento de software** através da criação de uma solução inspirada em sistemas utilizados no cotidiano.

---

<sub>💳 <b>Ictus Solutionis</b> — Tecnologia transformando ideias em soluções.</sub>
