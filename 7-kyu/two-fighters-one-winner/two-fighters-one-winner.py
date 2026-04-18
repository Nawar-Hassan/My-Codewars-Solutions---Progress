def declare_winner(fighter1, fighter2, first_attacker):
        
        attacks_to_defeat_fighter1 = (fighter1.health + fighter2.damage_per_attack - 1) // fighter2.damage_per_attack
        attacks_to_defeat_fighter2 = (fighter2.health + fighter1.damage_per_attack - 1) // fighter1.damage_per_attack
        
        
        if attacks_to_defeat_fighter1 < attacks_to_defeat_fighter2:
            return fighter2.name
        elif attacks_to_defeat_fighter2 < attacks_to_defeat_fighter1:
            return fighter1.name
        else:
            
            return first_attacker   
print(declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew"))