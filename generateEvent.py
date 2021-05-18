import pyperclip

option_template = """
	option = {
		name = "dmm_keyboard_$$UI_NAME$$"
		custom_gui = "dmm_keyboard_$$UI_NAME$$"
		is_dialog_only = yes
		response_text = "dmm_keyboard_$$UI_NAME$$_response"
        hidden_effect = {
            dmm_keyboard_add_letter = yes
			event_target:dmm_keyboard_leader = {
				set_name = "[dmm_keyboard_current_leader.GetName]"
			}
            event_target:dmm_keyboard_current_leader = {
                set_name = "[dmm_keyboard_current_leader.GetName][This.GetKeyboardSpace]$$LETTER$$"
            }
			event_target:dmm_keyboard_country = {
				set_variable = {
					which = dmm_keyboard_spaces_amount
					value = 0
				}
			}
        }
	}"""

# "[dmm_keyboard_current_leader.GetName][This.GetKeyboardSpace]$$LETTER$$"

container_template = """
	containerWindowType = {
		name = "dmm_keyboard_$$UI_NAME$$"
		position = { x=0 y=0 }
		size = { width = 0 height = 0 }
		moveable = no
		
		buttonType = {
			name = "option_button"
			quadTextureSprite = "GFX_button_animated_265_34"
			position = { x=$$x$$ y=$$y$$ }
			size = { x = 40 y = 30 }
			font = "cg_16b"
            text = "OPTION_TEXT"
            shortcut = "$$SHORTCUT$$"
		}
	}
"""

scripted_loc_template = """
defined_text = {
	name = GetKeyboard$$LETTER_UPPERCASE$$
	text = {
		trigger = {
			has_country_flag = dmm_keyboad_capslock
		}
		localization_key = "dmm_keyboard_$$LETTER_LOWERCASE$$_shift"
	}
	text = {
		trigger = {
			NOT = {
				has_country_flag = dmm_keyboad_capslock
			}
		}
		localization_key = "dmm_keyboard_$$LETTER_LOWERCASE$$_lowercase"
	}
}
"""

loc_template = """
    dmm_keyboard_$$UI_NAME$$: \"$$LETTER$$\"
    dmm_keyboard_$$UI_NAME$$_response: \"[dmm_keyboard_current_leader.GetName][This.GetKeyboardSpace]$$LETTER$$\""""

# [actual key, ui name of the key, shortcut]
# ["A", "a_shift", "SHIFT+a"]
supported_keys = []
for i in range(ord("a"), ord("z") + 1):
    supported_keys.append(["[dmm_keyboard_country.GetKeyboard" + chr(i).upper()+"]", chr(i), chr(i)])
for i in range(ord("A"), ord("Z") + 1):
    supported_keys.append([chr(i), chr(i).lower()+"_shift", "SHIFT+"+chr(i).lower()])
for i in range(10):
    supported_keys.append([str(i), str(i), str(i)])
# supported_keys.append([" ", "space", "SPACE"])
supported_keys.append(["-", "kp_minus", "kp_minus"])
# supported_keys.append(["'", "apostrophe"])
print(supported_keys)


def generate_option(key):
    return option_template.replace("$$LETTER$$", key[0]).replace("$$UI_NAME$$", key[1])

def generate_all_options():
    s = ""
    for k in supported_keys:
        s += generate_option(k)
    pyperclip.copy(s)


def generate_container(key, x=0):
    return container_template.replace("$$UI_NAME$$", key[1]).replace("$$SHORTCUT$$", key[2]).replace("$$x$$",x).replace("$$y$$", "0")

def generate_all_containers():
    s = ""
    x=0
    for k in supported_keys:
        s += generate_container(k, str(x))
        x+=10
    pyperclip.copy(s)


def generate_scripted_loc(key):
    return scripted_loc_template.replace("$$LETTER_LOWERCASE$$", key).replace("$$LETTER_UPPERCASE$$", key.upper())

def generate_scripted_locs():
    s = ""
    for k in range(ord("a"), ord("z") + 1):
        s += generate_scripted_loc(chr(k))
    pyperclip.copy(s)


def generate_loc(key):
    return loc_template.replace("$$LETTER$$", key[0]).replace("$$UI_NAME$$", key[1])

def generate_all_locs():
    s = ""
    for k in supported_keys:
        s += generate_loc(k) # + "\n"
    pyperclip.copy(s)

# replace by what you want
# will copy the result to clipboard

# generate_all_options()
# generate_all_containers()
# generate_scripted_locs()
generate_all_locs()