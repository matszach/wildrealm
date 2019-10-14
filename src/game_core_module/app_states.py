from util.id_generator import IdGenerator


class AppStates:

    id_generator: IdGenerator = IdGenerator()

    MAIN_MENU: int = id_generator.next()
    NEW_GAME_MENU: int = id_generator.next()
    LOADING: int = id_generator.next()
    GENERATING_MAP: int = id_generator.next()
    IN_GAME_PLAY: int = id_generator.next()
    IN_GAME_PAUSED: int = id_generator.next()
    IN_GAME_INVENTORY: int = id_generator.next()
    IN_GAME_GAME_OVER: int = id_generator.next()

