extends Control


func _ready():
	var new_dialog = Dialogic.start("res://timeline.dtl")
	add_child(new_dialog)
#	pass




#func start_novel():
#	var new_dialog = Dialogic.start("res://timeline.dtl")
#	add_child(new_dialog)

