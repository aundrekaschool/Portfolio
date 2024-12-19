import datetime
import random
import calendar
import tkinter as tk
from tkinter import messagebox, simpledialog
import ephem
from datetime import date, timedelta

class User:
    def __init__(self, name, date_of_birth, birth_time=None, birth_location=None):
        self.name = name
        self.date_of_birth = datetime.datetime.strptime(date_of_birth, '%m/%d/%Y').date()
        self.birth_time = birth_time
        self.birth_location = birth_location

    def get_zodiac_sign(self):
        zodiac_signs = [
            ("Capricorn", datetime.date(self.date_of_birth.year, 12, 22), datetime.date(self.date_of_birth.year, 1, 19)),
            ("Aquarius", datetime.date(self.date_of_birth.year, 1, 20), datetime.date(self.date_of_birth.year, 2, 18)),
            ("Pisces", datetime.date(self.date_of_birth.year, 2, 19), datetime.date(self.date_of_birth.year, 3, 20)),
            ("Aries", datetime.date(self.date_of_birth.year, 3, 21), datetime.date(self.date_of_birth.year, 4, 19)),
            ("Taurus", datetime.date(self.date_of_birth.year, 4, 20), datetime.date(self.date_of_birth.year, 5, 20)),
            ("Gemini", datetime.date(self.date_of_birth.year, 5, 21), datetime.date(self.date_of_birth.year, 6, 20)),
            ("Cancer", datetime.date(self.date_of_birth.year, 6, 21), datetime.date(self.date_of_birth.year, 7, 22)),
            ("Leo", datetime.date(self.date_of_birth.year, 7, 23), datetime.date(self.date_of_birth.year, 8, 22)),
            ("Virgo", datetime.date(self.date_of_birth.year, 8, 23), datetime.date(self.date_of_birth.year, 9, 22)),
            ("Libra", datetime.date(self.date_of_birth.year, 9, 23), datetime.date(self.date_of_birth.year, 10, 22)),
            ("Scorpio", datetime.date(self.date_of_birth.year, 10, 23), datetime.date(self.date_of_birth.year, 11, 21)),
            ("Sagittarius", datetime.date(self.date_of_birth.year, 11, 22), datetime.date(self.date_of_birth.year, 12, 21))
        ]
        for sign, start, end in zodiac_signs:
            if start <= self.date_of_birth <= end:
                return sign
        return "Capricorn"
    
    def get_moon_sign(self):
        dob = self.date_of_birth.strftime('%Y/%m/%d')
        observer = ephem.Observer()
        observer.date = dob
        moon = ephem.Moon(observer)
        moon_sign = ephem.constellation(moon)[1]
        return moon_sign
    
    def calculate_rising_sign(self):
        if self.birth_time is None:
            return "Cannot calculate rising sign without birth time."
        observer = ephem.Observer()
        observer.lat = '14.5995' 
        observer.lon = '120.9842' 
        observer.date = self.date_of_birth.strftime('%Y/%m/%d') + ' ' + self.birth_time
        rising_sign = ephem.constellation(ephem.Sun(observer))[0]
        return rising_sign
    
    def calculate_chinese_zodiac(self):
        chinese_zodiac_animals = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"]
        chinese_zodiac_start_year = 1908
        birth_year = self.date_of_birth.year
        zodiac_index = (birth_year - chinese_zodiac_start_year) % 12
        return chinese_zodiac_animals[zodiac_index]

