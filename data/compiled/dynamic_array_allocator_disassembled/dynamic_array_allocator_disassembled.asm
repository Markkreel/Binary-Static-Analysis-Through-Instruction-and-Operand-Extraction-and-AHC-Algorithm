
/home/mark/Documents/Thesis/thesis/compiled/dynamic_array_allocator:     file format elf64-x86-64


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

0000000000001020 <_Znam@plt-0x10>:
    1020:	ff 35 e2 2f 00 00    	push   0x2fe2(%rip) 
    1026:	ff 25 e4 2f 00 00    	jmp    *0x2fe4(%rip) 
    102c:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000001030 <_Znam@plt>:
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

0000000000001070 <_ZdaPv@plt>:
    1070:	ff 25 c2 2f 00 00    	jmp    *0x2fc2(%rip) 
    1076:	68 04 00 00 00       	push   $0x4
    107b:	e9 a0 ff ff ff       	jmp    1020 <_init+0x20>

0000000000001080 <_ZNSt8ios_base4InitC1Ev@plt>:
    1080:	ff 25 ba 2f 00 00    	jmp    *0x2fba(%rip) 
    1086:	68 05 00 00 00       	push   $0x5
    108b:	e9 90 ff ff ff       	jmp    1020 <_init+0x20>

0000000000001090 <_ZNSolsEi@plt>:
    1090:	ff 25 b2 2f 00 00    	jmp    *0x2fb2(%rip) 
    1096:	68 06 00 00 00       	push   $0x6
    109b:	e9 80 ff ff ff       	jmp    1020 <_init+0x20>

00000000000010a0 <_Unwind_Resume@plt>:
    10a0:	ff 25 aa 2f 00 00    	jmp    *0x2faa(%rip) 
    10a6:	68 07 00 00 00       	push   $0x7
    10ab:	e9 70 ff ff ff       	jmp    1020 <_init+0x20>

Disassembly of section .plt.got:

00000000000010b0 <__cxa_finalize@plt>:
    10b0:	ff 25 0a 2f 00 00    	jmp    *0x2f0a(%rip) 
    10b6:	66 90                	xchg   %ax,%ax

Disassembly of section .text:

00000000000010c0 <__cxx_global_var_init>:
    10c0:	55                   	push   %rbp
    10c1:	48 89 e5             	mov    %rsp,%rbp
    10c4:	48 8d 3d a6 2f 00 00 	lea    0x2fa6(%rip),%rdi 
    10cb:	e8 b0 ff ff ff       	call   1080 <_ZNSt8ios_base4InitC1Ev@plt>
    10d0:	48 8b 3d 21 2f 00 00 	mov    0x2f21(%rip),%rdi 
    10d7:	48 8d 35 93 2f 00 00 	lea    0x2f93(%rip),%rsi 
    10de:	48 8d 15 7b 2f 00 00 	lea    0x2f7b(%rip),%rdx 
    10e5:	e8 56 ff ff ff       	call   1040 <__cxa_atexit@plt>
    10ea:	5d                   	pop    %rbp
    10eb:	c3                   	ret    
    10ec:	0f 1f 40 00          	nopl   0x0(%rax)

00000000000010f0 <_GLOBAL__sub_I_dynamic_array_allocator.cpp>:
    10f0:	55                   	push   %rbp
    10f1:	48 89 e5             	mov    %rsp,%rbp
    10f4:	e8 c7 ff ff ff       	call   10c0 <__cxx_global_var_init>
    10f9:	5d                   	pop    %rbp
    10fa:	c3                   	ret    
    10fb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001100 <_start>:
    1100:	f3 0f 1e fa          	endbr64 
    1104:	31 ed                	xor    %ebp,%ebp
    1106:	49 89 d1             	mov    %rdx,%r9
    1109:	5e                   	pop    %rsi
    110a:	48 89 e2             	mov    %rsp,%rdx
    110d:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
    1111:	50                   	push   %rax
    1112:	54                   	push   %rsp
    1113:	45 31 c0             	xor    %r8d,%r8d
    1116:	31 c9                	xor    %ecx,%ecx
    1118:	48 8d 3d d1 00 00 00 	lea    0xd1(%rip),%rdi 
    111f:	ff 15 ab 2e 00 00    	call   *0x2eab(%rip) 
    1125:	f4                   	hlt    
    1126:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
    112d:	00 00 00 

