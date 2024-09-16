import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path
from std_msgs.msg import Header
from queue import PriorityQueue
import math
from node import Node

class AStarPlanner:
    def __init__(self):
        self.map_data = None
        self.map_resolution = 0.0
        self.map_origin_x = 0.0
        self.map_origin_y = 0.0
        self.start_pose_x = None
        self.start_pose_y = None
        self.goal_pose_x = None
        self.goal_pose_y = None
        self.map_width = 0
        self.map_height = 0
        self.execution_speed = 0.1

    # Função para converter coordenadas da grade para o mundo real
    def grid_to_world(self, x, y):
        world_x = x * self.map_resolution + self.map_origin_x
        world_y = y * self.map_resolution + self.map_origin_y
        return world_x, world_y, 0

    # Função para converter coordenadas do mundo real para a grade
    def world_to_grid(self, x, y):
        world_x = int((x - self.map_origin_x) / self.map_resolution)
        world_y = int((y - self.map_origin_y) / self.map_resolution)
        return world_x, world_y

    # Função de callback para receber o occupancy grid
    def map_callback(self, data):
        self.map_data = data.data
        self.map_resolution = data.info.resolution
        self.map_origin_x = data.info.origin.position.x
        self.map_origin_y = data.info.origin.position.y
        self.map_width = data.info.width
        self.map_height = data.info.height

    # Função para verificar se uma célula está livre (valor < 50)
    def is_cell_free(self, x, y):
        index = x + y * self.map_width
        if index >= 0 and index < len(self.map_data):
            if self.map_data[index] > -1 and self.map_data[index] < 50:
                return True
        return False

    # Função de heurística
    def heuristic(self, x, y):  
        goal_pose_x, goal_pose_y = self.world_to_grid(self.goal_pose_x, self.goal_pose_y) 
        dist = abs(x - goal_pose_x) + abs(y- goal_pose_y)                                    
        # dist = math.sqrt((x - self.goal_pose_x)**2 + 
        #                  (y - self.goal_pose_y)**2)
        return dist

    # Função para obter os vizinhos de um nó
    def get_neighbors(self, node):
        neighbors = []
        x = node.x
        y = node.y

        # Movimentos possíveis: cima, baixo, esquerda, direita
        possible_moves = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]

        for move in possible_moves:
            nx, ny = move
            if self.is_cell_free(nx, ny):
                g_cost = node.g_cost + 1  # Custo do movimento para uma célula vizinha
                h_cost = self.heuristic(nx, ny)
                new_node = Node(nx, ny, g_cost, h_cost, node)
                neighbors.append(new_node)

        return neighbors

    # Função para encontrar o caminho utilizando o algoritmo A*
    def find_path(self, rviz=None):
        if self.map_data is None:
            rospy.loginfo("Map or start/goal pose not received yet.")
            return

        # Converter as coordenadas do mundo real para as coordenadas da grade
        start_x, start_y = self.world_to_grid(self.start_pose_x, self.start_pose_y)
        goal_x, goal_y = self.world_to_grid(self.goal_pose_x, self.goal_pose_y)

        # Inicializar a lista aberta e fechada
        open_list = PriorityQueue()
        closed_list = []

        # Criar o nó inicial e adicionar à lista aberta
        start_node = Node(start_x, start_y, 0, self.heuristic(start_x, start_y))
        open_list.put((start_node.f_cost(), start_node))

        # Origin and Goal Markers
        rviz.publish_marker(self.grid_to_world(start_x, start_y), (1.0, 0, 0), self.map_resolution)
        rviz.publish_marker(self.grid_to_world(goal_x, goal_y), (1.0, 0.0, 0.0), self.map_resolution)

        counter = 0
        past_node = None
        while open_list:
            # Obter o nó com o menor custo da lista aberta
            _, current_node = open_list.get()

            # Verificar se chegamos ao nó objetivo
            if current_node.x == goal_x and current_node.y == goal_y:
                rospy.loginfo("Goal reached!")

                self.publish_path(current_node, rviz)
                return

            # Adicionar o nó atual à lista fechada
            closed_list.append((current_node.x, current_node.y))
            if counter != 0:
                rviz.update_marker_color(self.grid_to_world(past_node.x, past_node.y), (1, 0, 0))
            counter += 1
            past_node = current_node
            rviz.update_marker_color(self.grid_to_world(current_node.x, current_node.y), (1, 1, 0))
            rospy.sleep(self.execution_speed)

            # Obter os vizinhos do nó atual
            neighbors = self.get_neighbors(current_node)

            for neighbor in neighbors:
                # Verificar se o vizinho já está na lista fechada
                if (neighbor.x, neighbor.y) in closed_list:
                    continue

                # Verificar se o vizinho já está na lista aberta
                if any(node[1].x == neighbor.x and node[1].y == neighbor.y for node in open_list.queue):
                    continue

                rviz.publish_marker(self.grid_to_world(neighbor.x, neighbor.y), (0, 1, 0.0), self.map_resolution)
                # Adicionar o vizinho à lista aberta
                open_list.put((neighbor.f_cost(), neighbor))

        rospy.loginfo("Path not found.")

    def publish_path(self, goal_node, rviz=None):
        # Percorrer o caminho a partir do nó objetivo
        current_node = goal_node
        while current_node is not None:
            rviz.update_marker_color(self.grid_to_world(current_node.x, current_node.y), (1.0, 1.0, 0.0))
            rospy.sleep(0.05)
            current_node = current_node.parent