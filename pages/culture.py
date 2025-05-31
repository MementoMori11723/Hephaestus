from components import culture
from components.common import Layout

try:
    # Getting Placeholders
    main, side_main = Layout()

    # Start of Culture page content
    culture.Sidebar(side_main)

    # First Section of the page
    culture.History(main)

    # Second Section of the page
    culture.Music(main)

    # Third Section of the page
    culture.Flavors_of_india(main)

    # Fourth Section of the page
    culture.Most_visited(main)

    # Final Section of the page
    culture.Future(main)
except Exception as e:
    raise e
