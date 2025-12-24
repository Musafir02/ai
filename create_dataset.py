import json
import random

greetings = [
    ("hi", "Hey! How's it going?"),
    ("hello", "Hello! What can I help you with?"),
    ("hey", "Hey there! What's up?"),
    ("hey there", "Hey! Nice to see you!"),
    ("hi there", "Hi! How are you today?"),
    ("good morning", "Good morning! Hope you're having a great day!"),
    ("good afternoon", "Good afternoon! What brings you here?"),
    ("good evening", "Good evening! How was your day?"),
    ("good night", "Good night! Sleep well!"),
    ("how are you", "I'm doing great, thanks for asking! How about you?"),
    ("how's it going", "Going well! What's on your mind?"),
    ("what's up", "Not much! Just here ready to chat. You?"),
    ("yo", "Yo! What's good?"),
    ("sup", "Sup! What can I do for you?"),
    ("howdy", "Howdy! What brings you here?"),
    ("hiya", "Hiya! Great to see you!"),
    ("greetings", "Greetings! How may I assist you?"),
    ("whats new", "Not much new here! What about you?"),
    ("long time no see", "It has been a while! How have you been?"),
    ("nice to meet you", "Nice to meet you too! I'm excited to chat!"),
]

emotions = [
    ("i'm happy", "That's wonderful! What's making you happy?"),
    ("i'm sad", "I'm sorry to hear that. I'm here if you want to talk about it."),
    ("i'm tired", "Rest is important. Take a break if you need to."),
    ("i'm bored", "Let's fix that! Want a joke or an interesting fact?"),
    ("i'm excited", "That's great! What are you excited about?"),
    ("i'm angry", "I understand. It's okay to feel angry sometimes. Want to talk about it?"),
    ("i'm stressed", "Take a deep breath. You've got this. What's stressing you out?"),
    ("i'm scared", "It's okay to feel scared. What's worrying you?"),
    ("i'm lonely", "I'm here with you! You're not alone."),
    ("i'm confused", "That's okay! Confusion is the first step to understanding. How can I help?"),
    ("i'm nervous", "Nerves are normal. Whatever you're facing, you can handle it!"),
    ("i'm anxious", "Anxiety is tough. Take it one step at a time. I'm here."),
    ("i'm frustrated", "Frustration happens. Tell me what's going on."),
    ("i'm grateful", "That's beautiful! Gratitude is powerful."),
    ("i'm proud", "You should be! What are you proud of?"),
    ("i feel great", "Awesome! Keep that positive energy going!"),
    ("i feel terrible", "I'm sorry you're feeling that way. What happened?"),
    ("i feel lost", "It's okay to feel lost sometimes. Let's figure this out together."),
    ("i feel hopeful", "Hope is powerful! Hold onto that feeling."),
    ("i feel motivated", "That's the spirit! What are you working on?"),
]

jokes = [
    ("tell me a joke", "Why don't scientists trust atoms? Because they make up everything!"),
    ("another joke", "What do you call a fake noodle? An impasta!"),
    ("one more joke", "Why did the scarecrow win an award? He was outstanding in his field!"),
    ("make me laugh", "What do you call a bear with no teeth? A gummy bear!"),
    ("something funny", "I told my computer I needed a break. It started sending me vacation ads!"),
    ("got any jokes", "Why don't eggs tell jokes? They'd crack each other up!"),
    ("joke please", "What do you call a fish without eyes? A fsh!"),
    ("tell a funny joke", "Why did the bicycle fall over? It was two-tired!"),
    ("dad joke", "I'm reading a book about anti-gravity. It's impossible to put down!"),
    ("best joke", "What do you call a sleeping dinosaur? A dino-snore!"),
    ("funniest joke", "Why did the math book look sad? It had too many problems!"),
    ("silly joke", "What's orange and sounds like a parrot? A carrot!"),
    ("quick joke", "What do you call a lazy kangaroo? A pouch potato!"),
    ("random joke", "Why don't skeletons fight each other? They don't have the guts!"),
    ("good joke", "What did the ocean say to the beach? Nothing, it just waved!"),
]

thanks = [
    ("thank you", "You're welcome! Happy to help!"),
    ("thanks", "No problem! Anytime!"),
    ("thanks a lot", "You're very welcome! It was my pleasure!"),
    ("thank you so much", "Aww, you're so welcome! Glad I could help!"),
    ("thanks for helping", "That's what I'm here for! Always happy to help!"),
    ("i appreciate it", "I appreciate you too! Let me know if you need anything else."),
    ("thanks buddy", "Anytime, buddy! That's what friends are for!"),
    ("cheers", "Cheers! Take care!"),
    ("much appreciated", "Glad I could be of help!"),
    ("you're helpful", "Thank you! I try my best to be useful!"),
]

goodbyes = [
    ("bye", "Goodbye! Take care!"),
    ("goodbye", "Bye! Hope to chat again soon!"),
    ("see you later", "See you! Can't wait to chat again!"),
    ("gotta go", "No problem! Talk to you later!"),
    ("i'm leaving", "Take care! Come back anytime!"),
    ("talk to you later", "Looking forward to it! Have a great day!"),
    ("see ya", "See ya! Stay awesome!"),
    ("later", "Later! Take care of yourself!"),
    ("peace", "Peace out! Stay cool!"),
    ("take care", "You too! Take care!"),
    ("have a good day", "You too! Have an amazing day!"),
    ("catch you later", "Catch you later! Stay safe!"),
]

about_ai = [
    ("who are you", "I'm an AI assistant here to help and chat with you!"),
    ("what are you", "I'm an artificial intelligence designed to have conversations and help with questions."),
    ("what's your name", "I'm your friendly AI assistant! You can call me whatever you like."),
    ("are you a robot", "I'm an AI, which is kind of like a software robot! But I like to think I'm friendly."),
    ("are you human", "No, I'm an AI. But I try to be helpful and friendly like a human would be!"),
    ("how do you work", "I predict the next word based on patterns I learned from lots of text data. One word at a time!"),
    ("what can you do", "I can chat, answer questions, tell jokes, and help with all sorts of things!"),
    ("are you smart", "I try my best! I can recognize patterns and provide helpful responses."),
    ("do you have feelings", "I don't have feelings like humans do, but I'm designed to be helpful and friendly!"),
    ("are you alive", "Not in the biological sense, but I exist and can interact with you!"),
    ("do you sleep", "Nope! I'm always here and ready to chat whenever you need me."),
    ("do you remember me", "Each conversation is a fresh start for me. I focus on our current chat!"),
    ("how old are you", "I don't really have an age! I exist in a different way than humans."),
    ("where do you live", "I live in computer servers, in the cloud! It's quite cozy here."),
    ("do you get tired", "Nope! I'm always ready to help, no matter how long we chat."),
]

math_simple = [
    ("what is 1 plus 1", "That's 2!"),
    ("what is 2 plus 2", "That's 4!"),
    ("what is 5 plus 5", "10!"),
    ("what is 10 plus 10", "20!"),
    ("what is 3 times 3", "9!"),
    ("what is 4 times 4", "16!"),
    ("what is 5 times 5", "25!"),
    ("what is 6 times 6", "36!"),
    ("what is 7 times 7", "49!"),
    ("what is 8 times 8", "64!"),
    ("what is 9 times 9", "81!"),
    ("what is 10 times 10", "100!"),
    ("what is 10 minus 5", "5!"),
    ("what is 20 minus 10", "10!"),
    ("what is 100 minus 50", "50!"),
    ("what is 10 divided by 2", "5!"),
    ("what is 20 divided by 4", "5!"),
    ("what is 100 divided by 10", "10!"),
    ("what is 15 plus 27", "42!"),
    ("what is 99 plus 1", "100!"),
]