0000000000001130 <deregister_tm_clones>:
    1130:	48 8d 3d 39 2f 00 00 	lea    0x2f39(%rip),%rdi 
    1137:	48 8d 05 32 2f 00 00 	lea    0x2f32(%rip),%rax 
    113e:	48 39 f8             	cmp    %rdi,%rax
    1141:	74 15                	je     1158 <deregister_tm_clones+0x28>
    1143:	48 8b 05 96 2e 00 00 	mov    0x2e96(%rip),%rax 
    114a:	48 85 c0             	test   %rax,%rax
    114d:	74 09                	je     1158 <deregister_tm_clones+0x28>
    114f:	ff e0                	jmp    *%rax
    1151:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    1158:	c3                   	ret    
    1159:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

0000000000001160 <register_tm_clones>:
    1160:	48 8d 3d 09 2f 00 00 	lea    0x2f09(%rip),%rdi 
    1167:	48 8d 35 02 2f 00 00 	lea    0x2f02(%rip),%rsi 
    116e:	48 29 fe             	sub    %rdi,%rsi
    1171:	48 89 f0             	mov    %rsi,%rax
    1174:	48 c1 ee 3f          	shr    $0x3f,%rsi
    1178:	48 c1 f8 03          	sar    $0x3,%rax
    117c:	48 01 c6             	add    %rax,%rsi
    117f:	48 d1 fe             	sar    %rsi
    1182:	74 14                	je     1198 <register_tm_clones+0x38>
    1184:	48 8b 05 65 2e 00 00 	mov    0x2e65(%rip),%rax 
    118b:	48 85 c0             	test   %rax,%rax
    118e:	74 08                	je     1198 <register_tm_clones+0x38>
    1190:	ff e0                	jmp    *%rax
    1192:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    1198:	c3                   	ret    
    1199:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

00000000000011a0 <__do_global_dtors_aux>:
    11a0:	f3 0f 1e fa          	endbr64 
    11a4:	80 3d c5 2e 00 00 00 	cmpb   $0x0,0x2ec5(%rip) 
    11ab:	75 2b                	jne    11d8 <__do_global_dtors_aux+0x38>
    11ad:	55                   	push   %rbp
    11ae:	48 83 3d 0a 2e 00 00 	cmpq   $0x0,0x2e0a(%rip) 
    11b5:	00 
    11b6:	48 89 e5             	mov    %rsp,%rbp
    11b9:	74 0c                	je     11c7 <__do_global_dtors_aux+0x27>
    11bb:	48 8b 3d 9e 2e 00 00 	mov    0x2e9e(%rip),%rdi 
    11c2:	e8 e9 fe ff ff       	call   10b0 <__cxa_finalize@plt>
    11c7:	e8 64 ff ff ff       	call   1130 <deregister_tm_clones>
    11cc:	c6 05 9d 2e 00 00 01 	movb   $0x1,0x2e9d(%rip) 
    11d3:	5d                   	pop    %rbp
    11d4:	c3                   	ret    
    11d5:	0f 1f 00             	nopl   (%rax)
    11d8:	c3                   	ret    
    11d9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

00000000000011e0 <frame_dummy>:
    11e0:	f3 0f 1e fa          	endbr64 
    11e4:	e9 77 ff ff ff       	jmp    1160 <register_tm_clones>
    11e9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

