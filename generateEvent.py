import pyperclip

option_template = """
	option = {
		name = "dmm_keyboard_$$UI_NAME$$"
		custom_gui = "dmm_keyboard_$$UI_NAME$$"
		is_dialog_only = yes
		response_text = "[dmm_keyboard_current_leader.GetName]$$LETTER$$"
        hidden_effect = {
            dmm_keyboard_add_letter = yes
			event_target:dmm_keyboard_leader = {
				set_name = "[dmm_keyboard_current_leader.GetName]"
			}
            event_target:dmm_keyboard_current_leader = {
                set_name = "[dmm_keyboard_current_leader.GetName]$$LETTER$$"
            }
        }
	}"""

container_template = """
	containerWindowType = {
		name = "dmm_keyboard_$$UI_NAME$$"
		position = { x=0 y=0 }
		size = { width = 0 height = 0 }
		moveable = no
		
		buttonType = {
			name = "option_button"
			quadTextureSprite = "GFX_button_animated_265_34"
			position = { x=0 y=0 }
			size = { x = 40 y = 30 }
			font = "cg_16b"
            text = "OPTION_TEXT"
            shortcut = "$$SHORTCUT$$"
		}
	}
"""

# [actual key, ui name of the key, shortcut]
# ["A", "a_uppercase", "SHIFT+a"]
supported_keys = []
for i in range(ord("A"), ord("Z") + 1):
    supported_keys.append([chr(i), chr(i).lower()+"_uppercase", "SHIFT"+chr(i).lower()])
for i in range(ord("a"), ord("z") + 1):
    supported_keys.append([chr(i), chr(i), chr(i)])
supported_keys.append([" ", "space", "SPACE"])
# supported_keys.append(["-", "minus"])
# supported_keys.append(["'", "apostrophe"])
print(supported_keys)


def generate_option(key):
    return option_template.replace("$$LETTER$$", key[0]).replace("$$UI_NAME$$", key[1])

def generate_all_options():
    s = ""
    for k in supported_keys:
        s += generate_option(k)
    pyperclip.copy(s)


def generate_container(key):
    return container_template.replace("$$UI_NAME$$", key[1]).replace("$$SHORTCUT$$", key[2])

def generate_all_containers():
    s = ""
    for k in supported_keys:
        s += generate_container(k)
    pyperclip.copy(s)

# replace by what you want
# will copy the result to clipboard
generate_all_options()