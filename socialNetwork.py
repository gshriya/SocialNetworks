import random

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]
    

 
    for i in range(len(friends)):
        friends[i]=friends[i].split(' ')
        if i!=0:
            if ((int(friends[i][0]),[]) not in network):
                network.append((int(friends[i][0]),[]))
            if ((int(friends[i][1]),[]) not in network):
                network.append((int(friends[i][1]),[]))

    network.sort()
    friends.remove(friends[0])
    
    for v in range(len(network)):
        for h in range(len(friends)):
            if network[v][0] == int(friends[h][0]):
                network[v][1].append(int(friends[h][1]))
            if network[v][0] == int(friends[h][1]):
                network[v][1].append(int(friends[h][0]))
                
    return network

def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->int
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]

    
    
    user1l = []
    user2l = []
    network.sort()

    for y in range(len(network)):
        if network[y][0] == user1:
            user1l = network[y][1]
        if network[y][0] == user2:
            user2l = network[y][1]

    for i in range(len(user1l)):
        if user1l[i] in user2l:
            common.append(user1l[i])
    

    return common

    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''
    
    
    
    user1l=[]
    index = 0
    currentlength=0
    currentuser=None
    
    for y in range(len(network)):
        if network[y][0] == user:
            user1l = network[y][1]
            index = y

    for i in range(len(network)):
        if i != index:
            if (len(getCommonFriends(user,network[i][0],network)) > currentlength and (network[i][0] not in user1l)):
                currentlength = len(getCommonFriends(user,network[i][0],network))
                currentuser = network[i][0]

    return currentuser


def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''

    
    
    atleast=0


    for n in range(len(network)):
        if len(network[n][1]) >=  k:
            atleast = atleast + 1
    
    return atleast

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has. Same most friends
    '''

    
    
    currentmax = 0

    for k in range(len(network)):
        if len(network[k][1]) > currentmax:
            currentmax = len(network[k][1])
    return currentmax
    

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    
    
    findmax = maximum_num_friends(network)

    for u in range(len(network)):
        if (findmax == len(network[u][1])):
            max_friends.append(network[u][0])

                             
    return max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''
    
    
    
    total1 = 0
    
    for i in range(len(network)):

        total1 = total1 + len(network[i][1])

    
    return total1/len(network)
    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''

   

    for z in range(len(network)):
        if len(network[z][1]) == len(network)-1:
            return True
      
    return False


####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''()->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''

    

    a = "Nothing"

    user = input("Enter an integer for a user ID: ").strip()

    while (exists(user,network) == False):

        try:
            int(user)
        except:
            a = True

        if a!=True:
            print("That user ID does not exist. Try again.")
            user = input("Enter an integer for a user ID: ").strip()
        else:
            print("That was not an integer. Please try again.")
            a = False
            user = input("Enter an integer for a user ID: ").strip()
            
        
    return int(user)

def exists(user,network):
    '''(2Dlist)->bool '''

    u = False
    for i in range(len(network)):
        if user == str(network[i][0]):
            u = True

    return u
    

##############################
# main
##############################


file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommed the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinaly, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    
