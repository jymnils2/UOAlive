# version 1.0
# requisitos : tener al menos 1 item del elemento "lockpick" en la bolsa
#              colocar el serial de los lockpick en el scrip  *** mejorar esto
#              ver "cosas que debes saber hacer"
#              archivo color.py para que los mensajes se vean a colores
# descripcion : usa los lockpicks para intentar abrir una caja cerrada
# configuracion este scrip debe estar configurado para ejecutarse con la tecla F1
#               asi es mas facil ejecutarlo y detenerlo para cambiar la dificultad
#               de la caja de entrenamiento
#               para crear un bucle infinito activar la opcion de los scripts para repetirse
#               ver "cosas que debes saber hacer"    
# consejos      para volverlo un bucle infinito quitar el comentario de la linea 22
#               si usamos la caja de entrenamiento de la libreria de UOAlive subir a 100
#               de lockpicking es cosa de 1 hora, llevar muchos lockpicks porque se romperan muchos
#               la caja de la libreria puede cambiar su dificultad haciendo doble click
#               sobre ella, asi la ganancias son posibles hasta 120
##############################################################################

Items.UseItem(0x40A70AD9) # doble click en los lockpicks
Target.WaitForTarget(10000, False)
Misc.Pause(1000)                # esperar 1 segundo por diplomacia con el servidor
# Target.Last()                 # quitar el primer caracter de comentario para hacer un bucle infinito