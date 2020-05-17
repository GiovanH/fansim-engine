# Search for '~CHANGES EACH VOLUME~' to find screens that need modification every time a new volume comes out.
# spoiler: there aren't any, since this is written well

################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

default pick = ""
screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    # CREATE NEW ICON:
    # #00baff and #f0f0f0 for hatch
    # import into photoshop
    # add bg #d3e9f1
    # save
    # sat -60 light -10
    # transparent bg 15%
    # save

    if quick_menu:

        imagebutton auto "gui/quick_save_%s.png" action ShowMenuFallback('save') pos (20, 566)
        imagebutton auto "gui/quick_log_%s.png" action ShowMenuFallback('history') pos (20, 640)
        imagebutton auto "gui/quick_skip_%s.png" action Skip() alternate Skip(fast=True, confirm=True) pos (94, 640)

        imagebutton auto "gui/quick_menu_%s.png" action MainMenu(confirm=True) pos (1122, 640)
        imagebutton auto "gui/quick_options_%s.png" action ShowMenuFallback('preferences') pos (1196, 640)

        if renpy.variant("pc"):
            imagebutton auto "gui/quick_help_%s.png" action ShowMenuFallback('help') pos (1196, 566)



## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

# ################################################################################
# ## Main and Game Menu Screens
# ################################################################################

# ## Navigation screen ###########################################################
# ##
# ## This screen is included in the main and game menus, and provides navigation
# ## to other menus, and to start the game.

# screen navigation():

#     vbox:
#         style_prefix "navigation"

#         xpos gui.navigation_xpos
#         yalign 0.5

#         spacing gui.navigation_spacing

#         if not main_menu:

#             textbutton _("History") action ShowMenu("history")

#             textbutton _("Save") action ShowMenu("save")

#         textbutton _("Load") action ShowMenu("load")

#         textbutton _("Options") action ShowMenu("preferences")

#         if _in_replay:

#             textbutton _("End Replay") action EndReplay(confirm=True)

#         elif not main_menu:

#             textbutton _("Main Menu") action MainMenu()

#         textbutton _("Chumroll") action ShowMenu("achievements")

#         textbutton _("Credits") action ShowMenu("about")

#         if renpy.variant("pc"):

#             ## Help isn't necessary or relevant to mobile devices.
#             textbutton _("Help") action ShowMenu("help")

#         textbutton _("Warnings") action ShowMenu("content_warnings")

#         textbutton _("Close Menu"):

#             action Return()


screen vol_icon(icon):

    image icon

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, bg=gui.game_menu_background):

    style_prefix "game_menu"

    add bg

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    label title

    if renpy.variant("pc"):

        textbutton _("Quit Game"):

            style "return_button"
            action Quit(confirm=not main_menu)


## Game Menu screen, modified ############################################################
##
## A slightly modified variant of the usual game menu screen, which I use on the volume select screen.

screen game_menu_volumes(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    label title

    if renpy.variant("pc"):

        textbutton _("Quit Game"):

            style "return_button"
            action Quit(confirm=not main_menu)



## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5
                ypos 240

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0
                ypos 480

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

# screen preferences():
#     tag menu
#     use game_menu(_("Options"), scroll="viewport"):
#         vbox:
#             hbox:
#                 box_wrap True
#                 if renpy.variant("pc"):
#                     vbox:
#                         style_prefix "radio"
#                         label _("Display")
#                         textbutton _("Window") action Preference("display", "window")
#                         textbutton _("Fullscreen") action Preference("display", "fullscreen")

#                 vbox:
#                     style_prefix "radio"
#                     label _("Rollback Side")
#                     textbutton _("Disable") action Preference("rollback side", "disable")
#                     textbutton _("Left") action Preference("rollback side", "left")
#                     textbutton _("Right") action Preference("rollback side", "right")

#                 vbox:
#                     style_prefix "check"
#                     label _("Skip")
#                     textbutton _("Unseen Text") action Preference("skip", "toggle")
#                     textbutton _("After Choices") action Preference("after choices", "toggle")
#                     textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

#                 vbox:
#                     style_prefix "radio"
#                     label _("Flashing Lights")
#                     textbutton _("Enabled") action SetField(persistent, 'flash', True)
#                     textbutton _("Disabled") action SetField(persistent, 'flash', False)

#             null height (4 * gui.pref_spacing)
#             hbox:
#                 box_wrap True
#                 ## Additional vboxes of type "radio_pref" or "check_pref" can be
#                 ## added here, to add additional creator-defined preferences.
#                 transclude

#             null height (4 * gui.pref_spacing)
#             hbox:
#                 style_prefix "slider"
#                 box_wrap True

#                 vbox:
#                     label _("Text Speed")
#                     bar value Preference("text speed")
#                     label _("Auto-Forward Time")
#                     bar value Preference("auto-forward time")

#                 vbox:
#                     if config.has_music:
#                         label _("Music Volume")
#                         hbox:
#                             bar value Preference("music volume")

#                     if config.has_sound:
#                         label _("Sound Volume")
#                         hbox:
#                             bar value Preference("sound volume")
#                             if config.sample_sound:
#                                 textbutton _("Test") action Play("sound", config.sample_sound)


#                     if config.has_voice:
#                         label _("Voice Volume")
#                         hbox:
#                             bar value Preference("voice volume")
#                             if config.sample_voice:
#                                 textbutton _("Test") action Play("voice", config.sample_voice)

#                     if config.has_music or config.has_sound or config.has_voice:
#                         null height gui.pref_spacing
#                         textbutton _("Mute All"):
#                             action Preference("all mute", "toggle")
#                             style "mute_all_button"


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                # $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                $ what = h.what
                text what

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set() # set("b", "i", "quirk")



## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

                #textbutton _("Content Warnings") action SetScreenVariable("device", "cwarns")


            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help
            #elif device == "cwarns":
            #    use content_warnings


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Right Click")
        text _("Hides the user interface.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()



## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

