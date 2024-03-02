import pygame
import sys
import time

import tictactoe as ttt
import test as t

pygame.init()
size = width, height = 700, 700

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (1, 50, 32)
gray = (150.2, 150.2, 150.2)
light_green = (140, 240, 140)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

user = None
ai = None
board = ttt.initial_state()
ai_turn = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(green)

    # Let user choose a player.
    if user is None:

        # Draw title
        title = largeFont.render("Othello", True, white)
        author = mediumFont.render("By Luka M.S. and Pedro M.", True, white)
        titleRect = title.get_rect()
        authorRect = title.get_rect()
        titleRect.center = ((width / 2.05), 50)
        authorRect.center = ((width / 3), height - 100)
        screen.blit(title, titleRect)
        screen.blit(author, authorRect)

        # Draw buttons
        playXButton = pygame.Rect((width / 2.75), (height / 3), width / 4, 50)
        playX = mediumFont.render("Play as Black", True, white)
        playXRect = playX.get_rect()
        playXRect.center = playXButton.center
        pygame.draw.rect(screen, black, playXButton)
        screen.blit(playX, playXRect)

        playOButton = pygame.Rect((width / 2.75), (height / 2), width / 4, 50)
        playO = mediumFont.render("Play as White", True, black)
        playORect = playO.get_rect()
        playORect.center = playOButton.center
        pygame.draw.rect(screen, white, playOButton)
        screen.blit(playO, playORect)

        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playXButton.collidepoint(mouse):
                time.sleep(0.2)
                user = ttt.B
                ai = ttt.W
                player = ttt.B
            elif playOButton.collidepoint(mouse):
                time.sleep(0.2)
                user = ttt.W
                ai = ttt.B
                player = ttt.B
                ai_turn = True

    else:

        # Draw game board
        tile_size = 60
        tile_origin = (width / 3.5 - (1.5 * tile_size),
                       height / 3.5 - (1.5 * tile_size))
        tiles = []
        for i in range(8):
            row = []
            for j in range(8):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 1)

                if board[i][j] != ttt.EMPTY:
                    if board[i][j] == ttt.B:
                        pygame.draw.circle(screen, black, rect.center, 20)
                    else:
                        pygame.draw.circle(screen, white, rect.center, 20)
                    # move = moveFont.render(, True, white)
                    # # moveRect = move.get_rect()
                    # # moveRect.center = rect.center
                    # # screen.blit(move, moveRect)
                    
                row.append(rect)
            tiles.append(row)

        game_over = ttt.terminal(board)

        # Show title
        if game_over:
            winner = ttt.winner(board)
            if winner is None:
                title = f"Game Over: Tie."
            else:
                title = f"Game Over: {winner} wins."
        elif user == player:
            title = f"Player's Turns"
            possible_actions = ttt.actions(board, player)

            for action in possible_actions:

                rectTest = pygame.Rect(
                        tile_origin[1] + action[1] * tile_size,
                        tile_origin[0] + action[0] * tile_size,
                        tile_size, tile_size
                    )
                pygame.draw.circle(screen, light_green, rectTest.center, 20, 1)
        else:
            title = f"Computer thinking..."
        title = largeFont.render(title, True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)

        # Check for AI move
        if not game_over:
            if ai_turn:
                time.sleep(0.5)
                move = ttt.minimax(board)
                board = ttt.result(board, move)
                ai_turn = False
            else:
                ai_turn = True

        # Check for a user move
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and user == player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(8):
                for j in range(8):
                    if (board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse)):
                        board = ttt.result(board, (i, j), player)

        if game_over:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            again = mediumFont.render("Play Again", True, black)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, white, againButton)
            screen.blit(again, againRect)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    user = None
                    board = ttt.initial_state()
                    ai_turn = False

    pygame.display.flip()

