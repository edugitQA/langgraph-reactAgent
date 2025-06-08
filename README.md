# Langgraph React Agent

## Descrição
Este projeto implementa um agente de pesquisa baseado em React utilizando a biblioteca Langgraph e ferramentas da Langchain. O agente é configurado para buscar informações na web e responder de forma clara e objetiva.

## Funcionalidades
- Integração com Langgraph e Langchain.
- Busca de informações na web utilizando Tavily.
- Configuração de mensagens do sistema para personalizar o comportamento do agente.

## Estrutura do Projeto
- `langgraph-101.py`: Arquivo principal que define o agente e suas ferramentas.
- `langgraph.json`: Configuração de dependências e gráficos.
- `requirements.txt`: Lista de dependências do projeto.

## Configuração
1. Certifique-se de ter o Python 3.11 instalado.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   pip install -U "langgraph-cli[inmem]" 
   ```
3. Configure as variáveis de ambiente no arquivo `.env`:
   ```env
   API_KEY=<sua_api_key>
   TAVILY_API_KEY=<sua_tavily_api_key>
   ```

## Execução
Para iniciar o agente, execute:
```bash
langgraph dev
```

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests no repositório [Langgraph React Agent](https://github.com/edugitQA/langgraph-reactAgent).

## Atenção

Alguns usuários relataram problemas ao usar o projeto no Windows. O problema pode ser resolvido executando o comando:
```bash
langgraph dev --allow-blocking
```

### Observação sobre Navegadores
Ao executar o agente, ele será exibido no navegador padrão. Caso o navegador bloqueie a execução (como demonstrado no Brave), recomenda-se usar o Chrome, onde funciona perfeitamente.

## Requisitos
- Python 3.11 ou superior
- Google Generative AI API Key
- Tavily API Key

## Execução no Terminal
Para iniciar o agente, execute:
```bash
langgraph dev
```

## Detalhes do Script
- Usa `dotenv` para carregar variáveis de ambiente.
- Inicializa o modelo `gemini-2.0-flash`.
- Define a ferramenta `search_web` com Tavily.
- Cria um agente ReAct via `create_react_agent`.
