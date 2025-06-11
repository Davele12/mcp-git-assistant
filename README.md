# mcp-git-assistant

El objetivo de este repositorio es crear un MCP potenciado por el modelo de lenguaje LLaMA para crear, actualizar y modificar repositorios con palabras simples. Una manera de darle una tarea a la inteligencia artificial con lenguaje natural.

---

> [!NOTE]
>
> Para poder usar este proyecto necesitas saber como crear un token de github para tus repositorios, [settings?](https://github.com/settings/tokens)
>
> -- Sebaxsus

---

## Tabla de Contenidos

1. [Descripción del Proyecto](#mcp-git-assistant)
2. [Tabla de Contenidos](#tabla-de-contenidos)
3. [Instalación](#instalar--clonar-el-repositorio)
4. [Configuración](#configuración)
5. [Como obtener el token](#como-obtener-el-token-de-acceso-a-github)

---

## Instalar / Clonar el Repositorio

Para usar el MCP primero clona este repositoria en su rama **main**

```bash
git clone https://github.com/Davele12/mcp-git-assistant.git
```

---

## Configuración

Usa como ejemplo de configuracion el archivo `.env.Example` para saber que variables de entorno debes configurar

```bash
GITHUB_TOKEN = "TU_TOKEN_DE_ACCESO"
GITHUB_USERNAME = "TU_NOMBRE_DE_USUARIO_EN_GITHUB"
```

---

## Como obtener el token de acceso a GitHub

1. Entra a [GitHub](https://github.com/)
2. Ingresa a tu cuenta.
3. Selecciona tu Perfil (El icono arriba a la derecha).
4. Selecciona Configuración o Settings (Es lo mismo).
5. Selecciona la Opcion `Developer Settings`.
6. Selecciona `Personal access tokens`.
7. Selecciona `Tokens (classic)`.
8. Selecciona `Generate new token (classic)`.
9. Copia el Token y pegalo en tu `.env`.

