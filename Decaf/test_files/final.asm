.data
.align 2
  G: .space 40
.text
      la $s7, G
      j main
  Minimo:
      sub $sp, $sp, 4
      sw $ra, ($sp)
      sub $fp, $sp, 12
      la $sp, ($fp)
      lw $t0, 0($sp)
      li $t1, 4
      mul $t0, $t0, $t1
      li $t1, 0
      add $t1, $t0, $t1
      lw $t2, 4($sp)
      add $t1, $t1, $s7
      move $t2, $t3
      lw $t4, 8($sp)
      lw $t5, 0($sp)
      move $t4, $t5
  loop1_begin:
      li $t6, 10
      j s1_next
  block1_true:
      li $t6, 4
      mul $t6, $t5, $t6
      li $t7, 0
      add $t7, $t6, $t7
      li $t8, G[t4]
      j s2_next
  block2_true:
      li $t8, 4
      mul $t8, $t5, $t8
      li $t9, 0
      add $t9, $t8, $t9
      sw $t0
      add $t9, $t9, $s7
      move $t2, $t0
      move $t4, $t5
  s2_next:
      sw $t1, t7
      sw $t1, t7
      move $t5, $t1
      j loop1_begin
  s1_next:
      move $v0, $t4
      add $sp, $fp, 12
      lw $ra, ($sp)
      add $sp, $sp, 4
      jr $ra
  Ordenar:
      sub $sp, $sp, 4
      sw $ra, ($sp)
      sub $fp, $sp, 16
      la $sp, ($fp)
      lw $t0, 0($sp)
      li $t1, 0
      move $t0, $t1
  loop2_begin:
      li $t2, 10
      j s3_next
  block3_true:
      lw $t0, 0($sp)
      sw $t0, -8($sp)
      j Minimo
      lw $t2, 12($sp)
      move $t2, $v0
      li $t3, 4
      mul $t3, $t2, $t3
      li $t4, 0
      add $t4, $t3, $t4
      lw $t5, 8($sp)
      add $t4, $t4, $s7
      move $t5, $t6
      li $t7, 4
      mul $t7, $t2, $t7
      li $t8, 0
      add $t8, $t7, $t8
      li $t9, 4
      mul $t9, $t0, $t9
      sw $t0, t6
      sw $t0
      sw $t0
      add $t8, $t8, $s7
      sw $t0, t6
      add $t0, $t0, $s7
      move $t0, $t0
      sw $t1, t7
      sw $t1, t8
      sw $t1, t7
      sw $t1
      sw $t1, t8
      add $t1, $t1, $s7
      move $t1, $t5
      sw $t1, t9
      sw $t1, t9
      move $t0, $t1
      j loop2_begin
  s3_next:
      add $sp, $fp, 16
      lw $ra, ($sp)
      add $sp, $sp, 4
      jr $ra
  OutputInt:
      sub $sp, $sp, 4
      sw $ra, ($sp)
      sub $fp, $sp, 4
      la $sp, ($fp)
      add $sp, $fp, 4
      lw $ra, ($sp)
      add $sp, $sp, 4
      jr $ra
  InputInt:
      sub $sp, $sp, 4
      sw $ra, ($sp)
      sub $fp, $sp, 0
      la $sp, ($fp)
      li $t0, 0
      move $v0, $t0
      add $sp, $fp, 0
      lw $ra, ($sp)
      add $sp, $sp, 4
      jr $ra
  main:
      sub $sp, $sp, 4
      sw $ra, ($sp)
      sub $fp, $sp, 4
      la $sp, ($fp)
      lw $t0, 0($sp)
      li $t1, 0
      move $t0, $t1
  loop3_begin:
      li $t2, 10
      j s4_next
  block4_true:
      li $t2, 4
      mul $t2, $t0, $t2
      li $t3, 0
      add $t3, $t2, $t3
      j InputInt
      add $t3, $t3, $s7
      move $t4, $v0
      li $t4, 1
      add $t4, $t0, $t4
      move $t0, $t4
      j loop3_begin
  s4_next:
      j Ordenar
      li $t5, 0
      move $t0, $t5
  loop4_begin:
      li $t6, 10
      j s5_next
  block5_true:
      li $t6, 4
      mul $t6, $t0, $t6
      li $t7, 0
      add $t7, $t6, $t7
      li $t8, G[t5]
      lw $t8
      sw $t8, -8($sp)
      j OutputInt
      li $t8, 1
      add $t8, $t0, $t8
      move $t0, $t8
      j loop4_begin
  s5_next:
      add $sp, $fp, 4
      lw $ra, ($sp)
      add $sp, $sp, 4
      jr $ra
