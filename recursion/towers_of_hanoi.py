def move_tower(number_of_disks,fromTower, toTower, withTower):
    if number_of_disks >= 1:
        move_tower(number_of_disks-1,fromTower,withTower,toTower)
        move_disk(fromTower,toTower)
        move_tower(number_of_disks-1,withTower,toTower,fromTower)

def move_disk(fromTower,toTower):
    print("Moving disk from ",fromTower," to ",toTower)

move_tower(3,"Source","Destination","Auxiliary")
