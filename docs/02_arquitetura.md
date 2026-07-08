# Arquitetura do UAP OS

# Flow Engine

## Objetivo

O Flow Engine é o núcleo responsável por executar qualquer automação criada pelo usuário.

Ele interpreta os componentes, suas conexões e executa os eventos na ordem correta.

O usuário nunca programa diretamente. Toda lógica é construída visualmente.

---

## Funcionamento

Todo projeto é composto por:

* Componentes
* Conexões
* Fluxos
* Eventos

O Flow Engine lê o projeto e transforma essas informações em uma automação executável.

---

## Fluxo básico

Entrada

↓

Evento

↓

Flow Engine

↓

Validação

↓

Execução

↓

Saída

---

## Tipos de Eventos

* Clique
* Sensor ativado
* Sensor desativado
* Temporizador
* Agendamento
* Mudança de valor
* Recebimento MQTT
* Recebimento HTTP
* Recebimento Serial
* Inicialização do sistema

---

## Tipos de Ações

* Ligar
* Desligar
* Alternar
* Esperar
* Incrementar
* Decrementar
* Comparar
* Enviar mensagem
* Imprimir
* Acionar motor
* Alterar velocidade
* Publicar MQTT
* Chamar API
* Executar Plugin

---

## Regras

O Flow Engine nunca conhecerá dispositivos específicos.

Ele executará apenas Componentes Universais.

Dessa forma qualquer equipamento poderá ser utilizado sem alterar o núcleo do sistema.

---

## Objetivo Final

Separar completamente a lógica da automação do hardware físico, permitindo que o mesmo projeto funcione em diferentes dispositivos apenas trocando os drivers.
