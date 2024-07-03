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
    ;E=a / (b - c) + d, a byte, b, word, c byte, d doubleword
    ; e = 10 / (4 - 2) + 1
    a db 10
    b dw 4
    c db 2
    d dd 1

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov bx, [b]
        mov al, [c]
        cbw
        sub bx, ax; bx = bx - ax
        mov al, [a]
        cbw
        cwd
        idiv bx; ax = cat, dx = rest
        cwd
        mov ebx, [d]
        push dx
        push ax
        pop eax
        add ebx, eax
        
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
