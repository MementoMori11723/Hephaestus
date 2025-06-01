from components import personalize
from components.common import Layout

try:
    # Getting Placeholders
    main, side_main = Layout()

    # Personalize sidebar content
    personalize.Sidebar(side_main)

    # Personalize page content
    personalize.Quiz(main)
except Exception as e:
    raise e
