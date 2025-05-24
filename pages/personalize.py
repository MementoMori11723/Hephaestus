from components.common import Layout 
from components import personalize

try:
    # Getting Placeholders
    main, side_main = Layout()
   
    # Personalize page content  
    personalize.Quiz(main)

except Exception as e:
    raise e
