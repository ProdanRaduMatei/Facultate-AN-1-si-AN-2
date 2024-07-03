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
    ; E = 20 / (a + b * c - 9) - d a,b,c-byte d-doubleword
    ; E = 20 / (18 + 1 * 1 - 9) - 1 = 20 / 10 - 1 = 2 - 1 = 1

    a db 18
    b db 1
    c db 1
    d dd 1

; our code starts here
segment code use32 class=code
    start:
        ; ...
        ; b * c
        mov al, [b] ; al = b
        mov bl, [c] ; bl = c
        imul bl ; ax = al * bl

        ; a + b * c = a + ax
        mov bl, [a] ; bl = a
        movsx bx, bl ; bx = bl
        add bx, ax ; bx = bx + ax


        ; a + b * c - 9 = bx - 9
        mov cx, 9 ; cx = 9
        sub bx, cx ; bx = bx - cx

        ; 20 / (a + b * c - 9)
        mov ax, 20 ; ax = 20
        cwd ; dx:ax = ax
        idiv bx ; ax = dx:ax / bx

        ; 20 / (a + b * c - 9) - d
        movsx eax, ax ; eax = ax
        mov ebx, [d] ; ebx = d
        sub eax, ebx ; eax = eax - ebx
        ; eax = 1

    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