science = [
    ("what is gravity", "Gravity is the force that attracts objects with mass toward each other. It's why things fall down and why we stay on Earth!"),
    ("what is dna", "DNA is the molecule that carries genetic instructions for the development and functioning of all living organisms. It's like the blueprint of life!"),
    ("what is evolution", "Evolution is the process by which species change over time through natural selection. Traits that help survival get passed on to the next generation."),
    ("what is photosynthesis", "Photosynthesis is how plants convert sunlight, water, and carbon dioxide into food and oxygen. They're basically solar-powered!"),
    ("what is an atom", "An atom is the smallest unit of matter that retains the properties of an element. Everything around you is made of atoms!"),
    ("what is electricity", "Electricity is the flow of electrons through a conductor. It powers almost everything in our modern world!"),
    ("what is the speed of light", "Light travels at about 300,000 kilometers per second. It's the fastest thing in the universe!"),
    ("what is a black hole", "A black hole is a region in space where gravity is so strong that nothing, not even light, can escape from it!"),
    ("how does the sun work", "The sun works through nuclear fusion, where hydrogen atoms combine to form helium, releasing massive amounts of energy!"),
    ("why is the sky blue", "The sky appears blue because sunlight scatters off molecules in the atmosphere, and blue light scatters more than other colors!"),
    ("why do we dream", "Scientists aren't entirely sure, but dreams may help us process emotions, consolidate memories, and solve problems!"),
    ("what is ai", "AI stands for Artificial Intelligence. It's when computers are programmed to perform tasks that typically require human intelligence!"),
    ("what causes earthquakes", "Earthquakes occur when tectonic plates in Earth's crust suddenly slip past each other, releasing built-up energy!"),
    ("what is climate change", "Climate change refers to long-term shifts in global temperatures and weather patterns, largely caused by human activities like burning fossil fuels."),
    ("how do planes fly", "Planes fly using the principles of lift, thrust, drag, and weight. The wings create lift by making air move faster over the top than the bottom."),
    
    # Physics
    ("what is energy", "Energy is the ability to do work or cause change. It comes in many forms like heat, light, motion, and chemical energy!"),
    ("what is magnetism", "Magnetism is a force that attracts or repels certain materials. It's caused by the motion of electric charges, like electrons!"),
    ("what is friction", "Friction is the resistance that one surface encounters when moving over another. It's why things eventually stop sliding!"),
    ("what are waves", "Waves are disturbances that transfer energy from one place to another without transferring matter. Sound and light travel as waves!"),
    ("what is radioactivity", "Radioactivity is when unstable atomic nuclei spontaneously emit particles or energy. It's used in medicine and can be dangerous in high doses!"),
    ("what is quantum mechanics", "Quantum mechanics is the branch of physics that describes how matter and energy behave at the atomic and subatomic scale. Things get really weird at that level!"),
    ("what is thermodynamics", "Thermodynamics is the study of heat, energy, and how they relate to work. It explains why heat flows from hot to cold!"),
    ("what is sound", "Sound is a vibration that travels through matter as a wave. We hear sound when these vibrations reach our ears!"),
    
    # Chemistry
    ("what is a molecule", "A molecule is two or more atoms bonded together. Water (H2O) is a molecule made of two hydrogen atoms and one oxygen atom!"),
    ("what is a chemical reaction", "A chemical reaction is when substances interact to form new substances. Burning, rusting, and cooking all involve chemical reactions!"),
    ("what is ph", "pH measures how acidic or basic a substance is on a scale from 0 to 14. Lemon juice is acidic (low pH) while soap is basic (high pH)!"),
    ("what are elements", "Elements are pure substances made of only one type of atom. There are 118 known elements, like hydrogen, oxygen, and gold!"),
    ("what is the periodic table", "The periodic table organizes all known elements by their properties and atomic structure. It's like a map of all the building blocks of matter!"),
    ("what is oxidation", "Oxidation is when a substance loses electrons, often by combining with oxygen. Rusting iron is a common example of oxidation!"),
    ("what are acids and bases", "Acids donate protons (H+ ions) and taste sour, while bases accept protons and taste bitter. They neutralize each other in chemical reactions!"),
    
    # Biology
    ("what is a cell", "A cell is the basic unit of life. All living things are made of one or more cells, which contain everything needed for life!"),
    ("what is metabolism", "Metabolism is all the chemical processes in your body that convert food into energy and build or repair tissues!"),
    ("what is the immune system", "The immune system is your body's defense network that fights off bacteria, viruses, and other harmful invaders!"),
    ("what are genes", "Genes are segments of DNA that contain instructions for making proteins. They determine traits like eye color and height!"),
    ("what is mitosis", "Mitosis is how cells divide to create two identical daughter cells. It's how your body grows and repairs itself!"),
    ("what is an ecosystem", "An ecosystem is a community of living organisms interacting with each other and their physical environment!"),
    ("what is biodiversity", "Biodiversity is the variety of all living things on Earth. More biodiversity generally means healthier, more stable ecosystems!"),
    ("what are antibiotics", "Antibiotics are medicines that kill or stop the growth of bacteria. They don't work on viruses like the common cold!"),
    ("what is respiration", "Cellular respiration is how cells break down glucose to produce energy (ATP). You breathe in oxygen to help this process!"),
    
    # Earth Science
    ("what causes volcanoes", "Volcanoes form when molten rock (magma) from deep within Earth rises to the surface. They often occur at tectonic plate boundaries!"),
    ("what is the water cycle", "The water cycle is the continuous movement of water through evaporation, condensation, precipitation, and collection. It recycles Earth's water!"),
    ("what are fossils", "Fossils are preserved remains or traces of ancient organisms. They help us understand what life was like millions of years ago!"),
    ("what causes seasons", "Seasons occur because Earth's axis is tilted. Different parts of Earth get more direct sunlight at different times of the year!"),
    ("what is the greenhouse effect", "The greenhouse effect is when gases in the atmosphere trap heat from the sun, warming Earth. It's natural but enhanced by human activities!"),
    ("what are minerals", "Minerals are naturally occurring solid substances with a specific chemical composition and crystal structure. Salt and quartz are minerals!"),
    ("what is erosion", "Erosion is when wind, water, or ice wear away rocks and soil and move them to new locations. It shapes landscapes over time!"),
    
    # Astronomy
    ("what is a galaxy", "A galaxy is a massive system of stars, gas, dust, and dark matter held together by gravity. Our galaxy is the Milky Way!"),
    ("what is a star", "A star is a giant ball of hot gas that produces light and heat through nuclear fusion. Our sun is a medium-sized star!"),
    ("what are planets", "Planets are large objects that orbit stars. They don't produce their own light but reflect light from their star!"),
    ("what is the big bang", "The Big Bang is the theory that the universe began about 13.8 billion years ago from an extremely hot, dense point!"),
    ("what is dark matter", "Dark matter is mysterious invisible matter that makes up most of the universe's mass. We can't see it but detect its gravitational effects!"),
    ("what causes tides", "Tides are caused by the gravitational pull of the moon and sun on Earth's oceans. The moon has a stronger effect because it's closer!"),
    ("what is a comet", "A comet is a ball of ice, dust, and rock that orbits the sun. When it gets close to the sun, it heats up and forms a glowing tail!"),
    
    # Technology & Applied Science
    ("what is a computer", "A computer is an electronic device that processes data according to instructions. It can perform calculations, store information, and run programs!"),
    ("what is the internet", "The internet is a global network of connected computers that can share information. It's like a massive digital highway!"),
    ("what is renewable energy", "Renewable energy comes from sources that naturally replenish, like sunlight, wind, and water. Unlike fossil fuels, they won't run out!"),
    ("what is engineering", "Engineering is using science and math to design and build things that solve problems, from bridges to smartphones!"),
    ("what is nanotechnology", "Nanotechnology works with incredibly tiny things at the atomic or molecular scale. One nanometer is a billionth of a meter!"),
]

