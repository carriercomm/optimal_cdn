from client import ClientManager
from server import ServerManager
from placement_algorithms import placement, optimal_placement

def read_input(file_name):
    """
    Input: file name (string).
    File format:
        int algorithm (1 or 2)
        int number of servers
        list of int [client demands]
    Reads file and outputs a list of clients, a list of servers and the algorithm.
    """
    f = open(file_name, 'r')
    client_manager = ClientManager()
    server_manager = ServerManager()
    algorithm = int(f.readline())
    number_servers = int(f.readline())
    servers = [server_manager.create_server() for i in range(number_servers)]
    demands = map(int, f.readline().split())
    clients = [client_manager.create_client(demand) for demand in demands]
    return clients, servers, algorithm

if __name__ == '__main__':
    clients, servers, algorithm = read_input('input_1.txt')
    placement_algorithm = placement if algorithm==1 else optimal_placement
    placement_manager = placement_algorithm(clients, servers)
    for server in servers:
        served_clients = placement_manager.get_clients_served_by(server)
        print ("Server", server.id, ", used capacity =", server.used_capacity)
        print ("Client ids:", [client.id for client in served_clients])
        print ("Client demands:", [client.demand for client in served_clients])
        print ("########################################################################")




