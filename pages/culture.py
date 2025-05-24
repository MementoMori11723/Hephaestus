from components.common import Layout
from components import culture

try:
    # Getting Placeholders
    main, side_main = Layout()
    
    culture.Culture(main)
except Exception as e:
    raise e
