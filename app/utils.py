from flask import request
from app import db
from .models import Log

def registrar_log(user_id, action) :
    ip = request.remote_addr
    descricao = f"{action} | IP: {ip}"
    log  = Log(user_id, action=descricao)
    db.session.add(log)
    db.session.commit()