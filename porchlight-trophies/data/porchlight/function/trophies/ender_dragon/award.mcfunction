# Runs as the winning player: mark the trophy as claimed, hand it over, tell everyone.
data modify storage porchlight:trophies ender_dragon.awarded set value 1b
function porchlight:trophies/ender_dragon/give
tellraw @a [{selector:"@s",color:"#FFD58A"},{text:" landed the final blow on the Ender Dragon and takes home the ",color:"#F6EEDF"},{text:"Ender Dragon Trophy",color:"#F2A541"},{text:".",color:"#F6EEDF"}]
execute as @a at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
