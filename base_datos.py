import sqlite3

id = "21"
with sqlite3.connect("bd_btf.db") as conexion:
    sentencia = "DELETE FROM players WHERE id=?"
    cursor = conexion.execute(sentencia, (id,))