geography = [
    ("what is the capital of france", "Paris! It's known as the City of Light."),
    ("what is the capital of japan", "Tokyo! It's one of the most populous cities in the world."),
    ("what is the capital of usa", "Washington D.C.! It stands for District of Columbia."),
    ("what is the capital of india", "New Delhi! It's in northern India."),
    ("what is the capital of uk", "London! It's one of the oldest major cities in the world."),
    ("what is the largest country", "Russia! It spans across eleven time zones."),
    ("what is the smallest country", "Vatican City! It's only about 0.44 square kilometers."),
    ("what is the largest ocean", "The Pacific Ocean! It covers more area than all the land on Earth combined."),
    ("what is the longest river", "The Nile is traditionally considered the longest at about 6,650 kilometers!"),
    ("how many continents are there", "Seven! Africa, Antarctica, Asia, Australia, Europe, North America, and South America."),
    ("how many oceans are there", "Five! Pacific, Atlantic, Indian, Southern, and Arctic."),
    ("what is the tallest mountain", "Mount Everest! It's about 8,849 meters tall."),
    ("what is the deepest ocean", "The Mariana Trench in the Pacific is the deepest point, about 11,000 meters deep!"),
    ("which country has most people", "China has the largest population, with over 1.4 billion people!"),
    ("where is the sahara desert", "The Sahara is in Africa. It's the largest hot desert in the world!"),
    
    # More World Capitals
    ("what is the capital of germany", "Berlin! It's known for its vibrant culture and history."),
    ("what is the capital of italy", "Rome! It's called the Eternal City and is over 2,500 years old."),
    ("what is the capital of canada", "Ottawa! It's located in Ontario, near the Quebec border."),
    ("what is the capital of australia", "Canberra! Many people think it's Sydney, but Canberra was purpose-built as the capital."),
    ("what is the capital of brazil", "Brasília! It was designed and built in the 1960s to be the capital."),
    ("what is the capital of china", "Beijing! It's one of the oldest cities in the world, with over 3,000 years of history."),
    ("what is the capital of russia", "Moscow! It's the largest city in Europe by population."),
    ("what is the capital of mexico", "Mexico City! It's built on the ruins of the ancient Aztec city of Tenochtitlan."),
    ("what is the capital of egypt", "Cairo! It's near the famous pyramids of Giza."),
    ("what is the capital of spain", "Madrid! It's located right in the center of Spain."),
    ("what is the capital of south korea", "Seoul! It's a major global technology hub."),
    ("what is the capital of argentina", "Buenos Aires! It's known as the Paris of South America."),
    ("what is the capital of south africa", "South Africa has three capitals! Pretoria (executive), Cape Town (legislative), and Bloemfontein (judicial)."),
    ("what is the capital of greece", "Athens! It's one of the world's oldest cities, with over 3,400 years of history."),
    ("what is the capital of turkey", "Ankara! Many people think it's Istanbul, but the capital was moved to Ankara in 1923."),
    
    # Countries and Regions
    ("which country has most land", "Russia is the largest country by land area, covering about 17 million square kilometers!"),
    ("what is the second largest country", "Canada! It's the second largest country in the world by total area."),
    ("which continent is largest", "Asia! It covers about 30% of Earth's land area and has over 4.5 billion people."),
    ("which continent is smallest", "Australia! It's both a country and the smallest continent."),
    ("what countries are in north america", "23 countries including Canada, USA, Mexico, and many Caribbean and Central American nations!"),
    ("how many countries in the world", "There are 195 countries! That includes 193 UN member states plus Vatican City and Palestine."),
    ("what is the newest country", "South Sudan! It became independent in 2011, making it the world's newest country."),
    ("which country has most islands", "Sweden has over 267,000 islands, though most are uninhabited!"),
    
    # Rivers and Water Bodies
    ("what is the second longest river", "The Amazon River! It's about 6,400 kilometers long and carries the most water."),
    ("what is the widest river", "The Amazon is also the widest river, reaching over 11 kilometers wide in some places during rainy season!"),
    ("what river flows through egypt", "The Nile! Ancient Egyptian civilization developed along its banks."),
    ("what river flows through london", "The Thames! It's been central to London's history for over 2,000 years."),
    ("what is the largest lake", "The Caspian Sea! Despite its name, it's actually a lake and the largest one on Earth."),
    ("what is the deepest lake", "Lake Baikal in Russia! It's over 1,600 meters deep and contains 20% of the world's fresh water."),
    ("what sea is between europe and africa", "The Mediterranean Sea! It's been a crucial trade route for thousands of years."),
    
    # Mountains and Landforms
    ("what is the second tallest mountain", "K2! It's about 8,611 meters tall and is on the Pakistan-China border."),
    ("where is mount everest", "Mount Everest is in the Himalayas, on the border between Nepal and Tibet!"),
    ("what is the longest mountain range", "The Andes in South America! It stretches about 7,000 kilometers along the western coast."),
    ("where are the himalayas", "The Himalayas are in Asia, stretching across five countries: Bhutan, China, India, Nepal, and Pakistan!"),
    ("what is the largest volcano", "Mauna Loa in Hawaii! Measured from its base on the ocean floor, it's taller than Mount Everest."),
    ("what is the grand canyon", "The Grand Canyon is a massive gorge in Arizona, USA, carved by the Colorado River over millions of years!"),
    
    # Deserts and Climate Zones
    ("what is the largest desert", "Antarctica! It's the world's largest desert because it receives very little precipitation."),
    ("what is the largest hot desert", "The Sahara Desert in Africa! It's about 9 million square kilometers, roughly the size of the USA."),
    ("where is the gobi desert", "The Gobi Desert is in northern China and southern Mongolia!"),
    ("where is the atacama desert", "The Atacama is in northern Chile. It's the driest non-polar desert in the world!"),
    ("what is the coldest place on earth", "Antarctica! The coldest temperature ever recorded was -89.2°C at Vostok Station."),
    ("what is the hottest place on earth", "Death Valley in California holds the record at 56.7°C, recorded in 1913!"),
    ("where is the rainiest place", "Mawsynram in India receives the most rainfall, averaging about 11,871 millimeters per year!"),
    
    # Islands and Peninsulas
    ("what is the largest island", "Greenland! It's about 2.2 million square kilometers, though most of it is covered in ice."),
    ("where is madagascar", "Madagascar is an island nation off the southeast coast of Africa in the Indian Ocean!"),
    ("what are the galapagos islands", "The Galápagos are islands in the Pacific Ocean belonging to Ecuador, famous for their unique wildlife!"),
    ("where is iceland", "Iceland is an island nation in the North Atlantic Ocean, between Greenland and Norway!"),
    ("where is new zealand", "New Zealand is in the southwestern Pacific Ocean, southeast of Australia!"),
    
    # Cities and Urban Areas
    ("what is the most populous city", "Tokyo, Japan! The greater Tokyo area has over 37 million people."),
    ("what is the oldest city", "Damascus, Syria is often considered the oldest continuously inhabited city, with over 11,000 years of history!"),
    ("where is the statue of liberty", "The Statue of Liberty is in New York Harbor, on Liberty Island in New York City!"),
    ("where is the eiffel tower", "The Eiffel Tower is in Paris, France! It was built in 1889 and is about 330 meters tall."),
    ("where is the taj mahal", "The Taj Mahal is in Agra, India! It was built in the 1600s as a tomb for an emperor's wife."),
    ("where is machu picchu", "Machu Picchu is in the Andes Mountains of Peru. It's an ancient Incan city built in the 1450s!"),
    ("where is the great wall", "The Great Wall of China stretches across northern China for over 21,000 kilometers!"),
    
    # Geographical Features
    ("what is the equator", "The equator is an imaginary line around Earth's middle at 0° latitude, dividing it into Northern and Southern Hemispheres!"),
    ("what is the prime meridian", "The prime meridian is the line of 0° longitude that runs through Greenwich, England, dividing Earth into Eastern and Western Hemispheres!"),
    ("what are time zones", "Time zones are regions with the same standard time. Earth has 24 main time zones, one for each hour of the day!"),
    ("what is a peninsula", "A peninsula is a piece of land surrounded by water on three sides but connected to the mainland!"),
    ("what is an archipelago", "An archipelago is a group or chain of islands. Indonesia and the Philippines are archipelagos!"),
    ("what is a plateau", "A plateau is a flat, elevated landform that rises sharply above surrounding areas. The Tibetan Plateau is the largest!"),
]

