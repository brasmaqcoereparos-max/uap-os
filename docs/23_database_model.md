# Modelo do Banco de Dados

## 1. Objetivo

Definir a estrutura lógica do banco de dados do UAP OS, estabelecendo as entidades principais, seus relacionamentos e regras de persistência.

O modelo deverá ser compatível com SQLite (desenvolvimento) e PostgreSQL (produção).

---

## 2. Entidades Principais

O banco deverá possuir inicialmente as seguintes entidades:

* Usuário
* Projeto
* Fluxo
* Componente
* Conexão
* Variável
* Dispositivo
* Driver
* Plugin
* Evento
* Log
* Configuração

---

## 3. Relacionamentos

* Um Usuário pode possuir vários Projetos.
* Um Projeto pode possuir vários Fluxos.
* Um Fluxo pode possuir vários Componentes.
* Um Fluxo pode possuir várias Conexões.
* Um Projeto pode possuir várias Variáveis.
* Um Dispositivo utiliza um Driver.
* Um Plugin pode fornecer vários Componentes e Drivers.
* Um Projeto gera vários Eventos e Logs.

---

## 4. Requisitos Técnicos

* Todas as tabelas deverão utilizar UUID como chave primária.
* As datas deverão ser armazenadas em UTC.
* O banco deverá utilizar chaves estrangeiras para garantir integridade.
* Campos de auditoria deverão estar presentes nas principais entidades:

  * Data de criação
  * Data de atualização
  * Usuário responsável (quando aplicável)

---

## 5. Migrações

As alterações no esquema do banco deverão ser controladas por migrações utilizando Alembic.

Nenhuma alteração manual no banco de produção será permitida.

---

## 6. Critérios de Aceitação

Este módulo será considerado concluído quando:

* Todas as entidades estiverem modeladas.
* Os relacionamentos estiverem definidos.
* As migrações puderem ser geradas automaticamente.
* O banco puder ser criado em SQLite e PostgreSQL sem alterações no modelo.
