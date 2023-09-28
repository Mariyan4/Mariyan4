lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

trashed_helmet = lost_fights_count // 2
trashed_sword = lost_fights_count // 3
trashed_shield = lost_fights_count // (2 * 3)
trashed_armor = trashed_shield // 2
total_sum = (trashed_armor*armor_price) + (trashed_sword*sword_price) + (trashed_shield * shield_price) + (trashed_helmet * helmet_price)
print(f"Gladiator expenses: {total_sum:.2f} aureus")