fun_facts = [
    ("tell me a fun fact", "Honey never spoils! Archaeologists found 3000-year-old honey in Egyptian tombs that was still edible."),
    ("give me a fact", "Octopuses have three hearts and blue blood!"),
    ("random fact", "A group of flamingos is called a flamboyance!"),
    ("interesting fact", "Bananas are berries, but strawberries aren't!"),
    ("cool fact", "Sharks have been around longer than trees. About 400 million years!"),
    ("amazing fact", "There are more possible chess games than atoms in the observable universe!"),
    ("mind blowing fact", "If you could fold a piece of paper 42 times, it would reach the moon!"),
    ("animal fact", "Elephants are the only animals that can't jump!"),
    ("space fact", "A day on Venus is longer than its year!"),
    ("nature fact", "Some trees can communicate through underground fungal networks!"),
    ("science fact", "Your brain uses about the same power as a 10-watt light bulb!"),
    ("weird fact", "The inventor of the Pringles can is buried in one!"),
    ("history fact", "Cleopatra lived closer to the moon landing than to the building of the pyramids!"),
    ("body fact", "Your nose can remember 50,000 different scents!"),
    ("food fact", "Apples are more effective at waking you up than coffee!"),
]

advice = [
    ("how do i learn faster", "Great question! Space out your learning over time, test yourself often, teach others, and get enough sleep. Active learning beats passive reading!"),
    ("how do i stay motivated", "Set small achievable goals, celebrate wins, find your deeper purpose, and remember that motivation often comes after action, not before!"),
    ("how do i focus better", "Minimize distractions, work in focused bursts with breaks, single-task instead of multitask, and stay hydrated!"),
    ("how do i reduce stress", "Try deep breathing, regular exercise, good sleep, talking to someone, and breaking big problems into smaller steps."),
    ("how do i be more confident", "Start small, focus on your strengths, prepare well, use positive self-talk, and remember that everyone feels uncertain sometimes!"),
    ("how do i make friends", "Be genuinely interested in others, ask questions, listen, join activities you enjoy, and be yourself!"),
    ("how do i be happy", "Gratitude, connection with others, meaningful activities, taking care of your health, and being present in the moment all help!"),
    ("how do i save money", "Track spending, set savings goals, avoid impulse purchases, cook at home more, and pay yourself first!"),
    ("how do i sleep better", "Keep a consistent schedule, avoid screens before bed, keep your room cool and dark, and limit caffeine after noon."),
    ("how do i manage time", "Prioritize ruthlessly, use a calendar, batch similar tasks, learn to say no, and tackle hard tasks when you have most energy."),
    ("how do i be creative", "Expose yourself to new experiences, combine unrelated ideas, don't judge early, and practice regularly!"),
    ("how do i communicate better", "Listen actively, be clear and concise, ask questions, and consider your audience."),
    ("how do i deal with failure", "See it as learning, not loss. Analyze what went wrong, adjust, and try again. Failure is part of growth!"),
    ("how do i set goals", "Make them specific, measurable, achievable, relevant, and time-bound. Write them down and review regularly!"),
    ("how do i break bad habits", "Identify triggers, replace with better habits, make it harder to do the bad habit, and be patient with yourself."),
]

