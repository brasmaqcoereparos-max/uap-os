# Core da Plataforma

## Objetivo

O Core é o núcleo permanente do UAP OS.

Todo o restante da plataforma depende dele.

O Core nunca conhecerá regras específicas de lavanderia, vending machine, restaurante ou automação residencial.

Ele conhece apenas Projetos, Componentes, Dispositivos, Eventos e Fluxos.

---

# Responsabilidades

O Core será responsável por:

* Gerenciamento de Projetos
* Gerenciamento de Componentes
* Gerenciamento de Dispositivos
* Gerenciamento de Plugins
* Gerenciamento de Fluxos
* Gerenciamento de Eventos
* Configurações Gerais
* Segurança
* Usuários
* Logs
* Persistência de Dados

---

# O Core nunca fará

* Controlar GPIO diretamente
* Controlar motores diretamente
* Ler sensores diretamente
* Executar drivers específicos
* Conhecer protocolos de fabricantes

Essas funções pertencem aos Drivers.

---

# Comunicação

Todo o sistema se comunica através do Event Bus.

Nenhum módulo poderá acessar outro módulo diretamente.

---

# Objetivo

Manter o núcleo pequeno, estável, modular e independente do hardware.
