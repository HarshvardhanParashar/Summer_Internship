## Build Docker Image

```bash
docker build -t assignment16 .
```

---

## Run Docker Container

```bash
docker run -p 8080:8080 -v ${PWD}:/workspace assignment16
```
