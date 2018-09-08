# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
from sets import Set
class Solution(object):
    def faceup(self):
        if self.orientation == 2:
            self.robot.turnLeft()
            self.robot.turnLeft()
        elif self.orientation == 3:
            self.robot.turnRight()
        elif self.orientation == 4:
            self.robot.turnLeft()
        self.orientation = 1

    def facedown(self):
        if self.orientation == 1:
            self.robot.turnLeft()
            self.robot.turnLeft()
        elif self.orientation == 3:
            self.robot.turnLeft()
        elif self.orientation == 4:
            self.robot.turnRight()
        self.orientation = 2

    def faceleft(self):
        if self.orientation == 1:
            self.robot.turnLeft()
        elif self.orientation == 2:
            self.robot.turnRight()
        elif self.orientation == 4:
            self.robot.turnLeft()
            self.robot.turnLeft()
        self.orientation = 3
        
    def faceright(self):
        if self.orientation == 1:
            self.robot.turnRight()
        elif self.orientation == 2:
            self.robot.turnLeft()
        elif self.orientation == 3:
            self.robot.turnLeft()
            self.robot.turnLeft()
        self.orientation = 4


    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.robot = robot
        self.robot.clean()
        self.cleaned = Set()
        self.cleaned.add((0,0))
        self.orientation = 1
        #1 up
        #2 down
        #3 left
        #4 right
        stack = [(0,0)]
        self.dfs(1,stack)
        self.dfs(3,stack)
        self.dfs(2,stack)
        self.dfs(4,stack)

    def stepback(self,stack):
        des = stack[-2]
        cur = stack[-1]
        diff = (des[0]-cur[0],des[1]-cur[1])
        if diff[0] == -1:
            self.faceup()
        elif diff[0] == 1:
            self.facedown()
        elif diff[1] == -1:
            self.faceleft()
        elif diff[1] == 1:
            self.faceright()
        self.robot.move()
        stack.pop()

    def dfs(self,direction,stack):
        destination = None

        if direction == 1:
            self.faceup()
            destination = (stack[-1][0]-1,stack[-1][1])
        elif direction == 2:
            self.facedown()
            destination = (stack[-1][0]+1,stack[-1][1])
        elif direction == 3:
            self.faceleft()
            destination = (stack[-1][0],stack[-1][1]-1)
        elif direction == 4:
            self.faceright()
            destination = (stack[-1][0],stack[-1][1]+1)

        #print direction,destination

        if destination not in self.cleaned:
            if self.robot.move():
                self.robot.clean()
                #print "cleaned:",destination,stack
                self.cleaned.add(destination)
                stack.append(destination)
                self.dfs(1,stack)
                self.dfs(3,stack)
                self.dfs(2,stack)
                self.dfs(4,stack)
                self.stepback(stack)


#Robot Room Cleaner
#https://leetcode.com/problems/robot-room-cleaner/description/