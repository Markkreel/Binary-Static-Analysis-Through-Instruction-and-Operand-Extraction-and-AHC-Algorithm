
/home/mark/Documents/Thesis/thesis/compiled/simple_calculator:     file format elf64-x86-64


Disassembly of section .init:

0000000000001000 <_init>:
    1000:	f3 0f 1e fa          	endbr64 
    1004:	48 83 ec 08          	sub    $0x8,%rsp
    1008:	48 8b 05 d9 2f 00 00 	mov    0x2fd9(%rip),%rax   
    100f:	48 85 c0             	test   %rax,%rax
    1012:	74 02                	je     1016 <_init+0x16>
    1014:	ff d0                	call   *%rax
    1016:	48 83 c4 08          	add    $0x8,%rsp
    101a:	c3                   	ret    

Disassembly of section .plt:

0000000000001020 <_ZNSirsERd@plt-0x10>:
    1020:	ff 35 e2 2f 00 00    	push   0x2fe2(%rip)        
    1026:	ff 25 e4 2f 00 00    	jmp    *0x2fe4(%rip)        
    102c:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000001030 <_ZNSirsERd@plt>:
    1030:	ff 25 e2 2f 00 00    	jmp    *0x2fe2(%rip)        
    1036:	68 00 00 00 00       	push   $0x0
    103b:	e9 e0 ff ff ff       	jmp    1020 <_init+0x20>

0000000000001040 <__cxa_atexit@plt>:
    1040:	ff 25 da 2f 00 00    	jmp    *0x2fda(%rip)        
    1046:	68 01 00 00 00       	push   $0x1
    104b:	e9 d0 ff ff ff       	jmp    1020 <_init+0x20>

0000000000001050 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>:
    1050:	ff 25 d2 2f 00 00    	jmp    *0x2fd2(%rip)        
    1056:	68 02 00 00 00       	push   $0x2
    105b:	e9 c0 ff ff ff       	jmp    1020 <_init+0x20>

0000000000001060 <_ZNSolsEPFRSoS_E@plt>:
    1060:	ff 25 ca 2f 00 00    	jmp    *0x2fca(%rip)        
    1066:	68 03 00 00 00       	push   $0x3
    106b:	e9 b0 ff ff ff       	jmp    1020 <_init+0x20>

0000000000001070 <_ZStrsIcSt11char_traitsIcEERSt13basic_istreamIT_T0_ES6_RS3_@plt>:
    1070:	ff 25 c2 2f 00 00    	jmp    *0x2fc2(%rip)        
    1076:	68 04 00 00 00       	push   $0x4
    107b:	e9 a0 ff ff ff       	jmp    1020 <_init+0x20>

0000000000001080 <_ZNSt8ios_base4InitC1Ev@plt>:
    1080:	ff 25 ba 2f 00 00    	jmp    *0x2fba(%rip)        
    1086:	68 05 00 00 00       	push   $0x5
    108b:	e9 90 ff ff ff       	jmp    1020 <_init+0x20>

0000000000001090 <_ZNSolsEd@plt>:
    1090:	ff 25 b2 2f 00 00    	jmp    *0x2fb2(%rip)        
    1096:	68 06 00 00 00       	push   $0x6
    109b:	e9 80 ff ff ff       	jmp    1020 <_init+0x20>

Disassembly of section .plt.got:

00000000000010a0 <__cxa_finalize@plt>:
    10a0:	ff 25 12 2f 00 00    	jmp    *0x2f12(%rip)        
    10a6:	66 90                	xchg   %ax,%ax

Disassembly of section .text:

00000000000010b0 <__cxx_global_var_init>:
    10b0:	55                   	push   %rbp
    10b1:	48 89 e5             	mov    %rsp,%rbp
    10b4:	48 8d 3d a6 2f 00 00 	lea    0x2fa6(%rip),%rdi        
    10bb:	e8 c0 ff ff ff       	call   1080 <_ZNSt8ios_base4InitC1Ev@plt>
    10c0:	48 8b 3d 31 2f 00 00 	mov    0x2f31(%rip),%rdi        
    10c7:	48 8d 35 93 2f 00 00 	lea    0x2f93(%rip),%rsi        
    10ce:	48 8d 15 83 2f 00 00 	lea    0x2f83(%rip),%rdx        
    10d5:	e8 66 ff ff ff       	call   1040 <__cxa_atexit@plt>
    10da:	5d                   	pop    %rbp
    10db:	c3                   	ret    
    10dc:	0f 1f 40 00          	nopl   0x0(%rax)

