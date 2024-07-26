# Nauru1000C

Repositório que contém a simulação de um drone VTOL, similar ao drone Nauru 1000C, da empresa XMobots. Este é um trabalho realizado para a disciplina de SEM0576 - Veículos Aéreos Autônomos.

# Simulação do Drone com Gazebo e PX4

Este repositório contém instruções para rodar uma simulação de um drone VTOL usando Gazebo e PX4, além de scripts para controle do drone e obtenção de dados provenientes dos sensores. Foram elaborados 4 (quatro) arquivos para simulação do drone. O primeiro arquivo, `drone-control.py`, e o segundo, `sensor-data.py`, servem apenas para exemplificar uma movimentação manual do drone, sendo possível realizar a decolagem e pouso, e coletas de dados de sensores (recomenda-se que ambos os códigos sejam rodados ao mesmo tempo). Já os outros dois `simulation.py` e `simulation_sensor.py` são os scripts de simulações mais completas. O `simulation.py` realiza uma simulação em que o drone, sozinho, decola e navega até uma certa posição preestabelecida e retorna para a base da qual partiu. O `simulation_sensor.py` realiza a mesma simulação, além de coletar dados de velocidade pelos sensores do drone e, ao final, plota-se um gráfico com as diferentes velocidades em função do tempo. 

Vale ressaltar que as duas simulações mais completas buscaram se aproximar do funcionamento do Nauru 1000C, em que as hélices são usadas para decolagem e pouso, e as asas fixas para o voo em si.

## Pré-requisitos
1. **Instalar ROS e Gazebo:**
   - Caso ainda não os tenha, siga as orientações de instalação da [wiki do ROS](https://wiki.ros.org/noetic/Installation).

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

## Instruções para rodar a simulação completa sem dados do sensor:

1. **Com o repositório já clonado, está disponível o arquivo simulation.py;**
2. **Rode esse arquivo;**

    ```bash
    cd /nauru
    python3 simulation.py
    ```
    
3. **No Gazebo, pode-se observar a simulação do drone voando.**

## Instruções para rodar a simulação completa com dados do sensor:

1. **Com o repositório já clonado, está disponível o arquivo simulation_sensor.py;**
2. **Rode esse arquivo;**

    ```bash
    cd /nauru
    python3 simulation_sensor.py
    ```
    
3. **No Gazebo, pode-se observar a simulação do drone voando. Ao final da simulação será gerado um gráfico com as velocidades medidas pelos sensores do drone durante a simulação.**

# Autores
- Carlos Nery Ribeiro - 12547698
- Gabriel Ribeiro Rodrigues Dessotti - 12547228
- Lucas Carvalho Freiberger Stapf - 1180059
- Edson Jose Brumatti Junior - 9880169
- Lucas Bosso de Mello - 14590670

