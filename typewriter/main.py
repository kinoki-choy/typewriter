import os
import time
import json

import tomllib
import pyperclip
from openai import OpenAI
from string import Template
from Levenshtein import distance

from rich.console import Console
console = Console(log_path=False)

from pynput import keyboard
from pynput.keyboard import Key, Controller
controller = Controller()

config_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.toml')
config = tomllib.load(open(config_filepath, 'rb'))


def typewriter(singlish:bool):
    singlish = singlish
    client = OpenAI(
        base_url='http://localhost:11434/v1' if 'gpt' not in config['model'] else None,
        api_key=os.environ.get('OPENAI_API_KEY')
    )

    def get_input() -> None:
        with controller.pressed(Key.cmd):
            controller.tap('c')
        time.sleep(0.1)
        return pyperclip.paste()

    def process(singlish:bool, mode:str, text:str) -> str:
        if not text: return
        response = client.chat.completions.create(
            model=config['model'],
            response_format={ 'type': 'json_object' },
            messages=[
                {
                    'role': 'user',
                    'content': Template(config['templates'][mode]).substitute(
                        text=text,
                        singlish_prompt='please preserve the words' if singlish else 'please translate it'
                    )
                },
            ]
        )
        content = json.loads(response.choices[0].message.content)
        if mode == 'correction':
            content.update({
                'levenshtein_distance': distance(text, content['correction'])
            })
        console.log(content)
        return content

    def copy_and_paste(text):
        pyperclip.copy(text)
        time.sleep(0.1)
        with controller.pressed(Key.cmd):
            controller.tap('v')

    def correction():
        res = process(singlish, mode='correction', text=get_input())
        copy_and_paste(res['correction'])

    def translation():
        # Toggling singlish mode off produces better translation results
        res = process(singlish=False, mode='translation', text=get_input())
        copy_and_paste(res['translation'])

    # Set up keyboard listeners
    with keyboard.GlobalHotKeys({
        config['hotkeys']['correction']: correction,
        config['hotkeys']['translation']: translation,
    }) as hotkeys:
        hotkeys.join()

if __name__ == '__main__':
    console.log('Typewriter started...', style='bold bright_cyan')
    # start the clipboard in a clean state
    pyperclip.copy(' ')
    typewriter(singlish=True)