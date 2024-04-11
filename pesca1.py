# version 1.0
# requisitos : una caña de pesca que debe estar en la mano del personaje
#              haber usado una vez el scrip pesca1 y tener exito en la pesca (animacion de pesca)
#              colocar el serial de la caña de pesca en el scrip  *** mejorar esto
#              ver "cosas que debes saber hacer"
#              archivo color.py para que los mensajes se vean a colores
# descripcion : realiza la actividad de pesca 10 veces en el mismo lugar 
#               donde se realizo la pesca en el scrip pesca1
#               el scrip se corta con un mensaje "Ya no hay peces" si es que
#               hay que cambiar de posicion de pesca, caso contrario
#               se puede ejecutar el scrips muchas veces seguidas
#               sin necesidad de cambiar de posicion de pesca.
# configuracion este scrip debe estar configurado para ejecutarse con la tecla F1
#               y el scrip pesca2 en la tecla F2 para mayor comodidad
# consejos      ya que los peces y trofeos pesan mucho, es bueno andar con una pet de carga
#               una llama o mejor aun una cucaracha para poder meter dentro lo que pesquemos
#               la pesca desde los puertos o la tierra firme no crea moustruos que te ataquen
#               para subir la habilidad mas que 65 es mejor salir de las ciudades
##############################################################################

from colors import colors
canadepesca = 0x41414DA6
Items.UseItem(canadepesca)
Target.WaitForTarget(10000, False)
#Target.Last()
#Target.TargetExecute(3492, 2601 ,-5 ,6044)
Misc.Pause(11000)
Player.HeadMessage( colors[ 'green' ], 'Primera pesca Grabada')
