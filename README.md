# 📦 Freelancer API #

API RESTful desenvolvida com Flask para servir como back-end de uma aplicação web full-stack de gerenciamento de freelancers.

## 🚀 Sumário de Funcionalidades ##

- CRUD de usuários (freelancers e clientes)
- Validações e mensagens de erro padronizadas
- Respostas consistentes com estrutura padrão
- Estrutura preparada para expansão (autenticação, filtros, etc.)

## 📤 Estrutura Padrão das Respostas ##

Todas as respostas da API seguem o seguinte padrão JSON:

```json
{
  "message": "Descrição do resultado da operação",
  "errors": "Erros encontrados (ou null)",
  "data": "Conteúdo retornado pela operação"
}
```

## 🛠 Tecnologias Utilizadas ##

Python – Linguagem principal

Flask – Microframework web

SQLAlchemy – ORM para manipulação de banco de dados

PostgreSQL – Banco de dados relacional
