import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Initialize 4K Canvas (16:9 Landscape - 3840 x 2160 at 240 DPI)
fig = plt.figure(figsize=(16, 9), dpi=240)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_facecolor('#070b14')  # Deep Tech Midnight Navy
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Color Palette
CYAN = '#00f2fe'
INDIGO = '#7000ff'
AMBER = '#ffb300'
RED = '#ff3366'
WHITE = '#ffffff'
SLATE = '#94a3b8'
DARK_CARD = '#0f172a'
BORDER_COLOR = '#1e293b'

# Helper: Draw Rounded Card
def draw_card(x, y, w, h, title=""):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.8,rounding_size=1.2",
                                  facecolor=DARK_CARD, edgecolor=BORDER_COLOR, linewidth=1.2)
    ax.add_patch(rect)
    if title:
        ax.text(x + 1.2, y + h - 2.8, title, fontsize=11, fontweight='bold', color=CYAN, family='sans-serif')
        ax.plot([x + 1.2, x + w - 1.2], [y + h - 3.8, y + h - 3.8], color=BORDER_COLOR, lw=0.9)

# ==========================================
# 1. TOP HEADER BANNER
# ==========================================
header_rect = patches.FancyBboxPatch((2, 88.5), 96, 9.5, boxstyle="round,pad=0.5,rounding_size=1.0",
                                     facecolor='#0b1329', edgecolor=CYAN, linewidth=1.5)
ax.add_patch(header_rect)

ax.text(3.5, 94.7, "PROJECT ECOSENSE AIoT", fontsize=18.5, fontweight='black', color=WHITE, family='sans-serif')
ax.text(3.5, 91.8, "Edge-Computing Gas Monitoring & Autonomous Hazard Mitigation Station", fontsize=11, fontweight='bold', color=CYAN, family='sans-serif')
ax.text(3.5, 89.5, "Real-Time Dual Gas Profiling • Dynamic Hysteresis Calibration • Autonomous Damper/Fan Mitigation • Sub-200ms SoftAP Telemetry", fontsize=8, color=SLATE, family='sans-serif')

# Student & Institution Credits
ax.text(96.5, 95.0, "COLLEGE: SHRI RAJENDRA JUNIOR COLLEGE", fontsize=9.5, fontweight='bold', color=WHITE, ha='right', family='sans-serif')
ax.text(96.5, 93.0, "Location: New Nandanvan, Nagpur | Session 2026 - 2027", fontsize=8, color=SLATE, ha='right', family='sans-serif')
ax.text(96.5, 91.0, "Developer: Arhan Tariq Ansari | Tech: ESP32 Dual-Core (240MHz)", fontsize=8, color=AMBER, ha='right', family='sans-serif')
ax.text(96.5, 89.2, "Display: SH1106 OLED (Fast 400kHz I2C) | Web Hub: 192.168.4.1", fontsize=7.5, color=CYAN, ha='right', family='sans-serif')

# ==========================================
# COLUMN 1: SENSING & ALGORITHMIC ARCHITECTURE
# ==========================================
# Card 1: Problem & Approach
draw_card(2, 60, 30, 26.5, "1. PROBLEM & OBJECTIVES")
col1_text1 = (
    "• INDUSTRIAL SAFETY CHALLENGE:\n"
    "  Conventional gas sensors operate as passive, isolated sirens.\n"
    "  They lack live telemetry, suffer false triggers from thermal\n"
    "  drift, and fail to provide immediate localized mitigation\n"
    "  without human intervention.\n\n"
    "• ENGINEERING OBJECTIVE:\n"
    "  Engineer a self-contained edge-computing hub that tracks\n"
    "  baseline atmospheric drift dynamically, sounds proportional\n"
    "  frequency alarms, and triggers mechanical barriers instantly\n"
    "  with zero cloud or internet reliance."
)
ax.text(3.2, 82.5, col1_text1, fontsize=8, color=WHITE, linespacing=1.45, va='top', family='monospace')

