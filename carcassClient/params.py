from enum import Enum
class Params(Enum):
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT =560
    SQUARE_DIM=70
    MENU_WIDTH=80
    PNG_DIR="../png_tuiles/" 
    BACKGROUND="background_"+str(WINDOW_HEIGHT)+".png"
    P_LATERAL="panneau_lateral_"+str(WINDOW_HEIGHT)+".png"
    END_TUILE="fintoplace.png"
    CLICKABLE="greenSquare.png"
    
