url = "https://test/test.html" # тут меняем страницу, на которой хотим проверить

# Resolutions to check
resolutions = [
    {"width": 1920, "height": 1080, "deviceScaleFactor": 1, "mobile": False},
    {"width": 1440, "height": 900, "deviceScaleFactor": 1, "mobile": False},
    {"width": 1280, "height": 768, "deviceScaleFactor": 1, "mobile": False},
    {"width": 768, "height": 1024, "deviceScaleFactor": 1, "mobile": False},
    {"width": 375, "height": 812, "deviceScaleFactor": 1, "mobile": False},
]

# element_types отвечает за количество проверяемых элементов, в скобки нужно вставить те элементы css, которые будут проверятся
element_types = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'text1', 'text2', 'text3', 'text4']

expected_fonts = {
    'h1': { # Это элемент css, который нужно вставить в element_types, если он будет проверятся
        '1920': {
            'font-size': '100px',                               # тут меняем размер шрифта на 1920
            'font-family': 'Road Radio',                        # тут меняем сам шрифт на 1920
            'font-weight': '700',                               # тут меняем толшину шрифта на 1920
            'color': 'rgba(244, 240, 230, 1)'                   # тут меняем цвет шрифта на 1920
        },                                                      # подобным образом можно добавить ещё значений styles для проверок, например 'margin-left'
        '1440': {
            'font-size': '72px',
            'font-family': 'roadradio',
            'font-weight': '700',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1280': {
            'font-size': '64px',
            'font-family': 'Road Radio',
            'font-weight': '700',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '768': {
            'font-size': '60px',
            'font-family': 'Road Radio", Arial',
            'font-weight': '700',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '375': {
            'font-size': '40px',
            'font-family': 'Road Radio',
            'font-weight': '700',
            'color': 'rgba(244, 240, 230, 1)'
            },
    },
    'h2': {
        '1920': {
            'font-size': '64px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1440': {
            'font-size': '48px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1280': {
            'font-size': '42px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '768': {
            'font-size': '36px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '375': {
            'font-size': '26px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
            },
    },
    'h3': {
        '1920': {
            'font-size': '52px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1440': {
            'font-size': '40px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1280': {
            'font-size': '36px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '768': {
            'font-size': '32px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '375': {
            'font-size': '24px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
            },
    },
    'h4': {
        '1920': {
            'font-size': '40px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1440': {
            'font-size': '30px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1280': {
            'font-size': '24px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '768': {
            'font-size': '20px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '375': {
            'font-size': '20px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
            },
    },
    'h5': {
        '1920': {
            'font-size': '32px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1440': {
            'font-size': '26px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1280': {
            'font-size': '24px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '768': {
            'font-size': '20px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '375': {
            'font-size': '20px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
            },
    },
    'h6': {
        '1920': {
            'font-size': '28px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1440': {
            'font-size': '24px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1280': {
            'font-size': '24px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '768': {
            'font-size': '20px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '375': {
            'font-size': '20px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
            },
    },
    'h7': {
        '1920': {
            'font-size': '20px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1440': {
            'font-size': '16px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1280': {
            'font-size': '16px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '768': {
            'font-size': '14px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '375': {
            'font-size': '14px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
            },
    },
    'h8': {
        '1920': {
            'font-size': '26px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1440': {
            'font-size': '20px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1280': {
            'font-size': '18px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '768': {
            'font-size': '20px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '375': {
            'font-size': '20px',
            'font-family': '"Road Radio", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
            },
    },
    'text1': {
        '1920': {
            'font-size': '24px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1440': {
            'font-size': '18px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1280': {
            'font-size': '18px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '768': {
            'font-size': '16px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '375': {
            'font-size': '16px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
            },
    },
    'text2': {
        '1920': {
            'font-size': '20px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1440': {
            'font-size': '16px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1280': {
            'font-size': '16px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '768': {
            'font-size': '16px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '375': {
            'font-size': '16px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
            },
    },
    'text3': {
        '1920': {
            'font-size': '16px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1440': {
            'font-size': '14px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1280': {
            'font-size': '14px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '768': {
            'font-size': '14px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '375': {
            'font-size': '12px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
            },
    },
    'text4': {
        '1920': {
            'font-size': '14px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1440': {
            'font-size': '14px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '1280': {
            'font-size': '12px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '768': {
            'font-size': '12px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
        },
        '375': {
            'font-size': '12px',
            'font-family': '"Montserrat", Arial, sans-serif',
            'font-weight': '400',
            'color': 'rgba(244, 240, 230, 1)'
            },
    },
}
