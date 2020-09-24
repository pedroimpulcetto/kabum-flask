from app import create_app

CONFIG_FILE = 'config'

if __name__ == '__main__':
    manager = create_app(CONFIG_FILE)
    manager.run()
