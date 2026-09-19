# 🎮 Dockerized Flask Tic-Tac-Toe & Docker Learning Guide

A containerized interactive **Tic-Tac-Toe Web Application** built with **Python Flask** and **Docker**.

This repository documents my journey of learning Docker fundamentals, core container concepts, and step-by-step containerization of a Python web application.

---

## 📑 Table of Contents

- [What is Docker?](#-what-is-docker)
- [Core Concepts: Images vs Containers](#-core-concepts-images-vs-containers)
- [Dockerfile Breakdown](#-dockerfile-breakdown)
- [Essential Docker Commands Reference](#-essential-docker-commands-reference)
- [How to Run This Project](#-how-to-run-this-project)
- [Key Learnings & Best Practices](#-key-learnings--best-practices)

---

## 🐳 What is Docker?

**Docker** is an open-source platform that enables developers to package applications and all their dependencies (libraries, code, runtime, system tools) into standardized units called **containers**.

### Why Docker?
- **Eliminates "It works on my machine"**: Guarantees identical execution regardless of the host OS or environment.
- **Lightweight & Fast**: Unlike virtual machines (VMs) that require a full guest OS, containers share the host kernel and start in seconds.
- **Portability & Isolation**: Runs consistently across local development, testing, staging, and production servers or cloud providers.

---

## 🧠 Core Concepts: Images vs Containers

Understanding the difference between an **Image** and a **Container** is fundamental to mastering Docker:

```
+----------------------------------------------------------------+
|                          Dockerfile                            |
|             (The Recipe: Instructions on how to build)         |
+----------------------------------------------------------------+
                               |
                        [docker build]
                               v
+----------------------------------------------------------------+
|                         Docker Image                           |
|        (The Blueprint: Read-only package with code & runtime)  |
+----------------------------------------------------------------+
                               |
                         [docker run]
                               v
+----------------------------------------------------------------+
|                       Docker Container                         |
|     (The Living Instance: Running, isolated process in action) |
+----------------------------------------------------------------+
```

### 1. Docker Image
- **Definition**: A read-only template that contains the application code, runtime libraries, environment variables, and configuration files.
- **Analogy**: A **Class** in Object-Oriented Programming, or a **Recipe** for baking a cake.
- **Characteristics**: Immutable (cannot be changed once built), composed of stacked layers.

### 2. Docker Container
- **Definition**: A runnable, isolated instance of a Docker image. It is an active process running on the host system with its own filesystem, network interface, and resource allocation.
- **Analogy**: An **Object (instance)** created from a Class, or the **actual cake** baked from the recipe.
- **Characteristics**: Ephemeral by default, can be started, stopped, inspected, and destroyed without affecting the base image.

### Quick Comparison

| Feature | Docker Image | Docker Container |
|---|---|---|
| **State** | Static / Read-only | Dynamic / Running or Stopped |
| **Modification** | Rebuild required to change | Can write temporary changes in container layer |
| **Relationship** | One image can create multiple containers | Derived from a single image |
| **Analogy** | Recipe / Blueprint / Class | Baked Cake / House / Object Instance |

---

## 🛠️ Dockerfile Breakdown

Here is the line-by-line explanation of the [`Dockerfile`](file:///c:/Users/hp/Desktop/Ai%20and%20agents/docker/dockerise-flask-app/Dockerfile) used in this project:

```dockerfile
# 1. Base Image: Lightweight Python 3.11 environment
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy requirements first (leverages Docker layer caching)
COPY requirements.txt .

# 4. Install Python dependencies without caching wheels to save space
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy all project files into the container working directory
COPY . /app

# 6. Expose the port where the Flask application listens
EXPOSE 5000

# 7. Default command executed when container starts
CMD ["python", "./app.py"]
```

> **💡 Why copy `requirements.txt` before copying the rest of the code?**  
> Docker caches each instruction layer. If we only modify `app.py`, Docker reuses the cached layer for `pip install`, making subsequent builds drastically faster!

---

## 📋 Essential Docker Commands Reference

### 1. Building Images
```bash
# Build an image with a custom tag name using current directory (.)
docker build -t mdahtasham112/dockerise_tic_tac_toe .

# Build with a specific tag version
docker build -t mdahtasham112/dockerise_tic_tac_toe:v1.0 .
```

### 2. Running Containers
```bash
# Run container in background (detached mode) and map host port to container port
docker run -d -p 5000:5000 --name tic-tac-toe-app mdahtasham112/dockerise_tic_tac_toe

# Run container interactively with a terminal attached
docker run -it -p 5000:5000 --name tic-tac-toe-app mdahtasham112/dockerise_tic_tac_toe

# Run and automatically remove container when it exits
docker run --rm -p 5000:5000 mdahtasham112/dockerise_tic_tac_toe
```

### 3. Monitoring & Managing Containers
```bash
# List only running containers
docker ps

# List all containers (including stopped ones)
docker ps -a

# View real-time container logs
docker logs -f <container_name_or_id>

# Execute a bash/sh shell inside a running container
docker exec -it <container_name_or_id> sh

# Stop a running container
docker stop <container_name_or_id>

# Start a stopped container
docker start <container_name_or_id>

# Remove a stopped container
docker rm <container_name_or_id>

# Force remove a running container
docker rm -f <container_name_or_id>
```

### 4. Managing Images
```bash
# List all local images
docker images

# Delete an image
docker rmi <image_name_or_id>

# Remove unused / dangling images and build cache
docker image prune
```

### 5. Docker Hub & Sharing
```bash
# Login to Docker Hub
docker login

# Tag an image for Docker Hub repository
docker tag mdahtasham112/dockerise_tic_tac_toe mdahtasham112/dockerise_tic_tac_toe:latest

# Push image to Docker Hub
docker push mdahtasham112/dockerise_tic_tac_toe:latest
```

---

## 🚀 How to Run This Project

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
- Git (optional, for cloning).

### 1. Build the Docker Image
```bash
docker build -t mdahtasham112/dockerise_tic_tac_toe .
```

### 2. Run the Container
```bash
docker run -d -p 5000:5000 --name tic-tac-toe-game mdahtasham112/dockerise_tic_tac_toe
```

### 3. Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

### 4. Stop the Container
```bash
docker stop tic-tac-toe-game
docker rm tic-tac-toe-game
```

---

## 💡 Key Learnings & Best Practices

1. **Port Binding (`-p HOST:CONTAINER`)**:
   - The `-p 5000:5000` argument bridges traffic from `localhost:5000` on your host machine to port `5000` inside the isolated container.
   - Flask must listen on `0.0.0.0` (all interfaces) rather than `127.0.0.1` to receive traffic forwarded into the container.

2. **Slim Base Images**:
   - Using `python:3.11-slim` significantly reduces image size compared to the standard `python:3.11` full image while keeping all essential Python runtimes.

3. **Layer Caching Optimization**:
   - Order Dockerfile instructions from least frequently changed (dependencies) to most frequently changed (application source code) to maximize build speed.

4. **Clean Builds with `.dockerignore`**:
   - Always exclude virtual environments (`venv/`), `__pycache__`, and `.git` folders from the Docker build context.