class AstrologyFacts:
    def __init__(self, user):
        self.user = user

    def get_zodiac_sign_description(self):
        zodiac_sign_descriptions = {
            "Capricorn": """Capricorns are known for their practicality, discipline, and ambition. They are hardworking and dedicated individuals who strive for success in all aspects of their lives. Capricorns are also known for their traditional values and strong sense of responsibility.""",
            "Aquarius": """Aquarians are independent, innovative, and forward-thinking. They are often described as intellectuals who value freedom and individuality. Aquarians are known for their humanitarian nature and desire to make the world a better place through their unique ideas and perspectives.""",
            "Pisces": """Pisceans are compassionate, imaginative, and sensitive individuals. They are deeply empathetic and often have a strong connection to their emotions and intuition. Pisceans are creative and artistic, with a love for music, art, and poetry. They are also known for their spiritual nature and ability to connect with the mystical realm.""",
            "Aries": """Arians are confident, courageous, and adventurous individuals. They are natural leaders who are not afraid to take risks and pursue their goals with passion and determination. Arians are also known for their competitive spirit and love of challenges.""",
            "Taurus": """Taureans are reliable, practical, and patient individuals. They value stability and security in their lives and are often associated with a strong work ethic and determination. Taureans are also known for their love of luxury and comfort, as well as their appreciation for beauty and the finer things in life.""",
            "Gemini": """Geminis are curious, adaptable, and social individuals. They are quick-witted and intellectually stimulating, with a love for learning and communication. Geminis are often described as the life of the party, as they enjoy engaging with others and exploring new ideas and experiences.""",
            "Cancer": """Cancerians are intuitive, nurturing, and deeply emotional individuals. They are highly empathetic and compassionate, with a strong sense of loyalty and devotion to their loved ones. Cancerians are also known for their protective nature and ability to create a sense of home and security wherever they go.""",
            "Leo": """Leos are confident, charismatic, and creative individuals. They are natural leaders who thrive in the spotlight and enjoy being the center of attention. Leos are known for their generosity and warmth, as well as their passion for self-expression and creativity.""",
            "Virgo": """Virgos are analytical, practical, and detail-oriented individuals. They are perfectionists who strive for excellence in everything they do. Virgos are also known for their strong sense of duty and service, as well as their willingness to help others and make a difference in the world.""",
            "Libra": """Librans are social, diplomatic, and charming individuals. They are natural peacemakers who value harmony and balance in their relationships and surroundings. Librans are also known for their love of beauty and aesthetics, as well as their appreciation for art, culture, and romance.""",
            "Scorpio": """Scorpios are passionate, intense, and mysterious individuals. They are known for their deep emotional depth and powerful intuition. Scorpios are also highly determined and resilient, with a strong sense of purpose and inner strength.""",
            "Sagittarius": """Sagittarians are optimistic, adventurous, and free-spirited individuals. They are natural explorers who crave excitement and new experiences. Sagittarians are also known for their philosophical outlook on life and their love of learning and expanding their horizons."""
        }
        zodiac_sign = self.user.get_zodiac_sign()
        return zodiac_sign_descriptions.get(zodiac_sign, "No description available")

    def get_moon_sign_description(self):
        moon_sign_descriptions = {
            "Aries": """Moon in Aries suggests a strong need for independence and self-expression. Individuals with this placement may have a fiery temperament, often acting impulsively and assertively. They may be quick to react emotionally, but also quick to forgive and forget. Their emotions are intense and passionate, and they seek excitement and adventure in their lives. Moon in Aries individuals are natural leaders, driven by a desire to conquer challenges and achieve their goals. They thrive on competition and may become impatient or restless when faced with obstacles.""",
            "Taurus": """Moon in Taurus indicates a deep need for security and stability. Individuals with this placement are practical and grounded, valuing comfort and material possessions. They have a strong sense of loyalty and possessiveness in their relationships, and may be slow to change or adapt to new situations. Their emotions are steady and reliable, but they can also be stubborn and resistant to change. Moon in Taurus individuals are sensual and pleasure-seeking, enjoying life's simple pleasures and indulging in luxurious comforts.""",
            "Gemini": """Moon in Gemini suggests a restless and curious mind. Individuals with this placement are adaptable and versatile, with a need for mental stimulation and variety. They may be talkative and sociable, enjoying lively conversations and intellectual debates. Their emotions are often changeable and unpredictable, leading to mood swings and indecisiveness. Moon in Gemini individuals are curious and inquisitive, always seeking new experiences and learning opportunities. They may struggle with emotional depth and may avoid confronting deeper feelings.""",
            "Cancer": """Moon in Cancer indicates a strong need for emotional security and nurturing. Individuals with this placement are sensitive and empathetic, deeply attuned to the feelings of others. They are deeply attached to their family and home, seeking comfort and solace in familiar surroundings. Their emotions are intense and profound, often fluctuating with the phases of the moon. Moon in Cancer individuals are nurturing and protective, with a natural instinct to care for others. They may be prone to moodiness and clinginess, but also possess a strong intuition and psychic sensitivity.""",
            "Leo": """Moon in Leo suggests a need for recognition and admiration. Individuals with this placement are proud and confident, with a desire to shine and be noticed. They crave attention and approval from others, seeking validation for their talents and achievements. Their emotions are dramatic and expressive, and they may have a flair for the dramatic. Moon in Leo individuals are generous and warm-hearted, with a natural charisma and magnetism that draws others to them. They may struggle with issues of ego and pride, but also possess a strong sense of self-worth and dignity.""",
            "Virgo": """Moon in Virgo indicates a need for order and perfection. Individuals with this placement are analytical and detail-oriented, with a desire to organize and categorize their emotions. They may be critical of themselves and others, striving for perfection in all aspects of their lives. Their emotions are practical and pragmatic, and they may struggle with expressing vulnerability or emotionality. Moon in Virgo individuals are conscientious and diligent, with a strong sense of duty and responsibility. They may be reserved and cautious, but also possess a keen intellect and problem-solving ability.""",
            "Libra": """Moon in Libra suggests a need for harmony and balance. Individuals with this placement are diplomatic and fair-minded, with a desire to create peace and harmony in their relationships. They may be indecisive and conflict-averse, seeking to avoid confrontation and maintain harmony at all costs. Their emotions are idealistic and romantic, and they may have a strong sense of justice and fairness. Moon in Libra individuals are charming and sociable, with a natural ability to connect with others. They may struggle with indecision and people-pleasing tendencies, but also possess a strong sense of empathy and compassion.""",
            "Scorpio": """Moon in Scorpio indicates a deep and intense emotional nature. Individuals with this placement are passionate and secretive, with a desire to delve into the depths of their own psyche and the mysteries of life. They may be fiercely loyal and possessive in their relationships, with a need for emotional intimacy and connection. Their emotions are intense and transformative, often leading to periods of emotional upheaval and regeneration. Moon in Scorpio individuals are intuitive and perceptive, with a natural ability to uncover hidden truths and motivations. They may struggle with issues of trust and control, but also possess a powerful inner strength and resilience.""",
            "Sagittarius": """Moon in Sagittarius suggests a need for freedom and adventure. Individuals with this placement are optimistic and adventurous, with a desire to explore new horizons and expand their knowledge and experiences. They may be idealistic and philosophical, seeking meaning and purpose in their lives. Their emotions are expansive and enthusiastic, and they may have a tendency to exaggerate or over-dramatize their feelings. Moon in Sagittarius individuals are independent and open-minded, with a natural curiosity and thirst for adventure. They may struggle with restlessness and impulsiveness, but also possess a sense of optimism and faith in the future.""",
            "Capricorn": """Moon in Capricorn indicates a need for structure and control. Individuals with this placement are ambitious and disciplined, with a desire to achieve success and recognition in their careers and personal lives. They may be reserved and cautious, with a tendency to suppress their emotions in favor of practicality and realism. Their emotions are steady and reliable, but they may struggle with expressing vulnerability or sentimentality. Moon in Capricorn individuals are responsible and hardworking, with a strong sense of duty and tradition. They may be prone to self-criticism and perfectionism, but also possess a strong sense of integrity and determination.""",
            "Aquarius": """Moon in Aquarius suggests a need for independence and individuality. Individuals with this placement are progressive and unconventional, with a desire to break free from traditional norms and expectations. They may be idealistic and visionary, seeking to create positive change in the world around them. Their emotions are detached and objective, and they may have a tendency to intellectualize their feelings. Moon in Aquarius individuals are humanitarian and open-minded, with a strong sense of social justice and equality. They may struggle with emotional detachment and unpredictability, but also possess a deep empathy and concern for others.""",
            "Pisces": """Moon in Pisces indicates a deep sensitivity and empathy. Individuals with this placement are intuitive and compassionate, with a strong connection to the collective unconscious and spiritual realms. They may be dreamy and idealistic, with a tendency to escape into fantasy and imagination. Their emotions are fluid and impressionable, and they may absorb the feelings"""
        }
        moon_sign = self.user.get_moon_sign()
        return moon_sign_descriptions.get(moon_sign, "No description available")
    
    def get_rising_description(self):
        rising = {
            "Ari": """Aries Rising individuals have a dynamic and energetic presence. They exude confidence and assertiveness, often appearing bold and determined in their demeanor. With their strong and direct gaze, they make an instant impression as natural leaders and pioneers. Their fiery temperament is reflected in their brisk movements and lively expressions, conveying a sense of independence and self-assurance.""",
            "Tau": """Taurus Rising individuals possess a serene and composed demeanor. They radiate an aura of stability and reliability, appearing grounded and steadfast in their posture and movements. With their gentle and soothing voice, they create an immediate sense of calmness and assurance. Their earthy charm and sensual appeal draw others in, leaving a lasting impression of warmth and comfort.""",
            "Gem": """Gemini Rising individuals have a lively and engaging presence. They captivate with their quick wit and animated gestures, effortlessly sparking conversation and laughter. Their curious and inquisitive gaze reflects their keen intellect and adaptability, making them instantly approachable and sociable. With their expressive and versatile mannerisms, they leave a memorable impression as vibrant and intellectually stimulating individuals.""",
            "Can": """Cancer Rising individuals emanate a nurturing and empathetic energy. They exude a sense of warmth and familiarity, inviting others into their protective embrace. Their compassionate gaze and gentle smile convey a deep understanding of emotions and a genuine concern for others. With their caring touch and attentive listening, they create an immediate sense of comfort and security, leaving a lasting impression of emotional depth and sensitivity.""",
            "Leo": """Leo Rising individuals command attention with their confident and regal presence. They radiate charisma and authority, effortlessly captivating the room with their magnetic charm and theatrical flair. Their proud and majestic bearing exudes a sense of confidence and self-assurance, leaving a lasting impression of strength and vitality. With their dramatic gestures and expressive gestures, they make an unforgettable mark as dynamic and captivating individuals.""",
            "Vir": """Virgo Rising individuals project an air of poise and refinement. They appear meticulous and well-groomed, with an attention to detail that speaks to their discerning taste and practicality. Their precise and measured movements convey a sense of order and control, creating an immediate impression of reliability and competence. With their analytical gaze and thoughtful demeanor, they leave a lasting impression as intelligent and industrious individuals.""",
            "Lib": """Libra Rising individuals exude charm and elegance in their every gesture. They appear poised and graceful, with an effortless sense of harmony and balance in their movements. Their diplomatic and fair-minded demeanor creates an immediate sense of peace and cooperation, inviting others into their circle with open arms. With their charming smile and gracious mannerisms, they leave a lasting impression of beauty and refinement.""",
            "Sco": """Scorpio Rising individuals possess an intense and magnetic allure. They exude an air of mystery and intrigue, drawing others in with their penetrating gaze and enigmatic presence. Their powerful and hypnotic gaze reveals a depth of emotion and intensity that is both captivating and intimidating. With their secretive and alluring mannerisms, they leave a lasting impression as enigmatic and passionate individuals.""",
            "Sag": """Sagittarius Rising individuals project an aura of optimism and adventure. They appear vibrant and free-spirited, with a boundless energy that inspires others to follow their lead. Their expansive and enthusiastic demeanor conveys a sense of openness and curiosity, inviting others on a journey of discovery and exploration. With their adventurous spirit and infectious laughter, they leave a lasting impression as adventurous and spirited individuals.""",
            "Cap": """Capricorn Rising individuals exude an air of maturity and authority. They appear composed and dignified, with a quiet confidence that commands respect. Their disciplined and hardworking demeanor reflects a sense of purpose and determination, leaving a lasting impression of reliability and dependability. With their reserved and measured approach, they make an indelible mark as capable and responsible individuals.""",
            "Aqu": """Aquarius Rising individuals project an aura of independence and individuality. They appear eccentric and unconventional, with a unique style that sets them apart from the crowd. Their detached and intellectual demeanor conveys a sense of curiosity and open-mindedness, inviting others to explore new ideas and perspectives. With their visionary spirit and progressive outlook, they leave a lasting impression as innovative and forward-thinking individuals.""",
            "Psc": """Pisces Rising individuals emanate a dreamy and ethereal energy. They appear gentle and compassionate, with a softness to their features that reflects their sensitive nature. Their empathetic gaze and serene smile convey a deep understanding of emotions and a profound connection to the spiritual realm. With their intuitive and imaginative mannerisms, they leave a lasting impression of sensitivity and depth."""
        }
        rising_sign = self.user.calculate_rising_sign()
        return rising.get(rising_sign, "No description available")
    
    def chinese(self):
        zodiac = {
            "Rat": """Those born in the Year of the Rat are known for their resourcefulness and intelligence. They are quick-witted and adaptable, able to navigate through any situation with ease. Rats are charming and sociable, with a knack for making connections and forming alliances. They are also ambitious and hardworking, always striving for success in their endeavors.""",
            "Ox": """Those born in the Year of the Ox are known for their strength and determination. They are reliable and steadfast, able to overcome any obstacle through sheer perseverance and willpower. Oxen are practical and disciplined, with a strong sense of duty and responsibility. They are also patient and methodical, taking a slow and steady approach to achieve their goals.""",
            "Tiger": """Those born in the Year of the Tiger are known for their courage and passion. They are fearless and bold, unafraid to take risks and pursue their dreams with conviction. Tigers are charismatic and confident, with a magnetic presence that commands attention. They are also fiercely independent and competitive, always eager to prove themselves and emerge victorious.""",
            "Rabbit": """Those born in the Year of the Rabbit are known for their gentleness and diplomacy. They are kind-hearted and compassionate, always ready to lend a listening ear or offer a helping hand. Rabbits are also artistic and refined, with a love for beauty and harmony in all aspects of life. They are skilled communicators and peacemakers, able to diffuse tension and bring people together.""",
            "Dragon": """Those born in the Year of the Dragon are known for their charisma and leadership abilities. They are confident and ambitious, with a natural talent for inspiring others and rallying them towards a common goal. Dragons are also imaginative and innovative, always seeking new challenges and opportunities for growth. They are fiercely independent and unafraid to blaze their own trail.""",
            "Snake": """Those born in the Year of the Snake are known for their wisdom and intuition. They are insightful and perceptive, able to see beneath the surface and uncover hidden truths. Snakes are also mysterious and enigmatic, with a magnetic allure that draws others in. They are strategic and calculated in their actions, always thinking several steps ahead to achieve their objectives.""",
            "Horse": """Those born in the Year of the Horse are known for their independence and freedom-loving spirit. They are adventurous and energetic, always seeking new experiences and challenges to keep life exciting. Horses are also sociable and outgoing, with a natural charm and magnetism that makes them popular among friends and acquaintances. They are also hardworking and resilient, able to overcome any obstacle with grace and determination.""",
            "Goat": """Those born in the Year of the Goat are known for their gentle and nurturing nature. They are compassionate and empathetic, always putting the needs of others before their own. Goats are also creative and artistic, with a love for beauty and aesthetics. They are sensitive and intuitive, able to pick up on subtle cues and emotions that others may overlook.""",
            "Monkey": """Those born in the Year of the Monkey are known for their intelligence and wit. They are clever and resourceful, able to find solutions to even the most challenging problems. Monkeys are also playful and mischievous, with a lively sense of humor that brightens the mood wherever they go. They are sociable and outgoing, with a knack for making friends and charming others with their quick wit and charm.""",
            "Rooster": """Those born in the Year of the Rooster are known for their confidence and self-assurance. They are proud and assertive, unafraid to speak their minds and stand up for what they believe in. Roosters are also hardworking and diligent, with a strong sense of responsibility and duty. They are also organized and detail-oriented, always striving for perfection in everything they do.""",
            "Dog": """Those born in the Year of the Dog are known for their loyalty and devotion. They are faithful and dependable, always there to offer support and companionship to those they care about. Dogs are also compassionate and empathetic, with a strong sense of justice and fairness. They are protective of their loved ones and will go to great lengths to ensure their safety and well-being.""",
            "Pig": """Those born in the Year of the Pig are known for their kindness and generosity. They are warm-hearted and affectionate, always ready to lend a helping hand or offer a word of encouragement. Pigs are also sociable and easygoing, with a love for good company and lively conversation. They are also practical and down-to-earth, with a sensible approach to life's challenges and uncertainties."""
        }
        zodiacsign = self.user.calculate_chinese_zodiac()
        return zodiac.get(zodiacsign, "No description available")

    def get_facts(self):
        zodiac_fact = f"\nZODIAC SIGN/SUN SIGN (Represents your true identity)): {self.user.get_zodiac_sign()} \n{self.get_zodiac_sign_description()}"
        moon_fact = f"\nMOON SIGN (Represents your emotional self): {self.user.get_moon_sign()} \n{self.get_moon_sign_description()}"
        rising_fact = f"\nRISING SIGN (Represents your outward impression): {self.user.calculate_rising_sign()} \n{self.get_rising_description()}"
        chinese_fact = f"\nCHINESE ZODIAC SIGN (Represents your core values): {self.user.calculate_chinese_zodiac()} \n{self.chinese()}"

        facts = "\n".join([zodiac_fact, moon_fact, rising_fact, chinese_fact])
        return facts

