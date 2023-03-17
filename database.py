import sqlite3

con = sqlite3.connect('Cadastro.db')

cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL,
    Email TEXT NOT NULL,
    senha TEXT NOT NULL,
    cSenha TEXT NOT NULL
)
""")

print('Banco de dados Conectado...')