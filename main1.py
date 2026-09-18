from fastapi import FastAPI, Depends, HTTPException # SErvidor, Proteção, Erros
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm # Login padrão do Swagger
from pydantic import BaseModel # Validador de dados
from passlib.context import CryptContext # Criptografa senha
from jose import jwt # Cria e lê Token JWT
from datetime import datetime, timedelta # tempo

app = FastAPI() # 1. Cria o servidor. É o "app"

# 1. CONFIGURAÇÕES GERAIS
CHAVE = "segredo123" # Chave secreta. NUNCA commita isso no Git. Serve pra assinar o token
