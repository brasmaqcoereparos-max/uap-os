# API REST do UAP OS

## 1. Objetivo

A API REST é a interface oficial de comunicação entre o Frontend, o Runtime, os Plugins e os serviços externos.

Toda operação deverá ser realizada através de endpoints versionados.

---

# 2. Padrões

* Base URL: /api/v1
* Formato: JSON
* UTF-8
* HTTPS obrigatório em produção
* Autenticação via JWT

---

# 3. Módulos da API

## Autenticação

* POST /auth/login
* POST /auth/logout
* POST /auth/refresh

---

## Usuários

* GET /users
* GET /users/{id}
* POST /users
* PUT /users/{id}
* DELETE /users/{id}

---

## Projetos

* GET /projects
* GET /projects/{id}
* POST /projects
* PUT /projects/{id}
* DELETE /projects/{id}
* POST /projects/{id}/publish
* POST /projects/{id}/start
* POST /projects/{id}/stop

---

## Componentes

* GET /components
* GET /components/{id}

---

## Plugins

* GET /plugins
* POST /plugins/install
* POST /plugins/update
* DELETE /plugins/{id}

---

## Drivers

* GET /drivers
* POST /drivers/reload

---

## Dispositivos

* GET /devices
* GET /devices/{id}
* POST /devices/scan

---

## Runtime

* GET /runtime/status
* POST /runtime/start
* POST /runtime/stop
* POST /runtime/restart

---

## Eventos

* GET /events
* GET /events/{id}

---

## Dashboard

* GET /dashboard

---

# 4. Requisitos Técnicos

* Todas as respostas deverão ser JSON.
* Todos os erros deverão utilizar um formato padronizado.
* A API deverá possuir documentação automática via OpenAPI (Swagger).
* Os endpoints deverão ser versionados para garantir compatibilidade futura.

---

# 5. Critérios de Aceitação

Este módulo será considerado concluído quando:

* A documentação OpenAPI estiver disponível.
* Os endpoints responderem corretamente.
* A autenticação JWT estiver funcionando.
* Os principais módulos puderem ser acessados pela API.
