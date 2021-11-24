.data
.align 2
  G: .space 40
  newline: .asciiz "\n"
  intPrompt: .asciiz "Ingrese un numero entero: "
.text
      la $s7, G
      j main
  test:
      sub $sp, $sp, 4
      sw $ra, ($sp)
      sub $fp, $sp, 12
      la $sp, ($fp)
      sw $a0, 0($sp)
      sw $a1, 4($sp)
      sw $a2, 8($sp)
      lw $t0, 0($sp)
      li $t1, 0
      move $t0, $t1
      lw $t2, 4($sp)
      li $t3, 1
      move $t2, $t3
      lw $t4, 8($sp)
      li $t5, 2
      move $t4, $t5
      add $sp, $fp, 12
      lw $ra, ($sp)
      add $sp, $sp, 4
      jr $ra
  main:
      sub $fp, $sp, 12
      la $sp, ($fp)
      lw $t0, 0($sp)
      li $t1, 3
      move $t0, $t1
      lw $t2, 4($sp)
      li $t3, 4
      move $t2, $t3
      lw $t4, 8($sp)
      li $t5, 5
      move $t4, $t5
      move $a0, $t0
      move $a1, $t2
      move $a2, $t4
      jal test
      j terminate
  terminate:
      li $v0, 10
      syscall 
