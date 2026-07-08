# Device Manager

## Objetivo

O Device Manager é responsável por descobrir, cadastrar, configurar, monitorar e remover todos os dispositivos conectados ao UAP OS.

Ele representa o inventário completo da plataforma.

Nenhum outro módulo acessará diretamente um equipamento físico.

Toda interação ocorrerá através do Device Manager.

---

# Tipos de Dispositivos

O Device Manager deverá suportar qualquer equipamento físico ou virtual.

Exemplos:

* Raspberry Pi
* ESP32
* Arduino
* PLC
* Computador
* Impressora
* Leitor RFID
* Câmera
* Display
* Sensor
* Relé
* Inversor de frequência
* Módulo MQTT
* Equipamentos Modbus
* Equipamentos TCP/IP
* Equipamentos USB
* Equipamentos Bluetooth

---

# Informações Armazenadas

Cada dispositivo deverá possuir:

* UUID
* Nome
* Categoria
* Fabricante
* Modelo
* Número de série
* Firmware
* Driver
* Endereço IP
* Porta
* Protocolo
* Localização
* Status
* Data de instalação
* Última comunicação

---

# Estados

Todo dispositivo poderá estar em:

* Novo
* Detectado
* Configurado
* Online
* Offline
* Atualizando
* Erro
* Desativado

---

# Responsabilidades

* Detectar novos dispositivos
* Registrar dispositivos
* Atualizar informações
* Monitorar conexão
* Validar compatibilidade
* Informar falhas
* Disponibilizar dispositivos para o Runtime

---

# Objetivo Final

Criar uma camada única de gerenciamento para qualquer equipamento utilizado pelo UAP OS, independente do fabricante ou da tecnologia de comunicação.