# Card 2: Dual Atmospheric Sensing
draw_card(2, 31, 30, 27.5, "2. ATMOSPHERIC SENSING CORE")
col1_text2 = (
    "• MQ-2 SENSOR (Combustible Gas & Smoke / GPIO 34):\n"
    "  Heated SnO2 semiconductor sensor with high sensitivity to\n"
    "  LPG, propane, methane (CH4), butane, and smoke particles.\n\n"
    "• MQ-135 SENSOR (Air Quality Index / GPIO 35):\n"
    "  Quantifies hazardous airborne chemical contaminants: ammonia\n"
    "  (NH3), carbon dioxide (CO2), nitrogen oxides, and benzene.\n\n"
    "• 16-PASS FAST ADC NOISE REDUCTION:\n"
    "  Analog inputs run a 16-sample oversampled bit-shifted\n"
    "  average (>> 4) to eliminate electrical sensor jitter\n"
    "  without causing CPU delay blocks."
)
ax.text(3.2, 54.5, col1_text2, fontsize=8, color=WHITE, linespacing=1.45, va='top', family='monospace')

# Card 3: Dynamic Baseline Algorithm
draw_card(2, 2, 30, 27.5, "3. DYNAMIC BASELINE & HYSTERESIS")
col1_text3 = (
    "• ROLLING BASELINE DRIFT TRACKING (EMA):\n"
    "  Eliminates seasonal & temperature false triggers:\n"
    "  Base = (0.99 x Base) + (0.01 x Live_ADC)\n"
    "  Threshold = Base + Safe_Margin (MQ2:+300 / MQ135:+250)\n\n"
    "• 50-POINT CONTACT HYSTERESIS BAND:\n"
    "  Prevents destructive mechanical contact bounce on relay &\n"
    "  servo gears near trigger boundaries:\n"
    "  - Trigger Alarm: When Live_ADC > Threshold\n"
    "  - Clear Alarm:   When Live_ADC < (Threshold - 50)"
)
ax.text(3.2, 25.5, col1_text3, fontsize=8, color=WHITE, linespacing=1.45, va='top', family='monospace')

# ==========================================
# COLUMN 2: HARDWARE PINOUT & FINITE STATE MACHINE
# ==========================================
# Card 4: Pinout Table
draw_card(34, 46, 32, 40.5, "4. HARDWARE PINOUT & SPECIFICATIONS")
table_header = "MODULE / COMPONENT       PIN/PORT   VOLTAGE   ROLE / FUNCTION"
ax.text(35.2, 82.2, table_header, fontsize=7.8, fontweight='bold', color=AMBER, family='monospace')
ax.plot([35.2, 64.8], [81.2, 81.2], color=BORDER_COLOR, lw=0.9)

table_rows = [
    ("ESP32 NodeMCU-32S",    "Core MCU", "5V USB", "Dual Core 240MHz, AP Hub"),
    ("MQ-2 Gas Sensor",       "GPIO 34",  "5V / 3.3V", "ADC1 Analog Combustible"),
    ("MQ-135 AQI Sensor",     "GPIO 35",  "5V / 3.3V", "ADC1 Analog Air Quality"),
    ("SH1106 OLED (SDA)",     "GPIO 33",  "3.3V",      "Fast I2C Data Line (400kHz)"),
    ("SH1106 OLED (SCL)",     "GPIO 32",  "3.3V",      "Fast I2C Clock (400kHz)"),
    ("5V Single Relay",       "GPIO 27",  "5V",        "Exhaust Fan Isolation Circuit"),
    ("TowerPro SG90 Servo",   "GPIO 26",  "5V (PWM)",  "Vent Flap Damper (0°/90°)"),
    ("Piezo Alert Buzzer",    "GPIO 14",  "3.3V",      "Dynamic Staccato Frequency"),
    ("Status Indicator LED",  "GPIO 2",   "3.3V",      "Pulse & Heartbeat Monitor")
]

y_t = 78.4
for mod, pin, volt, func in table_rows:
    ax.text(35.2, y_t, f"{mod:<22} {pin:<10} {volt:<9} {func}", fontsize=7.2, color=WHITE, family='monospace')
    y_t -= 3.3

# Card 5: Operational FSM (Corrected coordinates & no overlap)
draw_card(34, 2, 32, 42.5, "5. OPERATIONAL FINITE STATE MACHINE (FSM)")

# Adjusted vertical positions for clean spacing
fsm_steps = [
    ("STAGE 1: THERMAL STABILIZATION (INIT)", 
     "Duration: 30 Seconds | Heaters Reach 200°C-300°C\nBaselines Locked | Actuators & Buzzers Silenced", AMBER, 29.5),
    ("STAGE 2: ARMED & CONTINUOUS TRACKING (SAFE)", 
     "Live < Threshold | Baseline Drift Actively Tracked\nExhaust Fan OFF | Vent Closed (0°) | Buzzer Silent", CYAN, 18.0),
    ("STAGE 3: ACTIVE DEFENSE & MITIGATION (HAZARD)", 
     "Threshold Breached | Relay Latches Instantly (0ms)\nServo Flap Deploys 90° (+250ms) | Pulsed Audible Alert", RED, 6.5)
]

