from components import explore
from components.common import Layout

try:
    # Getting Placeholders
    main, side_main = Layout()

    explore.Sidebar(side_main)

    explore.Flavors(main)

    explore.Places(main)
except Exception as e:
    raise e