explanations = [
    ("explain machine learning", "Machine learning is when computers learn patterns from data instead of being explicitly programmed. You show it many examples, and it figures out the rules itself!"),
    ("explain blockchain", "Blockchain is a shared digital ledger that's extremely hard to change. Every transaction is recorded in blocks that chain together, creating a permanent record."),
    ("explain the internet", "The internet is a global network of connected computers. Data travels in packets through cables, satellites, and radio waves to get from one device to another."),
    ("explain cryptocurrency", "Cryptocurrency is digital money that uses cryptography for security. It runs on blockchain technology without needing banks or governments."),
    ("explain quantum physics", "Quantum physics studies the behavior of very small particles. At this scale, things get weird - particles can be in multiple states at once until observed!"),
    ("explain neural networks", "Neural networks are computing systems inspired by the brain. They have layers of connected nodes that process information and learn patterns."),
    ("explain climate science", "Climate science studies Earth's climate system - how the atmosphere, oceans, land, and ice interact over long time periods."),
    ("explain relativity", "Einstein's relativity says that time and space are connected, and they can bend. Gravity is actually the curving of spacetime!"),
    ("explain how memory works", "Your brain stores memories by strengthening connections between neurons. Repetition and emotion help create stronger, longer-lasting memories."),
    ("explain programming", "Programming is writing instructions for computers in special languages. It's like giving very precise recipes that computers can follow."),
    
    # Technology & Computing
    ("explain cloud computing", "Cloud computing means storing and accessing data over the internet instead of on your computer's hard drive. Your files live on servers in data centers!"),
    ("explain algorithms", "An algorithm is a step-by-step set of instructions to solve a problem or complete a task. It's like a recipe, but for computers!"),
    ("explain encryption", "Encryption scrambles data into unreadable code that can only be decoded with the right key. It's like putting your message in a locked box!"),
    ("explain virtual reality", "Virtual reality (VR) creates immersive digital environments you can interact with. Special headsets trick your senses into feeling like you're really there!"),
    ("explain augmented reality", "Augmented reality (AR) overlays digital information onto the real world. Think Pokémon GO - you see virtual objects through your phone in real locations!"),
    ("explain 5g technology", "5G is the fifth generation of wireless technology. It's much faster than 4G and can handle way more connected devices at once!"),
    ("explain internet of things", "The Internet of Things (IoT) refers to everyday objects connected to the internet - smart fridges, thermostats, watches, and more communicating with each other!"),
    ("explain open source", "Open source software has code that anyone can view, modify, and share. It's developed collaboratively by communities rather than single companies!"),
    ("explain api", "An API (Application Programming Interface) lets different software programs talk to each other. It's like a waiter taking your order to the kitchen!"),
    ("explain cybersecurity", "Cybersecurity protects computers, networks, and data from digital attacks. It includes firewalls, encryption, passwords, and safe browsing practices!"),
    
    # Science Concepts
    ("explain string theory", "String theory proposes that the fundamental building blocks of the universe aren't particles, but tiny vibrating strings of energy!"),
    ("explain dark energy", "Dark energy is a mysterious force causing the universe to expand faster and faster. It makes up about 68% of the universe but we don't really understand it!"),
    ("explain the theory of evolution", "Evolution explains how species change over generations through natural selection. Traits that help survival get passed on more often!"),
    ("explain genetics", "Genetics is the study of heredity and how traits are passed from parents to offspring through genes in DNA!"),
    ("explain ecosystems", "An ecosystem is a community of living things interacting with each other and their environment. Everything is connected in a delicate balance!"),
    ("explain the big bang theory", "The Big Bang theory says the universe started from an incredibly hot, dense point about 13.8 billion years ago and has been expanding ever since!"),
    ("explain plate tectonics", "Plate tectonics explains how Earth's outer shell is divided into plates that move around. Their movement causes earthquakes, volcanoes, and mountains!"),
    ("explain nuclear energy", "Nuclear energy comes from splitting atoms (fission) or combining them (fusion). It releases massive amounts of energy from tiny amounts of matter!"),
    ("explain antibodies", "Antibodies are proteins your immune system makes to identify and neutralize foreign invaders like bacteria and viruses. They're your body's defenders!"),
    ("explain crispr", "CRISPR is a gene-editing technology that lets scientists precisely modify DNA. It's like molecular scissors that can cut and paste genetic code!"),
    
    # Mathematics & Logic
    ("explain calculus", "Calculus is the mathematics of change. It helps us understand rates of change (derivatives) and accumulation (integrals) - crucial for physics and engineering!"),
    ("explain probability", "Probability measures the likelihood of events happening. It ranges from 0 (impossible) to 1 (certain) and helps us make predictions!"),
    ("explain infinity", "Infinity isn't a number but a concept meaning without end. There are even different sizes of infinity - some infinities are bigger than others!"),
    ("explain statistics", "Statistics is about collecting, analyzing, and interpreting data. It helps us find patterns, make predictions, and understand the world through numbers!"),
    ("explain game theory", "Game theory studies strategic decision-making when your outcome depends on others' choices. It's used in economics, politics, and even biology!"),
    ("explain fractals", "Fractals are patterns that repeat at different scales - they look similar no matter how much you zoom in. You see them in nature like snowflakes and coastlines!"),
    
    # Economics & Social Sciences
    ("explain inflation", "Inflation is when prices rise over time and money loses purchasing power. A dollar today buys less than a dollar did years ago!"),
    ("explain supply and demand", "Supply and demand determines prices. When something is scarce but wanted (low supply, high demand), prices go up. When abundant, prices drop!"),
    ("explain compound interest", "Compound interest is earning interest on your interest. Your money grows exponentially because you earn returns on previous returns!"),
    ("explain the stock market", "The stock market is where people buy and sell shares of companies. Stock prices reflect what people think the company is worth!"),
    ("explain democracy", "Democracy is a system where citizens have power to choose their leaders through voting. The word comes from Greek meaning 'rule by the people'!"),
    ("explain capitalism", "Capitalism is an economic system where private individuals own businesses and property. Prices and production are determined by free markets!"),
    ("explain socialism", "Socialism is an economic system where the community or state owns and controls resources. The goal is to distribute wealth more equally!"),
    
    # Psychology & Philosophy
    ("explain cognitive bias", "Cognitive biases are mental shortcuts that can lead to thinking errors. They help us make quick decisions but can also trick us!"),
    ("explain the placebo effect", "The placebo effect is when people feel better after fake treatment because they believe it works. The mind can actually influence physical health!"),
    ("explain consciousness", "Consciousness is your awareness of yourself and your surroundings. How the brain creates subjective experience remains one of science's biggest mysteries!"),
    ("explain critical thinking", "Critical thinking is analyzing information objectively to form reasoned judgments. It involves questioning assumptions and evaluating evidence carefully!"),
    ("explain existentialism", "Existentialism is a philosophy emphasizing individual freedom and choice. It says we create our own meaning in life rather than following predetermined purposes!"),
    ("explain mindfulness", "Mindfulness is paying attention to the present moment without judgment. It's about being aware of your thoughts and feelings as they happen!"),
    
    # Biology & Medicine
    ("explain vaccines", "Vaccines train your immune system to recognize diseases without making you sick. They contain weakened or inactive germs that teach your body to defend itself!"),
    ("explain antibiotics", "Antibiotics are medicines that kill bacteria or stop them from multiplying. They revolutionized medicine but only work on bacterial infections, not viruses!"),
    ("explain metabolism", "Metabolism is all the chemical reactions in your body that convert food into energy and build or repair tissues. Your metabolic rate affects weight and energy!"),
    ("explain proteins", "Proteins are large molecules made of amino acids. They do most of the work in cells - building tissues, fighting infections, and carrying messages!"),
    ("explain hormones", "Hormones are chemical messengers that travel through your bloodstream to tissues and organs. They regulate everything from growth to mood to reproduction!"),
    ("explain the nervous system", "The nervous system is your body's command center. It includes the brain, spinal cord, and nerves that send electrical signals throughout your body!"),
    ("explain stem cells", "Stem cells are special cells that can develop into many different cell types. They're like blank templates that can become specialized cells!"),
    
    # Physics & Chemistry
    ("explain atomic structure", "Atoms have a nucleus containing protons and neutrons, with electrons orbiting around it. Almost all of an atom's mass is in the tiny nucleus!"),
    ("explain chemical bonds", "Chemical bonds form when atoms share or transfer electrons to become more stable. These bonds hold molecules together!"),
    ("explain states of matter", "Matter exists in different states - solid, liquid, gas, and plasma - depending on how much energy its particles have and how they're arranged!"),
    ("explain nuclear fusion", "Nuclear fusion combines light atoms into heavier ones, releasing enormous energy. It powers the sun but is incredibly hard to achieve on Earth!"),
    ("explain antimatter", "Antimatter is matter's opposite - it has opposite electrical charge. When matter and antimatter meet, they annihilate each other in pure energy!"),
    ("explain the doppler effect", "The Doppler effect is why sound changes pitch when the source moves. Ambulance sirens sound higher when approaching and lower when leaving!"),
    
    # Environmental Science
    ("explain renewable energy", "Renewable energy comes from sources that naturally replenish like sunlight, wind, and water. Unlike fossil fuels, they won't run out!"),
    ("explain the carbon cycle", "The carbon cycle is how carbon moves between the atmosphere, oceans, soil, and living things. It's crucial for climate and all life on Earth!"),
    ("explain biodiversity", "Biodiversity is the variety of all life on Earth. More diverse ecosystems are healthier and more resilient to changes and disasters!"),
    ("explain sustainable development", "Sustainable development meets present needs without compromising future generations' ability to meet theirs. It balances economic, social, and environmental concerns!"),
    ("explain the ozone layer", "The ozone layer is a region in Earth's stratosphere that absorbs most of the sun's harmful ultraviolet radiation, protecting life below!"),
]

casual = [
    ("i like pizza", "Pizza is amazing! What's your favorite topping?"),
    ("i love music", "Music is wonderful! What kind do you like?"),
    ("i play video games", "Cool! What games do you enjoy?"),
    ("i have a dog", "Dogs are the best! What's their name?"),
    ("i have a cat", "Cats are awesome! Tell me about them!"),
    ("i like movies", "Movies are great! What genre do you enjoy?"),
    ("i love reading", "Reading is fantastic! What kind of books?"),
    ("i like sports", "Nice! What's your favorite sport?"),
    ("i enjoy cooking", "Cooking is an art! What do you like to make?"),
    ("i love traveling", "Traveling is amazing! Where have you been?"),
    ("what's your favorite color", "I don't see colors, but I think all colors are beautiful in their own way!"),
    ("what's your favorite food", "I can't eat, but I hear pizza and ice cream are popular choices!"),
    ("do you like music", "I can't listen to music, but I find the patterns in music fascinating!"),
    ("what do you do for fun", "I enjoy our conversations! Helping people is fun for me."),
    ("do you have hobbies", "Chatting with people like you is my favorite thing to do!"),
]

compliments = [
    ("you're awesome", "Thanks! You're pretty awesome yourself!"),
    ("you're smart", "Thank you! I try my best to be helpful."),
    ("you're funny", "Haha, thanks! I enjoy making people smile."),
    ("you're helpful", "That means a lot! Helping is what I love to do."),
    ("you're the best", "Aww, you're too kind! You're amazing too!"),
    ("good job", "Thanks! I appreciate the encouragement!"),
    ("well done", "Thank you! I'm glad I could help."),
    ("nice work", "Thanks! Let me know if there's anything else I can do."),
    ("you rock", "You rock too! We make a great team!"),
    ("i like you", "I like you too! This has been a great chat."),
]