class TarotReading:
    def __init__(self):
        self.card_descriptions = {
            "The Fool": {
                "upright": "New beginnings, adventure, spontaneity. Today, you might find yourself embarking on a new journey filled with excitement and possibilities.",
                "reversed": "Recklessness, folly, and poor decisions. Be cautious today as you may be acting impulsively without considering the consequences.",
                "type": "Major Arcana"
            },
            "The Magician": {
                "upright": "Skill, creativity, focus, and control. Today, your talents and abilities are at their peak, allowing you to manifest your desires with ease.",
                "reversed": "Manipulation, deceit, and misdirection. Beware of others trying to deceive you or of your own tendency to use your skills for selfish gain.",
                "type": "Major Arcana"
            },
            "The High Priestess": {
                "upright": "Intuition, wisdom, secrets, and the unconscious. Today, trust your inner voice and instincts, as they will guide you towards hidden truths and insights.",
                "reversed": "Hidden agendas, confusion, and lack of intuition. You may feel disconnected from your inner wisdom, leading to confusion and uncertainty.",
                "type": "Major Arcana"
            },
            "The Empress": {
                "upright": "Fertility, nurturing, abundance, and motherhood. Today, focus on nurturing yourself and others. It's a time of growth and abundance.",
                "reversed": "Neglect, smothering, and dependence. You may be neglecting your own needs or suffocating others with your demands. Find balance.",
                "type": "Major Arcana"
            },
            "The Emperor": {
                "upright": "Authority, structure, power, and control. Today, take charge of situations with confidence and leadership. Set clear boundaries.",
                "reversed": "Domineering, inflexibility, and tyranny. You may be exerting control in a negative way or struggling to maintain authority.",
                "type": "Major Arcana"
            },
            "The Hierophant": {
                "upright": "Tradition, conformity, spiritual guidance, and institutions. Today, seek guidance from tradition and authority figures. Embrace rituals.",
                "reversed": "Rebellion, non-conformity, and challenging tradition. You may be questioning established norms or feeling restricted by tradition.",
                "type": "Major Arcana"
            },
            "The Lovers": {
                "upright": "Partnerships, relationships, love, and harmony. Today, focus on deepening your connections with loved ones. Make choices from the heart.",
                "reversed": "Conflict, disharmony, and imbalance. There may be tensions or disagreements in your relationships. Seek resolution through open communication.",
                "type": "Major Arcana"
            },
            "The Chariot": {
                "upright": "Willpower, determination, victory, and self-control. Today, harness your inner strength and determination to overcome obstacles and achieve success.",
                "reversed": "Lack of direction, aggression, and defeat. You may be feeling aimless or encountering setbacks. Take a moment to reassess your goals.",
                "type": "Major Arcana"
            },
            "Strength": {
                "upright": "Inner strength, courage, patience, and compassion. Today, tap into your inner resilience and face challenges with grace and compassion.",
                "reversed": "Weakness, insecurity, and self-doubt. You may be feeling overwhelmed or doubting your abilities. Trust in your inner strength.",
                "type": "Major Arcana"
            },
            "The Hermit": {
                "upright": "Soul-searching, introspection, solitude, and guidance. Today, take time for introspection and self-discovery. Seek guidance from within.",
                "reversed": "Isolation, loneliness, and withdrawal. You may be feeling disconnected from others or struggling to find meaning in solitude.",
                "type": "Major Arcana"
            },
            "Wheel of Fortune": {
                "upright": "Luck, destiny, cycles, and fate. Today, embrace the ebb and flow of life's cycles. Trust that things are unfolding as they should.",
                "reversed": "Bad luck, resistance to change, and control issues. You may be resisting necessary changes or feeling trapped in a cycle of negativity.",
                "type": "Major Arcana"
            },
            "Justice": {
                "upright": "Fairness, truth, law, and balance. Today, seek justice and truth in all matters. Make decisions with integrity and fairness.",
                "reversed": "Injustice, dishonesty, and legal issues. You may encounter unfairness or deception. Stand up for what is right and seek resolution.",
                "type": "Major Arcana"
            },
            "The Hanged Man": {
                "upright": "Sacrifice, release, surrender, and letting go. Today, embrace surrender and release what no longer serves you. Trust in the process.",
                "reversed": "Stagnation, delays, and resistance to change. You may be resisting necessary sacrifices or feeling stuck. Let go of control.",
                "type": "Major Arcana"
            },
            "Death": {
                "upright": "Endings, change, transformation, and new beginnings. Today, embrace endings as opportunities for growth and transformation.",
                "reversed": "Resistance to change, fear of the unknown, and stagnation. You may be clinging to the past or resisting necessary changes. Embrace transformation.",
                "type": "Major Arcana"
            },
            "Temperance": {
                "upright": "Balance, moderation, patience, and harmony. Today, seek balance in all areas of your life. Practice patience and moderation.",
                "reversed": "Imbalance, excess, and lack of moderation. You may be feeling out of sync or experiencing extremes. Reevaluate your priorities.",
                "type": "Major Arcana"
            },
            "The Devil": {
                "upright": "Materialism, bondage, ignorance, and temptation. Today, beware of illusions and false promises. Break free from unhealthy attachments.",
                "reversed": "Release from bondage, enlightenment, and freedom. You are breaking free from limitations and reclaiming your power.",
                "type": "Major Arcana"
            },
            "The Tower": {
                "upright": "Disaster, upheaval, sudden change, and revelation. Today, expect the unexpected as old structures collapse to make way for new beginnings.",
                "reversed": "Avoidance of disaster, delaying inevitable change, and fear of change. You may be resisting necessary upheaval or ignoring warning signs.",
                "type": "Major Arcana"
            },
            "The Star": {
                "upright": "Hope, inspiration, spirituality, and renewal. Today, have faith in the future and trust that better times are ahead. Stay optimistic.",
                "reversed": "Lack of faith, despair, and disappointment. You may be feeling hopeless or losing sight of your dreams. Find renewed faith and optimism.",
                "type": "Major Arcana"
        

        },
            "The Moon": {
                "upright": "Illusion, fear, anxiety, and subconscious. Today, pay attention to your intuition and subconscious messages. Things may not be as they seem.",
                "reversed": "Release of fear, confusion, and clarity. You are gaining clarity and understanding, dispelling illusions and facing your fears.",
                "type": "Major Arcana"
            },
            "The Sun": {
                "upright": "Joy, success, positivity, and vitality. Today, bask in the warmth of success and happiness. Embrace optimism and celebrate life.",
                "reversed": "Temporary depression, negativity, and lack of vitality. You may be feeling down or experiencing setbacks. Trust that brighter days are ahead.",
                "type": "Major Arcana"
            },
            "Judgement": {
                "upright": "Rebirth, inner calling, absolution, and redemption. Today, embrace self-reflection and forgiveness. It's a time of renewal and transformation.",
                "reversed": "Self-doubt, self-criticism, and lack of accountability. You may be avoiding responsibility or struggling to forgive yourself. Embrace self-acceptance.",
                "type": "Major Arcana"
            },
            "The World": {
                "upright": "Completion, accomplishment, fulfillment, and travel. Today, celebrate your achievements and embrace new opportunities. The world is yours.",
                "reversed": "Lack of completion, unfinished business, and stagnation. You may be feeling unfulfilled or struggling to reach your goals. Take steps to bring closure.",
                "type": "Major Arcana"
            },
            "Ace of Cups": {
                "upright": "New beginnings, love, joy, and emotional fulfillment. Today, open your heart to new experiences and connections. Embrace love and compassion.",
                "reversed": "Emotional loss, blocked creativity, and emptiness. You may be feeling disconnected from your emotions or struggling to find inspiration. Seek healing.",
                "type": "Cups"
            },
            "Two of Cups": {
                "upright": "Partnership, love, harmony, and mutual attraction. Today, focus on building strong and meaningful connections with others. Work together for a common goal.",
                "reversed": "Imbalance, disharmony, and broken relationships. There may be conflicts or disagreements in your relationships. Seek compromise and understanding.",
                "type": "Cups"
            },
            "Three of Cups": {
                "upright": "Friendship, celebration, community, and joy. Today, gather with loved ones and celebrate your achievements. Enjoy the camaraderie and support.",
                "reversed": "Overindulgence, excess, and shallow friendships. Be mindful of overdoing it or engaging in superficial connections. Focus on meaningful relationships.",
                "type": "Cups"
            },
            "Four of Cups": {
                "upright": "Apathy, boredom, and contemplation. Today, take time to reflect on your emotions and desires. Be open to new opportunities and perspectives.",
                "reversed": "Self-reflection, introspection, and emotional clarity. You are gaining insight into your true feelings and desires, leading to greater emotional fulfillment.",
                "type": "Cups"
            },
            "Five of Cups": {
                "upright": "Loss, regret, disappointment, and focusing on the negative. Today, acknowledge your feelings of loss or disappointment, but don't dwell on them. Look for the silver lining.",
                "reversed": "Moving on, acceptance, and forgiveness. You are releasing the past and moving forward with renewed optimism. Embrace forgiveness and healing.",
                "type": "Cups"
            },
            "Six of Cups": {
                "upright": "Nostalgia, childhood memories, innocence, and generosity. Today, revisit fond memories from the past and reconnect with your inner child. Spread kindness and generosity.",
                "reversed": "Moving forward, letting go of the past, and breaking cycles. You are releasing old patterns and embracing new opportunities for growth and happiness.",
                "type": "Cups"
            },
            "Seven of Cups": {
                "upright": "Fantasy, illusion, and wishful thinking. Today, be mindful of unrealistic expectations and fantasies. Focus on practical goals and take decisive action.",
                "reversed": "Alignment of goals, prioritization, and focus. You are gaining clarity and focus, aligning your goals with your actions. Stay grounded and focused.",
                "type": "Cups"
            },
            "Eight of Cups": {
                "upright": "Disappointment, abandonment, and walking away. Today, you may feel a sense of disillusionment or dissatisfaction with your current situation. Trust your intuition and follow your heart.",
                "reversed": "Seeking fulfillment, inner clarity, and turning point. You are on the brink of a major life change or realization. Embrace the journey of self-discovery.",
                "type": "Cups"
            },
            "Nine of Cups": {
                "upright": "Contentment, satisfaction, and emotional fulfillment. Today, celebrate your achievements and enjoy the abundance of blessings in your life. You are at peace with yourself and the world.",
                "reversed": "Complacency, smugness, and dissatisfaction. Be wary of becoming too comfortable or arrogant. Strive for continued growth and improvement.",
                "type": "Cups"
            },
            "Ten of Cups": {
                "upright": "Harmony, happiness, and emotional fulfillment in relationships. Today, cherish the love and support of your family and loved ones. You are surrounded by joy and contentment.",
                "reversed": "Broken relationships, disharmony, and disconnection. There may be tensions or conflicts within your family or social circle. Seek reconciliation and healing.",
                "type": "Cups"
            },
            "Page of Cups": {
                "upright": "Creativity, intuition, and emotional exploration. Today, embrace your imaginative and intuitive side. Explore your feelings and express yourself creatively.",
                "reversed": "Overly emotional, moodiness, and insecurity. You may be feeling overly sensitive or prone to mood swings. Find healthy outlets for your emotions.",
                "type": "Cups"
            },
            "Knight of Cups": {
                "upright": "Romance, charm, and imagination. Today, follow your heart and pursue your dreams with passion and creativity. Let your intuition guide you in matters of love.",
                "reversed": "Unreliable, escapist, and disillusioned. Beware of making decisions based solely on emotion or fantasy. Stay grounded and realistic.",
                "type": "Cups"
            },
            "Queen of Cups": {
                "upright": "Compassion, intuition, and emotional stability. Today, trust your intuition and empathize with others. Nourish your emotional well-being and nurture your relationships.",
                "reversed": "Emotional insecurity, codependency, and overemotional. You may be feeling emotionally overwhelmed or dependent on others for validation. Focus on self-care and boundaries.",
                "type": "Cups"
            },
            "King of Cups": {
                "upright": "Emotional maturity, wisdom, and compassion. Today, lead with empathy and understanding in your interactions. Maintain emotional stability and offer support to those in need.",
                "reversed": "Emotional manipulation, moodiness, and emotional suppression. Beware of using emotional manipulation to control situations or suppressing your true feelings. Practice honesty and transparency.",
                "type": "Cups"
            },
            "Ace of Swords": {
                "upright": "Clarity, truth, mental breakthroughs, and new ideas. Today, seek clarity of thought and communicate your truth with confidence. Embrace new perspectives and opportunities for growth.",
                "reversed": "Confusion, chaos, and mental blockages. You may be feeling mentally foggy or struggling to make sense of a situation. Take a step back and clear your mind.",
                "type": "Swords"
            },
            "Two of Swords": {
                "upright": "Indecision, stalemate, and avoidance. Today, confront difficult decisions with courage and clarity. Avoidance only prolongs the inevitable.",
                "reversed": "Indecision, confusion, and information overload. You may be overwhelmed by choices or struggling to make a decision. Trust your instincts and seek clarity.",
                "type": "Swords"
            },
            "Three of Swords": {
                "upright": "Heartbreak, sorrow, and grief. Today, acknowledge your pain and allow yourself to heal. Embrace the support of loved ones as you navigate through difficult emotions.",
                "reversed": "Recovery, forgiveness, and moving on. You are finding closure and healing from past heartache. Embrace forgiveness and release the pain of the past.",
                "type": "Swords"
            },
            "Four of Swords": {
                "upright": "Rest, relaxation, and recuperation. Today, prioritize self-care and take a break from the demands of life. Recharge your batteries and replenish your energy.",
                "reversed": "Exhaustion, burnout, and overwhelm. You may be pushing yourself too hard or neglecting your need for rest. Listen to your body and prioritize your well-being.",
                "type": "Swords"
            },
            "Five of Swords": {
                "upright": "Conflict, tension, and defeat. Today, choose your battles wisely and avoid unnecessary conflict. Sometimes it's better to walk away than to win at all costs.",
                "reversed": "Reconciliation, resolution, and compromise. You are finding common ground and resolving conflicts with grace and diplomacy. Focus on finding solutions.",
                "type": "Swords"
            },
            "Six of Swords": {
                "upright": "Transition, moving on, and mental clarity. Today, embrace change and leave behind what no longer serves you. Trust that brighter days are ahead.",
                "reversed": "Resistance to change, emotional baggage, and delays. You may be clinging to the past or afraid to move forward. Let go of old patterns and embrace the journey.",
                "type": "Swords"
            },
            "Seven of Swords": {
                "upright": "Deception, betrayal, and secrecy. Today, be cautious of deceitful individuals or hidden agendas. Trust your instincts and avoid being misled.",
                "reversed": "Revelation, confession, and coming clean. Secrets are being revealed, and truths are coming to light. Be honest with yourself and others.",
                "type": "Swords"
            },
            "Eight of Swords": {
                "upright": "Restriction, confinement, and self-imposed limitations. Today, break free from mental barriers and take control of your destiny. You have the power to overcome obstacles.",
                "reversed": "Self-acceptance, freedom, and empowerment. You are releasing self-imposed limitations and embracing your personal power. Break free from mental constraints.",
                "type": "Swords"
            },
            "Nine of Swords": {
                "upright": "Anxiety, worry, and fear. Today, confront your fears and anxieties head-on. Seek support from loved ones and practice self-care to ease your troubled mind.",
                "reversed": "Inner turmoil, nightmares, and guilt. You may be overwhelmed by negative thoughts or haunted by past mistakes. Practice self-compassion and seek professional help if needed.",
                "type": "Swords"
            },
            "Ten of Swords": {
                "upright": "Betrayal, backstabbing, and painful endings. Today, acknowledge the end of a difficult situation and embrace the opportunity for renewal and growth.",
                "reversed": "Recovery, survival, and healing. You are overcoming adversity and rising above challenges with resilience and strength. Embrace the lessons learned.",
                "type": "Swords"
            },
            "Page of Swords": {
                "upright": "Curiosity, intellect, and new ideas. Today, embrace your inquisitive nature and seek out new knowledge and experiences. Be open to fresh perspectives.",
                "reversed": "Intellectual immaturity, impulsiveness, and recklessness. You may be jumping to conclusions or acting without considering the consequences. Think before you speak.",
                "type": "Swords"
            },
            "Knight of Swords": {
                "upright": "Ambition, action, and determination. Today, pursue your goals with focus and determination. Take decisive action and overcome obstacles with confidence.",
                "reversed": "Hasty decisions, recklessness, and aggression. Beware of rushing into action without considering the consequences. Take a step back and assess the situation.",
                "type": "Swords"
            },
            "Queen of Swords": {
                "upright": "Independence, clarity, and direct communication. Today, speak your truth with confidence and assertiveness. Trust your intellect and make decisions with clarity.",
                "reversed": "Coldness, harsh judgment, and overly critical. You may be coming across as aloof or judgmental. Practice empathy and compassion in your interactions.",
                "type": "Swords"
            },
            "King of Swords": {
                "upright": "Authority, leadership, and intellectual power. Today, lead with wisdom and logic in your decision-making. Maintain objectivity and assert your authority when necessary.",
                "reversed": "Tyranny, manipulation, and abuse of power. Beware of using your intellect to manipulate or control others. Lead with integrity and fairness.",
                "type": "Swords"
            },
            "Ace of Wands": {
                "upright": "Inspiration, new opportunities, and creative potential. Today, embrace new beginnings and pursue your passions with enthusiasm and confidence. Take bold action.",
                "reversed": "Lack of direction, delays, and missed opportunities. You may be feeling uninspired or stuck in a rut. Reconnect with your passions and take proactive steps.",
                "type": "Wands"
            },
            "Two of Wands": {
                "upright": "Planning, preparation, and future vision. Today, focus on setting long-term goals and making strategic plans for the future. Take the first steps towards your dreams.",
                "reversed": "Lack of planning, fear of the unknown, and indecision. You may be feeling overwhelmed by uncertainty or hesitant to take action. Trust in your abilities and make decisions with confidence.",
                "type": "Wands"
            },
            "Three of Wands": {
                "upright": "Expansion, foresight, and progress. Today, embrace opportunities for growth and expansion. Trust in your vision and take bold steps towards your goals.",
                "reversed": "Lack of foresight, delays, and obstacles. You may encounter setbacks or delays in your plans. Stay focused on your long-term vision and adapt to challenges.",
                "type": "Wands"
            },
            "Four of Wands": {
                "upright": "Celebration, harmony, and stability. Today, celebrate your achievements and enjoy the fruits of your labor. Surround yourself with loved ones and bask in the joy of success.",
                "reversed": "Instability, disharmony, and lack of celebration. You may be feeling disconnected from others or struggling to find balance in your life. Take time to appreciate your accomplishments.",
                "type": "Wands"
            },
            "Five of Wands": {
                "upright": "Conflict, competition, and disagreement. Today, be prepared for challenges and conflicts that may arise. Work together with others to find mutually beneficial solutions.",
                "reversed": "Resolution, reconciliation, and cooperation. You are finding common ground and resolving conflicts with grace and diplomacy. Focus on collaboration and teamwork.",
                "type": "Wands"
            },
            "Six of Wands": {
                "upright": "Victory, success, and public recognition. Today, celebrate your accomplishments and embrace the recognition you deserve. You have overcome obstacles and achieved your goals.",
                "reversed": "Ego, arrogance, and self-doubt. Beware of letting success go to your head or doubting your abilities. Stay humble and focused on continued growth.",
                "type": "Wands"
            },
            "Seven of Wands": {
                "upright": "Courage, determination, and standing your ground. Today, defend your beliefs and values with conviction. Trust in your abilities to overcome challenges and obstacles.",
                "reversed": "Self-doubt, insecurity, and giving up. You may be feeling overwhelmed by opposition or questioning your ability to succeed. Stay strong and persevere.",
                "type": "Wands"
            },
            "Eight of Wands": {
                "upright": "Speed, action, and swift progress. Today, expect rapid developments and exciting opportunities. Stay focused and seize the moment to make progress towards your goals.",
                "reversed": "Delays, frustration, and miscommunication. You may encounter obstacles or setbacks that slow your progress. Stay patient and adaptable.",
                "type": "Wands"
            },
            "Nine of Wands": {
                "upright": "Resilience, perseverance, and strength. Today, stand firm in the face of adversity and keep moving forward. You have the resilience to overcome any challenges.",
                "reversed": "Defensiveness, paranoia, and exhaustion. You may be feeling defensive or worn out from constantly fighting battles. Take time to rest and recharge.",
                "type": "Wands"
            },
            "Ten of Wands": {
                "upright": "Burden, responsibility, and overwhelm. Today, acknowledge the weight of your responsibilities and seek support if needed. Delegate tasks and prioritize self-care.",
                "reversed": "Release, surrender, and lightening the load. You are letting go of burdens and reclaiming your freedom. Focus on what truly matters and release what no longer serves you.",
                "type": "Wands"
            },
            "Page of Wands": {
                "upright": "Inspiration, enthusiasm, and exploration. Today, embrace your adventurous spirit and pursue new opportunities with passion and curiosity. Be open to adventure and spontaneity.",
                "reversed": "Lack of direction, missed opportunities, and impulsiveness. You may be feeling directionless or prone to making rash decisions. Take time to clarify your goals and priorities.",
                "type": "Wands"
            },
            "Knight of Wands": {
                "upright": "Energy, passion, and adventure. Today, embrace your adventurous side and pursue your passions with enthusiasm and confidence. Take bold risks and explore new opportunities.",
                "reversed": "Haste, recklessness, and frustration. Beware of rushing into action without considering the consequences. Take a step back and assess the situation before proceeding.",
                "type": "Wands"
            },
            "Queen of Wands": {
                "upright": "Confidence, independence, and leadership. Today, lead with confidence and assertiveness in your endeavors. Trust your instincts and embrace your inner strength.",
                "reversed": "Self-doubt, egotism, and domineering behavior. You may be feeling insecure or overly controlling in your interactions. Practice humility and open-mindedness.",
                "type": "Wands"
            },
            "King of Wands": {
                "upright": "Charisma, leadership, and vision. Today, lead with passion and inspiration in your pursuits. Trust your instincts and inspire others to follow your lead.",
                "reversed": "Impulsiveness, arrogance, and recklessness. Beware of making hasty decisions or letting your ego get in the way. Stay grounded and consider the consequences of your actions.",
                "type": "Wands"
            },
            "Ace of Pentacles": {
                "upright": "Opportunity, prosperity, and new beginnings. Today, embrace new opportunities for growth and abundance. Plant the seeds for future success with confidence.",
                "reversed": "Missed opportunities, lack of planning, and financial loss. You may be overlooking potential opportunities or failing to invest in your future. Take proactive steps to secure your financial stability.",
                "type": "Pentacles"
            },
            "Two of Pentacles": {
                "upright": "Balance, adaptability, and juggling priorities. Today, find harmony in the midst of chaos by prioritizing your responsibilities and adapting to changing circumstances.",
                "reversed": "Imbalance, disorganization, and overcommitment. You may be feeling overwhelmed by competing demands or struggling to find balance in your life. Simplify your priorities and focus on what truly matters.",
                "type": "Pentacles"
            },
            "Three of Pentacles": {
                "upright": "Teamwork, collaboration, and craftsmanship. Today, work together with others to achieve common goals and bring your vision to life. Celebrate the value of cooperation and shared success.",
                "reversed": "Disconnection, lack of teamwork, and poor quality work. You may encounter obstacles or conflicts in your collaborative efforts. Foster open communication and mutual respect to overcome challenges.",
                "type": "Pentacles"
            },
            "Four of Pentacles": {
                "upright": "Security, stability, and conservatism. Today, focus on building a solid foundation for your future by managing your resources wisely and saving for rainy days.",
                "reversed": "Financial insecurity, greed, and materialism. You may be clinging to material possessions or hoarding resources out of fear. Let go of scarcity mindset and embrace abundance consciousness.",
                "type": "Pentacles"
            },
            "Five of Pentacles": {
                "upright": "Hard times, poverty, and financial loss. Today, acknowledge your struggles and seek support from others. Remember that tough times don't last forever, and better days are ahead.",
                "reversed": "Recovery, spiritual growth, and perseverance. You are overcoming adversity and finding inner strength in challenging times. Have faith in your resilience and trust in the universe's abundance.",
                "type": "Pentacles"
            },
            "Six of Pentacles": {
                "upright": "Generosity, charity, and giving back. Today, share your blessings with others and practice acts of kindness and compassion. Give freely without expecting anything in return.",
                "reversed": "Selfishness, greed, and financial instability. You may be hoarding resources or unwilling to share your blessings with others. Cultivate a spirit of generosity and abundance.",
                "type": "Pentacles"
            },
            "Seven of Pentacles": {
                "upright": "Assessment, patience, and investment. Today, take stock of your progress and evaluate your long-term goals. Have patience and trust that your efforts will bear fruit in due time.",
                "reversed": "Impatience, lack of progress, and unrealistic expectations. You may be feeling frustrated by slow progress or impatient for results. Trust in the process and stay focused on your goals.",
                "type": "Pentacles"
            },
            "Eight of Pentacles": {
                "upright": "Diligence, craftsmanship, and skill development. Today, focus on honing your craft and mastering your skills through hard work and dedication. Strive for excellence in all that you do.",
                "reversed": "Perfectionism, boredom, and lack of focus. You may be feeling uninspired or stuck in a rut. Break free from monotony and embrace new challenges to reignite your passion.",
                "type": "Pentacles"
            },
            "Nine of Pentacles": {
                "upright": "Abundance, luxury, and self-sufficiency. Today, enjoy the fruits of your labor and celebrate your accomplishments. You have created a life of prosperity and independence.",
                "reversed": "Financial loss, self-worth issues, and overindulgence. You may be experiencing setbacks or feeling insecure about your worth. Focus on self-care and gratitude to regain your balance.",
                "type": "Pentacles"
            },
            "Ten of Pentacles": {
                "upright": "Wealth, inheritance, and long-term success. Today, celebrate the stability and security of your family and home life. You have built a legacy of prosperity and abundance.",
                "reversed": "Financial loss, instability, and family discord. You may be experiencing challenges or conflicts within your family or struggling with financial setbacks. Focus on finding common ground and rebuilding stability.",
                "type": "Pentacles"
            },
            "Page of Pentacles": {
                "upright": "Opportunity, manifestation, and practicality. Today, embrace new opportunities for growth and abundance with a grounded and practical approach. Stay open to learning and exploring new possibilities.",
                "reversed": "Missed opportunities, lack of planning, and short-term thinking. You may be overlooking potential opportunities or failing to invest in your future. Take proactive steps to secure your financial stability.",
                "type": "Pentacles"
            },
            "Knight of Pentacles": {
                "upright": "Hard work, responsibility, and diligence. Today, approach your tasks with dedication and reliability. Focus on the long-term rewards of your efforts and stay committed to your goals.",
                "reversed": "Laziness, procrastination, and irresponsibility. Beware of becoming complacent or neglecting your duties. Take ownership of your actions and prioritize your responsibilities.",
                "type": "Pentacles"
            },
            "Queen of Pentacles": {
                "upright": "Practicality, abundance, and nurturing. Today, focus on creating a stable and nurturing environment for yourself and your loved ones. Trust in your ability to provide for your needs and the needs of others.",
                "reversed": "Financial insecurity, self-care neglect, and smothering. You may be neglecting your own needs or suffocating others with your demands. Find balance and prioritize self-care.",
                "type": "Pentacles"
            },
            "King of Pentacles": {
                "upright": "Security, control, and abundance. Today, take charge of your finances and investments with confidence and authority. Trust in your ability to build a solid foundation for long-term success.",
                "reversed": "Financial instability, greed, and materialism. Beware of being overly focused on wealth or using your resources for selfish gain. Cultivate generosity and gratitude to attract abundance.",
                "type": "Pentacles"
            },
        }

    def daily_draw(self):
        card = random.choice(list(self.card_descriptions.keys()))
        orientation = random.choice(["upright", "reversed"])
        description = self.card_descriptions[card][orientation]
        return card, orientation, description

    def fortune_telling(self, category):
        past_card = self.daily_draw()
        present_card = self.daily_draw()
        future_card = self.daily_draw()
        return {
            "category": category,
            "past": past_card,
            "present": present_card,
            "future": future_card
        }

    def predict_date(self, question):
        return date.today() + timedelta(days=random.randint(1, 1000))

    def show_calendar(self, month, year):
        return calendar.month(year, month)

