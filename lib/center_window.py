

def centralize(width, height, root_window):
    """
    This function creates a window centralized accordingly to the screen that is displayed.
    :param width: Width desired for the window
    :param height: Height desired for the window
    :param root_window: Tk() main element
    :return: None
    """
    screen_width, screen_height = root_window.winfo_screenwidth(), root_window.winfo_screenheight()
    posx, posy = screen_width / 2 - width / 2, screen_height / 2 - height / 2
    root_window.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
