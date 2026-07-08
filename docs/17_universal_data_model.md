# Universal Data Model

## Overview

The Universal Data Model (UDM) provides a standardized framework for representing, organizing, and managing data across the UAP-OS ecosystem. This document outlines the core principles, structure, and best practices for implementing and utilizing the UDM.

## Core Principles

### 1. Universality
- Single, consistent data representation across all system components
- Language and platform agnostic
- Supports heterogeneous data sources and formats

### 2. Interoperability
- Seamless data exchange between services
- Clear interfaces and well-defined contracts
- Version-aware compatibility management

### 3. Extensibility
- Pluggable data type definitions
- Custom domain models while maintaining core compatibility
- Forward and backward compatibility support

### 4. Performance
- Efficient serialization and deserialization
- Minimal overhead in data transformation
- Optimized for common access patterns

## Data Model Architecture

### Base Entity

```
Entity:
  - id: string (unique identifier)
  - type: string (entity type)
  - version: integer (schema version)
  - metadata: Metadata
  - created_at: timestamp
  - updated_at: timestamp
  - deleted_at: timestamp (optional)
```

### Metadata

```
Metadata:
  - source: string (originating system)
  - tags: string[]
  - attributes: Map<string, any>
  - audit_trail: AuditEntry[]
```

### Relationships

```
Relationship:
  - source_id: string
  - target_id: string
  - type: string (one_to_one, one_to_many, many_to_many)
  - direction: string (forward, bidirectional)
  - properties: Map<string, any>
```

## Data Types

### Primitive Types
- String
- Integer
- Float/Decimal
- Boolean
- Date/DateTime
- Binary

### Composite Types
- Array
- Object/Map
- Struct

### Domain-Specific Types
- Address
- ContactInfo
- GeoLocation
- Currency
- Document

## Schema Definition

### Format
Schemas are defined using a JSON Schema-like notation:

```json
{
  "$schema": "uap://data-model/v1",
  "id": "entity:user",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "description": "Unique user identifier"
    },
    "email": {
      "type": "string",
      "format": "email",
      "required": true
    },
    "profile": {
      "type": "object",
      "properties": {
        "first_name": { "type": "string" },
        "last_name": { "type": "string" }
      }
    }
  }
}
```

### Validation Rules
- Type checking: Strict type validation on write operations
- Constraint enforcement: min, max, pattern, enum
- Custom validators: Domain-specific validation logic
- Cross-field validation: Complex business rule enforcement

## Data Serialization

### Supported Formats

#### JSON
- Human-readable
- Default format for REST APIs
- Wide tool support

#### Protocol Buffers
- Compact binary format
- Type-safe schema definition
- Language generation support

#### MessagePack
- Efficient binary serialization
- Smaller payload size
- Fast serialization/deserialization

#### AVRO
- Schema versioning support
- Compression support
- Evolution compatibility

## Transformation Pipeline

```
Source Data → Validation → Transformation → Target Format → Storage/Output
```

### Transformation Steps

1. **Ingestion**: Parse source data into intermediate representation
2. **Validation**: Check against schema and constraints
3. **Normalization**: Standardize field names, types, and values
4. **Enrichment**: Add computed fields and relationships
5. **Serialization**: Convert to target format

## API Integration

### CRUD Operations

```
Create:  POST /api/v1/entities
Read:    GET /api/v1/entities/{id}
Update:  PATCH /api/v1/entities/{id}
Delete:  DELETE /api/v1/entities/{id}
```

### Query Interface

```
GET /api/v1/entities?
  type=user&
  status=active&
  created_after=2024-01-01&
  limit=100&
  offset=0
```

### Batch Operations

```
POST /api/v1/entities/batch
Content: [{ operation: 'create', data: {...} }, ...]
```

## Versioning Strategy

### Schema Versioning
- Major version: Breaking changes
- Minor version: Backward-compatible additions
- Patch version: Bug fixes and documentation

### Migration Path
- Dual-write: Write to both old and new schema
- Gradual migration: Move data incrementally
- Deprecation: Mark old schema as deprecated
- Sunset: Remove old schema after grace period

## Best Practices

### Design
- ✓ Keep schemas simple and focused
- ✓ Use meaningful, descriptive field names
- ✓ Document all custom types and rules
- ✓ Design for flexibility and extensibility
- ✗ Avoid deeply nested structures
- ✗ Don't store derived/computed data

### Implementation
- ✓ Validate on ingestion and write
- ✓ Use consistent error handling
- ✓ Implement proper audit trails
- ✓ Support idempotent operations
- ✗ Don't bypass validation
- ✗ Avoid tight coupling between schemas

### Performance
- ✓ Index frequently queried fields
- ✓ Use appropriate serialization format
- ✓ Implement caching where applicable
- ✓ Monitor transformation overhead
- ✗ Don't over-normalize
- ✗ Avoid large binary payloads

## Error Handling

### Validation Errors
```json
{
  "error": "ValidationError",
  "path": "email",
  "message": "Invalid email format",
  "code": "INVALID_FORMAT"
}
```

### Transformation Errors
```json
{
  "error": "TransformationError",
  "source_type": "xml",
  "target_type": "json",
  "message": "Unable to map field: legacy_field",
  "code": "MAPPING_NOT_FOUND"
}
```

## References

- [JSON Schema Specification](https://json-schema.org/)
- [Protocol Buffers Documentation](https://developers.google.com/protocol-buffers)
- [Apache AVRO Format](https://avro.apache.org/)
- [UAP-OS Architecture](./architecture.md)

## Glossary

- **Entity**: A distinct object with properties and relationships
- **Schema**: Formal definition of an entity's structure
- **Serialization**: Converting data into a storable/transmittable format
- **Normalization**: Standardizing data representation
- **Versioning**: Managing schema and API changes over time
