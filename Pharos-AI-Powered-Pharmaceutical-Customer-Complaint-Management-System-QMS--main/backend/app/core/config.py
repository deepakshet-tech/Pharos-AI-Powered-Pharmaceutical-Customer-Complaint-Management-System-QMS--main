from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Pharos - Customer Complaint Management"
    database_url: str = "sqlite:///./pharos_qms.db"
    groq_api_key: str = ""
    model_primary: str = "openai/gpt-oss-120b"      # fast extraction / risk / summary
    model_context: str = "openai/gpt-oss-120b"  # deep reasoning: root cause / CAPA
    cors_origins: list = ["http://localhost:5173", "http://127.0.0.1:5173"]

    class Config:
        env_file = ".env"

settings = Settings()


