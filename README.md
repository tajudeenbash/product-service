# Product Service — Lab 3

Python/Flask rewrite of the Lab 2 Rust catalog. GET /products returns the same products, IDs, names, and prices. Original Rust source remains for reference; Azure runs app.py.

## Local setup

Create a Python virtual environment, activate it, and run:

```sh
python -m pip install -r requirements.txt
python app.py
```

Open http://localhost:3030/products. Copy .env.example to .env to change PORT. Existing environment variables take precedence. Run checks with `python -m unittest -v`.

## Azure App Service

Use a Linux Python App Service with SCM_DO_BUILD_DURING_DEPLOYMENT=true. Startup command:

```sh
gunicorn --bind 0.0.0.0:8000 --timeout 600 app:app
```

Verify https://<actual-app-hostname>/products. This catalog has no RabbitMQ dependency; the order service owns messaging.

## First four factors

1. Codebase: one Git repository tracks this service across deployments.
2. Dependencies: requirements.txt declares dependencies; a virtual environment isolates them.
3. Config: PORT comes from the environment locally. Azure's startup command controls the production listener. .env is excluded from Git.
4. Backing services: this static catalog has no external backing service. The separate order service attaches RabbitMQ through environment configuration.