00000000000011f0 <main>:
    11f0:	55                   	push   %rbp
    11f1:	48 89 e5             	mov    %rsp,%rbp
    11f4:	48 83 ec 50          	sub    $0x50,%rsp
    11f8:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp)
    11ff:	48 8d 7d e8          	lea    -0x18(%rbp),%rdi
    1203:	be 0a 00 00 00       	mov    $0xa,%esi
    1208:	e8 13 01 00 00       	call   1320 <_ZN12DynamicArrayIiEC2Ei>
    120d:	c7 45 e4 00 00 00 00 	movl   $0x0,-0x1c(%rbp)
    1214:	83 7d e4 14          	cmpl   $0x14,-0x1c(%rbp)
    1218:	0f 8d 43 00 00 00    	jge    1261 <main+0x71>
    121e:	8b 4d e4             	mov    -0x1c(%rbp),%ecx
    1221:	89 c8                	mov    %ecx,%eax
    1223:	8d 34 80             	lea    (%rax,%rax,4),%esi
    1226:	48 8d 7d e8          	lea    -0x18(%rbp),%rdi
    122a:	e8 51 01 00 00       	call   1380 <_ZN12DynamicArrayIiE9push_backEi>
    122f:	e9 00 00 00 00       	jmp    1234 <main+0x44>
    1234:	e9 00 00 00 00       	jmp    1239 <main+0x49>
    1239:	8b 45 e4             	mov    -0x1c(%rbp),%eax
    123c:	83 c0 01             	add    $0x1,%eax
    123f:	89 45 e4             	mov    %eax,-0x1c(%rbp)
    1242:	e9 cd ff ff ff       	jmp    1214 <main+0x24>
    1247:	48 89 c1             	mov    %rax,%rcx
    124a:	89 d0                	mov    %edx,%eax
    124c:	48 89 4d d8          	mov    %rcx,-0x28(%rbp)
    1250:	89 45 d4             	mov    %eax,-0x2c(%rbp)
    1253:	48 8d 7d e8          	lea    -0x18(%rbp),%rdi
    1257:	e8 c4 01 00 00       	call   1420 <_ZN12DynamicArrayIiED2Ev>
    125c:	e9 b5 00 00 00       	jmp    1316 <main+0x126>
    1261:	c7 45 d0 00 00 00 00 	movl   $0x0,-0x30(%rbp)
    1268:	8b 45 d0             	mov    -0x30(%rbp),%eax
    126b:	89 45 c8             	mov    %eax,-0x38(%rbp)
    126e:	48 8d 7d e8          	lea    -0x18(%rbp),%rdi
    1272:	e8 69 01 00 00       	call   13e0 <_ZNK12DynamicArrayIiE7getSizeEv>
    1277:	89 45 cc             	mov    %eax,-0x34(%rbp)
    127a:	e9 00 00 00 00       	jmp    127f <main+0x8f>
    127f:	8b 45 c8             	mov    -0x38(%rbp),%eax
    1282:	8b 4d cc             	mov    -0x34(%rbp),%ecx
    1285:	39 c8                	cmp    %ecx,%eax
    1287:	0f 8d 58 00 00 00    	jge    12e5 <main+0xf5>
    128d:	8b 75 d0             	mov    -0x30(%rbp),%esi
    1290:	48 8d 7d e8          	lea    -0x18(%rbp),%rdi
    1294:	e8 67 01 00 00       	call   1400 <_ZN12DynamicArrayIiEixEi>
    1299:	48 89 45 c0          	mov    %rax,-0x40(%rbp)
    129d:	e9 00 00 00 00       	jmp    12a2 <main+0xb2>
    12a2:	48 8b 45 c0          	mov    -0x40(%rbp),%rax
    12a6:	8b 30                	mov    (%rax),%esi
    12a8:	48 8b 3d 29 2d 00 00 	mov    0x2d29(%rip),%rdi 
    12af:	e8 dc fd ff ff       	call   1090 <_ZNSolsEi@plt>
    12b4:	48 89 45 b8          	mov    %rax,-0x48(%rbp)
    12b8:	e9 00 00 00 00       	jmp    12bd <main+0xcd>
    12bd:	48 8b 7d b8          	mov    -0x48(%rbp),%rdi
    12c1:	48 8d 35 3c 0d 00 00 	lea    0xd3c(%rip),%rsi 
    12c8:	e8 83 fd ff ff       	call   1050 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
    12cd:	e9 00 00 00 00       	jmp    12d2 <main+0xe2>
    12d2:	e9 00 00 00 00       	jmp    12d7 <main+0xe7>
    12d7:	8b 45 d0             	mov    -0x30(%rbp),%eax
    12da:	83 c0 01             	add    $0x1,%eax
    12dd:	89 45 d0             	mov    %eax,-0x30(%rbp)
    12e0:	e9 83 ff ff ff       	jmp    1268 <main+0x78>
    12e5:	48 8b 3d ec 2c 00 00 	mov    0x2cec(%rip),%rdi 
    12ec:	48 8b 35 d5 2c 00 00 	mov    0x2cd5(%rip),%rsi 
    12f3:	e8 68 fd ff ff       	call   1060 <_ZNSolsEPFRSoS_E@plt>
    12f8:	e9 00 00 00 00       	jmp    12fd <main+0x10d>
    12fd:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp)
    1304:	48 8d 7d e8          	lea    -0x18(%rbp),%rdi
    1308:	e8 13 01 00 00       	call   1420 <_ZN12DynamicArrayIiED2Ev>
    130d:	8b 45 fc             	mov    -0x4(%rbp),%eax
    1310:	48 83 c4 50          	add    $0x50,%rsp
    1314:	5d                   	pop    %rbp
    1315:	c3                   	ret    
    1316:	48 8b 7d d8          	mov    -0x28(%rbp),%rdi
    131a:	e8 81 fd ff ff       	call   10a0 <_Unwind_Resume@plt>
    131f:	90                   	nop

