import sqlite3

import pandas as pd


def fetch(table: str) -> pd.DataFrame:
    conn = sqlite3.Connection("data/base.db")
    cursor = conn.cursor()

    cursor.execute(f"PRAGMA table_info({table})")
    column_info = cursor.fetchall()
    column_info = [row[1] for row in column_info]

    cursor.execute(f"select * from {table}")
    rows = cursor.fetchall()

    conn.close()
    return pd.DataFrame(rows, columns=column_info)


def Flavors():
    return fetch("flavors")


def Top_videos():
    return fetch("top_videos")


def Tourist_places():
    return fetch("tourist_places")


def Dance() -> dict:
    return {
        "Manipuri": {
            "img": "https://i0.wp.com/darshanajhaveri.com/wp-content/uploads/2018/11/image_33-e1543396552578.jpg?resize=303%2C447",
            "url": "https://youtu.be/HzqQjdCSmuY",
            "info": "Manipuri dance, also known as Jagoi or Manipuri Raas Leela, is one of India's classical dance forms, originating from the state of Manipur.",
        },
        "Bharatanatyam": {
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Bharata_Natyam_Performance_DS.jpg/330px-Bharata_Natyam_Performance_DS.jpg",
            "url": "https://youtu.be/YuxLEc2JqnE",
            "info": "Bharatanatyam is a classical Indian dance form from Tamil Nadu, known for its storytelling through intricate hand gestures, facial expressions, and rhythmic footwork.",
        },
        "Odissi": {
            "img": "https://lipsasatapathy.com/wp-content/uploads/2023/12/27973802_10155274930011475_6775249791606593842_n.jpg",
            "url": "https://youtu.be/LUHrTwrC3wU",
            "info": "Odissi dance is a classical Indian dance form originating from the state of Odisha.",
        },
        "Kathakali": {
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Kathakali_BNC.jpg/250px-Kathakali_BNC.jpg",
            "url": "https://youtu.be/GBbcYtkqVKQ",
            "info": "Kathakali is a classical Indian dance-drama form from Kerala, known for its stylized acting, intricate costumes, and vibrant makeup.",
        },
        "Kathak": {
            "img": "https://www.drishtiias.com/images/uploads/1579336257_image4.jpg",
            "url": "https://youtu.be/UBYqv21c0Yk",
            "info": "Kathak is one of the eight major forms of Indian classical dance. Its origin is attributed to the traveling bards in ancient northern India known as Kathakar",
        },
        "Sattriya": {
            "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkCHh7Ta2bWBau8reOoepbbgu9-eeldC-apw&s",
            "url": "https://youtu.be/-123CQlpqBY",
            "info": "Sattriya is a classical Indian dance form from Assam, India, with strong roots in neo-Vaishnavism.",
        },
        "Kuchipudi": {
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Indian_Dancer_%28Malabika_Sen%29.jpg/250px-Indian_Dancer_%28Malabika_Sen%29.jpg",
            "url": "https://youtu.be/tyTOe1wabgM",
            "info": "Kuchipudi is a classical Indian dance-drama form originating from the village of Kuchipudi in Andhra Pradesh, India.",
        },
        "Mohiniyattam": {
            "img": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Mohiniyattom_performance.jpg",
            "url": "https://youtu.be/Fl3g-RUYE3w",
            "info": "Mohiniyattam is a classical Indian dance form originating from Kerala, known for its graceful and feminine movements.",
        },
    }


