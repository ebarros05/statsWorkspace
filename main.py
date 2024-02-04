import statsWorkspace as spk

import code

def main():
    welcome_message = "Welcome to the Stats Terminal! You can call functions directly."
    banner = f"{welcome_message}\nType 'quit()' to exit."

    local_vars = globals().copy()
    local_vars.update(spk.__dict__)

    code.interact(banner=banner, local=local_vars)


if __name__ == "__main__":
    main()