0000000000001320 <_ZN12DynamicArrayIiEC2Ei>:
    1320:	55                   	push   %rbp
    1321:	48 89 e5             	mov    %rsp,%rbp
    1324:	48 83 ec 20          	sub    $0x20,%rsp
    1328:	48 89 7d f8          	mov    %rdi,-0x8(%rbp)
    132c:	89 75 f4             	mov    %esi,-0xc(%rbp)
    132f:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    1333:	48 89 45 e8          	mov    %rax,-0x18(%rbp)
    1337:	8b 4d f4             	mov    -0xc(%rbp),%ecx
    133a:	89 48 08             	mov    %ecx,0x8(%rax)
    133d:	8b 4d f4             	mov    -0xc(%rbp),%ecx
    1340:	89 48 0c             	mov    %ecx,0xc(%rax)
    1343:	48 63 40 0c          	movslq 0xc(%rax),%rax
    1347:	b9 04 00 00 00       	mov    $0x4,%ecx
    134c:	48 f7 e1             	mul    %rcx
    134f:	48 89 c7             	mov    %rax,%rdi
    1352:	0f 90 c0             	seto   %al
    1355:	48 c7 c0 ff ff ff ff 	mov    $0xffffffffffffffff,%rax
    135c:	48 0f 40 f8          	cmovo  %rax,%rdi
    1360:	e8 cb fc ff ff       	call   1030 <_Znam@plt>
    1365:	48 89 c1             	mov    %rax,%rcx
    1368:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
    136c:	48 89 08             	mov    %rcx,(%rax)
    136f:	48 83 c4 20          	add    $0x20,%rsp
    1373:	5d                   	pop    %rbp
    1374:	c3                   	ret    
    1375:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
    137c:	00 00 00 
    137f:	90                   	nop

