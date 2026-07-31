class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # there are n cars
        # you have 2 lists, one has the position of ith car in miles
        # and the other one is the speed of the ith car in mph
        
        # the destination we are trying to reach is at target position (miles)
        # a car cant pass the car ahead of it, a car fleet is a group or one car that reaches the target at either the same time or its own time

        # return the number of fleets

        # implementation: 
        # we need the times when these cars arrive
        # we would first sort the cars by position because then we know what cars are ahead of whom
        # from there, we calculate their arrival times
        # if cars from behind travel faster than cars up ahead, we know they catch up and dont update fleet size, 
        # if not (slower), we update the fleet size

        
        cars = list(zip(position, speed))
        cars.sort()

        # Stack will store the arrival time of each fleet.
        stack = []

        # Step 3:
        # Process cars from closest to the target back to the farthest.
        for pos, spd in reversed(cars):

            time = (target - pos) / spd

            if not stack or time > stack[-1]:
                stack.append(time)

            # Otherwise:
            # time <= stack[-1]
            #
            # The current car catches the fleet ahead
            # before (or exactly at) the destination.
            # We do nothing because it becomes part of
            # that existing fleet.

        # Every time stored in the stack represents one fleet.
        return len(stack)