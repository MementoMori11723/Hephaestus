from components import explore
from components.common import Layout

try:
    # Getting Placeholders
    main, side_main = Layout()

    explore.Sidebar(side_main)

    explore.Artwork(main)

    explore.Flavors(main)

    explore.Places(main)

    explore.Others(main)
except Exception as e:
    raise e