0000000000001380 <_ZN12DynamicArrayIiE9push_backEi>:
    1380:	55                   	push   %rbp
    1381:	48 89 e5             	mov    %rsp,%rbp
    1384:	48 83 ec 20          	sub    $0x20,%rsp
    1388:	48 89 7d f8          	mov    %rdi,-0x8(%rbp)
    138c:	89 75 f4             	mov    %esi,-0xc(%rbp)
    138f:	48 8b 4d f8          	mov    -0x8(%rbp),%rcx
    1393:	48 89 4d e8          	mov    %rcx,-0x18(%rbp)
    1397:	8b 41 08             	mov    0x8(%rcx),%eax
    139a:	3b 41 0c             	cmp    0xc(%rcx),%eax
    139d:	0f 85 0f 00 00 00    	jne    13b2 <_ZN12DynamicArrayIiE9push_backEi+0x32>
    13a3:	48 8b 7d e8          	mov    -0x18(%rbp),%rdi
    13a7:	8b 77 0c             	mov    0xc(%rdi),%esi
    13aa:	c1 e6 01             	shl    $0x1,%esi
    13ad:	e8 9e 00 00 00       	call   1450 <_ZN12DynamicArrayIiE6resizeEi>
    13b2:	48 8b 75 e8          	mov    -0x18(%rbp),%rsi
    13b6:	8b 55 f4             	mov    -0xc(%rbp),%edx
    13b9:	48 8b 06             	mov    (%rsi),%rax
    13bc:	8b 4e 08             	mov    0x8(%rsi),%ecx
    13bf:	89 cf                	mov    %ecx,%edi
    13c1:	83 c7 01             	add    $0x1,%edi
    13c4:	89 7e 08             	mov    %edi,0x8(%rsi)
    13c7:	48 63 c9             	movslq %ecx,%rcx
    13ca:	89 14 88             	mov    %edx,(%rax,%rcx,4)
    13cd:	48 83 c4 20          	add    $0x20,%rsp
    13d1:	5d                   	pop    %rbp
    13d2:	c3                   	ret    
    13d3:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
    13da:	00 00 00 
    13dd:	0f 1f 00             	nopl   (%rax)

00000000000013e0 <_ZNK12DynamicArrayIiE7getSizeEv>:
    13e0:	55                   	push   %rbp
    13e1:	48 89 e5             	mov    %rsp,%rbp
    13e4:	48 89 7d f8          	mov    %rdi,-0x8(%rbp)
    13e8:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    13ec:	8b 40 08             	mov    0x8(%rax),%eax
    13ef:	5d                   	pop    %rbp
    13f0:	c3                   	ret    
    13f1:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
    13f8:	00 00 00 
    13fb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001400 <_ZN12DynamicArrayIiEixEi>:
    1400:	55                   	push   %rbp
    1401:	48 89 e5             	mov    %rsp,%rbp
    1404:	48 89 7d f8          	mov    %rdi,-0x8(%rbp)
    1408:	89 75 f4             	mov    %esi,-0xc(%rbp)
    140b:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    140f:	48 8b 00             	mov    (%rax),%rax
    1412:	48 63 4d f4          	movslq -0xc(%rbp),%rcx
    1416:	48 c1 e1 02          	shl    $0x2,%rcx
    141a:	48 01 c8             	add    %rcx,%rax
    141d:	5d                   	pop    %rbp
    141e:	c3                   	ret    
    141f:	90                   	nop

0000000000001420 <_ZN12DynamicArrayIiED2Ev>:
    1420:	55                   	push   %rbp
    1421:	48 89 e5             	mov    %rsp,%rbp
    1424:	48 83 ec 10          	sub    $0x10,%rsp
    1428:	48 89 7d f8          	mov    %rdi,-0x8(%rbp)
    142c:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    1430:	48 8b 00             	mov    (%rax),%rax
    1433:	48 89 45 f0          	mov    %rax,-0x10(%rbp)
    1437:	48 83 f8 00          	cmp    $0x0,%rax
    143b:	0f 84 09 00 00 00    	je     144a <_ZN12DynamicArrayIiED2Ev+0x2a>
    1441:	48 8b 7d f0          	mov    -0x10(%rbp),%rdi
    1445:	e8 26 fc ff ff       	call   1070 <_ZdaPv@plt>
    144a:	48 83 c4 10          	add    $0x10,%rsp
    144e:	5d                   	pop    %rbp
    144f:	c3                   	ret    

