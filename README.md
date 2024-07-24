# Nauru1000c
Repository that contains the simulation of a quadcopter and VTOL drone, similar to the Nauru 1000C drone, from the company XMobots. This is work done for the Autonomous Aerial Vehicles discipline.

# Simulação do Drone com Gazebo e PX4

Este repositório contém instruções para rodar uma simulação de um drone VTOL usando Gazebo e PX4, além de scripts para controle do drone e obtenção de dados dos sensores.

## Pré-requisitos

1. **Instalar ROS e Gazebo:**
   - Caso ainda não os tenha, siga as orientações de instalação da [wiki do ROS](https://wiki.ros.org/ROS/Installation).

2. **Instalar o Firmware do PX4 Autopilot:**
   - O modelo escolhido para representar nosso drone é o `standard_vtol` e está contido na PX4.
   
   Execute os seguintes comandos:

   ```bash
   git clone https://github.com/PX4/PX4-Autopilot.git --recursive
   bash ./PX4-Autopilot/Tools/setup/ubuntu.sh

3. **Entrar no diretório da PX4 e rodar o comando para iniciar a simulação com Gazebo;**

    ```bash
    cd /PX4-Autopilot
    make px4_sitl gazebo-classic_standard_vtol
    ```
4. **Após essas etapas, o Gazebo vai estar aberto com o drone pousado.**

## Instruções para controle do drone:

1. **Clonar o repositório do GitHub que contém os códigos;**

    ```bash
    git clone https://github.com/dessotti1/Nauru1000c.git
    ```

2. **Rodar o código drone-control.py;**

    ```bash
    cd /nauru
    python3 drone-control.py
    ```

3. **No terminal, aparecem as informações para controle (‘t’ para takeoff, ‘l’ para pouso, dentre outros).**

## Instruções para obtenção de dados dos sensores:

1. **Com o repositório já clonado, está disponível o arquivo sensor-data.py;**
2. **Rode esse arquivo;**

    ```bash
    cd /nauru
    python3 sensor-data.py
    ```
    
3. **No terminal, pode-se observar os sensores disponíveis e digite um deles para ver os dados.**



