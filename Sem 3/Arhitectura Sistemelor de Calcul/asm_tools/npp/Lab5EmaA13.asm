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
    ; A string of bytes A is given. Construct string B containing only the values divisible with 6 from string A.
    ;If A = 12, 13, 14, 18 => B = 12, 18

    A db 12, 13, 14, 18
    ls equ $ - A
    B resb ls

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, 0
        mov edi, 0
        mov ecx, ls
        mov bl, 6
        repeta:
            movsx ax, byte [A + esi]; ax = A[esi]
            idiv bl; ax = A[esi] / bl; ah = A[esi] % bl
            cmp ah, 0; ah== 0?
            je divizibil; yes -> jump to divizibil
            jmp final
        divizibil: 
            mov [B + edi], byte [A + esi]; B[edi] = A[esi]
            inc edi; edi++
        final:
            inc esi; esi++
            loop repeta
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