def Painting() -> list[dict]:
    return [
        {
            "Name": "Gond Art",
            "Field": "gond",
            "Desc": "Gond art is a vibrant and expressive form of folk art practiced by the Gond people, one of the largest tribal groups in India, primarily in Madhya Pradesh. It's known for its use of natural pigments, detailed depictions of nature and mythology, and intricate dot and line patterns.",
        },
        {
            "Name": "Kalighat Art",
            "Field": "kalighat",
            "Desc": "Kalighat painting is a traditional art form from West Bengal, India, known for its vibrant colors, simplified forms, and strong lines. It originated in the mid-19th century near the Kalighat Kali Temple in Kolkata and was created by Patua artists, who were itinerant storytellers.",
        },
        {
            "Name": "Kangra Art",
            "Field": "kangra",
            "Desc": "Kangra painting, also known as Kangra miniature painting, is a school of Pahari (hill) painting that originated in the Kangra region of Himachal Pradesh, India. This art form developed in the 18th century and is characterized by its delicate brushwork, vivid colors, and depiction of themes from Hindu mythology, particularly the love stories of Radha and Krishna.",
        },
        {
            "Name": "Kerala Mural",
            "Field": "kerala-mural",
            "Desc": "Kerala mural paintings are a vibrant and traditional form of wall art found in temples and palaces throughout the state of Kerala, India. They are known for their intricate detailing, use of natural pigments, and depiction of scenes from Hindu mythology and epics like the Ramayana and Mahabharata.",
        },
        {
            "Name": "Madhubani Art",
            "Field": "madhubani",
            "Desc": "Madhubani art, also known as Mithila painting, is a vibrant and intricate style of folk art from the Mithila region of Bihar, India. It's characterized by bright colors, geometric patterns, and the use of natural dyes and pigments. ",
        },
        {
            "Name": "Mandana Art",
            "Field": "mandana",
            "Desc": "Mandana art is a traditional tribal art form from Madhya Pradesh and Rajasthan, primarily practiced by the Meena community. It involves creating paintings on walls and floors of homes, often using natural materials like clay, cow dung, and red ochre (geru). The art is a form of decoration and is used to mark auspicious occasions like births, weddings, and festivals, as well as to ward off evil spirits and invite good fortune. ",
        },
        {
            "Name": "Pichwai Art",
            "Field": "pichwai",
            "Desc": "Pichwai art is a traditional painting style from Rajasthan, India, particularly known for its depiction of Lord Krishna and his life, These paintings, typically on cloth, are vibrant, detailed, and often used as devotional art in temples and homes. They are characterized by intricate floral motifs, bright natural colors, and a distinct style related to the town of Nathdwara.",
        },
        {
            "Name": "Warli Art",
            "Field": "warli",
            "Desc": "Warli art is a traditional Indian folk art form from the Warli tribe in Maharashtra, known for its use of simple, geometric shapes and depictions of daily life, rituals, and nature. It's characterized by its minimalist graphic vocabulary, featuring circles, triangles, squares, and lines, often painted in white against a brown or red background.",
        },
    ]


def Dress() -> dict:
    return {
        "Kurta": {
            "url": "https://www.kraftindia.in/cdn/shop/files/IMG_1138.jpg?v=1690996847",
            "desc": "A kurta is a long, loose-fitting shirt commonly worn in South Asia, particularly India and Pakistan. It's a traditional garment with roots in the Indian subcontinent and is worn by both men and women. Kurtas are typically knee-length or longer and can be made from various fabrics like cotton, silk, or linen. They are often worn with trousers or pants, such as shalwars or churidars.",
        },
        "Saree": {
            "url": "https://cdn.shopify.com/s/files/1/1762/5129/files/saree-in-green.jpg?v=1638249949",
            "desc": "A saree is an iconic Indian garment, typically a long, flowing piece of fabric that's draped and worn around the body. It's known for its elegance, grace, and versatility, and is a symbol of India's rich cultural heritage.",
        },
        "Dhoti": {
            "url": "https://5.imimg.com/data5/ANDROID/Default/2024/10/459913942/SG/NN/DZ/26624364/product-jpeg-500x500.jpg",
            "desc": "A dhoti is a traditional Indian garment worn by men, typically made of a long rectangular piece of cloth, usually cotton or silk, wrapped around the waist and legs. It's a loose, draped garment, often worn for formal occasions, religious events, and in rural areas.",
        },
        "Salwar Kameez": {
            "url": "https://wholesalemegamart.com/wp-content/uploads/2024/11/RTC-5765-PARTY-WEAR-SALWAR-KAMEEZ-WHOLESALE-1.jpeg",
            "desc": 'A salwar kameez is a traditional garment worn in South Asia, typically by women, but sometimes by men. It consists of a long, loose-fitting shirt or tunic called a "kameez" paired with loose-fitting pants called "salwars" or "shalwars". The kameez often has side slits (chaak) below the waistline for greater freedom of movement. ',
        },
        "Sherwani": {
            "url": "https://shreeman.in/cdn/shop/files/3_b8e2a4a6-c653-465c-857c-235deb3b551d.jpg?v=1739618873",
            "desc": "A sherwani is a traditional Indian garment worn by men, typically for special occasions like weddings or festivals. It's a long, coat-like garment that usually extends below the knee and is often adorned with embroidery or other embellishments. Sherwanis are usually worn over a kurta and churidar or straight-cut pants. ",
        },
    }


