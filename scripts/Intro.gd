extends Control

func _ready():
	pass # Replace with function body.

# New game
func _on_Button_pressed():
	var new_game_scene = preload("res://screens/NewGame.tscn")
	get_tree().change_scene("res://screens/NewGame.tscn")
	pass

# Load
func _on_Button2_pressed():
	pass # Replace with function body.

# quit
func _on_Button3_pressed():
	get_tree().quit()
