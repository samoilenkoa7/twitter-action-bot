import PySimpleGUI as sg
import app

sg.theme('Black')

def make_window(theme=None):
    if theme:
        sg.theme(theme)
    layout = [
        [sg.Text('Twitter bot')],
        [sg.T('Choose file with twitter accounts'), sg.T('Enter the twitter link')],
        [sg.FileBrowse('Choose the path to "twitter.txt"', key='twitter_accs'),
         sg.Input('In format "https://twitter.com..."', key='post_url')],
        [sg.T('Theme:', pad=((3, 0), 0)),
         sg.B('Change them', key='Change Theme'), sg.Submit(),
         sg.Cancel()]
    ]
    return sg.Window('Twitter Bot', layout)



def main():
    window = make_window()

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'Change Theme':
            event, values = sg.Window('Choose Theme',
                                      [[sg.Combo(sg.theme_list(), readonly=True, k='-THEME LIST-'), sg.OK(),
                                        sg.Cancel()]]
                                      ).read(close=True)
            if event == 'OK':
                window.close()
                window = make_window(values['-THEME LIST-'])
        if event == 'Submit':
            app.app(file=values['twitter_accs'], twit_link=values['post_url'])
            sg.popup('Completed')
    window.close()

if __name__ == '__main__':
    main()

