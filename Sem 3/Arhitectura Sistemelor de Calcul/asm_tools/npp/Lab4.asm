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
    ; if (d + a) % 7 = 0 then e = 12 * b else e = c / 11
    a db 3
    b dw 1
    c dw 22
    d db 4
    e dd 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        ; d + a
        mov al, [a]
        mov bx, [d]
        cbw ; convert al (byte) to ax (word)
        add ax, bx ; ax = ax + bx = d + a
        
        ; (d + a) % 7
        mov cx, 7
        cwd ; convert ax (word) to dx:ax (double word)
        div cx     ; dx:ax / cx = ax remainder dx
        mov ax, dx ; ax = dx = (d + a) % 7

        ; if (d + a) % 7 = 0 then e = 12 * b else e = c / 11
        mov bx, 0
        cmp ax, bx ; compare ax with bx
        je if_true ; if ax == bx then jump to if_true
        jne if_false ; if ax != bx then jump to if_false

        if_true:
            ; e = 12 * b
            mov ax, [b]
            mov bx, 12
            mul bx     ; dx:ax = ax * 12
            mov [e+0], ax
            mov [e + 2], dx
            jmp end_if ; jump to end_if

        if_false:
            ; e = c / 11
            mov ax, [c]
            mov bx, 11
            cwd ; convert ax (word) to dx:ax (double word)
            div bx     ; dx:ax / bx = ax remainder dx
            movsx ebx, ax
            mov [e], ebx

        end_if:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
