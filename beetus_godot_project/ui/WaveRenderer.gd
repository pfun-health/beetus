extends Control

const GRID_W: int = 30
const GRID_H: int = 20

func _process(_delta: float) -> void:
    queue_redraw() # Force redraw every frame

func _draw() -> void:
    # Dashboard Panel bounds
    var p_rect = Rect2(20, 20, 350, 200)
    draw_rect(p_rect, Color(0.05, 0.05, 0.05, 0.9))
    draw_rect(p_rect, Color("22c55e"), false, 2.0)
    
    var block_w = p_rect.size.x / float(GRID_W)
    var block_h = p_rect.size.y / float(GRID_H)
    
    var high_y = p_rect.position.y + ((1.0 - GameManager.HIGH_BOUND) * p_rect.size.y)
    var low_y = p_rect.position.y + ((1.0 - GameManager.LOW_BOUND) * p_rect.size.y)
    
    draw_rect(Rect2(p_rect.position.x, p_rect.position.y, p_rect.size.x, high_y - p_rect.position.y), Color(0.9, 0.2, 0.2, 0.2))
    draw_rect(Rect2(p_rect.position.x, low_y, p_rect.size.x, p_rect.position.y + p_rect.size.y - low_y), Color(0.2, 0.5, 0.9, 0.2))
    
    var history = GameManager.history
    for i in range(history.size()):
        var val = history[i]
        var mapped_y = floor((1.0 - val) * (GRID_H - 1))
        var px_x = p_rect.position.x + (i * block_w)
        var px_y = p_rect.position.y + (mapped_y * block_h)
        
        var color = Color("22c55e")
        if i == history.size() - 1:
            if val >= GameManager.HIGH_BOUND: color = Color("ef4444")
            elif val <= GameManager.LOW_BOUND: color = Color("3b82f6")
            else: color = Color("4ade80")
            
        draw_rect(Rect2(px_x + 1, px_y + 1, block_w - 2, block_h - 2), color)
