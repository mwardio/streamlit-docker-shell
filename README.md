# streamlit-docker-shell  
A bare bones project shell for deploying a Streamlit app via Docker, configured with live reloading and other options to facilitate local development (see `.streamlit/config.toml`).  

## How to use:  

Clone the repository and navigate into it:

```bash
git clone https://github.com/mwardio/streamlit-docker-shell.git
cd streamlit-docker-shell/
```

Update `src/main.py` with your Streamlit app code and add dependencies to `requirements.txt` (optional). 

Build the Docker image and start the container using the included Compose file ([*docker-compose.yml*](https://github.com/mwardio/streamlit-docker-shell/blob/main/docker-compose.yml)):
```bash
docker-compose up -d --build
```