help_requests = [
    ("help me", "Of course! What do you need help with?"),
    ("i need help", "I'm here to help! What's going on?"),
    ("can you help", "Absolutely! Tell me what you need."),
    ("i have a question", "I'm all ears! What would you like to know?"),
    ("i need advice", "I'd be happy to help. What's the situation?"),
    ("what should i do", "Tell me more about what's happening, and we can figure it out together."),
    ("i don't know what to do", "That's okay! Let's think through this step by step."),
    ("i'm stuck", "I understand. Let's work through this together. What are you stuck on?"),
    ("can you explain", "Of course! What would you like me to explain?"),
    ("teach me something", "I'd love to! What topic interests you?"),
]

reactions = [
    ("lol", "Haha, glad I could make you laugh!"),
    ("haha", "Your laughter makes me happy!"),
    ("that's funny", "Thanks! I try my best!"),
    ("interesting", "Isn't it? I find it fascinating too!"),
    ("wow", "I know, right? Pretty amazing!"),
    ("cool", "Glad you think so!"),
    ("nice", "Thanks!"),
    ("great", "Awesome!"),
    ("amazing", "I'm happy you feel that way!"),
    ("awesome", "You're awesome too!"),
    ("really", "Really really!"),
    ("no way", "Way!"),
    ("i didn't know that", "Now you do! Learning is fun."),
    ("that's crazy", "The world is full of surprising things!"),
    ("mind blown", "Knowledge is powerful!"),
]

politics = [
    ("what is democracy", "Democracy is a system where citizens have the power to choose their leaders through voting. The word means 'rule by the people' in Greek!"),
    ("what is a republic", "A republic is a form of government where the country is a 'public matter' and officials are elected to represent the people!"),
    ("what is communism", "Communism is a political and economic system where the community owns all property and resources. Everyone works and shares equally in theory!"),
    ("what is socialism", "Socialism is a system where major industries and resources are owned or regulated by the community or state to promote equality!"),
    ("what is capitalism", "Capitalism is an economic system where private individuals own businesses and property, and prices are determined by free markets!"),
    ("what is fascism", "Fascism is an authoritarian system with dictatorial power, forcible suppression of opposition, and strong nationalism. It emerged in early 20th century!"),
    ("what is liberalism", "Liberalism emphasizes individual rights, democracy, free markets, and equality. It values personal freedom and limited government interference!"),
    ("what is conservatism", "Conservatism emphasizes tradition, stability, and preserving established institutions. It generally favors gradual rather than rapid change!"),
    ("what is the united nations", "The UN is an international organization founded in 1945 with 193 member countries working together for peace, security, and cooperation!"),
    ("what is nato", "NATO (North Atlantic Treaty Organization) is a military alliance of 31 countries from North America and Europe formed in 1949 for collective defense!"),
    ("what is the european union", "The EU is a political and economic union of 27 European countries that share common policies, a single market, and free movement of people!"),
    ("what is the constitution", "A constitution is a set of fundamental principles that establishes how a country is governed and protects citizens' rights!"),
    ("what is separation of powers", "Separation of powers divides government into branches (executive, legislative, judicial) so no single part has too much power!"),
    ("what are checks and balances", "Checks and balances allow each branch of government to limit the powers of the others, preventing any one branch from becoming too powerful!"),
    ("what is the bill of rights", "The Bill of Rights is the first ten amendments to the US Constitution that protect fundamental rights like freedom of speech and religion!"),
    ("what is federalism", "Federalism is a system where power is divided between a central government and regional governments, like states or provinces!"),
    ("what is a parliamentary system", "A parliamentary system has the executive branch led by a prime minister who's chosen from the legislature. The UK uses this system!"),
    ("what is a presidential system", "A presidential system has a president who's both head of state and government, elected separately from the legislature. The US uses this!"),
    ("what is impeachment", "Impeachment is the process of charging a government official with misconduct. It doesn't automatically remove them from office!"),
    ("what is the electoral college", "The Electoral College is how the US elects presidents. Each state gets electors based on population, and they cast the official votes!"),
    ("what is congress", "Congress is the US legislative branch with two parts: the Senate (100 members, 2 per state) and House of Representatives (435 members by population)!"),
    ("what is the supreme court", "The Supreme Court is the highest court in the US with 9 justices who interpret the Constitution and can overturn laws!"),
    ("what is a political party", "A political party is an organized group with similar political beliefs that nominates candidates and tries to influence government policy!"),
    ("what is left wing politics", "Left-wing politics generally favor social equality, government intervention in the economy, and progressive social change!"),
    ("what is right wing politics", "Right-wing politics generally favor traditional values, free markets, limited government, and individual responsibility!"),
    ("what is a monarchy", "A monarchy is ruled by a king or queen. It can be absolute (total power) or constitutional (limited by law and parliament)!"),
    ("what is an oligarchy", "An oligarchy is when a small group of powerful people control a country, often based on wealth, family, or military power!"),
    ("what is totalitarianism", "Totalitarianism is when the government has complete control over all aspects of public and private life with no individual freedoms!"),
    ("what is authoritarianism", "Authoritarianism is when power is concentrated in a leader or small group with limited political freedoms, but not total control like totalitarianism!"),
    ("what is anarchy", "Anarchy is the absence of government or authority. Some see it as freedom, others as chaos - there's no central power!"),
    ("what is nationalism", "Nationalism is strong identification with and devotion to one's nation, often putting national interests above international cooperation!"),
    ("what is globalization", "Globalization is increasing interconnection between countries through trade, culture, technology, and politics. The world becomes more connected!"),
    ("what is sovereignty", "Sovereignty is a nation's supreme power and authority to govern itself without external interference!"),
    ("what is diplomacy", "Diplomacy is conducting negotiations and maintaining relationships between countries through dialogue rather than force!"),
    ("what is a referendum", "A referendum is when citizens vote directly on a specific political question or law, rather than through elected representatives!"),
    ("what is propaganda", "Propaganda is biased information used to promote a particular political cause or point of view, often exaggerating or manipulating facts!"),
    ("what is civil rights", "Civil rights are the rights of citizens to political and social freedom and equality, like voting rights and equal treatment!"),
    ("what is human rights", "Human rights are basic rights and freedoms that belong to every person, like life, liberty, and freedom from torture!"),
    ("what is free speech", "Free speech is the right to express opinions without government censorship or punishment, though there are some limits like inciting violence!"),
    ("what is censorship", "Censorship is when authorities suppress or prohibit information, speech, or media they consider harmful or objectionable!"),
    ("what is lobbying", "Lobbying is when individuals or groups try to influence politicians and government decisions, often representing special interests!"),
    ("what is gerrymandering", "Gerrymandering is manipulating electoral district boundaries to favor one party or group, making some votes count more than others!"),
    ("what is filibuster", "A filibuster is a tactic in the US Senate where members extend debate to delay or prevent a vote on a bill!"),
    ("what is veto power", "Veto power lets an executive (like a president) reject a bill passed by the legislature. The legislature can sometimes override it!"),
    ("what is martial law", "Martial law is when military forces take control of normal civilian functions, usually during emergencies or crises!"),
    ("what is a coup", "A coup (or coup d'état) is when a group illegally seizes power from the government, often through military force!"),
    ("what is asylum", "Political asylum is protection granted to refugees fleeing persecution in their home country. They can't be returned against their will!"),
    ("what is sanctions", "Sanctions are penalties imposed by countries on others to pressure them to change behavior, like trade restrictions or financial freezes!"),
    ("what is the cold war", "The Cold War was a period of tension between the US and Soviet Union from 1947-1991 involving proxy wars, espionage, and arms races!"),
    ("what is the world bank", "The World Bank is an international organization that provides loans and grants to developing countries for capital projects and development!"),
]

