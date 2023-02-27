import os
import toml

config_dir = os.path.dirname(os.path.realpath(__file__))
user_toml_path = os.path.join(config_dir, 'user.toml')


def get_api_key_from_input():
    api_key_new = input("Enter the API key for HypatiaCatalog.com  see yours API after login at " +
                        "<https://hypatiacatalog.com/api>\n")
    save_key = input("Would you like to save this key and skip this step next time [N/y]?\n")

    if save_key.lower() in {'y', 'yes', 't', 'true'}:
        with open(os.path.join(user_toml_path), 'w') as f:
            toml.dump(dict(api_key=api_key_new), f)
    return api_key_new


def get_api_key_from_user_toml():
    user_data = toml.load(user_toml_path)
    return user_data['api_key']


try:
    api_key = get_api_key_from_user_toml()
except FileNotFoundError:
    api_key = get_api_key_from_input()