for title, desc, col, y_pos in fsm_steps:
    box = patches.FancyBboxPatch((35.5, y_pos), 29, 8.5, boxstyle="round,pad=0.3,rounding_size=0.6",
                                 facecolor='#1e293b', edgecolor=col, linewidth=1.2)
    ax.add_patch(box)
    ax.text(36.5, y_pos + 5.8, title, fontsize=7.8, fontweight='bold', color=col, family='sans-serif')
    ax.text(36.5, y_pos + 1.8, desc, fontsize=6.8, color=WHITE, family='monospace', linespacing=1.3)

# Connectors for FSM
ax.annotate('', xy=(50, 27.2), xytext=(50, 29.5), arrowprops=dict(arrowstyle="->", color=WHITE, lw=1.2))
ax.annotate('', xy=(50, 15.7), xytext=(50, 18.0), arrowprops=dict(arrowstyle="->", color=RED, lw=1.2))
ax.text(50.8, 16.6, "Breach", fontsize=6.5, fontweight='bold', color=RED, family='sans-serif')

# ==========================================
# COLUMN 3: MITIGATION, SYNC & WEB HUD
# ==========================================
# Card 6: Autonomous Hazard Mitigation
draw_card(68, 62, 30, 24.5, "6. AUTONOMOUS DUAL-STAGE DEFENSE")
col3_text1 = (
    "• INSTANT RELAY EXHAUST VENTILATION (0 ms):\n"
    "  High-volume exhaust fan circuit closes contacts instantly\n"
    "  upon threshold detection to initiate atmospheric extraction.\n\n"
    "• INRUSH CURRENT STAGGERED SERVO (+250 ms):\n"
    "  Damper flap moves to 90° after a 250ms delay. This prevents\n"
    "  simultaneous inrush currents from dropping the 5V bus and\n"
    "  brown-out resetting the microcontroller."
)
ax.text(69.2, 82.5, col3_text1, fontsize=8, color=WHITE, linespacing=1.4, va='top', family='monospace')

# Card 7: 5Hz Master Sync Engine
draw_card(68, 33, 30, 27.5, "7. UNIFIED 5 Hz MASTER SYNC ENGINE")
col3_text2 = (
    "• ZERO-LATENCY LOCK-STEP ARCHITECTURE:\n"
    "  Sensors, OLED rendering, physical alerts, and the wireless\n"
    "  dashboard operate on a synchronized 200ms master clock.\n\n"
    "• 400 kHz HIGH-SPEED I2C BUS:\n"
    "  Reduces OLED SH1106 frame transmission time from 100ms\n"
    "  down to 25ms, eliminating CPU thread starvation.\n\n"
    "• PRE-BUFFERED MEMORY JSON SERIALIZATION:\n"
    "  Dedicated string memory reserve stops heap fragmentation\n"
    "  and eliminates browser refresh stutter."
)
ax.text(69.2, 56.5, col3_text2, fontsize=8, color=WHITE, linespacing=1.4, va='top', family='monospace')

# Card 8: Dashboard & Oscilloscope
draw_card(68, 2, 30, 29.5, "8. REAL-TIME TELEMETRY & WEB HUD")
col3_text3 = (
    "• QUAD-TRACE REAL-TIME OSCILLOSCOPE:\n"
    "  Plots dynamic thresholds alongside live telemetry:\n"
    "  - Cyan Solid: MQ-2 Gas     | Amber Dashed: MQ-2 Target\n"
    "  - Indigo Solid: MQ-135 AQI | Red Dashed: MQ-135 Target\n\n"
    "• PROPORTIONAL HARDWARE BUZZER ALERT:\n"
    "  Acoustic chirp frequency modulates between 180ms to 60ms\n"
    "  directly proportional to gas hazard concentration.\n\n"
    "• LOCAL AUDIT EVENT STREAM:\n"
    "  Browser-native live timestamp logging and one-touch CSV export."
)
ax.text(69.2, 27.5, col3_text3, fontsize=8, color=WHITE, linespacing=1.4, va='top', family='monospace')

# Save 4K Output
output_filename = "EcoSense_AIoT_Presentation_Chart.png"
plt.savefig(output_filename, dpi=240, facecolor=fig.get_facecolor(), edgecolor='none')
print(f"Chart re-generated successfully: {output_filename}")