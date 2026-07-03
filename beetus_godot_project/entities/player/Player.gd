extends CharacterBody2D

const BASE_SPEED: float = 250.0

func _physics_process(delta: float) -> void:
    if GameManager.is_dead: return
        
    var direction := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    
    # Girth Penalty: Physically slows player down
    var current_speed = BASE_SPEED / GameManager.girth
    
    velocity = direction * current_speed
    move_and_slide()
    
    # Walking burns glucose toward Bound <Low>
    if velocity.length() > 0:
        GameManager.apply_metabolic_burn(delta)
