# Runs as the player who landed the final hit on an Ender Dragon
# (reward of the porchlight:trophies/ender_dragon advancement).

# Re-arm the trigger so it can fire again for a later dragon.
advancement revoke @s only porchlight:trophies/ender_dragon

# Only the first dragon kill of the season earns the trophy. To award it again
# (new season, or a re-run event) an admin runs:
#   /function porchlight:trophies/ender_dragon/reset
execute unless data storage porchlight:trophies ender_dragon{awarded:1b} run function porchlight:trophies/ender_dragon/award