def Tarot() -> dict:
    return {
        "month": {
            "January": "Capricorn",
            "February": "Aquarius",
            "March": "Pisces",
            "April": "Aries",
            "May": "Taurus",
            "June": "Gemini",
            "July": "Cancer",
            "August": "Leo",
            "September": "Virgo",
            "October": "Libra",
            "November": "Scorpio",
            "December": "Sagittarius",
        },
        "sign": {
            "Capricorn": (
                "Capricorn, the mountain goat, climbs steadily toward its goals. Your strength lies in discipline, resilience, and quiet ambition. ",
                "Now is the time to reconnect with your long-term vision. Though the road may be slow, each step you take is rooted in purpose. ",
                "Let go of distractions and trust your inner architect—you're building something lasting. Your grounded energy is your greatest gift.",
            ),
            "Aquarius": (
                "Aquarius is the water bearer who brings transformation through ideas. Your mind is electric, and you often stand at the edge of the future, seeing patterns others miss. ",
                "This is a moment to embrace your uniqueness and dare to challenge the norm. The world needs your voice and your vision. ",
                "Let your inner rebel speak—but do so with compassion. Innovation flows through you.",
            ),
            "Pisces": (
                "Pisces swims in the ocean of dreams, emotion, and intuition. You may feel pulled in many directions, but trust that your soul knows the way. ",
                "This is a season to reconnect with your creativity and spiritual depth. Don’t be afraid to withdraw briefly to find clarity. ",
                "Messages from the subconscious are rising—listen closely, and you’ll hear guidance in the whispers of your own heart.",
            ),
            "Aries": (
                "Aries is the first spark of fire, the fearless warrior stepping into the unknown. Your courage is contagious, and your drive can break through any barrier. ",
                "This is a time to take initiative—don’t wait for permission. Be mindful of recklessness, but don’t hold back your truth. ",
                "Lead with your heart, and your bravery will open doors others only dream of knocking on.",
            ),
            "Taurus": (
                "Taurus, rooted like the sacred oak, thrives in stability, beauty, and the pleasures of life. This is a time to ground yourself—physically, emotionally, and spiritually. ",
                "Honor the comfort of routine, but don’t be afraid to make space for gentle growth. Invest in what brings lasting joy. ",
                "Slow and steady wins your race, and the seeds you plant now will blossom in due season.",
            ),
            "Gemini": (
                "Gemini dances between dualities—the thinker and the talker, the curious and the restless. Communication is your magic, and your words can weave light into shadow. ",
                "Now is the moment to ask questions, explore new ideas, and share what you know. Don’t let indecision paralyze you—movement is your power. ",
                "A message awaits you, hidden in a conversation or a passing thought. Stay open.",
            ),
            "Cancer": (
                "Cancer is the moon-touched guardian of home, emotion, and intuition. You may be feeling tender, but that sensitivity is your superpower. ",
                "Let yourself feel deeply, and protect what matters most to your heart. This is a time for nurturing connections and embracing your vulnerability. ",
                "The shell protects, but don't hide for too long—your light is needed in the world.",
            ),
            "Leo": (
                "Leo, radiant and bold, you are the sun incarnate. This is your moment to shine without apology. Step into the spotlight and allow your inner fire to illuminate others. ",
                "You are a natural leader, but the truest strength comes when pride is tempered by generosity. ",
                "Share your gifts, and the world will echo your roar with applause. Your passion is contagious—use it to uplift.",
            ),
            "Virgo": (
                "Virgo, the sacred servant, sees the details others overlook. Your gift is refinement—of thought, space, and action. ",
                "This is a time to organize, analyze, and bring harmony to what feels chaotic. Don’t be too critical of yourself; perfection is not the goal—growth is. ",
                "Trust that your quiet diligence makes a lasting impact. Every small act ripples outward.",
            ),
            "Libra": (
                "Libra, the eternal balancer, seeks beauty, justice, and harmony in all things. You’re being called to examine your relationships—not just with others, but with yourself. ",
                "Where can peace be restored? Where can beauty be invited in? Let grace guide your decisions, and remember: balance does not mean silence. ",
                "Speak your truth gently, and the scales will naturally align.",
            ),
            "Scorpio": (
                "Scorpio is the alchemist of the zodiac—intense, passionate, and endlessly transformative. You’re in a season of shedding skin, diving into emotional depths others fear. ",
                "Trust the process, even when it feels like destruction. What dies now was never meant to remain. ",
                "You are being reborn in the fire of truth and desire. Embrace the mystery; you are its master.",
            ),
            "Sagittarius": (
                "Sagittarius, the archer, is ever-seeking, ever-wandering. Your soul craves expansion—of knowledge, experience, and perspective. ",
                "Now is a time for adventure, whether outward into the world or inward into wisdom. Speak your truths boldly and listen with an open mind. ",
                "Freedom is sacred to you—honor it, but don’t fear commitment to a path that fuels your spirit.",
            ),
        },
        "color": {
            "Red": (
                "Red surges with power and vitality. Today, your passions burn bright, and the universe urges you to channel that fire into action. ",
                "Don't hesitate—whether it's love, creativity, or ambition, now is the time to take bold steps. However, be mindful of impulsiveness. ",
                "Let your passion be your compass, but balance it with wisdom. The energy around you is magnetic; use it to ignite your purpose.",
            ),
            "Blue": (
                "Blue is the color of calm waters and deep reflection. This is a time for introspection and trusting your intuition. ",
                "You may feel the urge to withdraw slightly from chaos and seek peace—follow that instinct. Insights will come not from loud voices, ",
                "but from silence and stillness. Let go of tension and embrace the quiet clarity that surrounds you. Emotional healing is within reach.",
            ),
            "Green": (
                "Green is the color of nature, renewal, and abundance. Growth—both emotional and material—is within your grasp. ",
                "You may be entering a phase of healing, where past wounds begin to close and new paths begin to sprout. Nurture your body, mind, and spirit. ",
                "Connect with the earth or something grounding in your life. Prosperity will follow where you invest patience and care.",
            ),
            "Yellow": (
                "Yellow shines like sunlight, bringing clarity, confidence, and optimism. You're being asked to embrace joy and let it lead you out of confusion. ",
                "Your mental energy is high—use it to solve problems, express creativity, or simply bring warmth into others' lives. ",
                "Laughter and light-heartedness are more powerful than they seem. Allow yourself to glow without shame or fear.",
            ),
            "White": (
                "White represents purity, clarity, and a spiritual reset. This is a sacred pause in your life—an invitation to cleanse your space, your thoughts, and your intentions. ",
                "New beginnings are forming, and you are being offered a blank canvas. Release the past, however painful or precious. ",
                "Your soul is ready to move forward unburdened. Trust the light that lies ahead.",
            ),
            "Black": (
                "Black holds mystery, power, and profound transformation. Something in your life is ready to shed—an identity, belief, or chapter. ",
                "This may feel like darkness, but it is the fertile void where new potential is born. Embrace the unknown. ",
                "Let go of the need for control, and trust that even shadows hold sacred lessons. You are stepping into your power by releasing what no longer serves you.",
            ),
            "Pink": (
                "Pink radiates compassion, tenderness, and emotional openness. Today is a day to give and receive love freely. ",
                "Whether it’s a kind word, a warm hug, or a vulnerable truth, soft gestures carry profound strength. ",
                "Forgive yourself and others. Reconnect with the gentleness that lives within you. What you nurture with love will flourish beyond expectation.",
            ),
        },
    }


