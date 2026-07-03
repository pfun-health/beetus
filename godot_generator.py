import os
import shutil

# --- PROJECT STRUCTURE DEFINITION ---
PROJECT_NAME = "beetus_godot_project"

DIRECTORIES = ["globals", "entities/player", "entities/npcs", "ui", "levels"]

FILES = {
    # 1. Main Godot Project Config
    "project.godot": """; Engine configuration file.
; It's best edited using the editor UI and not directly,
; since the parameters that go here are not all obvious.

config_version=5

[application]
config/name="Beetus - Phase 3"
run/main_scene="res://levels/Clinic.tscn"
config/features=PackedStringArray("4.2", "Forward Plus")

[autoload]
GameManager="*res://globals/GameManager.gd"

[display]
window/size/viewport_width=1152
window/size/viewport_height=648
""",
    # 2. Global Autoload (The Math Engine)
    "globals/GameManager.gd": """extends Node

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
""",
    # 3. Player Movement Script
    "entities/player/Player.gd": """extends CharacterBody2D

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
""",
    # 4. Player Scene
    "entities/player/Player.tscn": """[gd_scene load_steps=3 format=3]

[ext_resource type="Script" path="res://entities/player/Player.gd" id="1_player"]

[sub_resource type="RectangleShape2D" id="RectangleShape2D_1"]
size = Vector2(32, 32)

[node name="Player" type="CharacterBody2D"]
script = ExtResource("1_player")

[node name="ColorRect" type="ColorRect" parent="."]
offset_left = -16.0
offset_top = -16.0
offset_right = 16.0
offset_bottom = 16.0
color = Color(0.258824, 0.854902, 0.439216, 1)

[node name="CollisionShape2D" type="CollisionShape2D" parent="."]
shape = SubResource("RectangleShape2D_1")
""",
    # 5. UI Wave Renderer Script
    "ui/WaveRenderer.gd": """extends Control

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
""",
    # 6. UI Scene
    "ui/Dashboard.tscn": """[gd_scene load_steps=2 format=3]

[ext_resource type="Script" path="res://ui/WaveRenderer.gd" id="1_wave"]

[node name="Dashboard" type="CanvasLayer"]

[node name="WaveRenderer" type="Control" parent="."]
layout_mode = 3
anchors_preset = 15
anchor_right = 1.0
anchor_bottom = 1.0
grow_horizontal = 2
grow_vertical = 2
script = ExtResource("1_wave")
""",
    # 7. Level Scene
    "levels/Clinic.tscn": """[gd_scene load_steps=3 format=3]

[ext_resource type="PackedScene" path="res://entities/player/Player.tscn" id="1_player"]
[ext_resource type="PackedScene" path="res://ui/Dashboard.tscn" id="2_ui"]

[node name="Clinic" type="Node2D"]

[node name="Background" type="ColorRect" parent="."]
offset_right = 2000.0
offset_bottom = 2000.0
color = Color(0.129412, 0.14902, 0.180392, 1)

[node name="Player" parent="." instance=ExtResource("1_player")]
position = Vector2(576, 324)

[node name="Camera2D" type="Camera2D" parent="Player"]

[node name="Dashboard" parent="." instance=ExtResource("2_ui")]
""",
}


def build_project():
    print(f"🚀 Initializing Godot project: {PROJECT_NAME}...")

    if os.path.exists(PROJECT_NAME):
        shutil.rmtree(PROJECT_NAME)
    os.makedirs(PROJECT_NAME)

    for directory in DIRECTORIES:
        os.makedirs(os.path.join(PROJECT_NAME, directory), exist_ok=True)

    for filepath, content in FILES.items():
        full_path = os.path.join(PROJECT_NAME, filepath)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"   [CREATED] {filepath}")

    print("📦 Zipping project archive...")
    shutil.make_archive(PROJECT_NAME, "zip", PROJECT_NAME)

    print(f"✅ Success! {PROJECT_NAME}.zip is ready.")
    print(
        "-> Unzip the file, open Godot 4, click 'Import', and select the project.godot file."
    )


if __name__ == "__main__":
    build_project()
