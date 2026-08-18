import os 
from datetime import datetime
import pandas as pd
import kits
import programa_lab

programa_lab.inicializar_sistema()
programa_lab.menu_principal()

'''streamlite faz com que voce tenha um ip acessivel para a aplicação remota. ou seja, um frontend 
consegue requisitar sua aplicacao python.

É o proximo passo que eu gostaria de dar, porque ele roda no prompt de comando e eu estava pensando 
em transformar em um progama para os alunos acessarem das maquinas deles e eu apenas avaliar depois, 
por enquanto ele salva tudo em excel'''


'''sim.tem que estar na mesma rede para que o ip possa ser acessível ou ser hospedado na web. para hospedar na web tem que ser 
um servidor que roda o python, o que nao é tao facilitado pq nao é uma aplicacao web nativa. talvez precisaria contratar 
uma vps pra esse caso. dai ao inves de estar na rede local, ficava web'''''