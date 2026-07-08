# Event Bus

## Objetivo

O Event Bus é o sistema de comunicação central do UAP OS.

Nenhum módulo da plataforma poderá comunicar-se diretamente com outro módulo.

Toda comunicação será realizada através da publicação e consumo de eventos.

Essa arquitetura reduz o acoplamento, facilita a manutenção e permite a expansão da plataforma por meio de plugins e novos dispositivos.

---

# Funcionamento

Todo evento possui um emissor.

Todo evento possui um ou mais consumidores.

Quando um evento é publicado, o Event Bus identifica quais módulos estão inscritos e entrega a mensagem.

---

# Estrutura de um Evento

Cada evento deverá conter:

* Identificador único (UUID)
* Data e hora
* Origem
* Destino
* Tipo
* Prioridade
* Carga útil (Payload)
* Status

---

# Exemplos de Eventos

* Botão pressionado
* Sensor ativado
* Sensor desativado
* Pagamento aprovado
* Pagamento recusado
* Impressão concluída
* Motor iniciado
* Motor parado
* Projeto publicado
* Plugin instalado
* Dispositivo conectado
* Dispositivo desconectado

---

# Benefícios

* Baixo acoplamento entre módulos.
* Comunicação padronizada.
* Fácil monitoramento.
* Registro de auditoria.
* Escalabilidade.
* Integração com novos plugins sem alterar o Core.

---

# Objetivo Final

Ser o único mecanismo de comunicação entre os módulos do UAP OS.
