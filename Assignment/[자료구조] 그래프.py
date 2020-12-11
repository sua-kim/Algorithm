# 파이썬으로 그래프 구현: Person 클래스

class Person:
  def __init__(self, name):
    self.name = name
    self.friends = []
   
  def add_friend(self, friend):
    self.friends.append(friend)

mary = Person("Mary")
peter = Person("Peter")
kim = Person("Kim")
mary.add_friend(peter)
peter.add_friend(mary)
peter.add_friend(kim)

print(peter)
print(mary)
print(peter.name)
print(mary.name)
print(mary.friends[0].name)
print(peter.friends[1].name)



# 파이썬으로 그래프 너비우선 탐색 구현: Person 클래스 + display_network 메서드 추가

class Person:
  def __init__(self, name):
    self.name = name
    self.friends = []
    self.visited = False
   
  def add_friend(self, friend):
    self.friends.append(friend)
  
  def display_network(self):
    to_reset = [self]
    queue = [self]
    self.visited = True
    
    while len(queue):
      current_vertex = shift(queue)
      print(current_vertex.name)
      
      for friend in current_vertex.friends:
        if not friend.visited:
          to_reset.append(friend)
          queue.append(friend)
          friend.visited = True
      
      for node in to_reset:
        node.visited = False

  def __str__(self):
    return self.name
    
def shift(list):
  vertex = list[0]
  for i in range(1, len(list)):
    list[i-1] = list[i]
  list.pop()
  return vertex
  
alice = Person("Alice")
bob = Person("Bob")
candy = Person("Candy")
derek = Person("Derek")
elaine = Person("Elaine")
fred = Person("Fred")
gina = Person("Gina")
helen = Person("Helen")
irena = Person("Irena")
alice.add_friend(bob)
alice.add_friend(candy)
alice.add_friend(derek)
alice.add_friend(elaine)
bob.add_friend(fred)
derek.add_friend(gina)
fred.add_friend(helen)
gina.add_friend(irena)

alice.display_network()


# 가중 그래프 구현: city 클래스

class City:
  def __init__(self, name):
    self.name = name
    self.routes = {}
  def add_route(self, city, price):
    self.routes[city] = price

dallas = City("Dallas")
toronto = City("Toronto")
dallas.add_route("Toronto", 138)
toronto.add_route("Dallas", 216)
dallas.add_route(toronto, 138)
toronto.add_route(dallas, 216)

print(list(dallas.routes.keys()))
print(list(dallas.routes.values()))
print(list(toronto.routes.values()))

t_friend = list(toronto.routes.keys())
print(t_friend)
print(type(str(t_friend[0])))
print(toronto.routes['Dallas'])
print(toronto.routes[str(t_friend[0])])
print(str(t_friend[0]))
print(dallas.name)

toronto.routes[dallas.name]

atlanta = City("Atlanta")
boston = City("Boston")
chicago = City("Chicago")
denver = City("Denver")
elpaso = City("Elpaso")
atlanta.add_route("Boston", 100)
atlanta.add_route("Denver", 160)
boston.add_route("Chicago", 120)
boston.add_route("Denver", 180)
chicago.add_route("Elpaso", 80)
denver.add_route("Chicago", 40)
denver.add_route("Elpaso", 140)
elpaso.add_route("Boston", 100)



# 최단경로 알고리즘: 다익스트라 알고리즘

class City:
  def __init__(self, name):
    self.name = name
    self.routes = {}
  def add_route(self, city, price):
    self.routes[city] = price

atlanta = City("Atlanta")
boston = City("Boston")
chicago = City("Chicago")
denver = City("Denver")
elpaso = City("Elpaso")
atlanta.add_route(boston, 100)
atlanta.add_route(denver, 160)
boston.add_route(chicago, 120)
boston.add_route(denver, 180)
chicago.add_route(elpaso, 80)
denver.add_route(chicago, 40)
denver.add_route(elpaso, 140)
elpaso.add_route(boston, 100)

def dijkstra(starting_city, other_cities):
  routes_from_city = {}
  routes_from_city[starting_city] = [0, None]
  
  for city in other_cities:
    routes_from_city[city] = [float('inf'), None] 
  visited_cities = []
  current_city = starting_city
  
  while current_city:
    visited_cities.append(current_city)
    for city in current_city.routes :
      price_info = current_city.routes[city]
      if routes_from_city[city][0] > price_info + routes_from_city[current_city][0] :
         routes_from_city[city] = [price_info + routes_from_city[current_city][0], current_city.name]
  current_city = None
  cheapest_route_from_current_city = float('inf')
  for city in routes_from_city :
    price_info = routes_from_city[city][0]
    if price_info < cheapest_route_from_current_city and not (city in visited_cities):
      cheapest_route_from_current_city = price_info
      current_city = city
  return routes_from_city
  
routes = dijkstra(atlanta, [boston, chicago, denver, elpaso])
for city in routes:
  price_info = routes[city][0]
  print("city name", city.name)
  print("price info", price_info)