00000000000010e0 <_GLOBAL__sub_I_simple_calculator.cpp>:
    10e0:	55                   	push   %rbp
    10e1:	48 89 e5             	mov    %rsp,%rbp
    10e4:	e8 c7 ff ff ff       	call   10b0 <__cxx_global_var_init>
    10e9:	5d                   	pop    %rbp
    10ea:	c3                   	ret    
    10eb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000010f0 <_start>:
    10f0:	f3 0f 1e fa          	endbr64 
    10f4:	31 ed                	xor    %ebp,%ebp
    10f6:	49 89 d1             	mov    %rdx,%r9
    10f9:	5e                   	pop    %rsi
    10fa:	48 89 e2             	mov    %rsp,%rdx
    10fd:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
    1101:	50                   	push   %rax
    1102:	54                   	push   %rsp
    1103:	45 31 c0             	xor    %r8d,%r8d
    1106:	31 c9                	xor    %ecx,%ecx
    1108:	48 8d 3d d1 00 00 00 	lea    0xd1(%rip),%rdi        
    110f:	ff 15 b3 2e 00 00    	call   *0x2eb3(%rip)       
    1115:	f4                   	hlt    
    1116:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
    111d:	00 00 00 

0000000000001120 <deregister_tm_clones>:
    1120:	48 8d 3d 39 2f 00 00 	lea    0x2f39(%rip),%rdi        
    1127:	48 8d 05 32 2f 00 00 	lea    0x2f32(%rip),%rax        
    112e:	48 39 f8             	cmp    %rdi,%rax
    1131:	74 15                	je     1148 <deregister_tm_clones+0x28>
    1133:	48 8b 05 9e 2e 00 00 	mov    0x2e9e(%rip),%rax        
    113a:	48 85 c0             	test   %rax,%rax
    113d:	74 09                	je     1148 <deregister_tm_clones+0x28>
    113f:	ff e0                	jmp    *%rax
    1141:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    1148:	c3                   	ret    
    1149:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

0000000000001150 <register_tm_clones>:
    1150:	48 8d 3d 09 2f 00 00 	lea    0x2f09(%rip),%rdi        
    1157:	48 8d 35 02 2f 00 00 	lea    0x2f02(%rip),%rsi        
    115e:	48 29 fe             	sub    %rdi,%rsi
    1161:	48 89 f0             	mov    %rsi,%rax
    1164:	48 c1 ee 3f          	shr    $0x3f,%rsi
    1168:	48 c1 f8 03          	sar    $0x3,%rax
    116c:	48 01 c6             	add    %rax,%rsi
    116f:	48 d1 fe             	sar    %rsi
    1172:	74 14                	je     1188 <register_tm_clones+0x38>
    1174:	48 8b 05 75 2e 00 00 	mov    0x2e75(%rip),%rax        
    117b:	48 85 c0             	test   %rax,%rax
    117e:	74 08                	je     1188 <register_tm_clones+0x38>
    1180:	ff e0                	jmp    *%rax
    1182:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    1188:	c3                   	ret    
    1189:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

0000000000001190 <__do_global_dtors_aux>:
    1190:	f3 0f 1e fa          	endbr64 
    1194:	80 3d c5 2e 00 00 00 	cmpb   $0x0,0x2ec5(%rip)        
    119b:	75 2b                	jne    11c8 <__do_global_dtors_aux+0x38>
    119d:	55                   	push   %rbp
    119e:	48 83 3d 12 2e 00 00 	cmpq   $0x0,0x2e12(%rip)        
    11a5:	00 
    11a6:	48 89 e5             	mov    %rsp,%rbp
    11a9:	74 0c                	je     11b7 <__do_global_dtors_aux+0x27>
    11ab:	48 8b 3d a6 2e 00 00 	mov    0x2ea6(%rip),%rdi        
    11b2:	e8 e9 fe ff ff       	call   10a0 <__cxa_finalize@plt>
    11b7:	e8 64 ff ff ff       	call   1120 <deregister_tm_clones>
    11bc:	c6 05 9d 2e 00 00 01 	movb   $0x1,0x2e9d(%rip)        
    11c3:	5d                   	pop    %rbp
    11c4:	c3                   	ret    
    11c5:	0f 1f 00             	nopl   (%rax)
    11c8:	c3                   	ret    
    11c9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

