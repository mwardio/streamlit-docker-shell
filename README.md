# streamlit-docker-shell  
A bare bones project shell for developing and deploying a Streamlit app via Docker.  

## How to use:  

Clone the repository and navigate into it:

```bash
git clone https://github.com/mwardio/streamlit-docker-shell.git
cd streamlit-docker-shell/
```

Update [*src/main.py*](https://github.com/mwardio/streamlit-docker-shell/blob/main/src/main.py) with your Streamlit app code and add dependencies to [*requirements.txt*](https://github.com/mwardio/streamlit-docker-shell/blob/main/requirements.txt) (optional), then build the Docker image:
```bash
docker build . -t streamlit-image
```

Run the Docker container on port 8501 (replace ```$(pwd)``` with ```${pwd}``` if using Windows):
```bash
docker run --name streamlit-app -p 8501:8501 -d -v $(pwd):/app streamlit-image
```

Alternatively, start the container via Docker Compose using the included Compose file ([*docker-compose.yml*](https://github.com/mwardio/streamlit-docker-shell/blob/main/docker-compose.yml)):
```bash
docker-compose up -d
```