def Month() -> dict:
    return {
        "January": (
            "1. Makar Sankranti is one of the few Hindu festivals based on the solar calendar.\n",
            "2. The Republic Day parade has been held at Rajpath since 1955.\n",
            "3. The coldest temperature ever recorded in India was −60°C in Dras, Jammu & Kashmir.\n",
            "4. Lohri is primarily celebrated in Punjab but is also popular in Himachal and Haryana.\n",
            "5. Pongal is Tamil Nadu's biggest harvest festival, spanning 4 days.",
        ),
        "February": (
            "1. February is the only month that can go without a full moon every 19 years.\n",
            "2. The Taj Mahotsav, held in Agra, began in 1992 to promote local art and culture.\n",
            "3. Vasant Panchami marks the start of spring and honors Goddess Saraswati.\n",
            "4. Arunachal Pradesh and Mizoram were granted statehood on 20 February 1987.\n",
            "5. The Kala Ghoda Arts Festival in Mumbai is one of the largest street festivals in India.",
        ),
        "March": (
            "1. Holi is celebrated differently in each region—e.g., Lathmar Holi in Barsana.\n",
            "2. The Indian fiscal year ends in March, a British colonial legacy.\n",
            "3. The spring equinox often occurs in March, affecting some regional festivals.\n",
            "4. Jamshedpur was founded in March 1919 and named after Jamsetji Tata.\n",
            "5. India’s first passenger train trial (Bombay to Thane) happened in March 1853.",
        ),
        "April": (
            "1. Bihu in Assam marks the Assamese New Year and is one of three Bihus.\n",
            "2. Mahavir Jayanti honors the birth of Lord Mahavir, the 24th Tirthankara.\n",
            "3. April is the peak time for mango flowering in central India.\n",
            "4. Ambedkar Jayanti is a public holiday only in some Indian states.\n",
            "5. The first Indian census under British rule began in April 1871.",
        ),
        "May": (
            "1. May is usually the hottest month in most parts of India.\n",
            "2. The Indian Rebellion of 1857 began in Meerut on 10 May.\n",
            "3. Buddha Purnima is celebrated across many regions but on different days.\n",
            "4. Mount Everest was first summited on 29 May 1953; many Indian expeditions now begin in May.\n",
            "5. Rabindranath Tagore, India’s first Nobel laureate, was born on 7 May 1861.",
        ),
        "June": (
            "1. The southwest monsoon typically begins in Kerala in early June.\n",
            "2. International Yoga Day on 21 June was proposed by India in the UN.\n",
            "3. Hemis Festival in Ladakh is celebrated in June or July every year.\n",
            "4. The Ratha Yatra of Puri usually begins in June or early July.\n",
            "5. June is peak tea-plucking season in Darjeeling and Assam.",
        ),
        "July": (
            "1. The Bombay High Court, one of India’s oldest, was established in July 1862.\n",
            "2. The Indian Meteorological Department tracks monsoon intensity daily from July.\n",
            "3. Guru Purnima is celebrated to honor spiritual and academic teachers.\n",
            "4. Cherrapunji and Mawsynram receive maximum rainfall in July.\n",
            "5. The first Indian postage stamp was issued on 1 July 1852.",
        ),
        "August": (
            "1. India gained independence on 15 August 1947.\n",
            "2. Raksha Bandhan often falls in August but varies with the lunar calendar.\n",
            "3. The Quit India Movement was launched on 8 August 1942.\n",
            "4. Janmashtami marks Lord Krishna’s birth and involves fasting and Dahi Handi.\n",
            "5. Nehru Planetarium in Delhi opened in August 1984.",
        ),
        "September": (
            "1. Teacher’s Day in India is celebrated on 5 September, Sarvepalli Radhakrishnan’s birthday.\n",
            "2. Hindi Diwas is observed on 14 September to mark the adoption of Hindi as an official language.\n",
            "3. Onam, the harvest festival of Kerala, often falls in September.\n",
            "4. The Indian Space Research Organisation (ISRO) was formed on 15 September 1969.\n",
            "5. World Ozone Day on 16 September is marked by many Indian schools with awareness events.",
        ),
        "October": (
            "1. Gandhi Jayanti on 2 October is also celebrated as the International Day of Non-Violence.\n",
            "2. India’s first National Wildlife Week is observed from 2 to 8 October.\n",
            "3. Navratri celebrates feminine power and varies in customs across states.\n",
            "4. Durga Puja in West Bengal is a UNESCO-listed cultural event.\n",
            "5. Air India’s first flight took off in October 1932 from Karachi to Mumbai.",
        ),
        "November": (
            "1. Diwali sometimes falls in November depending on the lunar calendar.\n",
            "2. Children’s Day is celebrated on 14 November, Nehru’s birthday.\n",
            "3. Guru Nanak Jayanti is a major Sikh festival celebrated in November.\n",
            "4. The Hornbill Festival preparations begin in November in Nagaland.\n",
            "5. The first Indian National Park, Jim Corbett, was named so in November 1957.",
        ),
        "December": (
            "1. Goa Liberation Day is observed on 19 December, marking freedom from Portuguese rule in 1961.\n",
            "2. Sikkim celebrates its State Day on 16 December.\n",
            "3. The Indian National Congress was founded in Bombay in December 1885.\n",
            "4. Hornbill Festival continues into early December.\n",
            "5. Christmas is widely celebrated even in non-Christian regions due to British legacy.",
        ),
    }


