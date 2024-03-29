from View.RenderAuthentication import auth



state = auth.render_main_menu

def get_state():
    return state

def set_state(new_state):
    global state
    state = new_state

