# test-flask-project

![Version](https://img.shields.io/badge/version-0.0.1-blue.svg)


<details>
<summary>Índice</summary>

- [Introducción](#introduccion)
- [Servicio Flask](#servicio-flask)
- [Referencias](#referencias)

</details>

---
## Introducción
Demo de constucción de un servicio Flask dockerizado y con versionado de APIs

## Servicio Flask
Contruir la imagen docker con el servicio Flask:
```bash
docker build --no-cache -t <NAME>:<TAG> .
```

Arrancar el servicio Flask
```bash
docker run -dt --name flask-service <NAME>:<TAG>
```

---
## Referencias
