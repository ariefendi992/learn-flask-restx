from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy


api = Api(
    title="API Sistem Monitoring Siswa",
    description="Sistem Monitoring Siswa",
    doc="/api",
)

db = SQLAlchemy()