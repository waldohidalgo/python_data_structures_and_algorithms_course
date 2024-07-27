# Python Data Structures and Algorithms Course

Repositorio con mis implementaciones de las estructuras de datos auxiliares y algoritmos del curso de Linkedin Learning llamado [Python Data Structures and Algorithms](https://www.linkedin.com/learning/python-data-structures-and-algorithms).

Se implementan las siguientes estructuras de datos:

- Stack creada en base a las listas de python

- Queue creada en base a las **deque** del módulo **collections** de python

- Priority queue implementada en base al módulo **heapq** de python (heaps son árboles binarios completos que cumplen la condición de invarianza: cada nodo padre posee un valor menor o igual a los valores de sus nodos hijos)

Además, se crean los algoritmos siguientes:

- Depth-First Search implementado sobre la Stack

- Breadth-First Search implementado sobre la Queue

- A Star Search implementado sobre la Priority Queue

## Tabla de Contenidos

- [Python Data Structures and Algorithms Course](#python-data-structures-and-algorithms-course)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Certificado](#certificado)
  - [Estructuras de Datos Auxiliares utilizadas para crear los algoritmos](#estructuras-de-datos-auxiliares-utilizadas-para-crear-los-algoritmos)
    - [Stack](#stack)
    - [Queue](#queue)
    - [Priority Queue](#priority-queue)
  - [Algoritmos](#algoritmos)
    - [Depth-First Search Algorithm](#depth-first-search-algorithm)
    - [Breadth-First Search Algorithm](#breadth-first-search-algorithm)
    - [A\* Search Algorithm](#a-search-algorithm)

## Certificado

![Certificado Finalización de Curso](./certificado.webp)

## Estructuras de Datos Auxiliares utilizadas para crear los algoritmos

### Stack

```py
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
```

### Queue

```py
from collections import deque

class Queue:
    def __init__(self,*args):
        self.items = deque(
            args
        )

    def is_empty(self):
        return not self.items
        # return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)
```

### Priority Queue

```py
import heapq

class PriorityQueue:

    def __init__(self):
        self.elements = []
    def is_empty(self):
        return not self.elements
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    def get(self):
        return heapq.heappop(self.elements)[1]
    def peek(self):
        return self.elements[0][1]
    def __str__(self):
        return str(self.elements)
```

## Algoritmos

Los algoritmos se implementan para buscar un nodo final partiendo de un nodo de inicio en tableros de 2 dimensiones que se denominan **mazes**. Dichos mazes se almacenan como archivos de texto y se utiliza python para leer tales archivos y crear los respectivas lista de listas que representan a los tableros en 2D.

### Depth-First Search Algorithm

```py
from helpers import get_path, offsets, is_legal_pos, read_maze
from stack import Stack

# depth first search algorithm based on the stack data structure

def dfs(maze, start, goal):
    stack = Stack()
    stack.push(start)
    predecessors = {start: None}
    while not stack.is_empty():
        current = stack.pop()
        if current == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            [row_offset, col_offset] = offsets[direction]
            next = (current[0] + row_offset, current[1] + col_offset)
            if is_legal_pos(maze, next) and next not in predecessors:
                stack.push(next)
                predecessors[next] = current
    return None
```

### Breadth-First Search Algorithm

```py
def bfs(maze, start, goal):
    queue = Queue()
    queue.enqueue(start)
    predecessors = {start: None}

    while not queue.is_empty():
        current_cell = queue.dequeue()
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(maze, neighbour) and neighbour not in predecessors:
                queue.enqueue(neighbour)
                predecessors[neighbour] = current_cell
    return None
```

### A\* Search Algorithm

El algoritmo A Star utiliza tres métricas para establecer la **prioridad** de los nodos que se agregan a la priority queue las cuales son las siguientes:

- G value: Distancia desde el nodo de inicio hasta el nodo actual de la iteración

- H value: Distancia desde el nodo actual al nodo final calculada utilizando la heuristica **Manhattan Distance**

- F value: la suma de las métricas G y H

```py
from helpers import get_path, offsets, is_legal_pos, read_maze
from priority_queue import PriorityQueue


def heuristic(a, b):
    """
    Calculates the Manhattan distance between two pairs of grid coordinates.
    """
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(maze, start, goal):
    # g value is the cost from the start to the current cell
    # h value is the estimated cost from the current cell to the goal getting from heuristic
    # f value is the sum of the g and h values
    pq=PriorityQueue()
    pq.put(start, 0)
    predecessors = {start: None}
    g_values={start:0}

    while not pq.is_empty():
        current_cell = pq.get()
        if current_cell == goal:

            return get_path(predecessors, start, goal)

        for direction in ["up", "right", "down", "left"]:

            [row_offset, col_offset] = offsets[direction]

            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)

            if is_legal_pos(maze, neighbour) and neighbour not in predecessors:
                g = heuristic(neighbour, goal)

                new_cost = g_values[current_cell] + 1

                g_values[neighbour] = new_cost
                f_value=new_cost + g
                pq.put(neighbour, f_value)
                predecessors[neighbour] = current_cell


    return None
```
