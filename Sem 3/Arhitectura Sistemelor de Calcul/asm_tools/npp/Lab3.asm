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
    ; E = [(a*b)-d]/(b+c) data types: a,b,c - byte, d - word
    ; E = [(5*2)-5]/(2+3) = (10 - 5) / 5 = 1

    a db 5
    b db 2
    c db 3
    d dw 5

; our code starts here
segment code use32 class=code
    start:
        ; ...
        ; a * b
        mov al, [a] ; al = a
        mov bl, [b] ; bl = b
        imul bl ; ax = al * bl

        ; ax - d
        mov bx, [d] ; bx = d
        sub ax, bx ; ax = ax - bx

        ; b + c
        mov bl, [b] ; bl = b
        mov cl, [c] ; cl = c
        add bl, cl ; bl = bl + cl

        ; ax / bl
        idiv bl ; al = ax / bl

        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
