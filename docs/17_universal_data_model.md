# Universal Data Model (UDM)

## Objetivo

O Universal Data Model (UDM) define a estrutura de dados utilizada por todo o UAP OS.

Todos os módulos da plataforma deverão utilizar esse modelo como referência para armazenamento, comunicação e processamento das informações.

---

# Entidades Principais

O UAP OS é composto por dez entidades fundamentais.

1. Projeto
2. Dispositivo
3. Componente
4. Driver
5. Plugin
6. Fluxo
7. Evento
8. Conexão
9. Variável
10. Usuário

---

# Projeto

Representa uma automação completa.

Exemplos:

* Lavanderia
* Vending Machine
* Restaurante
* Automação Residencial
* Irrigação

Cada Projeto possui:

* UUID
* Nome
* Descrição
* Versão
* Autor
* Data de criação
* Fluxos
* Componentes
* Variáveis

---

# Dispositivo

Representa qualquer equipamento físico ou virtual conectado ao sistema.

---

# Componente

Representa qualquer elemento reutilizável da automação.

---

# Driver

Representa a interface de comunicação entre o sistema e um equipamento.

---

# Plugin

Representa um pacote que adiciona novos Componentes e Drivers.

---

# Fluxo

Representa a lógica da automação.

---

# Evento

Representa qualquer ocorrência dentro da plataforma.

---

# Conexão

Representa a ligação entre dois Componentes.

---

# Variável

Representa informações utilizadas pelos Fluxos.

---

# Usuário

Representa qualquer operador autorizado da plataforma.

---

# Objetivo Final

Garantir que todos os módulos do UAP OS utilizem um modelo de dados único, consistente e independente da tecnologia utilizada.
