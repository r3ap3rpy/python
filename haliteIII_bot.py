#!/usr/bin/env python3
# Python 3.6

# Import the Halite SDK, which will let you interact with the game.
import hlt

# This library contains constant values.
from hlt import constants

# This library contains direction metadata to better interface with the game.
from hlt.positionals import Direction
import random
import logging

game = hlt.Game()
game.ready("r3ap3rpy")

logging.info("Successfully created bot! My Player ID is {}.".format(game.my_id))

ship_status = {}
ship_positions = []

dropoffctr = 0
shipctr = 0

allowship = True
allowdrop = False

boundMines = []
reservedCells = []

def safe_to_spawn(shipyardposition):
    forbidden = [ _.position for _ in me.get_ships() ]
    forbidden.append(shipyardposition)
    for position in shipyardposition.get_surrounding_cardinals():
        if position in forbidden:        
            return False
    else:
        return True

def next_mine(shipposition):
    mines = []
    for mine in shipposition.get_surrounding_cardinals():
        mines.append([mine , game_map[mine].halite_amount])
        
    return sorted(mines,key = lambda x: x[1])[-1][0] if sorted(mines,key = lambda x: x[1])[-1][1] else None
    
def next_free(shipposition):
    forbidden = [ _.position for _ in me.get_ships() ]
    forbidden.append(shipposition)
    for surr in shipposition.get_surrounding_cardinals():
        if not surr in forbidden:
            if not surr in reservedCells:
                reservedCells.append(surr)
                return surr
    else:
        return None
    
while True:
    game.update_frame()
    me = game.me
    game_map = game.game_map
    if game.turn_number % 2 == 0:
        reservedCells = []

    command_queue = []

    for ship in me.get_ships():
        if not hasattr(ship,'returning'):
            ship.returning = False
        logging.info('Ship {} state full: {}'.format(ship.id,ship.is_full))
        logging.info('Reserved: {}'.format(reservedCells))

            
        if ship.halite_amount < 600:            
            if game_map[ship.position].halite_amount == 0:
                logging.info('Mine: {}'.format(next_mine(ship.position)))
                if next_mine(ship.position) is None:
                    if next_free(ship.position) is None:
                        ship.stay_still()
                    else:
                        command_queue.append(ship.move(game_map.naive_navigate(ship, next_free(ship.position))))
                else:
                    command_queue.append(ship.move(game_map.naive_navigate(ship, next_mine(ship.position))))
            else:
                ship.stay_still()
                                
        else:
            ship.returning = True
         
        if not ship.returning and ship.halite_amount > 800:
            ship.stay_still()
            continue           
        
        if ship.returning:                            
            command_queue.append(ship.move(game_map.naive_navigate(ship, me.shipyard.position)))
                
        if me.halite_amount > 4000: 
            ship.make_dropoff()
    
    if safe_to_spawn(me.shipyard.position) and not game_map[me.shipyard].is_occupied and me.halite_amount >= constants.SHIP_COST:
        command_queue.append(me.shipyard.spawn())


            

    game.end_turn(command_queue)

