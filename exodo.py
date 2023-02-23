from time import sleep
import pyautogui as pt
import pyperclip
from pynput.mouse import Controller
from selenium import webdriver
from selenium.webdriver.common.by import By

while True:

    browser = webdriver.Firefox()
    browser.set_window_size(1024, 600)
    browser.maximize_window()
    browser.get('https://clubedetran.com.br/simuladao/')
    pt.FAILSAFE = True
    mouse = Controller()


    def nav_to_image(image, clicks, off_x=0, off_y=0):
        position = pt.locateCenterOnScreen(image)

        if position is None:
            print(f'{image} not found...!')
            return 0
        else:
            pt.moveTo(position, duration=3)
            pt.moveRel(off_x, off_y, duration=.2)
            pt.click(clicks=clicks, interval=.1)


    def start_exam():
        browser.find_element(By.XPATH,
                             '/html/body/div[2]/div/div[1]/main/article/div/div[2]/div[3]/div[4]/div/input').click()


    def close_ad():
        nav_to_image('./images/close_ad.png', 1)


    def check_box():
        nav_to_image('./images/mark.png', 1)


    def submit():
        nav_to_image('./images/submit.png', 1)
        # browser.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/main/article/div/div[2]/div[3]/div[13]/ol/li[
        # 1]/input[2]').click()


    def next_step():
        nav_to_image('./images/next.png', 1)
        # browser.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/main/article/div/'div[2]/div[3]/div[13]/ol/li[
        # 1]/input[3]').click()


    def find_correct():
        nav_to_image('./images/correct_2.png', 2, off_x=-23)


    def begin_copy():
        nav_to_image('./images/yellow_square.png', 0, off_x=-150,
                     off_y=130)


    def drag_copy():
        pt.mouseDown()
        nav_to_image('./images/submit.png', 0)
        pt.mouseUp()
        # pt.dragTo(430, 1055, 3, button='left')


    def scroll():
        pt.scroll(-1400)


    def copy():
        pt.keyDown('ctrl')
        pt.press('c')
        pt.keyUp('ctrl')


    def paste():
        file = open('perguntas_db.txt', 'a')
        file.write(pyperclip.paste())

    def response():
        file = open('perguntas_db.txt', 'a')
        file.write('RESPOSTA: ')

    def line():
        file = open('perguntas_db.txt', 'a')
        file.write('\n')
        file.write('\n')
        file.write('-' * 120)
        file.write('\n')
        file.write('\n')

    def opening():
        sleep(3)
        close_ad()
        sleep(10)
        start_exam()
        scroll()
        sleep(2)


    def get_question():
        begin_copy()
        sleep(1)
        drag_copy()
        sleep(1)
        copy()
        sleep(1)
        paste()
        sleep(1)
        submit()
        sleep(1)
        find_correct()
        sleep(1)
        copy()
        sleep(1)
        response()
        sleep(1)
        paste()
        sleep(1)
        line()
        sleep(1)
        next_step()


    opening()
    for count in range(40):
        get_question()
    browser.close()
    print('40 perguntas adicionadas!')
