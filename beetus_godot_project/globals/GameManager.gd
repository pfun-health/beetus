extends Node

var health: float = 100.0
var girth: float = 1.0
var glucose: float = 0.5
var is_dead: bool = false

const HIGH_BOUND: float = 0.8
const LOW_BOUND: float = 0.2
const FAIL_RATE: float = 15.0
const WIN_RATE: float = 2.0
var phenotype: String = "STABLE"
var drift_volatility: float = 0.15

var history: Array[float] = []
var history_size: int = 30
var tick_timer: float = 0.0

var inventory = {
    "INSULIN": {"max": 5, "uses": 5, "dG": -0.35, "dGirth": 0.0},
    "SODA":    {"max": 3, "uses": 3, "dG": 0.40,  "dGirth": 0.10},
    "MEAL":    {"max": 5, "uses": 5, "dG": 0.15,  "dGirth": 0.02}
}

func _ready() -> void:
    for i in range(history_size):
        history.append(0.5)

func _process(delta: float) -> void:
    if is_dead: return
        
    var girth_bias = (girth - 1.0) * 0.05
    var random_drift = ((randf() - 0.48) * drift_volatility * delta) + (girth_bias * delta)
    glucose = clamp(glucose + random_drift, 0.0, 1.0)
    
    var is_high = glucose >= HIGH_BOUND
    var is_low = glucose <= LOW_BOUND
    
    if is_high or is_low:
        var severity = (glucose - 0.8) / 0.2 if is_high else (0.2 - glucose) / 0.2
        health -= FAIL_RATE * max(1.0, severity * 2) * delta
    else:
        health = min(100.0, health + (WIN_RATE * delta))
        
    if health <= 0.0:
        is_dead = true
        print("H_bar -> 0: Patient has succumbed.")
        
    tick_timer += delta
    if tick_timer > 0.25:
        tick_timer = 0.0
        history.push_back(glucose)
        history.pop_front()
    else:
        history[history_size - 1] = glucose

func apply_metabolic_burn(delta: float) -> void:
    glucose = clamp(glucose - (0.01 * delta), 0.0, 1.0)
