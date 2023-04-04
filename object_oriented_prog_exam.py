import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        for load in self.connections.values():
            total += load
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    

server = Server()
server.add_connection("192.168.1.1")

# print(server.load())    # load is calculated randomly, should be different each time it's executed. Output should be a number between 1 and 10

# server.close_connection("192.168.1.1")
# print(server.load())    # output should be 0







#Begin Portion 2#
#Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        self.connections[connection_id] = server
        self.servers.append(server)

        # Add the connection to the dictionary with the selected server
        # Add the connection to the server

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer

    def avg_load(self):
        """Calculates the average load of all servers"""
        # sum = 0
        print(l.connections)
        # for Server.load in self.servers:
        #     print(Server.load)
            # sum += Server.load
        # return sum
        
        # Sum the load of each server and divide by the amount of servers

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        pass

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))






l = LoadBalancing()

l.add_connection("fdca:83d2::f20d")
l.add_connection("fdca:84d2::f10d")

print(l.avg_load())
