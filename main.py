import random as rand
import os
import time as ti
import colorama as colo
colo.init(autoreset=True)
def BubbleSort(arr, n=None):
    beforeimage = list(tuple(arr)) # this just records the state of the array before the changes. the tuple list thing is allocate new memory for copy

    for i in range(0, n-1):
        if arr[i] > arr [i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        yield beforeimage, arr, i
        beforeimage = list(tuple(arr))

def clear():
    ti.sleep(0.25)
    os.system('cls' if os.name == 'nt' else 'clear')

# ===========================================================================
# INPUT LIST HERE AND LET THE MAGIC HAPPEN. DO NOT INPUT ANYTHING LESS THAN 0

number_of_numbers = 20.5

# ===========================================================================
# PROGRAM START
try:
    int(number_of_numbers)
except ValueError:
    clear()
    print('Uh oh! Seems like the program cannot run!\nDid you input a string? Please use a number like 10.')
else:
    if number_of_numbers <= 0:
        clear()
        print('Uh oh! Seems like the program cannot run!\nDid you input a non positive number? Please use a positive number like 10.')
    else:
        number_of_numbers = int(number_of_numbers)
        A = [i for i in range(number_of_numbers)]

        rand.shuffle(A)
        B = list(tuple(A))
        clear()
        print('1. Terminal visualization')
        print('2. PyGame visualization')

        mode = input('\nPick mode (1 or 2): ')
        if mode not in ['1', '2']:
            print('That is not it! Run again.')
        elif mode == '1':
            for index in range(len(A), -1, -1):
                generator = BubbleSort(A, index)
                for single in generator:
                    clear()
                    beforearr, currentarr, i = single
                    print(f'Pass: {len(A) - index+1}')
                    for j in range(len(beforearr)):
                        if j+1 < 10:
                            print(f' {j+1} | ', end='')
                        else:
                            print(f'{j+1} | ', end='')
                        if j == i+1 or j == i:
                            print(colo.Back.BLUE + '##' * (beforearr[j]+1))
                        elif j > index-1:
                            print(colo.Back.GREEN + '##' * (beforearr[j]+1))
                        else:
                            print('##' * (beforearr[j]+1))
                    # If it is different, delete all and reprint. Otherwise, just delete all and move on
                    if beforearr[i] != currentarr[i] and beforearr[i+1] != currentarr[i+1]:
                        clear()
                        print(f'Pass: {len(A) - index+1}')
                        for j in range(len(currentarr)):
                            if j+1 < 10:
                                print(f' {j+1} | ', end='')
                            else:
                                print(f'{j+1} | ', end='')
                            if j == i+1 or j == i:
                                print(colo.Back.YELLOW + '##' * (currentarr[j]+1))
                            elif j > index - 1:
                                print(colo.Back.GREEN + '##' * (currentarr[j]+1))
                            else:
                                print('##' * (currentarr[j]+1))
                    else:
                        pass

            # We would want to print this one last time, without the color graded thing
            clear()
            print('Pass:', len(A)-1)
            for j in range(len(A)):
                if j+1 < 10:
                    print(f' {j+1} | ', end='')
                else:
                    print(f'{j+1} | ', end='')
                print('##' * (beforearr[j]+1))
            print(f'\nOriginal list: {B}')
            print(f'Sorted List:   {A}')
        else:
            # pygame visualization
            # BEcause of time, i suppose i have to use AI
            import pygame as pyg
            import random as rand

            # --- setup ---
            A = [i for i in range(int(number_of_numbers))]
            rand.shuffle(A)
            B = list(tuple(A))

            def BubbleSort(arr, n):
                beforeimage = list(tuple(arr))
                for i in range(0, n - 1):
                    if arr[i] > arr[i + 1]:
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    yield beforeimage, arr, i
                    beforeimage = list(tuple(arr))

            pyg.init()

            WIN_W, WIN_H   = 900, 600
            BAR_AREA_TOP   = 60
            BAR_AREA_BOT   = 80
            BAR_AREA_H     = WIN_H - BAR_AREA_TOP - BAR_AREA_BOT
            BG_COLOR       = (18, 18, 20)
            TEXT_COLOR     = (220, 220, 220)
            DIM_COLOR      = (100, 100, 100)
            WHITE_BAR      = (200, 200, 205)
            COMPARE_COLOR  = (100, 149, 237)
            SWAP_COLOR     = (255, 210, 80)
            SORTED_COLOR   = (80, 200, 120)
            STEP_DELAY_MS  = 150

            font_big   = pyg.font.SysFont('monospace', 20, bold=True)
            font_small = pyg.font.SysFont('monospace', 15)
            screen     = pyg.display.set_mode((WIN_W, WIN_H))
            clock      = pyg.time.Clock()
            pyg.display.set_caption('Bubble Sort Visualizer')

            def draw(arr, hi, mode, pass_num, cmp_count, sorted_from):
                screen.fill(BG_COLOR)
                n     = len(arr)
                bar_w = (WIN_W - 40) / n
                pad_x = 20

                for j in range(n):
                    val   = arr[j]
                    bar_h = int((val + 1) / n * BAR_AREA_H)
                    x     = int(pad_x + j * bar_w)
                    y     = BAR_AREA_TOP + BAR_AREA_H - bar_h
                    w     = max(int(bar_w) - 2, 1)

                    if j >= sorted_from:
                        color = SORTED_COLOR
                    elif j == hi or j == hi + 1:
                        color = COMPARE_COLOR if mode == 'compare' else SWAP_COLOR
                    else:
                        color = WHITE_BAR

                    pyg.draw.rect(screen, color, (x, y, w, bar_h), border_radius=3)

                screen.blit(font_big.render(f'Pass: {pass_num}',         True, TEXT_COLOR), (20, 18))
                screen.blit(font_big.render(f'Comparisons: {cmp_count}', True, TEXT_COLOR), (220, 18))

                legend_y = WIN_H - BAR_AREA_BOT + 18
                lx = 20
                for color, label in [(COMPARE_COLOR, 'Comparing'), (SWAP_COLOR, 'Swapping'), (SORTED_COLOR, 'Sorted')]:
                    pyg.draw.rect(screen, color, (lx, legend_y, 16, 16), border_radius=3)
                    screen.blit(font_small.render(label, True, TEXT_COLOR), (lx + 22, legend_y + 1))
                    lx += 130

                pyg.display.flip()

            def draw_end(original, sorted_arr):
                screen.fill(BG_COLOR)
                n     = len(sorted_arr)
                bar_w = (WIN_W - 40) / n
                pad_x = 20

                title = font_big.render('Sorting Complete!', True, SORTED_COLOR)
                screen.blit(title, (WIN_W // 2 - title.get_width() // 2, 20))

                for j in range(n):
                    val   = sorted_arr[j]
                    bar_h = int((val + 1) / n * BAR_AREA_H)
                    x     = int(pad_x + j * bar_w)
                    y     = BAR_AREA_TOP + BAR_AREA_H - bar_h
                    w     = max(int(bar_w) - 2, 1)
                    pyg.draw.rect(screen, SORTED_COLOR, (x, y, w, bar_h), border_radius=3)

                screen.blit(font_small.render(f'Original : {original}',   True, TEXT_COLOR), (20, WIN_H - 75))
                screen.blit(font_small.render(f'Sorted   : {sorted_arr}', True, TEXT_COLOR), (20, WIN_H - 52))
                screen.blit(font_small.render('Press any key to exit.',    True, DIM_COLOR),  (20, WIN_H - 25))
                pyg.display.flip()

            # --- state ---
            # pass_n is the n passed to BubbleSort — after a pass finishes, index pass_n-1 is sorted
            pass_n       = len(A)        # start with full array
            sort_gen     = BubbleSort(A, pass_n)
            pass_num     = 1
            cmp_count    = 0
            sorted_from  = len(A)        # nothing green yet
            pending_swap = None
            done         = False
            last_step_t  = pyg.time.get_ticks()
            running      = True

            while running:
                for event in pyg.event.get():
                    if event.type == pyg.QUIT:
                        running = False
                    if done and event.type == pyg.KEYDOWN:
                        running = False

                if done:
                    draw_end(B, A)
                    clock.tick(30)
                    continue

                now = pyg.time.get_ticks()
                if now - last_step_t < STEP_DELAY_MS:
                    clock.tick(60)
                    continue
                last_step_t = now

                if pending_swap is not None:
                    _, currentarr, i = pending_swap
                    draw(list(currentarr), i, 'swap', pass_num, cmp_count, sorted_from)
                    pending_swap = None
                    continue

                try:
                    beforearr, currentarr, i = next(sort_gen)
                    cmp_count += 1
                    swapped    = (beforearr[i] != currentarr[i])
                    draw(list(beforearr), i, 'compare', pass_num, cmp_count, sorted_from)
                    if swapped:
                        pending_swap = (beforearr, list(currentarr), i)

                except StopIteration:
                    # after a pass with pass_n, index pass_n-1 is now sorted
                    sorted_from = pass_n - 1
                    pass_n     -= 1
                    if pass_n > 1:
                        sort_gen  = BubbleSort(A, pass_n)
                        pass_num += 1
                    else:
                        done = True

            pyg.quit()