from components.common import Layout 
from components import about 

try:
    # Getting Placeholders
    main, side_main = Layout()

    # Creating content variable
    content = {}

    # assigning values to content variable
    for q, a in zip(about.Questions(), about.Answers()):
        content[q] = a

    # About Page content
    about.About(
        main, 
        side_main, 
        content
    )
except Exception as e:
    raise e
