import pygame
import random
from random import randint
import sys
import time
import os

os.environ['SDL_VIDEO_CENTERED'] = "True"
width = 1900
height = 500
line_color = (255, 255, 255)

pygame.display.set_caption("Selection sort")
(width, height) = (width, height)
 

def main():
    print("Array sorter visualizer\nChoose an option from the below ones")
    
    while True:
        os.system('cls')
        ans = input("0 => Selection Sort\n1 => Bubble Sort\n2 => Cocktail Shake Sort\n-1 => Quit\nOption => ")
        if str(ans) == "0":
            pygame.init()
            selection_sort()
            break
        elif str(ans) == "1":
            pygame.init()
            bubble_sort()
            break
        elif str(ans) == "2":
            pygame.init()
            cocktail_shaker_sort()
            break        
        elif str(ans) == "-1":
            sys.exit(0)
        else:
            continue

def draw(numbers):
    screen = pygame.display.set_mode((width, height))
    for p in range(len(numbers)):
        pygame.draw.line(screen, line_color, (p,height), (p,height-numbers[p]))
        #pygame.draw.line(screen, line_color, (p,height-numbers[p]+1), (p,height-numbers[p]))

def cocktail_shaker_sort():
    numbers = []
    for i in range(width):
        numbers.append(randint(0, height))

    while True:
        #pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                main()

        execute = False
        keys = pygame.key.get_pressed() 
        
        if keys[pygame.K_SPACE]:            
            execute = True        

        if not execute:
            draw(numbers)
            pygame.display.update()
        else:
            stop = False
            start = 0
            end = width
            tic = time.perf_counter()

            for j in range(width):
                for i in range(width - 1):
                    if numbers[width - 1 - i] < numbers[width - 2 - i]:
                        numbers[width - 1 - i],numbers[width - 2 - i] = numbers[width - 2 - i],numbers[width - 1 - i]
                    if numbers[i] > numbers[i + 1]:
                        numbers[i],numbers[i + 1] = numbers[i + 1],numbers[i]

                draw(numbers)
                pygame.display.update()
                toc = time.perf_counter()
            t = toc - tic
            print(f"Fineshed in {t:0.2f} seconds")

def bubble_sort():
    numbers = []
    for i in range(width):
        numbers.append(randint(0, height))

    while True:
        #pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                main()

        execute = False
        keys = pygame.key.get_pressed() 
        
        if keys[pygame.K_SPACE]:            
            execute = True        

        if not execute:
            draw(numbers)
            pygame.display.update()
        else:
            moves = -1
            tic = time.perf_counter()
            while moves > 0 or moves == -1:
                moves = 0
                for i in range(width):
                    if i + 1 < width:
                        if numbers[i] > numbers[i + 1]:
                            moves += 1
                            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                draw(numbers)
                pygame.display.update()
            toc = time.perf_counter()
            t = toc - tic
            print(f"Fineshed in {t:0.2f} seconds")                

def selection_sort():
    numbers = []
    for i in range(width):
        numbers.append(randint(0, height))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                main()

        execute = False
        keys = pygame.key.get_pressed() 
        
        if keys[pygame.K_SPACE]:            
            execute = True        

        if not execute:
            draw(numbers)
            pygame.display.update()
        else:
            tic = time.perf_counter()
            for i in range(width):            
                #sorting                
                if i == 0:
                    maxV = max(numbers)
                else:
                    maxV = max(numbers[:-i])

                numbers[len(numbers)-i-1], numbers[numbers.index(maxV)] = maxV, numbers[len(numbers)-i-1]

                draw(numbers)
                pygame.display.update()
            toc = time.perf_counter()
            t = toc - tic                
            print(f"Fineshed in {t:0.2f} seconds") 

if __name__ == "__main__":
    main()