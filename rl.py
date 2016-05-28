import libtcodpy as libtcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

LIMIT_FPS = 20


def handle_keys():
    global playerx, playery

    key = libtcod.console_wait_for_keypress(True)  #turn-based

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

    elif key.vk == libtcod.KEY_ESCAPE:
        return True

    #movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_KP7): # up and left
        playerx -= 1
        playery -= 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_KP8): # up
        playery -= 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_KP9): # up and right
        playerx += 1
        playery -= 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_KP6): # right
        playerx += 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_KP3): # down and right
        playerx += 1
        playery += 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_KP2): # down
        playery += 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_KP1):
        playerx -= 1
        playery += 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_KP4): # left
        playerx -= 1


#############################################
# Initialization & Main Loop
#############################################

libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)
libtcod.sys_set_fps(LIMIT_FPS)

playerx = SCREEN_WIDTH/2
playery = SCREEN_HEIGHT/2

while not libtcod.console_is_window_closed():

    libtcod.console_set_default_foreground(0, libtcod.white)
    libtcod.console_put_char(0, playerx, playery, '@', libtcod.BKGND_NONE)

    libtcod.console_flush()

    libtcod.console_put_char(0, playerx, playery, ' ', libtcod.BKGND_NONE)

    #handle keys and exit game if needed
    exit = handle_keys()
    if exit:
        break
