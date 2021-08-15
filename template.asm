org 100h
jmp start
;your vars here

start:
;your code here

end:
	mov ah, 0
	int 16h
	ret
include addons.inc