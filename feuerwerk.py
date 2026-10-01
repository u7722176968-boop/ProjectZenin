import os
import time
class Feuerwerk:
    def __init__(self):
        pass
    def explosion(self, name):
        frames = [
                    """
                         *    
                      *  |  *
                        \\|/
                     *---+---*
                        /|\\
                      *  |  *
                         *
                    """,
                    """
                           .
                      *         *
                   *      \\|/      *
                         --+--
                   *      /|\\      *
                      *         *
                           .
                    """,
                    """
                    *       .       *
                       \\    |    /
                    .----\\--+--/----.
                       /    |    \\
                    *       .       *
                    """,
                    """
                    *   *   *   *   *
                      \\  |  |  |  /
                    *---\\|--+--|/---*
                      /  |  |  |  \\
                    *   *   *   *   *
                    """
                ]

        for frame in frames:
            os.system("cls" if os.name == "nt" else "clear")
            print(frame)
            time.sleep(0.4)

        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================================")
        print("       🎉 GEWONNEN! 🎉")
        print()
        print("          " + name)
        print()
        print("================================")