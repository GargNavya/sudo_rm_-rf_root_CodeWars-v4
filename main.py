from engine.main import Game
import scriptblue
import scriptred
import sudo_rm_rf_root

if __name__ == "__main__":
    G = Game((40, 40), scriptblue, sudo_rm_rf_root)
    G.run_game()