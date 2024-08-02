import sqlite3

# QUERIES

# How many total Characters are there?
TOTAL_CHARACTERS= '''SELECT COUNT(*) 
    FROM charactercreator_character;'''

# How many of each specific subclass (the necromancer table)?
TOTAL_SUBCLASS= '''SELECT COUNT(*) 
    FROM charactercreator_necromancer;'''

# How many total Items?
TOTAL_ITEMS= '''SELECT COUNT(*)
    FROM charactercreator_character_inventory;
    '''

# How many of the Items are weapons?
WEAPONS= '''SELECT COUNT(*)
    FROM armory_weapon;
    ''' 

# How many of the items are not weapons?
# NON_WEAPONS= pass

'''SELECT COUNT(*)
FROM armory_item

SELECT COUNT(*)
FROM armory_weapon;'''

# How many Items does each character have? (Return first 20 rows)
CHARACTER_ITEMS= '''SELECT cc_char.name, SUM(ai.item_id) AS num_items_per_char
    FROM charactercreator_character AS cc_char
    JOIN charactercreator_character_inventory AS cc_inv
    ON cc_char.character_id = cc_inv.character_id
    JOIN armory_item AS ai
    ON cc_inv.item_id = ai.item_id
    GROUP BY cc_char.character_id
    ORDER BY num_items_per_char
    LIMIT 20;
    '''

# How many Weapons does each character have? (Return first 20 rows)
CHARACTER_WEAPONS='''SELECT cc_char.name, SUM(aw.item_ptr_id) AS weapons_per_char
    FROM charactercreator_character AS cc_char
    JOIN charactercreator_character_inventory AS cc_inv
    ON cc_char.character_id = cc_inv.character_id
    JOIN armory_item AS ai
    ON cc_inv.item_id = ai.item_id
    JOIN armory_weapon AS aw
    ON ai.item_id = aw.item_ptr_id
    GROUP BY cc_char.character_id
    ORDER BY weapons_per_char DESC
    LIMIT 20;'''

# On average, how many Items does each Character have?
AVG_CHARACTER_ITEMS= '''SELECT cc_char.name, AVG(ai.item_id)
    FROM charactercreator_character AS cc_char
    JOIN charactercreator_character_inventory AS cc_inv
    ON cc_char.character_id = cc_inv.character_id
    JOIN armory_item AS ai
    ON cc_inv.item_id = ai.item_id
    GROUP BY cc_char.character_id;
    '''

# On average, how many Weapons does each character have?
AVG_CHARACTER_WEAPONS='''SELECT cc_char.name, AVG(aw.item_ptr_id)
    FROM charactercreator_character AS cc_char
    JOIN charactercreator_character_inventory AS cc_inv
    ON cc_char.character_id = cc_inv.character_id
    JOIN armory_item AS ai
    ON cc_inv.item_id = ai.item_id
    JOIN armory_weapon AS aw
    ON ai.item_id = aw.item_ptr_id
    GROUP BY cc_char.character_id;'''

# Connection and Cursor

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

curs.execute(TOTAL_CHARACTERS).fetchall()
curs.execute(TOTAL_SUBCLASS).fetchall()
curs.execute(TOTAL_ITEMS).fetchall()
curs.execute(WEAPONS).fetchall()
# curs.execute(NON_WEAPONS).fetchall()
curs.execute(CHARACTER_ITEMS).fetchall()
curs.execute(CHARACTER_WEAPONS).fetchall()
curs.execute(AVG_CHARACTER_ITEMS).fetchall()
curs.execute(AVG_CHARACTER_WEAPONS).fetchall()