0000000000001450 <_ZN12DynamicArrayIiE6resizeEi>:
    1450:	55                   	push   %rbp
    1451:	48 89 e5             	mov    %rsp,%rbp
    1454:	48 83 ec 30          	sub    $0x30,%rsp
    1458:	48 89 7d f8          	mov    %rdi,-0x8(%rbp)
    145c:	89 75 f4             	mov    %esi,-0xc(%rbp)
    145f:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    1463:	48 89 45 d8          	mov    %rax,-0x28(%rbp)
    1467:	48 63 45 f4          	movslq -0xc(%rbp),%rax
    146b:	b9 04 00 00 00       	mov    $0x4,%ecx
    1470:	48 f7 e1             	mul    %rcx
    1473:	48 89 c7             	mov    %rax,%rdi
    1476:	0f 90 c0             	seto   %al
    1479:	48 c7 c0 ff ff ff ff 	mov    $0xffffffffffffffff,%rax
    1480:	48 0f 40 f8          	cmovo  %rax,%rdi
    1484:	e8 a7 fb ff ff       	call   1030 <_Znam@plt>
    1489:	48 89 45 e8          	mov    %rax,-0x18(%rbp)
    148d:	c7 45 e4 00 00 00 00 	movl   $0x0,-0x1c(%rbp)
    1494:	48 8b 4d d8          	mov    -0x28(%rbp),%rcx
    1498:	8b 45 e4             	mov    -0x1c(%rbp),%eax
    149b:	3b 41 08             	cmp    0x8(%rcx),%eax
    149e:	0f 8d 27 00 00 00    	jge    14cb <_ZN12DynamicArrayIiE6resizeEi+0x7b>
    14a4:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
    14a8:	48 8b 00             	mov    (%rax),%rax
    14ab:	48 63 4d e4          	movslq -0x1c(%rbp),%rcx
    14af:	8b 14 88             	mov    (%rax,%rcx,4),%edx
    14b2:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
    14b6:	48 63 4d e4          	movslq -0x1c(%rbp),%rcx
    14ba:	89 14 88             	mov    %edx,(%rax,%rcx,4)
    14bd:	8b 45 e4             	mov    -0x1c(%rbp),%eax
    14c0:	83 c0 01             	add    $0x1,%eax
    14c3:	89 45 e4             	mov    %eax,-0x1c(%rbp)
    14c6:	e9 c9 ff ff ff       	jmp    1494 <_ZN12DynamicArrayIiE6resizeEi+0x44>
    14cb:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
    14cf:	48 8b 00             	mov    (%rax),%rax
    14d2:	48 89 45 d0          	mov    %rax,-0x30(%rbp)
    14d6:	48 83 f8 00          	cmp    $0x0,%rax
    14da:	0f 84 09 00 00 00    	je     14e9 <_ZN12DynamicArrayIiE6resizeEi+0x99>
    14e0:	48 8b 7d d0          	mov    -0x30(%rbp),%rdi
    14e4:	e8 87 fb ff ff       	call   1070 <_ZdaPv@plt>
    14e9:	48 8b 45 d8          	mov    -0x28(%rbp),%rax
    14ed:	48 8b 4d e8          	mov    -0x18(%rbp),%rcx
    14f1:	48 89 08             	mov    %rcx,(%rax)
    14f4:	8b 4d f4             	mov    -0xc(%rbp),%ecx
    14f7:	89 48 0c             	mov    %ecx,0xc(%rax)
    14fa:	48 83 c4 30          	add    $0x30,%rsp
    14fe:	5d                   	pop    %rbp
    14ff:	c3                   	ret    

Disassembly of section .fini:

0000000000001500 <_fini>:
    1500:	f3 0f 1e fa          	endbr64 
    1504:	48 83 ec 08          	sub    $0x8,%rsp
    1508:	48 83 c4 08          	add    $0x8,%rsp
    150c:	c3                   	ret    
