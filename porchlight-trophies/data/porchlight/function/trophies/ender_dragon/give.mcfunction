# Admin only. Gives the Ender Dragon Trophy to whoever this runs as. The head
# carries that player's skin (seen when it is placed as a block); the name and
# lore are the same for everyone. Nothing in this pack awards trophies automatically.
#
#   One player:            /execute as <player> run function porchlight:trophies/ender_dragon/give
#   Everyone in the End:   /execute as @a[nbt={Dimension:"minecraft:the_end"}] run function porchlight:trophies/ender_dragon/give
loot give @s loot porchlight:trophies/ender_dragon
