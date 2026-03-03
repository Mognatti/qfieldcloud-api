import uvicorn

from src.config.factory import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(  # noqa
        app="main:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
        log_config="log-conf.yaml",
    )