def Personal_Options() -> dict:
    return {
        "color": ["Red", "Blue", "Green", "Yellow", "White", "Black", "Pink"],
        "num": [1, 2, 3, 4, 5],
        "month": [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
        "true": ["Yes", "No"],
        "nature": ["Nature", "Cities"],
        "region": ["North", "South", "East", "West", "Central", "Northeast"],
        "dress": ["Kurta", "Saree", "Dhoti", "Salwar Kameez", "Sherwani"],
        "art": ["Painting", "Dance", "Music"],
        "time": ["Morning", "Afternoon", "Evening", "Night"],
        "culture": ["Storytelling", "Rituals", "Crafts"],
    }

def Music_images() -> list[str]:
    return [
        "https://img.freepik.com/premium-vector/colorful-musical-note-art-with-vibrant-splashes-musical-note-black-surrounded_53876-651215.jpg?semt=ais_items_boosted&w=740",
        "https://freerangestock.com/thumbnail/116805/music-note-silhouette-.jpg",
        "https://cdn.pixabay.com/photo/2015/05/29/23/10/music-789957_1280.jpg"
    ]


def State_data() -> dict:
    return {
        "Jammu & Kashmir": """ 
        - Home to the world's only floating post office on Dal Lake in Srinagar.
        - The region boasts breathtaking landscapes, including the famous Dal Lake and the Himalayas.
        - Known for its rich handicrafts, especially Pashmina shawls and Kashmiri carpets.
        """,
        "Himachal Pradesh": """ 
        - Nicknamed "Dev Bhoomi" or "Land of the Gods" due to its numerous temples.
        - Home to the Great Himalayan National Park, a UNESCO World Heritage Site.
        - The state is known for its apple orchards, contributing significantly to India's apple production.
        """,
        "Delhi": """
        - Home to three UNESCO World Heritage Sites: Qutub Minar, Red Fort, and Humayun's Tomb.
        - The Delhi Metro is one of the largest and busiest metro networks in the world.
        - The city has a rich history, having been the capital of several empires.
        """,
        "Punjab": """ 
        - The Golden Temple in Amritsar is a major pilgrimage site for Sikhs worldwide.
        - Bhangra and Giddha are traditional dance forms originating from Punjab.
        - Known as the "Granary of India" due to its extensive wheat and rice production.
        """,
        "Haryana": """ 
        - The ancient city of Kurukshetra is believed to be the battlefield of the Mahabharata.
        - Home to the Sultanpur National Park, a bird watcher's paradise.
        - Known for its rich tradition in wrestling and producing many national-level athletes.
        """,
        "Uttarakhand": """ 
        - Hosts the Char Dham pilgrimage sites: Yamunotri, Gangotri, Kedarnath, and Badrinath.
        - The Jim Corbett National Park, India's first national park, is located here.
        - Known as the "Land of Gods" due to its numerous Hindu temples and pilgrimage centers.
        """,
        "Uttar Pradesh": """ 
        - Home to the iconic Taj Mahal in Agra, one of the Seven Wonders of the World.
        - Varanasi, one of the world's oldest inhabited cities, is located here.
        - The state has a rich tradition in classical music and dance, including Kathak.
        """,
        "Madhya Pradesh": """ 
        - Known as the "Heart of India" due to its central location.
        - Hosts the Khajuraho Group of Monuments, famous for their erotic sculptures.
        - The Bhimbetka rock shelters exhibit prehistoric cave paintings.
        """,
        "Chhattisgarh": """
        - The name translates to "Thirty-Six Forts," though the exact origin is debated.
        - Rich in mineral resources and dense forests, supporting diverse wildlife.
        - Home to the Chitrakote Falls, often referred to as the "Niagara Falls of India."
        """,
        "Rajasthan": """
        - Known for its majestic forts and palaces, including the Amber Fort and City Palace.
        - Hosts the Thar Desert, the world's 17th largest desert.
        - The Pushkar Camel Fair is one of the world's largest livestock fairs.
        """,
        "Gujarat": """
        - The Gir National Park is the only natural habitat of the Asiatic lion.
        - Tulsi Shyam in Gujarat is known for a gravity hill where vehicles appear to roll uphill.
        - The state is famous for its vibrant Navratri festival celebrations.
        """,
        "Maharashtra": """
        - Mumbai, the capital, is the financial hub of India and home to Bollywood.
        - The Ajanta and Ellora caves are UNESCO World Heritage Sites known for their ancient rock-cut temples.
        - The state has a rich tradition of Lavani, a genre of music popular in Maharashtra.
        """,
        "Goa": """
        - Known for its pristine beaches and Portuguese heritage.
        - The Basilica of Bom Jesus in Old Goa is a UNESCO World Heritage Site.
        - Celebrates vibrant festivals like Carnival and Shigmo with great enthusiasm.
        """,
        "Andhra Pradesh": """
        - The city of Amaravati is being developed as the state's new capital.
        - Home to the Tirumala Venkateswara Temple, one of the world's richest temples.
        - The state has a rich tradition of Kuchipudi, a classical Indian dance form.
        """,
        "Telangana": """
        - Hyderabad, the capital, is known for its historic Charminar and delicious biryani.
        - The region celebrates the Bonalu festival, dedicated to the Goddess Mahakali.
        - Known for its unique art forms like Nirmal paintings and Bidriware.
        """,
        "Karnataka": """
        - Bengaluru, the capital, is known as the "Silicon Valley of India."
        - Home to Hampi, a UNESCO World Heritage Site with ruins of the Vijayanagara Empire.
        - The state is rich in biodiversity, with numerous wildlife sanctuaries and national parks.
        """,
        "Tamil Nadu": """
        - Chennai is considered the cultural capital of South India.
        - Bharatanatyam, one of the oldest classical dance forms, originated here.
        - The state has a rich tradition of temple architecture, evident in structures like the Meenakshi Temple.
        """,
        "Kerala": """
        - Known as "God's Own Country" for its scenic landscapes and backwaters.
        - The state has the highest literacy rate in India.
        - Celebrates the Onam festival with traditional boat races and dances.
        """,
        "Bihar": """
        - Bodh Gaya in Bihar is where Gautama Buddha attained enlightenment.
        - The ancient Nalanda University was a renowned center of learning.
        - Chhath Puja, dedicated to the Sun God, is a major festival here.
        """,
        "Jharkhand": """
        - Rich in mineral resources, contributing significantly to India's economy.
        - Home to the Betla National Park, known for its wildlife and waterfalls.
        - Hosts the tribal festival of Sarhul, celebrating nature and community.
        """,
        "Odisha": """
        - The Sun Temple at Konark is a UNESCO World Heritage Site.
        - Hosts the Rath Yatra festival in Puri, attracting millions of devotees.
        - Known for its classical dance form, Odissi.
        """,
        "West Bengal": """
        - Kolkata was the capital of British India until 1911.
        - The Sundarbans, the world's largest mangrove forest, is located here.
        - Celebrates Durga Puja with grandeur and artistic pandals.
        """,
        "Assam": """
        - Famous for its Assam tea, exported worldwide.
        - Kaziranga National Park is home to the one-horned rhinoceros.
        - Celebrates Bihu, marking the Assamese New Year and agricultural cycles.
        """,
        "Arunachal Pradesh": """
        - Known as the "Land of the Rising Sun" in India.
        - Home to diverse indigenous tribes with unique cultures.
        - Tawang Monastery is the largest monastery in India.
        """,
    }
