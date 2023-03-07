from flet import *
import os
import asyncio
import openai
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
openai.api_key = api_key
bg = '#444654'
fg = '#202123'
side_bar_width = 260


class Main(UserControl):
    def __init__(self, page: Page,):
        page.padding = 0
        page.title = 'ChatGPT'
        page.theme = Theme(color_scheme_seed="green")
        page.update()
        self.blinking = False
        self.chat_response = ''

        self.page = page
        self.prompt = [
            {
                "role": "system",
                'content': 'As a large AI language model. You know almost everything. Your job is to provide solution / suggestion to problems.'
            }
        ]
        self.init()

    def init(self):
        self.chat_gpt_label = Container(
            padding=padding.only(top=120),
            alignment=alignment.center,
            content=Text(
                value='ChatGPT',
                size=35, weight=FontWeight.BOLD,
            )
        )
        self.cursor = Container(
            width=8, height=20, bgcolor='white', )
        self.message_field = TextField(
            border=InputBorder.NONE,
            expand=True,
            multiline=True,
            content_padding=0,
            # max_lines=5,
            # max_length=100,
            # min_lines=5,


        )

        self.side_bar = Container(
            width=side_bar_width,
            bgcolor=fg,
            padding=8,
            content=Column(
                controls=[
                    Container(
                        on_hover=self.new_chat_hover,
                        height=45,
                        border_radius=8,
                        border=border.all(
                            width=1, color='#4d4d4f'),
                        padding=8,
                        content=Row(
                            controls=[
                                Icon(
                                    icons.ADD,
                                    size=14,
                                ),
                                Text(
                                    value='New Chat',
                                    weight=FontWeight.W_100
                                )
                            ]
                        )

                    ),

                    Column(
                        expand=True,

                        controls=[

                            Container(
                                on_hover=self.hover,
                                height=45,
                                border_radius=8,

                                padding=8,
                                content=Row(
                                    # spacing=14,
                                    controls=[
                                        Icon(
                                            icons.CHAT_BUBBLE_OUTLINE_ROUNDED,
                                            size=16,
                                        ),
                                        Text(
                                            value='how to become a very good scientist',
                                            weight=FontWeight.W_100,
                                            width=200,
                                            no_wrap=True,
                                            size=16,

                                        )
                                    ]
                                )

                            ),

                        ]
                    ),

                    # Container(height=0.2, bgcolor='#4d4d4f'),

                    Divider(color='#4d4d4f', height=1),



                    Container(
                        on_hover=self.new_chat_hover,
                        height=45,
                        border_radius=8,
                        padding=8,
                        content=Row(
                            controls=[
                                Icon(
                                    icons.DELETE_OUTLINE_OUTLINED,
                                    size=18,
                                ),
                                Text(
                                    value='Clear conversations',
                                    weight=FontWeight.W_100
                                )
                            ]
                        )

                    ),
                    Container(
                        on_hover=self.new_chat_hover,
                        height=45,
                        border_radius=8,
                        padding=8,
                        content=Row(
                            alignment='spaceBetween',
                            controls=[
                                Row(
                                      controls=[
                                          Icon(
                                              icons.PERSON_OUTLINE_OUTLINED,
                                              size=18,
                                          ),
                                          Text(
                                              value='Upgrade to Plus',
                                              weight=FontWeight.W_100
                                          ),
                                      ]
                                ),
                                Container(
                                    width=40, height=20, bgcolor='#fae69e', border_radius=5,
                                    alignment=alignment.center,
                                    content=Text(
                                        'NEW', size=12, color=fg
                                    )
                                ),
                            ]
                        )

                    ),
                    Container(
                        on_hover=self.new_chat_hover,
                        height=45,
                        border_radius=8,
                        padding=8,
                        content=Row(
                            controls=[
                                Icon(
                                    icons.OPEN_IN_NEW_OUTLINED,
                                    size=18,
                                ),
                                Text(
                                    value='Updates & FAQ',
                                    weight=FontWeight.W_100
                                ),
                            ]
                        )

                    ),
                    Container(
                        on_hover=self.new_chat_hover,
                        height=45,
                        border_radius=8,
                        padding=8,
                        content=Row(
                            controls=[
                                Icon(
                                    icons.LOGOUT_OUTLINED,
                                    size=18,
                                ),
                                Text(
                                    value='Logout',
                                    weight=FontWeight.W_100
                                ),
                            ]
                        )

                    ),

                ]
            ),
        )

        self.content_area = Column(
            auto_scroll=True,
            spacing=30,
            scroll='auto',
            controls=[
                self.chat_gpt_label,
                Row(
                    alignment='center',
                    controls=[
                        Column(
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    content=Column(
                                        horizontal_alignment='center',
                                        controls=[
                                            Icon(icons.BRIGHTNESS_7_OUTLINED),
                                            Text('Examples')
                                        ]
                                    )
                                ),
                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    # height=100,
                                    padding=padding.only(
                                        top=20, bottom=30, left=20, right=20),
                                    border_radius=8,
                                    on_hover=self.hover2,
                                    bgcolor='#3e3f4b',
                                    content=Text(
                                        '"Explain quantum computing in simple terms"',
                                        text_align='center',
                                    )
                                ),

                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    # height=100,
                                    padding=padding.only(
                                        top=20, bottom=30, left=20, right=20),
                                    border_radius=8,
                                    on_hover=self.hover2,
                                    bgcolor='#3e3f4b',
                                    content=Text(
                                        '"Got any creative ideas for a 10 year old\'s birthday?"',
                                        text_align='center',
                                    )
                                ),

                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    # height=100,
                                    padding=padding.only(
                                        top=20, bottom=30, left=20, right=20),
                                    border_radius=8,
                                    on_hover=self.hover2,
                                    bgcolor='#3e3f4b',
                                    content=Text(
                                        '"How do I make an HTTP request in JavaScript?"',
                                        text_align='center',
                                    )
                                ),

                            ]
                        ),
                        Column(
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    content=Column(
                                        horizontal_alignment='center',
                                        controls=[
                                            Icon(icons.FLASH_ON_OUTLINED),
                                            Text('Capabilities')
                                        ]
                                    )
                                ),
                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    # height=100,
                                    padding=padding.only(
                                        top=20, bottom=30, left=20, right=20),
                                    border_radius=8,
                                    on_hover=self.hover2,
                                    bgcolor='#3e3f4b',
                                    content=Text(
                                        'Remember what user said earlier in the conversation',
                                        text_align='center',
                                    )
                                ),

                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    # height=100,
                                    padding=padding.only(
                                        top=20, bottom=30, left=20, right=20),
                                    border_radius=8,
                                    on_hover=self.hover2,
                                    bgcolor='#3e3f4b',
                                    content=Text(
                                        'Allows user to provide follow-up corrections',
                                        text_align='center',
                                    )
                                ),

                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    # height=100,
                                    padding=padding.only(
                                        top=20, bottom=30, left=20, right=20),
                                    border_radius=8,
                                    on_hover=self.hover2,
                                    bgcolor='#3e3f4b',
                                    content=Text(
                                        'Trained to decline inappropriate requests',
                                        text_align='center',
                                    )
                                ),

                            ]
                        ),
                        Column(
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    content=Column(
                                        horizontal_alignment='center',
                                        controls=[
                                            Icon(icons.DANGEROUS_OUTLINED),
                                            Text('Limitations')
                                        ]
                                    )
                                ),
                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    # height=100,
                                    padding=padding.only(
                                        top=20, bottom=30, left=20, right=20),
                                    border_radius=8,
                                    on_hover=self.hover2,
                                    bgcolor='#3e3f4b',
                                    content=Text(
                                        'May occationally generate incorrect information',
                                        text_align='center',
                                    )
                                ),

                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    # height=100,
                                    padding=padding.only(
                                        top=20, bottom=30, left=20, right=20),
                                    border_radius=8,
                                    on_hover=self.hover2,
                                    bgcolor='#3e3f4b',
                                    content=Text(
                                        'May occasionally produce harmful instruction or biased content',
                                        text_align='center',
                                    )
                                ),

                                Container(
                                    alignment=alignment.center,
                                    width=250,
                                    # height=100,
                                    padding=padding.only(
                                        top=20, bottom=30, left=20, right=20),
                                    border_radius=8,
                                    on_hover=self.hover2,
                                    bgcolor='#3e3f4b',
                                    content=Text(
                                        'Limited knowledge of world and events after 2021',
                                        text_align='center',
                                    )
                                ),

                            ]
                        ),
                    ]
                )



            ]
        )

        self.main_content = Container(
            padding=padding.only(top=20,),
            expand=True,
            bgcolor=bg,
            content=Column(
                alignment='spaceBetween',
                horizontal_alignment='center',
                controls=[
                    Container(
                        width=1000,
                        expand=True,
                        content=self.content_area


                    ),

                    Container(
                        margin=margin.only(top=30),
                        height=100,
                        content=Column(
                            horizontal_alignment='center',
                            spacing=0,
                            controls=[
                                Card(
                                    elevation=5,
                                    content=Container(
                                        border_radius=10,
                                        bgcolor='#40414f',
                                        padding=padding.only(
                                            top=5, right=4, left=10, bottom=5),
                                        height=50,
                                        width=1000,
                                        content=Row(
                                            controls=[
                                                self.message_field,
                                                Container(
                                                    on_click=self.send_clicked,
                                                    height=40,
                                                    width=40,
                                                    content=Icon(
                                                        icons.SEND,
                                                    ),
                                                    on_hover=self.hover,
                                                    border_radius=8

                                                )
                                            ]
                                        )
                                    )
                                ),
                                Row(
                                    expand=True,
                                    controls=[
                                        Text(
                                            expand=True,
                                            value='This is running on free plan. Created by @1mrnewton on YouTube',
                                            text_align='center'
                                        )
                                    ]
                                )
                            ]
                        )


                    ),

                ]
            )


        )

        self.page.add(
            Container(
                expand=True,
                bgcolor=bg,
                content=Row(
                    spacing=0,
                    controls=[
                        self.side_bar,
                        self.main_content,
                    ]
                )

            )
        )

    def new_chat_hover(self, e: HoverEvent):
        if e.data == 'true':
            e.control.bgcolor = '#2b2c2f'
        else:
            e.control.bgcolor = None
        e.control.update()

    def hover(self, e):
        if e.data == 'true':
            e.control.bgcolor = '#2a2b32'
        else:
            e.control.bgcolor = None
        e.control.update()

    def hover2(self, e):
        if e.data == 'true':
            e.control.bgcolor = '#2a2b32'
        else:
            e.control.bgcolor = '#3e3f4b'
        e.control.update()

    def send_clicked(self, e: TapEvent):
        message = self.message_field.value
        if message != '':
            self.message_field.value = ''
            self.message_field.update()

            if self.chat_gpt_label in self.content_area.controls:
                self.content_area.controls.clear()
                self.content_area.update()

            gpt_message = Row(
                vertical_alignment='center',
                controls=[
                    Container(
                        height=35, width=35,
                        content=Image(
                            src='assets/chatgpt.png',
                            fit=ImageFit.COVER,
                        )

                    ),
                    self.cursor
                ]
            )

            response_label = Text('', expand=True, size=16)
            if self.blinking is False:
                self.blinking = True

                self.content_area.controls.append(
                    Container(
                        bgcolor='#343541',
                        padding=padding.only(
                                top=20, bottom=60, left=20, right=20
                        ),
                        content=Row(
                            controls=[
                                Container(
                                    border_radius=8,
                                    clip_behavior=ClipBehavior.ANTI_ALIAS,
                                    height=35, width=35,
                                    content=Image(
                                        src='assets/user.png',
                                        fit=ImageFit.COVER,
                                    )

                                ),
                                Text(
                                    message,
                                    expand=True,
                                    size=16,
                                    selectable=True
                                )
                            ]
                        )
                    )

                )
                self.content_area.update()

                sleep(.1)

                self.content_area.controls.append(
                    Container(
                        padding=padding.only(
                            top=20, bottom=10, left=20, right=20),

                        content=gpt_message
                    ),
                )
                self.content_area.update()

                t = threading.Thread(target=self.blink)
                t.start()

                chat_response = self.call_chatgpt(message)

                self.blinking = False
                sleep(0.4)
                self.blinking = True
                if self.cursor in gpt_message.controls:
                    gpt_message.controls.remove(self.cursor)
                    gpt_message.update()
                if response_label not in gpt_message.controls:
                    gpt_message.controls.append(response_label)
                    gpt_message.vertical_alignment = 'start'
                    gpt_message.update()
                    for char in chat_response:
                        response_label.value += char
                        response_label.update()
                        sleep(0.02)
                self.blinking = False

    def call_chatgpt(self, text):
        self.prompt.append(
            {
                "role": "user",
                "content": text
            }
        )
        print(self.prompt)
        completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=self.prompt
        )
        chat_response = completion.choices[0].message.content
        self.prompt.append(
            {
                'role': 'assistant',
                'content': chat_response
            }
        )
        return chat_response

    def blink(self,):
        while True:
            if self.blinking == False:
                break
            if self.cursor.opacity == 100:
                self.cursor.opacity = 0
            else:
                self.cursor.opacity = 100
            self.cursor.update()

            sleep(.4)


app(target=Main, assets_dir='assets')
