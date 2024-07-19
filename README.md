# streamlit-docker-shell  
A bare bones project shell for deploying a Streamlit app via Docker, configured with live reloading and other options to facilitate local development (see `.streamlit/config.toml`).  

## How to use:  

Clone the repository and navigate into it:

```bash
git clone https://github.com/mwardio/streamlit-docker-shell.git
cd streamlit-docker-shell/
```

Update `src/main.py` with your Streamlit app code and add dependencies to `requirements.txt` (optional), then build the Docker image:
```bash
docker build . -t streamlit-image
```

Start the container via Docker Compose (recommended) using the included Compose file ([*docker-compose.yml*](https://github.com/mwardio/streamlit-docker-shell/blob/main/docker-compose.yml)):
```bash
docker-compose up -d
```

You can also run the Docker container directly, just be sure to mount the root project directory as a volume labeled `/app` (assuming you didn't change the Dockerfile WORKDIR command):
```bash
docker run --name streamlit-app -p 8501:8501 -d -v ./:/app streamlit-image
```
