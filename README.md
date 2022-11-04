# ENGG68 - Atividade 4


# Pré-Requisitos

- ROS Noetic
- Gazebo
- Husky
- PlotJuggler

**Observação:** Antes de rodar os packages que serão descritos abaixo, rodar o seguinte comando, dentro da pasta worskpace/husky_robot_localization/src para cada um dos arquivos .py:

```bash
chmod +x odom.py
```

```bash
chmod +x odom_filtered.py
```

```bash
chmod +x ground_truth.py
```

# Descrição

O package desenvolvido trás três opções de coleta de dados de coordenadas do robô: Através dos dados brutos de odometria dos sensores (odom.py), os dados de odometria filtrados (odom_filtered.py) e através do ground truth coletados direto do gazebo (ground_truth.py). 

## Odometry (odom.py)

Coleta dados de odometria e publica estes dados em um tópico, foi criado o package odom.py. Os dados publicados são do tipo Odometry, deixando flexível se o usuário deseja acessar os dados de pose ou se deseja acessar a coordenada atual do robô. 

Para ativar o tópico, basta rodar o seguinte comando:

```bash
rosrun husky_robot_localization odom.py
```

## Odometry/Filtered

Para criar o package que coleta dados de odometria filtrado e publica estes dados em um tópico, foi criado o package odom.py. Os dados publicados são do tipo Odometry, deixando flexível se o usuário deseja acessar os dados de pose ou se deseja acessar a coordenada atual do robô. 

Para ativar o tópico, basta rodar o seguinte comando:

```bash
rosrun husky_robot_localization odom_filtered.py
```

## Ground Truth

Para configurar o ground truth, é necessário adicionar o seguinte código no arquivo .URDF do Husky (husky.urdf.xacro):

```xml
<gazebo>
  <plugin name="ground_truth" filename="libgazebo_ros_p3d.so">
    <frameName>map</frameName>
    <bodyName>base_link</bodyName>
    <topicName>ground_truth</topicName>
    <updateRate>30.0</updateRate>
  </plugin>
</gazebo>
```

Após isso, os dados de ground truth ficarão acessíveis no ROS. Com isso, foi possível desenvolver o package ground_truth.py, responsável por publicar estes dados em um tópico de forma a ser possível a visualização destes dados. O comando para ativar o tópico é o seguinte:

```bash
rosrun husky_robot_localization ground_truth.py
```

# Visualização dos dados

Os dados serão visualizados no software PlotJuggler. Há duas opções para a visualização dos dados:

Executar  os três comandos descritos acima em terminais diferentes de forma a conseguir acessar os três tópicos no Plot Juggler. Em seguida, ativar a opção de streaming com um ROS topic subscriber.

Importar os dados a partir dos arquivos gerados através do rosbag (na pasta “husky_data” do package). Dentro da pasta há um arquivo .xml com o layout dos gráficos gerados no plotjugger.

# Comandos a serem executados no terminal

Segue abaixo todos os comandos necessários (e em ordem) para rodar o package em sua totalidade:

> Obs: Conferir em cada terminal se o setup.bash já foi inserido no source.
> 

### Inicialização do ROS

```bash
roscore
```

Iniciar o ambiente Gazebo com o Husky inserido no LAR

```bash
roslaunch lar_gazebo lar_husky.launch
```

### Rodar todos packages disponíveis no husky_robot_localization (em terminais diferentes).

> Obs: Há a opção também de adicionar estes packages para se iniciarem automaticamente no arquivo .launch, o que é uma opção mais interessante.
> 

```bash
rosrun husky_robot_localization odom.py
```

```bash
rosrun husky_robot_localization odom_filtered.py
```

```bash
rosrun husky_robot_localization ground_truth.py
```

### Rodar o package random_driver

```bash
rosrun random_husky_driver random_driver
```

### Rodar o plotjuggler

```bash
rosrun plotjuggler plotjuggler
```
