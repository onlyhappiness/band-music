extends Control


func _ready():
	pass


func _on_LineEdit_text_entered(new_text):
	Dialogic.set_variable("PlayerName", new_text)
	$LineEdit.queue_free()
	start_novel()


func start_novel():
	var new_dialogic = Dialogic.start("timeline")
	add_child(new_dialogic)
