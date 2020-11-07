#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    # empty dict
    hashtable = {}

# for loop through all the tickets...
    for ticket in tickets:
        # source of ticket is assigned to the destination of the ticket.
        hashtable[ticket.source] = ticket.destination

# setting up...
    locat = hashtable['none']
    route = [locat]

# while locat is not equal to none keep hashing each ticket...
    while locat is not 'none':
        locat = hashtable[locat]
        route.append(locat)

# return the route...
    return route
