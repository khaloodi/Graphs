import random


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name 

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return(False)
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return(False)
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return(True)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # 100 users, avg 10 friendships each?
        # ex: avg_friendships = total_friendships / num_users
        # 2 = total_friendships / 10
        # so total_friendships = 20
        # therefore, 10 = total_friendships / 100 ... = 1000
        # total_friendships = avg_friendships * num_users
        # BUT have to divide by 2 b/c every time we call add friendships, it adds 2 friendships !!!

        # Add users
        for i in range(num_users):
            self.add_user(f" User {i + 1}")

        # Create friendships
        # total_friendships = avg_friendships * num_users

        # create a list with all possible friendship combinations 
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # print('POSSIBLE FRIENDSHIPS:')
        # print(possible_friendships)
        # print('TOTAL POSSIBLE FRIENDSHIPS:')
        # print(len(possible_friendships))

        # shuffle the list,
        random.shuffle(possible_friendships)
        print(possible_friendships)

        # then grab the first N elements from the list. You will need to import random to get shuffle.
        # nuber of times to call add_friendship = avg_friendships * num_users
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        # O(N) solution:
        # total_friendships = avg_friendships * numUsers
        # friendshipsCreated = 0
        # while friendshipsCreated < totalFriendships:
            # pick a random number 1-n, pick another random number 1-n 
            # userID = random.randint(1, self.lastID)
            # friendID = random.randint(1, self.lastID)
            # create friendship between those 2 ids
            # if self.addFriendship(userID, friendID):
                # friendshipsCreated += 2

            # until you have friendship count == totalFriendships

        #  totalFriendships = avg


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # do a BFT, store the paths as we go
        # BFT steps:
        # create an empty queue
        q = Queue()
        visited = {}  # Note that this is a dictionary, not a set
        # add a PATH from the starting node to the queue
        q.enqueue([user_id])
        # while the queue is not empty... 
        while q.size() > 0:
            # dequeue FIRST PATH from the queue
            path = q.dequeue()
            v = path[-1]
            # check if it's been visited
            if v not in visited:
                # when we reach an unvisited node, add the path to visited dictionary
                visited[v] = path 
                # add a path to each neighbor to the back of the queue
                for friend in self.friendships[v]:
                    path_copy = path.copy() # or can do list of path
                    path_copy.append(friend)
                    q.enqueue(path_copy)
        # return visited dictionary
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(11, 3)
    print("----------")
    print('USERS:')
    print(sg.users)
    print("----------")
    print('FRIENDSHIPS:')
    print(sg.friendships)

    print('\nSocial Paths:')
    connections = sg.get_all_social_paths(1)
    print(connections)