00000000000011d0 <frame_dummy>:
    11d0:	f3 0f 1e fa          	endbr64 
    11d4:	e9 77 ff ff ff       	jmp    1150 <register_tm_clones>
    11d9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

00000000000011e0 <main>:
    11e0:	55                   	push   %rbp
    11e1:	48 89 e5             	mov    %rsp,%rbp
    11e4:	48 83 ec 30          	sub    $0x30,%rsp
    11e8:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp)
    11ef:	48 8b 3d da 2d 00 00 	mov    0x2dda(%rip),%rdi        
    11f6:	48 89 7d d0          	mov    %rdi,-0x30(%rbp)
    11fa:	48 8d 35 1b 0e 00 00 	lea    0xe1b(%rip),%rsi        
    1201:	e8 4a fe ff ff       	call   1050 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
    1206:	48 8b 3d d3 2d 00 00 	mov    0x2dd3(%rip),%rdi        
    120d:	48 89 7d d8          	mov    %rdi,-0x28(%rbp)
    1211:	48 8d 75 fb          	lea    -0x5(%rbp),%rsi
    1215:	e8 56 fe ff ff       	call   1070 <_ZStrsIcSt11char_traitsIcEERSt13basic_istreamIT_T0_ES6_RS3_@plt>
    121a:	48 8b 7d d0          	mov    -0x30(%rbp),%rdi
    121e:	48 8d 35 18 0e 00 00 	lea    0xe18(%rip),%rsi        
    1225:	e8 26 fe ff ff       	call   1050 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
    122a:	48 8b 7d d8          	mov    -0x28(%rbp),%rdi
    122e:	48 8d 75 f0          	lea    -0x10(%rbp),%rsi
    1232:	e8 f9 fd ff ff       	call   1030 <_ZNSirsERd@plt>
    1237:	48 89 c7             	mov    %rax,%rdi
    123a:	48 8d 75 e8          	lea    -0x18(%rbp),%rsi
    123e:	e8 ed fd ff ff       	call   1030 <_ZNSirsERd@plt>
    1243:	0f be 45 fb          	movsbl -0x5(%rbp),%eax
    1247:	83 c0 d6             	add    $0xffffffd6,%eax
    124a:	89 c1                	mov    %eax,%ecx
    124c:	48 89 4d e0          	mov    %rcx,-0x20(%rbp)
    1250:	83 e8 05             	sub    $0x5,%eax
    1253:	0f 87 db 01 00 00    	ja     1434 <main+0x254>
    1259:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
    125d:	48 8d 0d a0 0d 00 00 	lea    0xda0(%rip),%rcx        
    1264:	48 63 04 81          	movslq (%rcx,%rax,4),%rax
    1268:	48 01 c8             	add    %rcx,%rax
    126b:	ff e0                	jmp    *%rax
    126d:	f2 0f 10 45 f0       	movsd  -0x10(%rbp),%xmm0
    1272:	48 8b 3d 57 2d 00 00 	mov    0x2d57(%rip),%rdi        
    1279:	e8 12 fe ff ff       	call   1090 <_ZNSolsEd@plt>
    127e:	48 89 c7             	mov    %rax,%rdi
    1281:	48 8d 35 c9 0d 00 00 	lea    0xdc9(%rip),%rsi        
    1288:	e8 c3 fd ff ff       	call   1050 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
    128d:	48 89 c7             	mov    %rax,%rdi
    1290:	f2 0f 10 45 e8       	movsd  -0x18(%rbp),%xmm0
    1295:	e8 f6 fd ff ff       	call   1090 <_ZNSolsEd@plt>
    129a:	48 89 c7             	mov    %rax,%rdi
    129d:	48 8d 35 b1 0d 00 00 	lea    0xdb1(%rip),%rsi        
    12a4:	e8 a7 fd ff ff       	call   1050 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
    12a9:	48 89 c7             	mov    %rax,%rdi
    12ac:	f2 0f 10 45 f0       	movsd  -0x10(%rbp),%xmm0
    12b1:	f2 0f 58 45 e8       	addsd  -0x18(%rbp),%xmm0
    12b6:	e8 d5 fd ff ff       	call   1090 <_ZNSolsEd@plt>
    12bb:	48 89 c7             	mov    %rax,%rdi
    12be:	48 8b 35 fb 2c 00 00 	mov    0x2cfb(%rip),%rsi       
    12c5:	e8 96 fd ff ff       	call   1060 <_ZNSolsEPFRSoS_E@plt>
    12ca:	e9 87 01 00 00       	jmp    1456 <main+0x276>
    12cf:	f2 0f 10 45 f0       	movsd  -0x10(%rbp),%xmm0
    12d4:	48 8b 3d f5 2c 00 00 	mov    0x2cf5(%rip),%rdi       
    12db:	e8 b0 fd ff ff       	call   1090 <_ZNSolsEd@plt>
    12e0:	48 89 c7             	mov    %rax,%rdi
    12e3:	48 8d 35 6f 0d 00 00 	lea    0xd6f(%rip),%rsi        
    12ea:	e8 61 fd ff ff       	call   1050 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
    12ef:	48 89 c7             	mov    %rax,%rdi
    12f2:	f2 0f 10 45 e8       	movsd  -0x18(%rbp),%xmm0
    12f7:	e8 94 fd ff ff       	call   1090 <_ZNSolsEd@plt>
    12fc:	48 89 c7             	mov    %rax,%rdi
    12ff:	48 8d 35 4f 0d 00 00 	lea    0xd4f(%rip),%rsi       
    1306:	e8 45 fd ff ff       	call   1050 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
    130b:	48 89 c7             	mov    %rax,%rdi
    130e:	f2 0f 10 45 f0       	movsd  -0x10(%rbp),%xmm0
    1313:	f2 0f 5c 45 e8       	subsd  -0x18(%rbp),%xmm0
    1318:	e8 73 fd ff ff       	call   1090 <_ZNSolsEd@plt>
    131d:	48 89 c7             	mov    %rax,%rdi
    1320:	48 8b 35 99 2c 00 00 	mov    0x2c99(%rip),%rsi      
    1327:	e8 34 fd ff ff       	call   1060 <_ZNSolsEPFRSoS_E@plt>
    132c:	e9 25 01 00 00       	jmp    1456 <main+0x276>
    1331:	f2 0f 10 45 f0       	movsd  -0x10(%rbp),%xmm0
    1336:	48 8b 3d 93 2c 00 00 	mov    0x2c93(%rip),%rdi        
    133d:	e8 4e fd ff ff       	call   1090 <_ZNSolsEd@plt>
    1342:	48 89 c7             	mov    %rax,%rdi
    1345:	48 8d 35 11 0d 00 00 	lea    0xd11(%rip),%rsi       
    134c:	e8 ff fc ff ff       	call   1050 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
    1351:	48 89 c7             	mov    %rax,%rdi
    1354:	f2 0f 10 45 e8       	movsd  -0x18(%rbp),%xmm0
    1359:	e8 32 fd ff ff       	call   1090 <_ZNSolsEd@plt>
    135e:	48 89 c7             	mov    %rax,%rdi
    1361:	48 8d 35 ed 0c 00 00 	lea    0xced(%rip),%rsi       
    1368:	e8 e3 fc ff ff       	call   1050 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
    136d:	48 89 c7             	mov    %rax,%rdi
    1370:	f2 0f 10 45 f0       	movsd  -0x10(%rbp),%xmm0
    1375:	f2 0f 59 45 e8       	mulsd  -0x18(%rbp),%xmm0
    137a:	e8 11 fd ff ff       	call   1090 <_ZNSolsEd@plt>
    137f:	48 89 c7             	mov    %rax,%rdi
    1382:	48 8b 35 37 2c 00 00 	mov    0x2c37(%rip),%rsi        
    1389:	e8 d2 fc ff ff       	call   1060 <_ZNSolsEPFRSoS_E@plt>
    138e:	e9 c3 00 00 00       	jmp    1456 <main+0x276>
    1393:	f2 0f 10 45 e8       	movsd  -0x18(%rbp),%xmm0
    1398:	0f 57 c9             	xorps  %xmm1,%xmm1
    139b:	66 0f 2e c1          	ucomisd %xmm1,%xmm0
    139f:	0f 85 2d 00 00 00    	jne    13d2 <main+0x1f2>
    13a5:	0f 8a 27 00 00 00    	jp     13d2 <main+0x1f2>
    13ab:	48 8b 3d 1e 2c 00 00 	mov    0x2c1e(%rip),%rdi        
    13b2:	48 8d 35 a8 0c 00 00 	lea    0xca8(%rip),%rsi        
    13b9:	e8 92 fc ff ff       	call   1050 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
    13be:	48 89 c7             	mov    %rax,%rdi
    13c1:	48 8b 35 f8 2b 00 00 	mov    0x2bf8(%rip),%rsi        
    13c8:	e8 93 fc ff ff       	call   1060 <_ZNSolsEPFRSoS_E@plt>
    13cd:	e9 5d 00 00 00       	jmp    142f <main+0x24f>
    13d2:	f2 0f 10 45 f0       	movsd  -0x10(%rbp),%xmm0
    13d7:	48 8b 3d f2 2b 00 00 	mov    0x2bf2(%rip),%rdi       
    13de:	e8 ad fc ff ff       	call   1090 <_ZNSolsEd@plt>
    13e3:	48 89 c7             	mov    %rax,%rdi
    13e6:	48 8d 35 8c 0c 00 00 	lea    0xc8c(%rip),%rsi        
    13ed:	e8 5e fc ff ff       	call   1050 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
    13f2:	48 89 c7             	mov    %rax,%rdi
    13f5:	f2 0f 10 45 e8       	movsd  -0x18(%rbp),%xmm0
    13fa:	e8 91 fc ff ff       	call   1090 <_ZNSolsEd@plt>
    13ff:	48 89 c7             	mov    %rax,%rdi
    1402:	48 8d 35 4c 0c 00 00 	lea    0xc4c(%rip),%rsi        
    1409:	e8 42 fc ff ff       	call   1050 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
    140e:	48 89 c7             	mov    %rax,%rdi
    1411:	f2 0f 10 45 f0       	movsd  -0x10(%rbp),%xmm0
    1416:	f2 0f 5e 45 e8       	divsd  -0x18(%rbp),%xmm0
    141b:	e8 70 fc ff ff       	call   1090 <_ZNSolsEd@plt>
    1420:	48 89 c7             	mov    %rax,%rdi
    1423:	48 8b 35 96 2b 00 00 	mov    0x2b96(%rip),%rsi        
    142a:	e8 31 fc ff ff       	call   1060 <_ZNSolsEPFRSoS_E@plt>
    142f:	e9 22 00 00 00       	jmp    1456 <main+0x276>
    1434:	48 8b 3d 95 2b 00 00 	mov    0x2b95(%rip),%rdi        
    143b:	48 8d 35 3b 0c 00 00 	lea    0xc3b(%rip),%rsi        
    1442:	e8 09 fc ff ff       	call   1050 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
    1447:	48 89 c7             	mov    %rax,%rdi
    144a:	48 8b 35 6f 2b 00 00 	mov    0x2b6f(%rip),%rsi        
    1451:	e8 0a fc ff ff       	call   1060 <_ZNSolsEPFRSoS_E@plt>
    1456:	31 c0                	xor    %eax,%eax
    1458:	48 83 c4 30          	add    $0x30,%rsp
    145c:	5d                   	pop    %rbp
    145d:	c3                   	ret    

Disassembly of section .fini:

0000000000001460 <_fini>:
    1460:	f3 0f 1e fa          	endbr64 
    1464:	48 83 ec 08          	sub    $0x8,%rsp
    1468:	48 83 c4 08          	add    $0x8,%rsp
    146c:	c3                   	ret    
