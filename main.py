import re



text = """
        Da-da-da, da-da-da
        Da-da-da, da-da-da
        Let it never be said that romance is dead 
        'Cause there's so little else occupying my head 
        There is nothing I need, 'cept the function to breathe 
        But I'm not really fussed, doesn't matter to me
        Ruby, Ruby, Ruby, Ruby (ah-ah-ah-ah-ah-ah)
        Do ya, do ya, do ya, do ya (ah-ah-ah-ah-ah-ah)
        Know what your doing, doing to me? (Ah-ah-ah-ah-ah-ah)
        Ruby, Ruby, Ruby, Ruby (ah-ah-ah-ah-ah-ah)
        Due to lack of interest 
        Tomorrow is canceled 
        Let the clocks be reset and the pendulums held 
        'Cause there's nothing at all, 'cept the space in between 
        Finding out what you're called, and repeating your name
    """

list(map(lambda x: print(f'Количество Ruby в тексте -- {x}'), [len(re.findall(fr"\b{input('Введите: ')}\b", text))]))




