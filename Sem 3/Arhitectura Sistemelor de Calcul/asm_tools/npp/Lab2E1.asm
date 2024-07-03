bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    ; E = (100 * a + d + 5 - 75 * b) / (c - 5) data types: a,b,c - byte, d - word
    ; E = (100 * 1 + 5 + 5 - 75 * 1) / (10 - 5) = 35 / 5 = 7
    a db 1
    b db 1
    c db 10
    d dw 5

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov al, 100
        mul byte [a]      ; ax = al * [a] = 100 * 1 = 100
        mov bx, [d]
        add ax, bx        ; ax = ax + bx = 100 + 5 = 105
        mov bx, 5
        add ax, bx        ; ax = ax + bx = 105 + 5 = 110
        mov bl, 75
        mul byte [b]      ; bx = bl * [b] =  75 * 1 = 75
        sub ax, bx        ; ax = ax - bx = 110 - 75 = 35
        mov al, [c]
        sub al, 5         ; al = al - 5 = 10 - 5 = 5
        cwd               ; sign extend ax into dx:ax
        idiv byte [c]     ; dx:ax = dx:ax / [c] = 35 / 5 = 7
        push dx           ; push the result onto the stack
        push ax
        pop eax           ; pop the result into eax

        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
