from bottle import route,template,run,request,error,static_file
import MySQLdb

@route('/',method="GET")
def index():
	return template("index.html")

@route('/bases',method="GET")
def bases():
        return template("bases.html")

@route('/base',method="POST")
def base():
        DB_HOST_mysql = request.forms.get('host')
        DB_USER_mysql = request.forms.get('usuario')
        DB_PASS_mysql = request.forms.get('password')
        if DB_HOST_mysql==DB_HOST_mysql and DB_USER_mysql==DB_USER_mysql and DB_PASS_mysql==DB_PASS_mysql:
                datos = [DB_HOST_mysql,DB_USER_mysql,DB_PASS_mysql]
                conectar = MySQLdb.connect(*datos)
                cursor = conectar.cursor()
                datos = cursor.execute("SHOW DATABASES;")
                datos = cursor.fetchall()
                cursor.close()
                conectar.close()
       	return template('base.html',datos=datos,DB_USER_mysql=DB_USER_mysql)

@route('/tablas',method="GET")
def tablas():
        return template("tablas.html")

@route('/tabla',method="POST")
def tabla():
        DB_HOST_mysql = request.forms.get('host')
        DB_USER_mysql = request.forms.get('usuario')
        DB_PASS_mysql = request.forms.get('password')
        DB_NAME_mysql = request.forms.get('basedatos')
        if DB_HOST_mysql==DB_HOST_mysql and DB_USER_mysql==DB_USER_mysql and DB_PASS_mysql==DB_PASS_mysql and DB_NAME_mysql==DB_NAME_mysql:
                datos = [DB_HOST_mysql,DB_USER_mysql,DB_PASS_mysql,DB_NAME_mysql]
                conectar = MySQLdb.connect(*datos)
                cursor = conectar.cursor()
                datos = cursor.execute("SHOW TABLES;")
                datos = cursor.fetchall()
                cursor.close()
                conectar.close()
        return template('tabla.html',datos=datos,DB_USER_mysql=DB_USER_mysql,DB_NAME_mysql=DB_NAME_mysql)

@route('/consultas',method="GET")
def consultas():
        return template("consultas.html")

@route('/consulta',method="POST")
def consulta():
	DB_HOST_mysql = request.forms.get('host')
        DB_USER_mysql = request.forms.get('usuario')
        DB_PASS_mysql = request.forms.get('password')
	DB_NAME_mysql = request.forms.get('basedatos')
	consulta = request.forms.get('consulta')
        if DB_HOST_mysql==DB_HOST_mysql and DB_USER_mysql==DB_USER_mysql and DB_PASS_mysql==DB_PASS_mysql and DB_NAME_mysql==DB_NAME_mysql:
		datos = [DB_HOST_mysql,DB_USER_mysql,DB_PASS_mysql,DB_NAME_mysql]
        	conectar = MySQLdb.connect(*datos)
        	cursor = conectar.cursor()
        	datos = cursor.execute(consulta)
        	datos = cursor.fetchall()
        	cursor.close()
        	conectar.close()
	return template('consulta.html',datos=datos,DB_USER_mysql=DB_USER_mysql,DB_NAME_mysql=DB_NAME_mysql,consulta=consulta)

run(host='0.0.0.0', port='8000')