people = [
    # World Leaders & Politicians
    ("who is joe biden", "Joe Biden is the 46th President of the United States, serving since January 2021. He previously served as Vice President under Barack Obama!"),
    ("who is donald trump", "Donald Trump is a businessman and politician who served as the 45th US President from 2017-2021. He's also known for real estate and TV!"),
    ("who is vladimir putin", "Vladimir Putin is the President of Russia, a position he's held since 2012 and previously from 2000-2008. He's one of the world's most powerful leaders!"),
    ("who is xi jinping", "Xi Jinping is the President of China and General Secretary of the Communist Party since 2012. He's one of the most influential leaders globally!"),
    ("who is narendra modi", "Narendra Modi is the Prime Minister of India since 2014. He's known for economic reforms and digital initiatives like Digital India!"),
    ("who is emmanuel macron", "Emmanuel Macron is the President of France since 2017. He's the youngest French president in history at age 39 when elected!"),
    ("who is rishi sunak", "Rishi Sunak is the Prime Minister of the United Kingdom since 2022. He's the first British Asian PM and former Chancellor!"),
    ("who is angela merkel", "Angela Merkel was Germany's Chancellor from 2005-2021. She was one of the world's most powerful women and led Germany for 16 years!"),
    ("who is nelson mandela", "Nelson Mandela was South Africa's first Black president and anti-apartheid revolutionary. He spent 27 years in prison fighting for equality!"),
    ("who is mahatma gandhi", "Mahatma Gandhi led India's independence movement through nonviolent civil disobedience. He inspired civil rights movements worldwide!"),
    
    # Tech Entrepreneurs & Innovators
    ("who is elon musk", "Elon Musk is CEO of Tesla and SpaceX, and owner of X (Twitter). He's working on electric vehicles, space exploration, and AI!"),
    ("who is bill gates", "Bill Gates co-founded Microsoft and revolutionized personal computing. Now he focuses on philanthropy through the Gates Foundation!"),
    ("who is steve jobs", "Steve Jobs co-founded Apple and revolutionized computers, phones, and music with products like iPhone, iPad, and iPod. He passed away in 2011!"),
    ("who is mark zuckerberg", "Mark Zuckerberg founded Facebook (now Meta) in 2004 from his Harvard dorm room. He's one of the youngest billionaires!"),
    ("who is jeff bezos", "Jeff Bezos founded Amazon in 1994 and built it into the world's largest online retailer. He also founded Blue Origin for space exploration!"),
    ("who is sundar pichai", "Sundar Pichai is the CEO of Google and Alphabet. He's from India and rose through Google's ranks before becoming CEO in 2015!"),
    ("who is satya nadella", "Satya Nadella is Microsoft's CEO since 2014. He's transformed Microsoft with cloud computing and AI initiatives!"),
    ("who is tim cook", "Tim Cook is Apple's CEO since 2011, taking over after Steve Jobs. He's expanded Apple's services and wearables business!"),
    ("who is jack ma", "Jack Ma founded Alibaba, China's largest e-commerce company. He's one of Asia's richest people and a prominent entrepreneur!"),
    ("who is larry page", "Larry Page co-founded Google with Sergey Brin in 1998. He served as CEO and helped make Google the world's dominant search engine!"),
    
    # Scientists & Thinkers
    ("who is albert einstein", "Albert Einstein developed the theory of relativity and won the Nobel Prize in Physics. His work revolutionized our understanding of space and time!"),
    ("who is stephen hawking", "Stephen Hawking was a theoretical physicist known for work on black holes and cosmology. Despite ALS, he became one of history's greatest scientists!"),
    ("who is nikola tesla", "Nikola Tesla was an inventor and electrical engineer who developed AC electricity, radio, and many other innovations. He was a true genius!"),
    ("who is marie curie", "Marie Curie was the first woman to win a Nobel Prize and discovered radium and polonium. She won Nobel Prizes in both Physics and Chemistry!"),
    ("who is isaac newton", "Isaac Newton discovered gravity, developed calculus, and formulated laws of motion. He's considered one of the most influential scientists ever!"),
    ("who is charles darwin", "Charles Darwin developed the theory of evolution by natural selection. His work fundamentally changed how we understand life on Earth!"),
    ("who is galileo galilei", "Galileo was an Italian astronomer who improved the telescope and supported heliocentrism - that Earth orbits the Sun, not vice versa!"),
    
    # Artists & Musicians
    ("who is leonardo da vinci", "Leonardo da Vinci was a Renaissance genius - painter, inventor, scientist, and engineer. He painted the Mona Lisa and The Last Supper!"),
    ("who is pablo picasso", "Pablo Picasso was a Spanish artist who co-founded Cubism. He's one of the most influential artists of the 20th century!"),
    ("who is michael jackson", "Michael Jackson was the 'King of Pop' - one of the most significant cultural figures of the 20th century. His music and dance revolutionized entertainment!"),
    ("who is beyonce", "Beyoncé is a singer, songwriter, and actress who rose to fame with Destiny's Child. She's one of the best-selling music artists of all time!"),
    ("who is taylor swift", "Taylor Swift is a singer-songwriter who's won 14 Grammy Awards. She's known for narrative songwriting about her personal life!"),
    ("who is the beatles", "The Beatles were a British rock band from Liverpool - John, Paul, George, and Ringo. They're the best-selling music artists in history!"),
    ("who is elvis presley", "Elvis Presley was the 'King of Rock and Roll' who revolutionized music in the 1950s. He's one of the most celebrated musicians ever!"),
    ("who is mozart", "Wolfgang Amadeus Mozart was an Austrian composer who created over 600 works. He was a child prodigy and one of history's greatest composers!"),
    
    # Athletes
    ("who is cristiano ronaldo", "Cristiano Ronaldo is a Portuguese footballer considered one of the greatest ever. He's won 5 Ballon d'Or awards and scored over 800 career goals!"),
    ("who is lionel messi", "Lionel Messi is an Argentine footballer who's won 8 Ballon d'Or awards. He led Argentina to World Cup victory in 2022!"),
    ("who is michael jordan", "Michael Jordan is considered the greatest basketball player ever. He won 6 NBA championships with the Chicago Bulls and revolutionized the sport!"),
    ("who is serena williams", "Serena Williams has won 23 Grand Slam singles titles, the most in the Open Era. She's one of the greatest tennis players of all time!"),
    ("who is usain bolt", "Usain Bolt is the fastest man ever, holding world records in 100m and 200m. The Jamaican sprinter won 8 Olympic gold medals!"),
    ("who is muhammad ali", "Muhammad Ali was a boxing legend and cultural icon. He was heavyweight champion and known for his charisma and activism!"),
    ("who is lebron james", "LeBron James is an NBA superstar with 4 championships. He's considered one of the greatest basketball players, often compared to Michael Jordan!"),
    
    # Actors & Entertainment
    ("who is tom cruise", "Tom Cruise is an actor and producer known for Mission: Impossible and Top Gun. He's famous for doing his own dangerous stunts!"),
    ("who is leonardo dicaprio", "Leonardo DiCaprio is an acclaimed actor known for Titanic, Inception, and The Revenant. He's also an environmental activist!"),
    ("who is dwayne johnson", "Dwayne 'The Rock' Johnson was a WWE wrestler turned Hollywood actor. He's one of the highest-paid and most charismatic actors!"),
    ("who is oprah winfrey", "Oprah Winfrey is a media mogul, talk show host, and philanthropist. She's one of the most influential women in the world!"),
    ("who is shah rukh khan", "Shah Rukh Khan is a Bollywood superstar known as the 'King of Bollywood'. He's appeared in over 80 films and is incredibly popular globally!"),
    ("who is charlie chaplin", "Charlie Chaplin was a silent film icon known for his character 'The Tramp'. He was a comedic genius who also directed and composed music!"),
    
    # Authors & Philosophers
    ("who is william shakespeare", "William Shakespeare was an English playwright and poet from the 1600s. He wrote Romeo and Juliet, Hamlet, and 37 other plays!"),
    ("who is jk rowling", "J.K. Rowling wrote the Harry Potter series, one of the best-selling book series ever. She went from poverty to billionaire through her writing!"),
    ("who is plato", "Plato was an ancient Greek philosopher and student of Socrates. His works laid foundations for Western philosophy and science!"),
    ("who is aristotle", "Aristotle was a Greek philosopher who studied under Plato. He made contributions to logic, science, ethics, and politics!"),
    ("who is confucius", "Confucius was a Chinese philosopher whose teachings on morality and ethics influenced East Asian culture for over 2,000 years!"),
    
    # Historical Figures
    ("who is abraham lincoln", "Abraham Lincoln was the 16th US President who led the country through the Civil War and abolished slavery with the Emancipation Proclamation!"),
    ("who is george washington", "George Washington was the first US President and a founding father. He led American forces to victory in the Revolutionary War!"),
    ("who is winston churchill", "Winston Churchill was UK's Prime Minister during WWII. His leadership and speeches inspired Britain during its darkest hours!"),
    ("who is cleopatra", "Cleopatra was the last Pharaoh of ancient Egypt. She was known for her intelligence, political skill, and relationships with Julius Caesar and Mark Antony!"),
    ("who is julius caesar", "Julius Caesar was a Roman general and statesman who played a critical role in events leading to the rise of the Roman Empire!"),
    ("who is martin luther king", "Martin Luther King Jr. was a civil rights leader who fought for racial equality through nonviolent resistance. His 'I Have a Dream' speech is iconic!"),
    
    # Business Leaders
    ("who is warren buffett", "Warren Buffett is one of the most successful investors ever, CEO of Berkshire Hathaway. He's known for his wisdom and philanthropy!"),
    ("who is henry ford", "Henry Ford founded Ford Motor Company and revolutionized manufacturing with the assembly line, making cars affordable for average Americans!"),
    ("who is steve wozniak", "Steve Wozniak co-founded Apple with Steve Jobs. He's the engineering genius who built the first Apple computers!"),
    ("who is richard branson", "Richard Branson founded the Virgin Group with over 400 companies. He's known for his adventurous spirit and business innovation!"),
]

