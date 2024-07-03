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
    ; A string of words S is given. Compute string D constaining only low bytes of multiple of 9 from string S.
    ; If S = 3812h, 5678h, 1a09h => D = 12h, 09h

    S dw 3812h, 5678h, 1a09h
    ls equ ($-S) / 2 ; ls = length of S (in words)
    D resb ls

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, 0
        mov edi, 0
        mov ecx, ls
        mov bl, 9
        repeta: ; compute string D constaining only low bytes of multiple of 9 from string S
            mov ax, [S + esi] ; ax = S[esi]
            div bl ; ax = ax / bl (ax = quotient, ah = remainder)
            cmp ah, 0 ; if remainder = 0
            jne next ; jump to next
            mov [D + edi], al ; D[edi] = al
            inc edi ; edi++
            next:
            inc esi ; esi++
            loop repeta ; repeat

        ; ...        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
