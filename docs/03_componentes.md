# Componentes Universais

## Conceito

No UAP OS tudo é um componente.

Não importa se é um relé, uma câmera, um motor, uma impressora ou um serviço de pagamento. Todos seguem a mesma estrutura lógica.

---

## Estrutura padrão

Todo componente possui:

* Identificador único
* Nome
* Categoria
* Entradas
* Saídas
* Configurações
* Eventos
* Estado
* Ícone
* Versão
* Fabricante
* Driver

---

## Categorias

### Entradas

* Botão
* Sensor PIR
* Sensor Ultrassônico
* RFID
* NFC
* QR Code
* Câmera
* Microfone
* Temperatura
* Umidade

### Saídas

* Relé
* Motor
* Servo
* PWM
* LED
* Display
* Impressora
* Buzzer
* Válvula
* Bomba

### Controle

* Timer
* Delay
* Contador
* Agenda
* Variável
* Condição
* Loop
* Conversão

### Comunicação

* MQTT
* HTTP
* WebSocket
* Modbus
* Serial
* Bluetooth
* Wi-Fi
* TCP/IP

### Serviços

* PIX
* Banco de Dados
* WhatsApp
* E-mail
* SMS
* API Externa

---

## Regras

Todo componente deve ser reutilizável.

Todo componente deve possuir configuração visual.

Nenhum componente poderá exigir programação para utilização.

Todo componente poderá ser utilizado em qualquer tipo de projeto.

---

## Objetivo

Permitir que qualquer automação seja construída apenas conectando componentes visuais entre si.
