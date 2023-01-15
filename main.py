import pygame
import pygame_gui
import sys
from models import *


# constants
WIDTH = 1000
HEIGHT = 700
CELL_X = WIDTH / 10
CELL_Y = HEIGHT / 10
BUTTON_W = CELL_X * 2
BUTTON_H = CELL_Y


pygame.init()

pygame.display.set_caption("Quick Start")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz Game")
Icon = pygame.image.load("Assets/writing.png")
pygame.display.set_icon(Icon)
# bg image
bgImg = pygame.image.load("Assets/bground.jpg")
bgImg = pygame.transform.scale(bgImg, (WIDTH, HEIGHT))

clock = pygame.time.Clock()  # clock

# create user object
user = User()
# global
currentUser = user.getUser()


def background():
    screen.blit(bgImg, (0, 0))


def exit_window(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()


def main_menu():
    global currentUser
    uiManager = pygame_gui.UIManager((WIDTH, HEIGHT), "Assets/theme.json")

    # UI elements
    headerImg = pygame.image.load("Assets/QuizGameTitle.png")
    header = pygame_gui.elements.UIImage(
        relative_rect=pygame.Rect(
            ((CELL_X * 5) - ((CELL_X * 5) / 2), 0, CELL_X * 5, CELL_Y * 2),
        ),
        image_surface=headerImg,
        manager=uiManager,
    )

    login_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (CELL_X * 2, CELL_Y * 3, BUTTON_W, BUTTON_H),
        ),
        text="Login",
        manager=uiManager,
    )

    register_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (CELL_X * 6, CELL_Y * 3, BUTTON_W, BUTTON_H),
        ),
        text="Register",
        manager=uiManager,
    )

    play_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (CELL_X * 2, CELL_Y * 5, BUTTON_W, BUTTON_H),
        ),
        text="Play",
        manager=uiManager,
    )

    score_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (CELL_X * 6, CELL_Y * 5, BUTTON_W, BUTTON_H),
        ),
        text="Scores",
        manager=uiManager,
    )

    if currentUser["username"] == "":
        play_button.hide()
        score_button.hide()
    else:
        play_button.show()
        score_button.show()

    while True:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            exit_window(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == register_button:
                    register_screen()
                if event.ui_element == login_button:
                    login_screen()
                if event.ui_element == play_button:
                    subjects_screen()
                if event.ui_element == score_button:
                    score_screen()

            uiManager.process_events(event)

        # draw background
        background()

        # update UI manager
        uiManager.update(time_delta)
        uiManager.draw_ui(screen)

        # draw buttons

        pygame.display.update()


# register screen
def register_screen():
    global currentUser
    uiManager = pygame_gui.UIManager((WIDTH, HEIGHT), "Assets/theme.json")

    # ui elements
    main_menu_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (20, 20, BUTTON_W, BUTTON_H / 1.5),
        ),
        text="Main Menu",
        manager=uiManager,
        object_id="@sm_btn",
    )

    # text inputs
    username_entry = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect(CELL_X * 3, CELL_Y * 2, CELL_X * 4, CELL_Y),
        manager=uiManager,
    )
    username_entry.set_text("enter username here")

    password_entry = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect(CELL_X * 3, (CELL_Y * 3) + 20, CELL_X * 4, CELL_Y),
        manager=uiManager,
    )
    password_entry.set_text_hidden(is_hidden=True)

    # register button on register screen
    register_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (CELL_X * 3, CELL_Y * 5, CELL_X * 4, CELL_Y),
        ),
        text="Register",
        manager=uiManager,
    )

    # validation msg
    msg = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect(
            (CELL_X * 3, CELL_Y, CELL_X * 4, CELL_Y),
        ),
        text="",
        manager=uiManager,
        object_id="@errors",
    )

    while True:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            exit_window(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == main_menu_button:
                    main_menu()

                if event.ui_element == register_button:
                    currentUser["username"] = username_entry.get_text()
                    currentUser["password"] = password_entry.get_text()
                    user.setUser(currentUser)
                    if user.validate():
                        if user.isExists() == False:
                            user.save()
                            main_menu()
                        else:
                            msg.set_text("This username already taken :(")
                            username_entry.set_text("")
                            password_entry.set_text("")
                    else:
                        msg.set_text("Invalid Data please enter again")
                        username_entry.set_text("")
                        password_entry.set_text("")

            uiManager.process_events(event)

        # draw background
        background()

        # update UI manager
        uiManager.update(time_delta)
        uiManager.draw_ui(screen)

        # draw buttons

        pygame.display.update()


# login screen
def login_screen():
    global currentUser
    uiManager = pygame_gui.UIManager((WIDTH, HEIGHT), "Assets/theme.json")

    # ui elements
    main_menu_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (20, 20, BUTTON_W, BUTTON_H / 1.5),
        ),
        text="Main Menu",
        manager=uiManager,
        object_id="@sm_btn",
    )

    # text inputs
    username_entry = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect(CELL_X * 3, CELL_Y * 2, CELL_X * 4, CELL_Y),
        manager=uiManager,
    )
    username_entry.set_text("")

    password_entry = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect(CELL_X * 3, (CELL_Y * 3) + 20, CELL_X * 4, CELL_Y),
        manager=uiManager,
    )
    password_entry.set_text_hidden(is_hidden=True)

    # login button on login screen
    login_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (CELL_X * 3, CELL_Y * 5, CELL_X * 4, CELL_Y),
        ),
        text="Login",
        manager=uiManager,
    )

    # validation msg
    msg = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect(
            (CELL_X * 3, CELL_Y, CELL_X * 4, CELL_Y),
        ),
        text="",
        manager=uiManager,
        object_id="@errors",
    )

    while True:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            exit_window(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == main_menu_button:
                    main_menu()

                if event.ui_element == login_button:
                    currentUser["username"] = username_entry.get_text()
                    currentUser["password"] = password_entry.get_text()
                    user.setUser(currentUser)
                    if user.validate():
                        if user.authenticate():
                            main_menu()
                        else:
                            msg.set_text("Invalid login Data please try again")
                            username_entry.set_text("")
                            password_entry.set_text("")
                    else:
                        msg.set_text("Invalid Data please try again")
                        username_entry.set_text("")
                        password_entry.set_text("")

            uiManager.process_events(event)

        # draw background
        background()

        # update UI manager
        uiManager.update(time_delta)
        uiManager.draw_ui(screen)

        # draw buttons

        pygame.display.update()


# playscreen
def subjects_screen():
    global currentUser
    uiManager = pygame_gui.UIManager((WIDTH, HEIGHT), "Assets/theme.json")

    # ui element
    main_menu_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (20, 20, BUTTON_W, BUTTON_H / 1.5),
        ),
        text="Main Menu",
        manager=uiManager,
        object_id="@sm_btn",
    )

    pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect(
            ((CELL_X * 5) - ((CELL_X * 5) / 2), CELL_Y, CELL_X * 5, CELL_Y * 2)
        ),
        text="Hi! " + currentUser["username"],
        manager=uiManager,
        object_id="@header",
    )

    biology_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (CELL_X, CELL_Y * 3, BUTTON_W, BUTTON_H),
        ),
        text="Biology",
        manager=uiManager,
    )
    physics_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (CELL_X * 4, CELL_Y * 3, BUTTON_W, BUTTON_H),
        ),
        text="Physics",
        manager=uiManager,
    )
    chemistry_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (CELL_X * 7, CELL_Y * 3, BUTTON_W, BUTTON_H),
        ),
        text="Chemistry",
        manager=uiManager,
    )

    while True:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            exit_window(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == main_menu_button:
                    main_menu()
                if event.ui_element == biology_button:
                    play_screen("biology")
                if event.ui_element == physics_button:
                    play_screen("physics")
                if event.ui_element == chemistry_button:
                    play_screen("chemistry")

            uiManager.process_events(event)

        # draw background
        background()

        # update UI manager
        uiManager.update(time_delta)
        uiManager.draw_ui(screen)

        # draw buttons

        pygame.display.update()


def play_screen(subject):
    global currentUser
    user.resetScore(subject)
    uiManager = pygame_gui.UIManager((WIDTH, HEIGHT), "Assets/theme.json")
    quiz = Quiz()
    quizList = quiz.getQuizList(subject)
    print(quizList)
    for q in quizList:
        if q["image"] == "":
            q["image"] = "data/img/temp.png"
    currentQ = 0
    # ui element
    main_menu_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (20, 20, BUTTON_W, BUTTON_H / 1.5),
        ),
        text="Main Menu",
        manager=uiManager,
        object_id="@sm_btn",
    )

    score = pygame_gui.elements.UITextBox(
        html_text="Score : " + str(currentUser["score"][subject]),
        relative_rect=pygame.Rect(
            (CELL_X * 7, 20, BUTTON_W, BUTTON_H / 1.5),
        ),
        manager=uiManager,
    )

    qText = pygame_gui.elements.UITextBox(
        html_text="<b>" + quizList[0]["number"] + ") </b>" + quizList[0]["Q"],
        relative_rect=pygame.Rect((CELL_X, CELL_Y + 20, CELL_X * 8, CELL_Y * 1.5)),
        manager=uiManager,
    )
    qImg = pygame_gui.elements.UIImage(
        relative_rect=pygame.Rect(
            ((CELL_X * 5) - ((CELL_X * 5) / 2), CELL_Y * 3, CELL_X * 5, CELL_Y * 4),
        ),
        image_surface=pygame.image.load(quizList[0]["image"]),
        manager=uiManager,
    )

    aEntry = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect(
            ((CELL_X), CELL_Y * 7, (CELL_X * 4), CELL_Y),
        ),
        manager=uiManager,
    )

    Submit_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            ((CELL_X * 3), (CELL_Y * 8) + 10, BUTTON_W - 10, BUTTON_H / 1.5),
        ),
        text="Submit",
        manager=uiManager,
    )

    hint_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (CELL_X, (CELL_Y * 8) + 10, BUTTON_W - 10, BUTTON_H / 1.5),
        ),
        text="Hint",
        manager=uiManager,
    )

    hint = pygame_gui.elements.UITextBox(
        html_text="<b>Hint:</b>",
        relative_rect=pygame.Rect(
            (((CELL_X * 5) + 10, (CELL_Y * 7) + 10, CELL_X * 4, CELL_Y * 2),),
        ),
        manager=uiManager,
    )

    while True:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            exit_window(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == main_menu_button:
                    main_menu()
                if event.ui_element == hint_button:
                    hint.set_text("<b>Hint:</b>" + quizList[currentQ]["hint"])

                if event.ui_element == Submit_button:
                    for a in quizList[currentQ]["A"]:
                        if a.lower() == aEntry.get_text().lower():
                            user.addScore(subject, quizList[currentQ]["score"])
                            currentUser = user.getUser()
                            score.set_text(
                                "Score : " + str(currentUser["score"][subject])
                            )
                            aEntry.set_text("")
                            break

                    currentQ = currentQ + 1

                    if currentQ < len(quizList):
                        hint.set_text("<b>Hint:</b>")
                        qText.set_text(
                            "<b>%s) </b> %s"
                            % (quizList[currentQ]["number"], quizList[currentQ]["Q"]),
                        )
                        qImg.set_image(pygame.image.load(quizList[currentQ]["image"]))
                    else:
                        subjects_screen()

            uiManager.process_events(event)

        # draw background
        background()

        # update UI manager
        uiManager.update(time_delta)
        uiManager.draw_ui(screen)

        # draw buttons

        pygame.display.update()


# Scores
def score_screen():
    global currentUser
    currentUser = user.getUser()
    uiManager = pygame_gui.UIManager((WIDTH, HEIGHT), "Assets/theme.json")
    print(currentUser)
    # ui element
    main_menu_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (20, 20, BUTTON_W, BUTTON_H / 1.5),
        ),
        text="Main Menu",
        manager=uiManager,
        object_id="@sm_btn",
    )

    # biology score
    pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect(
            (CELL_X, CELL_Y * 2, CELL_X * 4, CELL_Y),
        ),
        text="Biology :",
        manager=uiManager,
        object_id="@score_board",
    )
    pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect(
            (CELL_X * 5, CELL_Y * 2, CELL_X * 4, CELL_Y),
        ),
        text=str(currentUser["score"]["biology"]),
        manager=uiManager,
        object_id="@score_board",
    )

    # physics score
    pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect(
            (CELL_X, CELL_Y * 3, CELL_X * 4, CELL_Y),
        ),
        text="Physics :",
        manager=uiManager,
        object_id="@score_board",
    )
    pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect(
            (CELL_X * 5, CELL_Y * 3, CELL_X * 4, CELL_Y),
        ),
        text=str(currentUser["score"]["physics"]),
        manager=uiManager,
        object_id="@score_board",
    )

    # chem score
    pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect(
            (CELL_X, CELL_Y * 4, CELL_X * 4, CELL_Y),
        ),
        text="Chemistry :",
        manager=uiManager,
        object_id="@score_board",
    )
    pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect(
            (CELL_X * 5, CELL_Y * 4, CELL_X * 4, CELL_Y),
        ),
        text=str(currentUser["score"]["chemistry"]),
        manager=uiManager,
        object_id="@score_board",
    )

    # total score
    pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect(
            (CELL_X, CELL_Y * 5, CELL_X * 4, CELL_Y),
        ),
        text="Total :",
        manager=uiManager,
        object_id="@score_board",
    )
    pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect(
            (CELL_X * 5, CELL_Y * 5, CELL_X * 4, CELL_Y),
        ),
        text=str(
            currentUser["score"]["chemistry"]
            + currentUser["score"]["biology"]
            + currentUser["score"]["physics"]
        ),
        manager=uiManager,
        object_id="@score_board",
    )

    while True:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            exit_window(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == main_menu_button:
                    main_menu()

            uiManager.process_events(event)

        # draw background
        background()

        # update UI manager
        uiManager.update(time_delta)
        uiManager.draw_ui(screen)

        # draw buttons

        pygame.display.update()


main_menu()
