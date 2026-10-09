# 💰 Calculadora de Salário Líquido

Aplicação web desenvolvida em **Python** com **Flask** para calcular o salário líquido a partir do salário bruto e do número de dependentes.

O projeto foi criado como atividade prática de desenvolvimento web e demonstra o uso de formulários HTML, rotas Flask, validação de dados, tratamento de erros e renderização dinâmica com Jinja2.

## ✨ Funcionalidades

- ✅ Cálculo do desconto de INSS;
- ✅ Cálculo condicional do Imposto de Renda;
- ✅ Acréscimo de R$ 200,00 por dependente;
- ✅ Aceitação de valores decimais com ponto ou vírgula;
- ✅ Validação de salários negativos;
- ✅ Validação de dependentes negativos;
- ✅ Tratamento de entradas não numéricas;
- ✅ Exibição detalhada dos valores calculados;
- ✅ Interface web simples e responsiva.

## 📐 Regras de cálculo

O salário líquido é calculado de acordo com a fórmula:

```text
Salário líquido = salário bruto - INSS - IR + valor dos dependentes
```

As regras utilizadas são:

| Item | Regra |
| --- | --- |
| INSS | 8% sobre o salário bruto |
| Imposto de Renda | 15% sobre o salário bruto quando ele for superior a R$ 2.500,00 |
| Dependentes | Acréscimo de R$ 200,00 por dependente |

### Exemplo

Para um salário bruto de **R$ 3.000,00** e **1 dependente**:

```text
INSS = 3.000 × 0,08 = R$ 240,00
IR = 3.000 × 0,15 = R$ 450,00
Dependentes = 1 × R$ 200,00 = R$ 200,00

Salário líquido = 3.000 - 240 - 450 + 200
Salário líquido = R$ 2.510,00
```

> **Observação:** as alíquotas deste projeto são simplificadas e foram definidas exclusivamente para fins didáticos. Elas não representam necessariamente as regras tributárias oficiais vigentes.

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **Flask**
- **HTML5**
- **CSS3**
- **Jinja2**

## 📁 Estrutura do projeto

```text
calculadora_salario_flask/
├── app.py
├── requirements.txt
├── README.md
└── templates/
    └── form.html
```

## 🚀 Como executar localmente

A aplicação é executada em um servidor local Flask. Antes de começar, verifique se o Python 3 está instalado:

```bash
python3 --version
```

No Windows, também podem ser utilizados:

```powershell
python --version
py --version
```

Caso nenhum comando seja reconhecido, instale o Python pelo site oficial [python.org](https://www.python.org/downloads/). No instalador do Windows, marque a opção **Add Python to PATH**.

### 🍎 macOS

Abra o Terminal e entre na pasta do projeto. Exemplo:

```bash
cd /caminho/para/calculadora_salario_flask
```

Crie o ambiente virtual:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Inicie o servidor:

```bash
python app.py
```

Se o ambiente virtual não estiver ativado, execute diretamente:

```bash
./venv/bin/python app.py
```

### 🐧 Linux

Abra o terminal e entre na pasta do projeto:

```bash
cd /caminho/para/calculadora_salario_flask
```

Crie o ambiente virtual:

```bash
python3 -m venv venv
```

> Em algumas distribuições, pode ser necessário instalar o pacote de ambientes virtuais antes: `sudo apt install python3-venv`.

Ative o ambiente virtual:

```bash
source venv/bin/activate
```

Instale as dependências e inicie a aplicação:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python app.py
```

### 🪟 Windows PowerShell

Abra o PowerShell e entre na pasta do projeto:

```powershell
cd C:\caminho\para\calculadora_salario_flask
```

Crie o ambiente virtual:

```powershell
py -3 -m venv venv
```

Ative o ambiente virtual:

```powershell
.\venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Inicie a aplicação:

```powershell
python app.py
```

Se o PowerShell bloquear a ativação do ambiente virtual, execute o comando abaixo apenas para o usuário atual e repita a ativação:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### 🪟 Windows Prompt de Comando (CMD)

Abra o Prompt de Comando e execute:

```bat
cd C:\caminho\para\calculadora_salario_flask
py -3 -m venv venv
venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python app.py
```

### 🌐 Acessar a aplicação

Quando o servidor iniciar, será exibida uma mensagem semelhante a:

```text
* Running on http://127.0.0.1:5000
```

Abra no navegador:

- http://127.0.0.1:5000
- http://localhost:5000

Mantenha o terminal aberto enquanto estiver utilizando a aplicação. Para encerrar o servidor, pressione `Ctrl + C`.

### ⏹️ Desativar o ambiente virtual

Depois de parar a aplicação, desative o ambiente virtual com:

```bash
deactivate
```

Para executar novamente em uma próxima ocasião, não é necessário recriar o ambiente virtual. Basta acessar a pasta, ativá-lo, se necessário, e iniciar o servidor:

```bash
python app.py
```

## 🧪 Cenários de validação

| Salário bruto | Dependentes | Resultado esperado |
| ---: | ---: | --- |
| R$ 3.000,00 | 2 | Salário líquido de R$ 2.710,00 |
| R$ 2.000,00 | 1 | Salário líquido de R$ 2.040,00 |
| R$ 1.000,00 | 0 | Salário líquido de R$ 920,00 |
| R$ -500,00 | 1 | Erro: salário negativo |
| `abc` | 2 | Erro: entrada inválida |
| R$ 2.000,00 | -1 | Erro: dependentes negativos |

## 🔒 Validação no backend

Os dados são validados no servidor antes do cálculo. Essa abordagem garante que as regras sejam aplicadas mesmo quando uma validação do navegador é ignorada ou alterada.

O backend verifica:

- se os campos foram enviados;
- se o salário pode ser convertido para número;
- se o número de dependentes é inteiro;
- se o salário é finito e não negativo;
- se a quantidade de dependentes não é negativa.

Quando há uma entrada inválida, a aplicação reapresenta o formulário com uma mensagem de erro e retorna o status HTTP `400`.

## 🧹 Encerrar o ambiente virtual

Depois de finalizar o uso da aplicação:

```bash
deactivate
```

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais.
