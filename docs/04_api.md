# 4. Especificação de API

## API de Sistema

### Operações Básicas

#### 1. Gerenciamento de Processos

```
POST /api/processes - Criar novo processo
GET /api/processes - Listar processos
GET /api/processes/{id} - Obter detalhes do processo
POST /api/processes/{id}/pause - Pausar processo
POST /api/processes/{id}/resume - Retomar processo
DELETE /api/processes/{id} - Terminar processo
```

#### 2. Gerenciamento de Recursos

```
GET /api/resources/memory - Informações de memória
GET /api/resources/cpu - Informações de CPU
GET /api/resources/storage - Informações de armazenamento
GET /api/resources/devices - Lista de dispositivos
```

#### 3. Sistema de Plugins

```
GET /api/plugins - Listar plugins instalados
POST /api/plugins - Instalar novo plugin
GET /api/plugins/{id} - Detalhes do plugin
POST /api/plugins/{id}/enable - Habilitar plugin
POST /api/plugins/{id}/disable - Desabilitar plugin
DELETE /api/plugins/{id} - Remover plugin
```

#### 4. Autenticação e Autorização

```
POST /api/auth/login - Fazer login
POST /api/auth/logout - Fazer logout
GET /api/auth/profile - Obter perfil do usuário
POST /api/auth/refresh - Renovar token
```

### Formatos de Resposta

**Sucesso:**
```json
{
  "status": "success",
  "data": { /* dados */ },
  "timestamp": "2026-07-08T10:30:00Z"
}
```

**Erro:**
```json
{
  "status": "error",
  "error": {
    "code": "ERROR_CODE",
    "message": "Descrição do erro"
  },
  "timestamp": "2026-07-08T10:30:00Z"
}
```

## Autenticação

- Método: JWT (JSON Web Tokens)
- Header: `Authorization: Bearer <token>`
- Refresh token para renovação de sessão

## Rate Limiting

- Limite: 1000 requisições por hora por usuário
- Header resposta: `X-RateLimit-Remaining`

## Versionamento

- Versão: `/api/v1/`
- Compatibilidade retroativa garantida
