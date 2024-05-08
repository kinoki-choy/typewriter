**Typewriter on steroids**

<img src='assets/typewriter.png' width='130'>

With the help of LLM, you can do these as you type
* Fix sentences with typo, casing, grammar and punctuation errors
* Translate text from English to Traditional Chinese(zh-tw)

**Demo**

https://github.com/kinoki-choy/typewriter/assets/128534974/7b58a7e8-5b47-4178-9bb4-50b587dc0ddc

Singlish mode off

https://github.com/kinoki-choy/typewriter/assets/128534974/5e826670-a73b-4aee-b27d-f50f31b32e20

**Installation**
```
poetry install
```

**Usage**

```
# Activate virtual environment
poetry shell
```
```
# Run it as per normal with stdout feedback
python typewriter/main.py
[11:50:22] Typewriter started...
[11:50:24] {
               'original': 'never di  antyhging by hakves if you wnat to get wawat wit hti.\nBe outrageous',
               'correction': 'Never do anything by halves if you want to get away with it.\nBe outrageous',
               'levenshtein_distance': 14
           }
[11:50:26] {
               'original': 'never do anything by halves if you want to get way with it.\nBe outrageous',
               'correction': 'Never do anything by halves if you want to get away with it.\nBe outrageous',
               'translation': '如果你想要成功，就不要半途而廢。\n勇於突破常規'
           }
```
```
# Alternatively, run it in the background using nohup and write to a log
nohup python typewriter/main.py > typewriter.log &
[1] 593658
nohup: ignoring input and redirecting stderr to stdout
```

**Hotkeys setup**

The default configuration listens to the following hotkeys:

`<cmd>+<alt>` Perform correction

`<cmd>+<ctrl>` Perform translation

To customise the hotkeys, refer to `config.toml`.

**Wah lau eh, what la?**

You can never remove singlish from a true blue Singaporean. Majority of Singaporeans can also code-switch effectively.

If you want to preserves Singlish terms and not translate them.
`typewriter(singlish=True)`
```
{
    'original': 'alamak...you know or nto one leh? the msot shiok dinner in teh worridd is actsully relattive bwecause eavh fof us warthc diffetnte shopw opn oru screenss whiel eating.',
    'correction': 'Alamak... you know or not one leh? The most shiok dinner in the world is actually relative because each of us watch different shows on our screens while eating.',
}
```

If you want to be understood by rest of the world.
`typewriter(singlish=False)`
```
{
    'original': 'alamak...you know or nto one leh? the msot shiok dinner in teh worridd is actsully relattive bwecause eavh fof us warthc diffetnte shopw opn oru screenss whiel eating.',
    'correction': 'Oh my...do you know? The most delicious dinner in the world is actually relative because each of us watch different shows on our screens while eating.',
}
```

**Translation Mode**

It's strongly recommended to turn singlish off in translation mode in order to get a higher accuracy rate as the LLM tends to translate it phonetically.


**LLM Dependency**

Ollama has built-in compatibility with OpenAI API. The same client API can be used for making requests to ChatGPT and Ollama on premise.


**Credits**

Typewriter vector by <a href="https://www.vecteezy.com/free-png/typewriter">Vecteezy</a>.