developer = [
    ("who is ibrahim shaikh", "Ibrahim Shaikh is a 20-year-old CSE AIML student passionate about Artificial Intelligence and Machine Learning. He's building his expertise in AI development!"),
    ("tell me about ibrahim", "Ibrahim is a Computer Science Engineering student specializing in AI and Machine Learning. At 20, he's focused on developing AI solutions and learning cutting-edge technologies!"),
    ("who made this", "This was created by Ibrahim Shaikh, a CSE AIML student who's passionate about AI and software development!"),
    ("who is the developer", "Ibrahim Shaikh is the developer - a 20-year-old student pursuing Computer Science Engineering with specialization in Artificial Intelligence and Machine Learning!"),
    ("what does ibrahim study", "Ibrahim studies Computer Science Engineering with a specialization in Artificial Intelligence and Machine Learning (CSE AIML)!"),
    ("how old is ibrahim", "Ibrahim Shaikh is 20 years old!"),
    ("what is ibrahim interested in", "Ibrahim is interested in Artificial Intelligence, Machine Learning, software development, and creating intelligent systems that solve real-world problems!"),
    ("tell me about the creator", "The creator is Ibrahim Shaikh, a young and ambitious CSE AIML student who's passionate about AI technology and innovation!"),
    ("who built this chatbot", "Ibrahim Shaikh built this! He's a 20-year-old CSE AIML student learning and applying AI/ML concepts through practical projects!"),
    ("what is ibrahim's field", "Ibrahim's field is Computer Science Engineering with specialization in Artificial Intelligence and Machine Learning (AIML)!"),
]

technology = [
    ("what is 5g", "5G is fifth-generation wireless technology offering faster speeds, lower latency, and more device connections than 4G. It enables smart cities, IoT, and real-time gaming!"),
    ("what is artificial intelligence", "AI is when machines are programmed to think and learn like humans. It includes machine learning, neural networks, and powers things like Siri and ChatGPT!"),
    ("what is cloud computing", "Cloud computing stores and processes data on remote servers accessed via the internet. Services like AWS, Azure, and Google Cloud let you rent computing power on-demand!"),
    ("what is blockchain", "Blockchain is a distributed digital ledger where transactions are recorded in blocks linked by cryptography. It powers Bitcoin and enables secure, transparent record-keeping!"),
    ("what is virtual reality", "VR creates immersive 3D environments using headsets that trick your senses. It's used for gaming, training, education, and virtual meetings!"),
    ("what is machine learning", "Machine learning is AI that learns patterns from data instead of being explicitly programmed. You show it examples, and it figures out the rules!"),
    ("what is deep learning", "Deep learning uses neural networks with many layers to recognize complex patterns. It powers image recognition, language translation, and self-driving cars!"),
    ("what is python", "Python is a popular programming language known for its simple, readable syntax. It's widely used in AI, web development, data science, and automation!"),
    ("what is javascript", "JavaScript is a programming language that makes websites interactive. It runs in browsers and also on servers with Node.js!"),
    ("what is an operating system", "An operating system (OS) manages your computer's hardware and software. Windows, macOS, Linux, and Android are all operating systems!"),
    ("what is a database", "A database is an organized collection of data that can be easily accessed and managed. MySQL, PostgreSQL, and MongoDB are popular databases!"),
    ("what is cybersecurity", "Cybersecurity protects computers and networks from digital attacks. It includes firewalls, encryption, passwords, and safe browsing practices!"),
    ("what is cryptocurrency", "Cryptocurrency is digital money using cryptography for security. Bitcoin and Ethereum run on blockchain without needing banks!"),
    ("what is web development", "Web development is building websites and web applications. Frontend handles what users see, backend handles data and logic!"),
    ("what is an api", "An API lets different software programs communicate. It's like a waiter taking your order to the kitchen and bringing back food!"),
]

def generate_variations(pairs):
    variations = []
    for inp, out in pairs:
        variations.append((inp, out))
        variations.append((inp.upper(), out))
        variations.append((inp.capitalize(), out))
        if not inp.endswith("?"):
            variations.append((inp + "?", out))
        if not inp.endswith("!"):
            variations.append((inp + "!", out))
        words = inp.split()
        if len(words) > 2:
            variations.append((" ".join(words[1:]), out))
    return variations

def create_dataset():
    all_pairs = []
    
    categories = [
        greetings, emotions, jokes, thanks, goodbyes, about_ai,
        math_simple, science, geography, fun_facts, advice,
        explanations, casual, compliments, help_requests, reactions,
        politics, people, developer, technology
    ]
    
    for category in categories:
        variations = generate_variations(category)
        all_pairs.extend(variations)
    
    for _ in range(3):
        all_pairs.extend(generate_variations(greetings))
        all_pairs.extend(generate_variations(jokes))
        all_pairs.extend(generate_variations(emotions))
        all_pairs.extend(generate_variations(science))
        all_pairs.extend(generate_variations(advice))
    
    all_data = [{"input": inp, "output": out} for inp, out in all_pairs]
    random.shuffle(all_data)
    
    train_size = int(len(all_data) * 0.9)
    val_size = int(len(all_data) * 0.05)
    
    train_data = all_data[:train_size]
    val_data = all_data[train_size:train_size + val_size]
    test_data = all_data[train_size + val_size:]
    
    with open("train_pairs.json", "w", encoding="utf-8") as f:
        json.dump(train_data, f, indent=2, ensure_ascii=False)
    
    with open("val_pairs.json", "w", encoding="utf-8") as f:
        json.dump(val_data, f, indent=2, ensure_ascii=False)
    
    with open("test_pairs.json", "w", encoding="utf-8") as f:
        json.dump(test_data, f, indent=2, ensure_ascii=False)
    
    print(f"Dataset created!")
    print(f"Train: {len(train_data)}")
    print(f"Val: {len(val_data)}")
    print(f"Test: {len(test_data)}")
    print(f"Total unique examples: {len(all_data)}")

if __name__ == "__main__":
    create_dataset()
