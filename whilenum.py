import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def create_cricket_poster_mockup():
    # Set up the figure and axis with a poster aspect ratio (2:3)
    fig, ax = plt.subplots(figsize=(8, 12))
    
    # Christmas Theme Colors
    bg_color = '#0b3d0b'      # Dark Christmas Green
    text_gold = '#FFD700'     # Gold
    text_white = '#FFFFFF'    # White
    text_red = '#D42426'      # Christmas Red
    
    # Set background
    ax.set_facecolor(bg_color)
    
    # Optional: subtle snow effect
    x = np.random.rand(120)
    y = np.random.rand(120)
    ax.scatter(x, y, s=6, color='white', alpha=0.25, zorder=1)
    
    # Festive border
    rect = patches.Rectangle(
        (0.05, 0.05), 0.9, 0.9,
        linewidth=4,
        edgecolor=text_gold,
        facecolor='none'
    )
    ax.add_patch(rect)
    
    # --- HEADER SECTION ---
    ax.text(
        0.5, 0.88, "THE",
        fontsize=15,
        color=text_white,
        ha='center',
        va='center',
        weight='bold'
    )
    
    ax.text(
        0.5, 0.82, "CHRISTMAS CUP",
        fontsize=40,
        color=text_red,
        ha='center',
        va='center',
        fontweight='bold',
        bbox=dict(
            facecolor=text_white,
            edgecolor=text_gold,
            linewidth=2,
            boxstyle='round,pad=0.35'
        )
    )
    
    ax.text(
        0.5, 0.75, "FESTIVE CRICKET SERIES",
        fontsize=14,
        color=text_gold,
        ha='center',
        va='center',
        weight='bold'
    )

    # --- VERSUS SECTION ---
    ax.text(
        0.5, 0.60, "ZAIN XI",
        fontsize=30,
        color=text_white,
        ha='center',
        va='center',
        weight='bold'
    )
    
    circle = patches.Circle((0.5, 0.53), 0.06, color=text_red)
    ax.add_patch(circle)
    ax.text(
        0.5, 0.53, "VS",
        fontsize=20,
        color=text_white,
        ha='center',
        va='center',
        weight='bold'
    )
    
    ax.text(
        0.5, 0.46, "MUBEEN XI",
        fontsize=30,
        color=text_white,
        ha='center',
        va='center',
        weight='bold'
    )
    
    # --- VISUAL PLACEHOLDER ---
    ax.text(
        0.5, 0.35, "[ VISUAL: CRICKET BATSMAN WITH SNOW ]",
        fontsize=10,
        color='lightgray',
        ha='center',
        va='center',
        style='italic'
    )

    # --- DETAILS SECTION ---
    ax.text(
        0.5, 0.25, "THE BATTLE FOR HOLIDAY GLORY",
        fontsize=16,
        color=text_gold,
        ha='center',
        va='center',
        weight='bold'
    )
    
    info_text = "DECEMBER 2025\nMATCHES START DAILY\n[STADIUM NAME], [CITY]"
    ax.text(
        0.5, 0.15,
        info_text,
        fontsize=14,
        color=text_white,
        ha='center',
        va='center'
    )

    # --- FOOTER ---
    ax.text(
        0.5, 0.08,
        "ENTRY: FREE FOR FAMILIES | FOLLOW @CHRISTMASCUP",
        fontsize=10,
        color=text_white,
        ha='center',
        va='center',
        alpha=0.85
    )

    # Clean canvas
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    # Save output
    plt.savefig(
        "christmas_cup_poster_mockup.png",
        dpi=300,
        bbox_inches='tight',
        pad_inches=0.1
    )
    plt.show()

create_cricket_poster_mockup()
