# version 1.0
# requisitos : haber aprendido el skill al menos a 30, pero la verdad no es necesario, solo acortaria el proceso
#               el serial de una caja o item en tu casa o en el banco
#               ver "cosas que debes saber hacer"
# descripcion : realiza la actividad de detecthidding cada 10 segundos
# configuracion este escript debe estar configurado para ejecutarse con la tecla F1
#               este debe configurase con la opcion del razor de  Loop Mode
#               ver "cosas que debes saber hacer"
# consejos      cualquier lugar es bueno para practicar detecthidding
#                tu casa o el banco son excelentes opciones
#                pero no elijas un lugar peligroso con npc agresivos
#                la libreria del UOAlive es ideal para entrenar esta habilidad y ganar Britcoins
#                este script puede ser usado como molde para entrenar muchas otras actividades como por ejemplo
#                skills gratuitas del server UOAlive arms lore, hidding(sin la linea 19 y 20), item identification taste identification
#                otras skills animal lore, evaluate intelligence, stealing, anatomy, 
#                solo basta con cambiar el skill de la linea 19 y el item de la linea 18 segun la skill requiera otra persona, un pet, o un item X
##############################################################################
item = 0x4034EDF5           #serial de un item en el piso
Player.UseSkill("Detect Hidden")
Target.WaitForTarget(10000, False)
Target.TargetExecute(item)
Misc.Pause(10000)