class UserManagement:
    def __init__(self, filename):
        self.filename = filename
        self.users = self.load_users()

    def load_users(self):
        users = {}
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    email, password, name, date_of_birth = data[0], data[1], data[2], data[3]
                    birthtime = data[4] if len(data) > 4 else None
                    users[email] = {'password': password, 'user': User(name, date_of_birth, birth_time=birthtime)}
        except FileNotFoundError:
            pass
        return users

    def save_users(self):
        with open(self.filename, 'w') as file:
            for email, data in self.users.items():
                user = data['user']
                file.write(f"{email},{data['password']},{user.name},{user.date_of_birth.strftime('%m/%d/%Y')},{user.birth_time}\n")

    def register_user(self, email, password, name, date_of_birth, birth_time):
        if email not in self.users:
            self.users[email] = {'password': password, 'user': User(name, date_of_birth, birth_time)}
            self.save_users()
            return True
        return False

    def authenticate_user(self, email, password):
        if email in self.users and self.users[email]['password'] == password:
            return self.users[email]['user']
        return None

class CustomDialog(tk.Toplevel):
    def __init__(self, parent, title="", text=""):
        super().__init__(parent)
        self.title(title)
        self.geometry("400x300")
        self.config(bg="#D7DDDF")
        self.parent = parent
        self.text = text

        tk.Label(self, text=self.text, font=("Arial", 12), bg="#D7DDDF", fg="#6D6970", wraplength=380, justify="left").pack(pady=20)
        tk.Button(self, text="Close", command=self.destroy, font=("Arial", 12), bg="#849CD4", fg="white", bd=0).pack(pady=10)

