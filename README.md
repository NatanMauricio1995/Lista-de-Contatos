# Sistema de Agenda de Contatos - Python

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

Sistema de gerenciamento de contatos desenvolvido em Python com operações CRUD completas e interface de linha de comando. Projeto acadêmico que demonstra aplicação prática de estruturas de dados e validação de entrada.

## Sobre o Projeto

Este sistema foi desenvolvido para consolidar conhecimentos em programação Python, focando especificamente em:

- **Operações CRUD** (Create, Read, Update, Delete)
- **Estruturas de dados** com dicionários Python
- **Validação rigorosa** de entrada de dados
- **Interface de usuário** intuitiva e organizada
- **Tratamento de exceções** e casos edge
- **Persistência de dados** em memória durante execução

## Funcionalidades Implementadas

### Operações de Gerenciamento
- **Adicionar Contato** - Inserção de novos contatos com validação de duplicatas
- **Alterar Contato** - Modificação de telefones de contatos existentes
- **Remover Contato** - Exclusão de contatos com confirmação
- **Listar Contatos** - Exibição formatada de todos os contatos cadastrados

### Características Técnicas
- **Validação de duplicatas** - Prevenção de contatos com nomes idênticos
- **Busca case-insensitive** - Pesquisa independente de maiúsculas/minúsculas
- **Formatação consistente** - Interface padronizada e profissional
- **Feedback imediato** - Confirmações e avisos claros para o usuário
- **Tratamento de erros** - Validação de entrada numérica no menu

## Arquitetura e Implementação

### Tecnologias Utilizadas
- **Python 3.x**
- **Estruturas de dados nativas** (dicionários, strings)
- **Estruturas de controle** (while, if/elif/else)
- **Tratamento de exceções** (try/except)
- **Manipulação de strings** (lower(), title())

### Estrutura do Código

```python
# Estrutura de dados principal
lista = {}  # Dicionário para armazenar contatos (nome: telefone)

# Exemplo de validação de duplicatas
def inserir_contato():
    while True:
        nome = input("Insira o nome do contato: ").lower()
        if nome in lista:
            print("Contato já existe. Tente outro nome.")
        else:
            break
```

```python
# Sistema de menu com validação robusta
def menu():
    opcao = 0
    while (opcao < 1) or (opcao > 5):
        try:
            opcao = int(input("Digite sua opção: "))
            if (opcao < 1) or (opcao > 5):
                print("Valor inválido! Insira novamente!")
        except ValueError:
            print("Erro: você deve digitar um número válido.")
    return opcao
```

## Como Executar

### Pré-requisitos
- Python 3.x instalado no sistema
- Terminal ou prompt de comando

### Instalação e Execução
```bash
# Executar o programa
python agenda_contatos.py
```

### Exemplo de Uso
```
====================================================================================================
                                                MENU
====================================================================================================

Opções:
 1 - Adicionar contato;
 2 - Alterar contato;
 3 - Remover contato;
 4 - Listar contatos;
 5 - Sair.

Digite sua opção: 1

====================================================================================================
                                          INSERIR CONTATO
====================================================================================================
Insira o nome do contato: João Silva
Insira o número de telefone: (24) 99999-9999
Contato inserido com sucesso!
```

## Sugestões de Fotos para Documentação

### 1. Screenshot do Menu Principal
- **Captura:** Tela inicial com o menu de opções numeradas
- **Foco:** Interface limpa e organizada do sistema
- **Uso:** Demonstrar usabilidade e design da aplicação

### 2. Operação de Inserção de Contato
- **Captura:** Processo completo de adicionar um novo contato
- **Foco:** Validação de entrada e confirmação de sucesso
- **Uso:** Mostrar funcionalidade principal em ação

### 3. Listagem de Contatos
- **Captura:** Tela mostrando múltiplos contatos cadastrados
- **Foco:** Formatação dos dados e organização visual
- **Uso:** Demonstrar saída de dados estruturada

### 4. Tratamento de Erro
- **Captura:** Tentativa de inserir contato duplicado ou valor inválido
- **Foco:** Mensagens de erro claras e tratamento de exceções
- **Uso:** Evidenciar robustez do sistema

### 5. Código-fonte no Editor
- **Captura:** Função principal (menu() ou inserir_contato()) no editor
- **Foco:** Código bem estruturado com syntax highlighting
- **Uso:** Demonstrar qualidade técnica da implementação

## Competências Técnicas Demonstradas

### Programação Estruturada
- Organização modular com funções especializadas
- Separação clara de responsabilidades
- Código limpo e bem documentado
- Reutilização eficiente de código

### Manipulação de Dados
- Uso apropriado de dicionários Python
- Operações CRUD completas e eficientes
- Tratamento de strings e formatação
- Validação e sanitização de entrada

### Interface e Usabilidade
- Design de menu intuitivo e profissional
- Feedback claro para todas as operações
- Tratamento de casos edge e erros
- Experiência de usuário consistente

## Próximas Implementações

- Persistência de dados em arquivo (JSON/CSV)
- Busca avançada de contatos por critérios
- Validação de formato de telefone
- Interface gráfica com tkinter
- Importação/exportação de contatos
- Sistema de backup automático
- Campos adicionais (email, endereço, categoria)

## Resultados e Aprendizados

Este projeto consolidou conhecimentos essenciais em:
- **Estruturas de dados** Python (dicionários, listas)
- **Operações CRUD** e persistência básica
- **Validação robusta** de entrada de usuário
- **Design de interface** de linha de comando
- **Tratamento de exceções** e casos edge
- **Organização modular** de código

## Autor

**Natan Mauricio Santos**  
Tecnólogo em Tecnologia da Informação - FAETERJ  
Petrópolis - RJ  
Email: natanmauriciosantos@hotmail.com  
LinkedIn: [linkedin.com/in/natan-mauricio-santos]

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

---

*Sistema desenvolvido como parte do portfólio acadêmico em Tecnologia da Informação, demonstrando aplicação prática de conceitos fundamentais de programação e estruturas de dados.*
