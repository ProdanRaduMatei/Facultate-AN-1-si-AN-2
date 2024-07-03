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
    ;A string of bytes A is given. Construct string B containing only odd values from string A.
    ;If A = 17, 4, 2, -2, -1 => B = 17, -1

    A db 17, 4, 2, -2, -1
    ls equ $ - A
   
    B resb ls
       

; our code starts here
segment code use32 class=code
    start:
    mov esi, 0
    mov edi, 0
    mov ecx, ls
    mov bl, 2 
        ; ...
        repeta:
            movsx ax, byte [A + esi] ; ax = A[esi]
            idiv bl ; al = ax / bl ; ah = ax % bl
            cmp ah, 1 ; ah == 1
            je odd ; if ah == 1 jump to odd
            jmp end
        odd:
            mov al, [A+esi]
            mov byte [B + edi], al ; B[edi] = al
            inc edi ; edi++
        end:
         inc esi ; esi++
         loop repeta
        ; ...
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
