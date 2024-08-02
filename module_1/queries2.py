# QUERIES

# Example 1
DISTINCT_CHARACTER_NAMES= '''SELECT COUNT(DISTINCT name) AS distinct_names
    FROM charactercreator_character;'''

# How many total Characters are there?
TOTAL_CHARACTERS= '''SELECT COUNT(*) 
    FROM charactercreator_character;'''

# How many of each specific subclass (the necromancer table)?
TOTAL_SUBCLASS= '''SELECT COUNT(*) 
    FROM charactercreator_necromancer;'''

# How many total Items?
TOTAL_ITEMS= '''SELECT COUNT(*)
    FROM armory_item;'''

# How many of the Items are weapons?
WEAPONS= '''SELECT COUNT(*)
    FROM armory_weapon;''' 

# How many of the items are not weapons?
NON_WEAPONS= '''SELECT COUNT(*)
    FROM armory_item AS ai
    LEFT JOIN armory_weapon AS aw
    ON ai.item_id = aw.item_ptr_id
    WHERE aw.power IS NULL;'''

# How many Items does each character have? (Return first 20 rows)
CHARACTER_ITEMS= '''SELECT name, COUNT(item_id) AS num_items_per_char
    FROM charactercreator_character AS cc_char
    JOIN charactercreator_character_inventory AS cc_inv
    ON cc_char.character_id = cc_inv.character_id
    GROUP BY cc_char.character_id
    LIMIT 20;'''

# How many Weapons does each character have? (Return first 20 rows)
CHARACTER_WEAPONS='''SELECT cc_char.name, COUNT(ai.item_id) AS total_weapons
    FROM armory_item AS ai
    INNER JOIN armory_weapon AS aw
    ON ai.item_id = aw.item_ptr_id
    -- 37 weapons
    INNER JOIN charactercreator_character_inventory AS cc_inv
    ON ai.item_id = cc_inv.item_id
    -- 203 weapons 
    INNER JOIN charactercreator_character as cc_char
    ON cc_char.character_id = cc_inv.character_id
    GROUP BY cc_char.character_id
    LIMIT 20;'''

# On average, how many Items does each Character have?
AVG_CHARACTER_ITEMS= '''SELECT AVG(num_items_per_char) AS average_items_per_character
    FROM (SELECT name, COUNT(item_id) AS num_items_per_char
        FROM charactercreator_character AS cc_char
        JOIN charactercreator_character_inventory AS cc_inv
        ON cc_char.character_id = cc_inv.character_id
        GROUP BY cc_char.character_id);'''

# On average, how many Weapons does each character have?
AVG_CHARACTER_WEAPONS='''SELECT AVG(total_weapons) AS average_weapons
    FROM (SELECT cc_char.name, COUNT(ai.item_id) AS total_weapons
    FROM armory_item AS ai
    INNER JOIN armory_weapon AS aw
    ON ai.item_id = aw.item_ptr_id
    -- 37 weapons
    INNER JOIN charactercreator_character_inventory AS cc_inv
    ON ai.item_id = cc_inv.item_id
    -- 203 weapons 
    INNER JOIN charactercreator_character as cc_char
    ON cc_char.character_id = cc_inv.character_id
    GROUP BY cc_char.character_id);'''


QUERY_LIST= [DISTINCT_CHARACTER_NAMES,
             TOTAL_CHARACTERS,
             TOTAL_SUBCLASS, 
             TOTAL_ITEMS,
             WEAPONS, 
             NON_WEAPONS,
             CHARACTER_ITEMS, 
             CHARACTER_WEAPONS,
             AVG_CHARACTER_ITEMS, 
             AVG_CHARACTER_WEAPONS]
