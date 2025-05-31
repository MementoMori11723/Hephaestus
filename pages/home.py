from components import home
from components.common import Layout

try:
    # Getting Placeholders
    main, side_main = Layout()

    # Sidebar menu
    home.Sidebar(side_main)

    # Hero section
    home.Hero(main)

    # About section
    home.About(main)

    # Personalize section
    home.Personalize(main)

    # Culture section
    home.Culture(main)

    # Explore section
    home.Explore(main)

except Exception as e:
    raise e
