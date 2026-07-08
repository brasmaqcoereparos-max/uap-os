# Stack Tecnológica do UAP OS

## 1. Objetivo

Definir oficialmente as tecnologias utilizadas no desenvolvimento do UAP OS.

Essas definições deverão ser seguidas durante toda a implementação, salvo decisão documentada em nova versão deste documento.

---

# 2. Backend

Tecnologia:

* Python 3.13+

Framework:

* FastAPI

Servidor ASGI:

* Uvicorn

Principais responsabilidades:

* API REST
* Gerenciamento de Projetos
* Runtime
* Event Bus
* Plugin Manager
* Driver Manager
* Component Manager

---

# 3. Banco de Dados

Durante o desenvolvimento:

* SQLite

Produção:

* PostgreSQL

ORM:

* SQLAlchemy

Migrações:

* Alembic

---

# 4. Frontend

Tecnologia:

* Flutter

Compatibilidade:

* Linux
* Windows
* Android
* Web

---

# 5. Runtime

Tecnologia:

* Python

Responsabilidades:

* Executar Fluxos
* Monitorar Componentes
* Gerenciar Eventos
* Coordenar Drivers

---

# 6. Comunicação

Protocolos principais:

* MQTT
* HTTP
* WebSocket
* Modbus TCP
* Modbus RTU
* Serial
* Bluetooth
* GPIO
* I²C
* SPI

---

# 7. Firmware

Dispositivos suportados inicialmente:

* Raspberry Pi
* ESP32
* Arduino

---

# 8. Segurança

Autenticação:

* JWT

Criptografia:

* TLS

Hash de senhas:

* Argon2

---

# 9. Controle de Versão

Repositório:

* Git

Hospedagem:

* GitHub

Fluxo recomendado:

* GitHub Flow

---

# 10. Objetivo Final

Manter uma base tecnológica consistente, moderna, modular e preparada para expansão futura.
