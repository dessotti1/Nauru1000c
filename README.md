# Nauru1000c
Repository that contains the simulation of a quadcopter and VTOL drone, similar to the Nauru 1000C drone, from the company XMobots. This is work done for the Autonomous Aerial Vehicles discipline.

Instruções para rodar nossa simulação:

Ter o ROS e o Gazebo instalados (caso não os tenha, siga as orientações de instalação da wiki do ROS);
Instalar o Firmware da PX4 Autopilot (o modelo escolhido para representar nosso drone é o standard_vtol e está contido na PX4);
git clone https://github.com/PX4/PX4-Autopilot.git --recursive
bash ./PX4-Autopilot/Tools/setup/ubuntu.sh
Entrar no diretório da PX4 e rodar o comando para iniciar a simulação com Gazebo;
cd /PX4-Autopilot
make px4_sitl gazebo-classic_standard_vtol
Após essas etapas, o Gazebo vai estar aberto com o drone pousado.

Instruções para controle do drone:

Clonar o repositório do GitHub que contém os códigos;
git clone https://github.com/dessotti1/Nauru1000c.git 
Rodar o código drone-control.py;
cd /nauru;
python3 drone-control.py;
No terminal, aparecem as informações para controle (‘t’ para takeoff, ‘l’ para pouso, ‘r’ para retorno, entre outras).

Instruções para obtenção de dados dos sensores:

Com o repositório já clonado, está disponível o arquivo sensor-data.py;
Rode esse arquivo;
cd /nauru;
python3 sensor-data.py
No terminal, pode-se observar os sensores disponíveis e digite um deles para ver os dados.



