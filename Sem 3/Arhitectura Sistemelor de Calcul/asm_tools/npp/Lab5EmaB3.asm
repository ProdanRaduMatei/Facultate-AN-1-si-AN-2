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
    ; A string of words S is given. Compute string D containing only low bytes multiple of 5 from string S.
    ; If S = 1223h, 5628h => D = 23h, 28h

    S dw 1223h, 5628h
    ls equ ($ - S) / 2; length of S in words
    D resw ls; reserve space for D

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, 0
        mov edi, 0
        mov ecx, ls
        mov bl, 5
        repeta: 
            mov ax, [S + esi * 2]; ax = S[esi]
            idiv bl; al = ax / bl, ah = ax % bl
            cmp ah, 0; if ah == 0
            je divizibil; jump to divizibil
        divizibil:
            mov [D + edi], ax; D[edi] = ax
            inc edi
        final:
            inc esi
            loop repeta
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
