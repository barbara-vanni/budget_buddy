# from View.RenderAuthentication import auth
from View.RenderBudgetGlobal import render

state = render.render_global_menu
# state = auth.render_main_menu

def get_state():
    return state

def set_state(new_state):
    global state
    state = new_state

