# Modelo Universal de Projetos

## 1. Visão Geral

Um Projeto representa uma automação completa criada no UAP OS.

Um projeto reúne componentes, fluxos, dispositivos, variáveis, configurações e informações necessárias para executar uma automação em qualquer ambiente compatível.

O projeto é a principal unidade de trabalho da plataforma.

---

## 2. Requisitos Funcionais

O sistema deverá permitir:

* Criar projetos
* Editar projetos
* Duplicar projetos
* Excluir projetos
* Importar projetos
* Exportar projetos
* Versionar projetos
* Publicar projetos
* Restaurar versões anteriores
* Criar projetos a partir de modelos (Templates)

---

## 3. Estrutura de um Projeto

Cada projeto deverá possuir no mínimo:

* UUID
* Nome
* Descrição
* Categoria
* Autor
* Empresa
* Versão
* Status
* Data de criação
* Data da última alteração
* Componentes
* Fluxos
* Variáveis
* Dispositivos associados
* Plugins utilizados
* Permissões

---

## 4. Estados

Um projeto poderá estar em:

* Rascunho
* Em edição
* Validado
* Publicado
* Em execução
* Pausado
* Arquivado

---

## 5. Requisitos Técnicos

* Cada projeto deve possuir um UUID único.
* O formato de armazenamento deve ser independente do sistema operacional.
* O projeto deverá ser exportável em um único arquivo.
* O formato deverá ser compatível entre diferentes versões do UAP OS.
* O Runtime deverá executar somente projetos validados.

---

## 6. Critérios de Aceitação

Este módulo será considerado concluído quando for possível:

* Criar um novo projeto.
* Salvar um projeto.
* Abrir um projeto salvo.
* Exportar um projeto.
* Importar um projeto.
* Publicar um projeto para execução.