class CustomChoiceDialog(tk.Toplevel):
    def __init__(self, parent, title="", choices=[]):
        super().__init__(parent)
        self.title(title)
        self.geometry("300x200")
        self.config(bg="#D7DDDF")
        self.parent = parent
        self.choice = None

        tk.Label(self, text="Choose an option:", font=("Arial", 12), bg="#D7DDDF", fg="#6D6970").pack(pady=10)

        for idx, choice in enumerate(choices, start=1):
            tk.Button(self, text=choice, command=lambda c=choice: self.set_choice(c), font=("Arial", 12), bg="#849CD4", fg="white", bd=0).pack(pady=5)

    def set_choice(self, choice):
        self.choice = choice
        self.destroy()

class CompatibilityDialog(tk.Toplevel):
    def __init__(self, parent, user1_zodiac, user2_zodiac, percentage, description):
        super().__init__(parent)
        self.title("Compatibility Result")
        self.geometry("400x300")
        self.config(bg="white")
        self.parent = parent

        tk.Label(self, text="Compatibility Result", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        tk.Label(self, text=f"Your Zodiac Sign: {user1_zodiac}", font=("Arial", 14), bg="white").pack()
        tk.Label(self, text=f"Their Zodiac Sign: {user2_zodiac}", font=("Arial", 14), bg="white").pack()
        tk.Label(self, text=description, wraplength=380, justify='center', font=("Arial", 12), bg="white").pack(pady=10)

        meter_canvas = tk.Canvas(self, width=200, height=200, bg="white")
        meter_canvas.pack()
        meter_canvas.create_arc(50, 50, 150, 150, start=0, extent=3.6*percentage, fill="#849CD4", outline="#849CD4")
        tk.Label(self, text=f"{percentage}%", font=("Arial", 36, "bold"), bg="white").pack(pady=10)

        tk.Button(self, text="Back to Main Menu", command=self.destroy, font=("Arial", 12), bg="#849CD4", fg="white", bd=0).pack(pady=10)
        

class UserSelectionDialog(tk.Toplevel):
    def __init__(self, master, user_names):
        super().__init__(master)
        self.user_names = user_names
        self.result = None
        self.title("Select User")
        self.geometry("300x300")
        self.config(bg="#D7DDDF")
        
        tk.Label(self, text="Select the active user for compatibility check:", font=("Arial", 12, "bold"), bg="#D7DDDF").pack(pady=10)
        
        self.entry = tk.Entry(self, font=("Arial", 12))
        self.entry.pack(pady=5)
        self.entry.focus_set()
        
        self.listbox = tk.Listbox(self, font=("Arial", 12), height=10)
        self.listbox.pack(pady=5)

        for name in user_names:
            self.listbox.insert(tk.END, name)

        self.entry.bind('<KeyRelease>', self.autocomplete)
        self.listbox.bind('<Double-1>', self.select_user)

        tk.Button(self, text="Select", command=self.select_user, font=("Arial", 12), bg="#849CD4", fg="white", bd=0).pack(pady=10)

    def autocomplete(self, event):
        pattern = self.entry.get().lower()
        self.listbox.delete(0, tk.END)
        for name in self.user_names:
            if pattern in name.lower():
                self.listbox.insert(tk.END, name)

    def select_user(self, event=None):
        if self.listbox.curselection():
            self.result = self.listbox.get(self.listbox.curselection())
            self.destroy()

class AstraiOS:
    def __init__(self, user_management):
        self.user_management = user_management
        self.current_user = None
        self.root = tk.Tk()
        self.root.title("AstraiOS")
        self.main_screen()
        self.center_window()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - self.root.winfo_reqwidth()) // 2
        y = (screen_height - self.root.winfo_reqheight()) // 2

        self.root.geometry(f"+{x}+{y}")

    def main_screen(self):
        self.clear_screen()

        self.root.config(bg="white")

        title_label = tk.Label(self.root, text="Welcome to AstraiOS!", font=("Helvetica", 28, "bold"), fg="#849CD4", bg="white")
        title_label.pack(pady=(50, 20))

        logo_image = tk.PhotoImage(file="logo.png")  
        resized_logo = logo_image.subsample(3, 3)  
        logo_label = tk.Label(self.root, image=resized_logo, bg="white")
        logo_label.image = resized_logo
        logo_label.pack()

        create_account_button = tk.Button(self.root, text="Create Account", command=self.create_account, width=20, height=2, bg="#849CD4", fg="white", font=("Helvetica", 14, "bold"), bd=0)
        create_account_button.pack(pady=20)

        log_in_button = tk.Button(self.root, text="Log In", command=self.log_in, width=20, height=2, bg="#76849E", fg="white", font=("Helvetica", 14, "bold"), bd=0)
        log_in_button.pack(pady=10)

        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, width=20, height=2, bg="#8E96A8", fg="white", font=("Helvetica", 14, "bold"), bd=0)
        exit_button.pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_account(self):
        self.clear_screen()
        create_account_window = tk.Toplevel(self.root)
        create_account_window.title("Create Account")
        create_account_window.config(bg="white")
        title_label = tk.Label(create_account_window, text="Create Account", font=("Helvetica", 24, "bold"), fg="#6D6970", bg="white")
        title_label.pack(pady=20)

        email_label = tk.Label(create_account_window, text="Email:", font=("Helvetica", 14), fg="#6D6970", bg="white")
        email_label.pack()
        email_entry = tk.Entry(create_account_window, font=("Helvetica", 14))
        email_entry.pack()

        password_label = tk.Label(create_account_window, text="Password:", font=("Helvetica", 14), fg="#6D6970", bg="white")
        password_label.pack()
        password_entry = tk.Entry(create_account_window, font=("Helvetica", 14), show="*")
        password_entry.pack()

        name_label = tk.Label(create_account_window, text="Name:", font=("Helvetica", 14), fg="#6D6970", bg="white")
        name_label.pack()
        name_entry = tk.Entry(create_account_window, font=("Helvetica", 14))
        name_entry.pack()

        birthdate_label = tk.Label(create_account_window, text="Birthdate (MM/DD/YYYY):", font=("Helvetica", 14), fg="#6D6970", bg="white")
        birthdate_label.pack()
        birthdate_entry = tk.Entry(create_account_window, font=("Helvetica", 14))
        birthdate_entry.pack()

        birthtime_label = tk.Label(create_account_window, text="Birth Time (HH:MM:SS):", font=("Helvetica", 14), fg="#6D6970", bg="white")
        birthtime_label.pack()
        birthtime_entry = tk.Entry(create_account_window, font=("Helvetica", 14))
        birthtime_entry.pack()

        create_account_button = tk.Button(create_account_window, text="Create Account", command=lambda: self.register_user(create_account_window, email_entry.get(), password_entry.get(), name_entry.get(), birthdate_entry.get(), birthtime_entry.get()), width=20, height=2, bg="#849CD4", fg="white", font=("Helvetica", 14, "bold"), bd=0)
        create_account_button.pack(pady=20)

    def register_user(self, window, email, password, name, birthdate, birthtime):
        if self.user_management.register_user(email, password, name, birthdate, birthtime):
            messagebox.showinfo("Success", "Your account has been created successfully! You can now log in and start exploring.")
            window.destroy()  
            self.main_screen()
        else:
            messagebox.showerror("Error", "An account with this email already exists.")

    def log_in(self):
        self.clear_screen()

        login_window = tk.Toplevel(self.root)
        login_window.title("Log In")
        login_window.config(bg="white")

        title_label = tk.Label(login_window, text="Log In", font=("Helvetica", 24, "bold"), fg="#6D6970", bg="white")
        title_label.pack(pady=20)

        email_label = tk.Label(login_window, text="Email:", font=("Helvetica", 14), fg="#6D6970", bg="white")
        email_label.pack()
        email_entry = tk.Entry(login_window, font=("Helvetica", 14))
        email_entry.pack()

        password_label = tk.Label(login_window, text="Password:", font=("Helvetica", 14), fg="#6D6970", bg="white")
        password_label.pack()
        password_entry = tk.Entry(login_window, font=("Helvetica", 14), show="*")
        password_entry.pack()

        login_button = tk.Button(login_window, text="Log In", command=lambda: self.authenticate_user(login_window, email_entry.get(), password_entry.get()), width=20, height=2, bg="#849CD4", fg="white", font=("Helvetica", 14, "bold"), bd=0)
        login_button.pack(pady=20)

    def authenticate_user(self, window, email, password):
        self.current_user = self.user_management.authenticate_user(email, password)
        if self.current_user:
            messagebox.showinfo("Success", f"Welcome back, {self.current_user.name}!")
            window.destroy()  
            self.main_menu()
        else:
            messagebox.showerror("Error", "Invalid email or password.")

    def main_menu(self):
        self.clear_screen()

        main_menu_frame = tk.Frame(self.root, bg="white")
        main_menu_frame.pack(expand=True)

        title_label = tk.Label(main_menu_frame, text="Main Menu", font=("Helvetica", 30, "bold"), fg="#6D6970", bg="white")
        title_label.pack(pady=20)

        astrological_facts_button = tk.Button(main_menu_frame, text="Astrological Facts About You", command=self.get_astrology_facts, font=("Helvetica", 14), bg="#849CD4", fg="white", bd=0)
        astrological_facts_button.pack(pady=10)

        lunar_lens_button = tk.Button(main_menu_frame, text="Lunar Lens, Comets, and Upcoming Celestial Events", command=self.lunarlens, font=("Helvetica", 14), bg="#849CD4", fg="white", bd=0)
        lunar_lens_button.pack(pady=10)

        tarot_reading_button = tk.Button(main_menu_frame, text="Val.AI Tarot Reading", command=self.val_ai_tarot_reading, font=("Helvetica", 14), bg="#849CD4", fg="white", bd=0)
        tarot_reading_button.pack(pady=10)

        compatibility_checker_button = tk.Button(main_menu_frame, text="Cosmic Compatibility Checker", command=self.check_compatibility, font=("Helvetica", 14), bg="#849CD4", fg="white", bd=0)
        compatibility_checker_button.pack(pady=10)

        update_birthday_button = tk.Button(main_menu_frame, text="Update Birthday", command=self.enter_birthday, font=("Helvetica", 14), fg="white", bg="gray", bd=0)
        update_birthday_button.pack(pady=10)

        log_out_button = tk.Button(main_menu_frame, text="Log Out", command=self.log_out, font=("Helvetica", 14), fg="white", bg="gray", bd=0)
        log_out_button.pack(pady=10)

    def get_astrology_facts(self):
        astrology_facts_window = tk.Toplevel(self.root)
        astrology_facts_window.title("Astrology Facts")
        astrology_facts_window.config(bg="#D7DDDF")

        facts = AstrologyFacts(self.current_user)
        zodiac_facts = facts.get_facts()

        title_label = tk.Label(astrology_facts_window, text="Astrology Facts", font=("Helvetica", 24, "bold"), fg="#6D6970", bg="#D7DDDF")
        title_label.pack(pady=20)

        zodiac_label = tk.Label(astrology_facts_window, text=f"Your Zodiac Sign: {self.current_user.get_zodiac_sign()}", font=("Helvetica", 14), fg="#6D6970", bg="#D7DDDF")
        zodiac_label.pack()

        facts_text = tk.Text(astrology_facts_window, font=("Helvetica", 14), wrap="word", bg="#D7DDDF")
        facts_text.insert(tk.END, zodiac_facts)
        facts_text.pack(pady=10, padx=20)
        facts_text.configure(state="disabled")

    def log_out(self):
        self.current_user = None
        messagebox.showinfo("Logged Out", "You have been successfully logged out. Thank you for using AstraiOS!")
        self.main_screen()

    def mark_calendar(self):
        events_2024 = {
            "January": [
                {"date": "Jan 3", "event": "Earth’s Perihelion"},
                {"date": "Jan 3/4", "event": "Quadrantids Meteors"},
                {"date": "Jan 11", "event": "New Moon"},
                {"date": "Jan 12", "event": "Mercury at Greatest Elongation West"},
                {"date": "Jan 25", "event": "Wolf Moon"}
            ],
            "February": [
                {"date": "Feb 9", "event": "Super New Moon"},
                {"date": "Feb 24", "event": "Snow Micromoon"}
            ],
            "March": [
                {"date": "Mar 10", "event": "Super New Moon"},
                {"date": "Mar 20", "event": "March Equinox"},
                {"date": "Mar 22", "event": "Comet 12P/Pons-Brooks"},
                {"date": "Mar 24", "event": "Mercury at Greatest Elongation East"},
                {"date": "Mar 24/25", "event": "Penumbral Lunar Eclipse"},
                {"date": "Mar 25", "event": "Worm Micromoon"}
            ],
            "April": [
                {"date": "Apr 1", "event": "Global Astronomy Month"},
                {"date": "Apr 8", "event": "Total Solar Eclipse"},
                {"date": "Apr 8", "event": "Super New Moon"},
                {"date": "Apr 21/22", "event": "Lyrid Meteor Shower"},
                {"date": "Apr 23", "event": "Pink Moon"}
            ],
            "May": [
                {"date": "May 4/5", "event": "Earthshine Mornings"},
                {"date": "May 5/6", "event": "Eta Aquarid Meteors"},
                {"date": "May 8", "event": "New Moon"},
                {"date": "May 9", "event": "Mercury at Greatest Elongation West"},
                {"date": "May 11/12", "event": "Earthshine Nights"},
                {"date": "May 23", "event": "Flower Moon"}
            ],
            "June": [
                {"date": "Jun 6", "event": "New Moon"},
                {"date": "Jun 20", "event": "June Solstice"},
                {"date": "Jun 22", "event": "Strawberry Moon"}
            ],
            "July": [
                {"date": "Jul 5", "event": "Earth’s Aphelion"},
                {"date": "Jul 5", "event": "New Moon"},
                {"date": "Jul 21", "event": "Buck Moon"},
                {"date": "Jul 22", "event": "Mercury at Greatest Elongation East"}
            ],
            "August": [
                {"date": "Aug 4", "event": "New Moon"},
                {"date": "Aug 12/13", "event": "Perseid Meteors"},
                {"date": "Aug 14", "event": "Conjunction of Mars and Jupiter"},
                {"date": "Aug 19", "event": "Blue Sturgeon Moon"},
                {"date": "Aug 21", "event": "Lunar Occultation of Saturn"},
                {"date": "Aug 28", "event": "Comet Tsuchinshan-ATLAS"}
            ],
            "September": [
                {"date": "Sep 3", "event": "New Moon"},
                {"date": "Sep 5", "event": "Mercury at Greatest Elongation West"},
                {"date": "Sep 8", "event": "Saturn at Opposition"},
                {"date": "Sep 17/18", "event": "Partial Lunar Eclipse"},
                {"date": "Sep 18", "event": "Super Harvest Moon"},
                {"date": "Sep 22", "event": "September Equinox"}
            ],
            "October": [
                {"date": "Oct 2", "event": "Annular Solar Eclipse"},
                {"date": "Oct 2", "event": "Micro New Moon"},
                {"date": "Oct 8/9", "event": "Draconid Meteor Shower"},
                {"date": "Oct 17", "event": "Super Hunter’s Moon"},
                {"date": "Oct 20/21", "event": "Orionid Meteor Shower"}
            ],
            "November": [
                {"date": "Nov 1", "event": "New Moon"},
                {"date": "Nov 15", "event": "Full Moon / Beaver Moon"},
                {"date": "Nov 16", "event": "Mercury at Greatest Elongation East"},
                {"date": "Nov 17/18", "event": "Leonid Meteor Shower"}
            ],
            "December": [
                {"date": "Dec 1", "event": "New Moon"},
                {"date": "Dec 7", "event": "Jupiter at Opposition"},
                {"date": "Dec 14/15", "event": "Geminid Meteors"},
                {"date": "Dec 15", "event": "Cold Moon"},
                {"date": "Dec 21", "event": "December Solstice"},
                {"date": "Dec 22/23", "event": "Ursid Meteors"},
                {"date": "Dec 25", "event": "Mercury at Greatest Elongation West"},
                {"date": "Dec 30", "event": "Black New Moon"}
            ]
        }

        calendar_window = tk.Toplevel(self.root)
        calendar_window.title("Lunar Events Calendar")
        calendar_window.geometry("1000x800") 

        self.center_window()

        canvas = tk.Canvas(calendar_window)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(calendar_window, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor=tk.NW)

        for month, events in events_2024.items():
            label_month = tk.Label(frame, text=month, font=("Arial", 16, "bold"))
            label_month.pack(anchor=tk.CENTER)

            month_calendar = calendar.month(2024, list(calendar.month_abbr).index(month[:3]))
            calendar_label = tk.Label(frame, text=month_calendar, font=("Arial", 12))
            calendar_label.pack(anchor=tk.CENTER)

            event_info = "\n".join([f"{event['date']}: {event['event']}" for event in events])
            event_label = tk.Label(frame, text=event_info, font=("Arial", 12), fg="blue")
            event_label.pack(anchor=tk.CENTER)

        frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox(tk.ALL))

    def lunarlens(self):
        root = tk.Tk()
        root.title("Lunar Lens, Comets, and Upcoming Celestial Events")

        current_date = datetime.datetime.now().date()
        observer = ephem.Observer()
        observer.date = current_date
        moon_phase = ephem.Moon(observer).phase
        lunar_phase = "New Moon" if moon_phase < 0.01 or moon_phase >= 0.99 else "Full Moon"

        messagebox.showinfo("Lunar Lens, Comets, and Upcoming Celestial Events",
                            f"Current Lunar Phase: {lunar_phase}\n"
                            f"Click OK to view the Lunar Events Calendar")

        btn_calendar = tk.Button(self.root, text="View Calendar", command=self.mark_calendar)
        btn_calendar.pack()

        root.mainloop() 

    def val_ai_tarot_reading(self):
        tarot = TarotReading()
        tarot_choice_dialog = CustomChoiceDialog(self.root, title="Tarot Reading", choices=["Daily Draw", "Fortune Telling", "Predict a Date"])
        self.root.wait_window(tarot_choice_dialog)

        if tarot_choice_dialog.choice == "Daily Draw":
            card, orientation, description = tarot.daily_draw()
            self.show_custom_dialog("Daily Tarot Draw", f"Today's Tarot Card: {card} ({orientation})\n\n: {description}")

        elif tarot_choice_dialog.choice == "Fortune Telling":
            category_dialog = CustomDialog(self.root, title="Fortune Telling Category", text="Choose a category: love, career, family, health, fame, friends, hobbies")
            self.root.wait_window(category_dialog)
            category = simpledialog.askstring("Fortune Telling", "Choose a category: love, career, family, health, fame, friends, hobbies")
            fortune = tarot.fortune_telling(category)
            self.show_custom_dialog("Fortune Telling",
                                    f"Category: {fortune['category']}\n\n"
                                    f"PAST:\n {fortune['past'][0]} ({fortune['past'][1]})\nDescription: {fortune['past'][2]}\n\n"
                                    f"PRESENT:\n {fortune['present'][0]} ({fortune['present'][1]})\nDescription: {fortune['present'][2]}\n\n"
                                    f"FUTURE:\n {fortune['future'][0]} ({fortune['future'][1]})\nDescription: {fortune['future'][2]}")

        elif tarot_choice_dialog.choice == "Predict a Date":
            question_dialog = CustomDialog(self.root, title="Tarot Question", text="What question would you like to ask the Tarot about timing?")
            self.root.wait_window(question_dialog)
            question = simpledialog.askstring("Tarot Question", "What question would you like to ask the Tarot about timing?")
            predicted_date = tarot.predict_date(question)
            predicted_month = predicted_date.month
            predicted_year = predicted_date.year
            predicted_calendar_str = tarot.show_calendar(predicted_month, predicted_year)

            card1, orientation1, description1 = tarot.daily_draw()
            card2, orientation2, description2 = tarot.daily_draw()

            self.show_custom_dialog("Tarot Prediction",
                                    f"\nPrediction Date: {predicted_date.strftime('%Y-%m-%d')}\n\n{predicted_calendar_str}\n\n"
                                    f"Card 1: {card1} ({orientation1})\nDescription: {description1}\n\n"
                                    f"Card 2: {card2} ({orientation2})\nDescription: {description2}")

    def show_custom_dialog(self, title, text):
        dialog = CustomDialog(self.root, title=title, text=text)
        self.root.wait_window(dialog)

    def check_compatibility(self):
        if not self.current_user:
            messagebox.showerror("Error", "You must be logged in to use this feature.")
            return

        self.clear_screen()
        tk.Label(self.root, text="Cosmic Compatibility Checker", font=("Arial", 18, "bold"), bg="#D7DDDF").pack(anchor="center")

        choice = messagebox.askyesno("Select Option", "Do you want to select an active user for compatibility check?")
        if choice:
            users = list(self.user_management.users.values())
            active_user_names = [user['user'].name for user in users]

            user_selection_dialog = UserSelectionDialog(self.root, active_user_names)
            self.root.wait_window(user_selection_dialog)

            selected_user = user_selection_dialog.result
            if not selected_user:
                messagebox.showerror("Error", "User not selected.")
                self.main_menu()
                return

            other_user = next((user for user in users if user['user'].name == selected_user), None)
            if not other_user:
                messagebox.showerror("Error", "User not found.")
                self.main_menu()
                return
        else:
            new_birthday = simpledialog.askstring("Enter Birthdate", "Enter the birthdate of the person you want to check compatibility with (MM/DD/YYYY):")
            name = simpledialog.askstring("Enter Name", "Enter the name of the person:")
            other_user = {'user': User(name, new_birthday)}

        user1_birthdate = self.current_user.date_of_birth
        if isinstance(other_user['user'].date_of_birth, str):
            user2_birthdate = datetime.datetime.strptime(other_user['user'].date_of_birth, '%m/%d/%Y').date()
        else:
            user2_birthdate = other_user['user'].date_of_birth

        compatibility_percentage = random.randint(1, 100)

        other_user_name = other_user['user'].name

        description = ""
        if compatibility_percentage <= 10:
            description = f"Your compatibility with {other_user_name} is quite low. You might face significant challenges in this relationship. However, with patience and effort, it can still work out."
        elif compatibility_percentage <= 30:
            description = f"Your compatibility with {other_user_name} is moderate. There are some obstacles, but with mutual understanding and communication, you may overcome them."
        elif compatibility_percentage <= 50:
            description = f"Your compatibility with {other_user_name} is fair. It could go either way, depending on how much effort both parties are willing to put into the relationship."
        elif compatibility_percentage <= 70:
            description = f"Your compatibility with {other_user_name} is good. You have much in common and share similar values, which can lead to a harmonious relationship."
        elif compatibility_percentage <= 90:
            description = f"Your compatibility with {other_user_name} is great. You are highly compatible and share a deep connection. Your relationship is likely to be very fulfilling and rewarding."
        else:
            description = f"Your compatibility with {other_user_name} is excellent. You are a perfect match and complement each other in every way. Your relationship is destined for success and happiness."

        CompatibilityDialog(self.root, self.current_user.get_zodiac_sign(), other_user['user'].get_zodiac_sign(), compatibility_percentage, description)
        self.main_menu()
        return
    
    def enter_birthday(self):
        if not self.current_user:
            messagebox.showerror("Error", "You must be logged in to use this feature.")
            return
        self.clear_screen()
        tk.Label(self.root, text="Update Birthday", font=("Arial", 18, "bold")).pack(anchor="center")
        new_birthday = simpledialog.askstring("Enter New Birthday", "Enter your new birthdate (MM/DD/YYYY):")
        self.current_user.date_of_birth = datetime.datetime.strptime(new_birthday, '%m/%d/%Y').date()
        self.user_management.save_users()
        messagebox.showinfo("Success", "Your birthday has been updated successfully!")
        self.main_menu()


def main():
    user_management = UserManagement('users.txt')
    app = AstraiOS(user_management)
    app.root.mainloop()

if __name__ == "__main__":
    main()