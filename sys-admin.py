# Importación de modulo "os" para administración de archivos:
import os

# Importación del modulo "subprocess"
import subprocess

# os.system() permite ejecutar comando Bash
os.system("ls")

print("\nSUBPROCESSES.RUN(): \n")

# Al igual que subprocess.run()
subprocess.run(["ls", "-l"])

print("\nSUBPROCESSES.RUN() con varios argumentos: \n")
# Uso de run para ejecutar comandos con multiples argumentos
subprocess.run(["ls", "-l", "README.md"])

# Ejemplo de subprocess.run para ejecutar comando "uname" con argumento
# para mostrar información del sistema:

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# Haciendo hincapié de subprocess.run() para obtener información de procesos:
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])