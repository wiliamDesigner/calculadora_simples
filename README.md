# 🧮 Calculadora Simples

Calculadora básica feita em Python, executada via terminal, que realiza as quatro operações matemáticas fundamentais.

## 🎯 Objetivo

Projeto desenvolvido para praticar conceitos iniciais de lógica de programação em Python, incluindo:

- Entrada e conversão de dados (`input`, `int`)
- Estruturas condicionais (`if` / `elif`)
- Estruturas de repetição (`while`)
- Operadores aritméticos

## ⚙️ O que a calculadora faz

- ✅ Pede dois números ao usuário
- ✅ Pergunta qual operação deseja realizar: soma (`+`), subtração (`-`), multiplicação (`*`) ou divisão (`/`)
- ✅ Exibe o resultado da operação escolhida
- ✅ Pergunta se o usuário quer fazer outro cálculo, repetindo o processo enquanto a resposta for "sim"

## 🛠️ Tecnologias utilizadas

- Python 3

## ▶️ Como rodar o projeto

1. Certifique-se de ter o Python instalado na máquina
2. No terminal, execute:
   ```
   python calculadora_simples.py
   ```
3. Siga as instruções exibidas no terminal

## 🖥️ Exemplo de uso

```
--Calculadora--
Digite seu primeiro numero:10
Digite seu segundo numero:5
Digite sua operação: +/-*:+
Sua soma é:  15
Deseja fazer mais calculo?
sim
```

## 💡 Possíveis melhorias futuras

- Validar se o usuário realmente digitou números (hoje o programa quebra se for digitado texto ou algo que não seja número)
- Tratar divisão por zero, que atualmente gera um erro e encerra o programa
- Aceitar qualquer variação de resposta para continuar (ex: "s", "sim", "yes"), e não apenas exatamente "sim"
- Adicionar mais operações, como potência, raiz quadrada ou resto de divisão (`%`)
- Transformar em uma versão com interface gráfica (usando, por exemplo, Tkinter)

## 👤 Autor

Projeto desenvolvido como exercício prático de lógica de programação em Python.
