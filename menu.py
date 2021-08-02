import pygame
import os

# load image and set size
MENU = pygame.transform.scale(pygame.image.load(os.path.join("images", "upgrade_menu.png")), (200, 200))
UPGRADE = pygame.transform.scale(pygame.image.load(os.path.join("images", "upgrade.png")), (70, 40))
SELL = pygame.transform.scale(pygame.image.load(os.path.join("images", "sell.png")), (40, 40))


class UpgradeMenu:
    def __init__(self, x, y):
        # the private button list with two button objects: "upgrade" and "sell"
        self.__buttons = [Button(UPGRADE, "upgrade", x, y - 70), Button(SELL, "sell", x, y + 75)]
        # init menu image
        self.menu_image = MENU
        self.menu_rect = self.menu_image.get_rect()
        self.menu_rect.center = (x, y)

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.menu_image, self.menu_rect)
        # for button objects in the private button list
        for button in self.__buttons:
            # draw button
            win.blit(button.image, button.rect)

    def get_buttons(self):
        """
        Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons


# the Button class is used to initial various buttons inclusive of
# "upgrade" and "sell" with their "name", "image", and "position(x, y)"
class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.image = image
        self.rect = image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x, y):
        """
        Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        # return True if the mouse click in the reck-image range of the button
        # else False
        return True if self.rect.collidepoint(x, y) else False

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        # by using str() to make sure that the return type of self.name is string
        return str(self.name)






