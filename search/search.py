"""
Project1: Implement generic search algorithms which are called by Pacman agents.
Submitted by: Vartika Sharma
ASU ID: 1213413043
"""


# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """    
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    ###util.raiseNotDefined()
    #We define the fringe using a stack
    stack = util.Stack()
    
    #We initialize the visited array for DFS implementation
    visited = []
    
    #List of actions that will lead the agent from the start to the goal
    listActions=[]  

    #Push the start state to the stack
    stack.push(problem.getStartState())
    
    #We maintain a stack to update the present list of actions
    presentActions = util.Stack()          
    
    #We pop the stack and save it in a node
    node = stack.pop()
    
    #While we have not yet found the goal
    while not problem.isGoalState(node):

        ##Iterate over the total amount of nodes which are not yet visited
        if node not in visited:
            visited.append(node)
            nextNode = problem.getSuccessors(node)
            #print nextNode

            for (childNode,directionNode,cost) in nextNode: 
                stack.push(childNode)
                currentactions = listActions + [directionNode]
                presentActions.push(currentactions)
        
        #Pop the stach and save it in the node
        node = stack.pop()
        #print node

        #Pop the present list of actions and save it in the list of actions for Pacman
        listActions = presentActions.pop()
    
    return listActions


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    ###util.raiseNotDefined()
    #We define the fringe using a queue
    queue = util.Queue()

    #We again initialize the visited array for BFS implementation
    visited = []
    initialNode = problem.getStartState()
    
    #Initialize cost and listActions
    cost = 0
    listActions = []

    #push the initial node, listActions and cost to the queue
    queue.push((initialNode,listActions,cost))
    
    #We pop the queue and save the node, listActions and cost 
    node,listActions,cost = queue.pop()
    
    #We append the node to visited array
    visited.append(node)

    #While we have not yet found the goal
    while not problem.isGoalState(node):
        #Get the nextNode 
        nextNode = problem.getSuccessors(node)
        
        for n in nextNode:
            
            ##Iterate over the total amount of nodes which are not yet visited
            if not n[0] in visited: 
                queue.push((n[0], listActions + [n[1]], cost + n[2])) 
                visited.append(n[0])
        
        #We pop the queue and save the node, listActions and cost
        node,listActions,cost = queue.pop()

    return listActions

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    ##util.raiseNotDefined()
    #We define the fringe using a Priority queue
    pQueue = util.PriorityQueue()

    #We again initialize the visited array for UCS implementation
    visited = []
    initialNode = problem.getStartState()
    
    #Initialize cost and listActions
    cost = 0
    listActions = []

    #push the initial node and cost to the queue
    pQueue.push(initialNode,cost)
    
    #We define one more priority queue which stores the list of actions till present node
    presentActions = util.PriorityQueue()            
    
    #We pop the node from pQueue and save it
    node = pQueue.pop()

    #While we have not yet found the goal
    while not problem.isGoalState(node):
        
        ##Iterate over the total amount of nodes which are not yet visited
        if node not in visited:
            #We append the node to visited array
            visited.append(node)
            nextNode = problem.getSuccessors(node)
            tempActions = [] 

            for (childNode,directionNode,cost) in nextNode:
                tempActions = listActions + [directionNode]
                cost = problem.getCostOfActions(tempActions)
                
                if childNode not in visited:
                    pQueue.push(childNode,cost)
                    presentActions.push(tempActions,cost)
        
        #We pop the node from pQueue and save it
        node = pQueue.pop()
        listActions = presentActions.pop()    
    
    return listActions


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    ###util.raiseNotDefined()
    
    #We define the fringe using a Priority queue
    pQueue = util.PriorityQueue()

    #We again initialize the visited array, cost and listActions for A* implementation 
    visited = []
    cost = 0
    listActions = []

    #We push the initial node and cost to the queue
    initialNode = problem.getStartState()

    #We assign initial node with priority number zero and add heuristic
    pQueue.push((initialNode,[],cost),0 + heuristic(initialNode,problem))

    #We pop the priority queue and save the node, listActions and cost 
    node,listActions,cost = pQueue.pop()

    #We append the node along with heuristic to visited array
    visited.append((node,cost + heuristic(initialNode,problem)))

    #While we have not yet found the goal
    while not problem.isGoalState(node):
        nextNode = problem.getSuccessors(node)
        
        ##Iterate over the total amount of nodes whether visited or not  
        for childNode in nextNode:
            sumCost = cost + childNode[2]

            #define a boolean variable to check if the node is visited or not
            checkinVisited = False
            for (nodeVisited, costVisited) in visited:
                if ((childNode[0] == nodeVisited) & (sumCost >= costVisited)): 
                    checkinVisited = True
                    break

            if not checkinVisited:        
                pQueue.push((childNode[0],listActions + [childNode[1]],cost + childNode[2]),cost + childNode[2] + heuristic(childNode[0],problem))
                # We append the visited array with updated node and cost
                visited.append((childNode[0],cost + childNode[2]))

        #We pop the priority queue and save the node, listActions and cost
        node, listActions, cost = pQueue.pop()

    return listActions

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
