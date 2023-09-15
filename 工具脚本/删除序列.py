import re

# 你的文本数据
data = r"""
1:
URL:  https://mail.google.com/
Username:  ozogp@gmail.com
Password:  4-#>(Rcr#]dV

2:
URL:  https://mail.google.com/
Username:  rfcyp@gmail.com
Password:  e2,Up&<a|:UC

3:
URL:  https://mail.google.com/
Username:  wwhza@gmail.com
Password:  4BpNF}BpA\UD

4:
URL:  https://mail.google.com/
Username:  deajz@gmail.com
Password:  25@._&C=QJOw

5:
URL:  https://mail.google.com/
Username:  wyjet@gmail.com
Password:  5_N:tTN\4^!P

6:
URL:  https://mail.google.com/
Username:  pyazf@gmail.com
Password:  +0&B`mkx"k1&

7:
URL:  https://mail.google.com/
Username:  tuumm@gmail.com
Password:  l:V&i]>jd2N>

8:
URL:  https://mail.google.com/
Username:  pcrza@gmail.com
Password:  ;J`T.=']UEv-

9:
URL:  https://mail.google.com/
Username:  fejph@gmail.com
Password:  8JSh%|(Gp+.j

10:
URL:  https://mail.google.com/
Username:  jspzp@gmail.com
Password:  U=9muC.`Q.#M

11:
URL:  https://mail.google.com/
Username:  lxqfl@gmail.com
Password:  =%`{C]YcufO/

12:
URL:  https://mail.google.com/
Username:  gaxsq@gmail.com
Password:  }v5+L(2m?P^k

13:
URL:  https://mail.google.com/
Username:  lmfmy@gmail.com
Password:  fkvS<5HpBfQ+

14:
URL:  https://mail.google.com/
Username:  lwgds@gmail.com
Password:  'vIrKU:{V~(.

15:
URL:  https://mail.google.com/
Username:  xfhsc@gmail.com
Password:  )l%~;C)#]:BF

16:
URL:  https://mail.google.com/
Username:  lqmnc@gmail.com
Password:  G7sYzB-5Y^4S

17:
URL:  https://mail.google.com/
Username:  dufva@gmail.com
Password:  [epVbqSY9i(C

18:
URL:  https://mail.google.com/
Username:  iprdb@gmail.com
Password:  !-{Y=4zCQNxe

19:
URL:  https://mail.google.com/
Username:  tdwtk@gmail.com
Password:  -&lI-L3F-qh3

20:
URL:  https://mail.google.com/
Username:  zndyh@gmail.com
Password:  /jc\jX3r`j0d

21:
URL:  https://mail.google.com/
Username:  rebpq@gmail.com
Password:  57E1#iS5cJHV

22:
URL:  https://mail.google.com/
Username:  zxcwn@gmail.com
Password:  }B%J;/T/]qU/

23:
URL:  https://mail.google.com/
Username:  yprzi@gmail.com
Password:  _Jy--b4C>VAi

24:
URL:  https://mail.google.com/
Username:  kcuak@gmail.com
Password:  BZ{tt\^!+n6}

25:
URL:  https://mail.google.com/
Username:  lovwb@gmail.com
Password:  1b3qg4':Haj6

26:
URL:  https://mail.google.com/
Username:  ldjtc@gmail.com
Password:  %W==M3DQ1sYf

27:
URL:  https://mail.google.com/
Username:  ucyvt@gmail.com
Password:  !PA_}_Gh/PAL

28:
URL:  https://mail.google.com/
Username:  gdxpf@gmail.com
Password:  #rGJXE*~<Fi9

29:
URL:  https://mail.google.com/
Username:  bxmxa@gmail.com
Password:  (NNv{.`rW$zk

30:
URL:  https://mail.google.com/
Username:  dhjxr@gmail.com
Password:  7Lf>)oBUmU_M

31:
URL:  https://mail.google.com/
Username:  oyogz@gmail.com
Password:  2\ZWv^\*\%?y

32:
URL:  https://mail.google.com/
Username:  kgukb@gmail.com
Password:  .:b'L/YGx'-v

33:
URL:  https://mail.google.com/
Username:  gceei@gmail.com
Password:  +Ubu5~y38}jA

34:
URL:  https://mail.google.com/
Username:  vvntt@gmail.com
Password:  W:4KRP6c.0!#

35:
URL:  https://mail.google.com/
Username:  dozie@gmail.com
Password:  5Nz/*uTbr52l

36:
URL:  https://mail.google.com/
Username:  fetpb@gmail.com
Password:  YRwzN8t}/'e{

37:
URL:  https://mail.google.com/
Username:  rwifn@gmail.com
Password:  *8+hE"z%.i1X

38:
URL:  https://mail.google.com/
Username:  umxdy@gmail.com
Password:  }d/pu.GZMw">

39:
URL:  https://mail.google.com/
Username:  xptit@gmail.com
Password:  `^zE^SvN|3{h

40:
URL:  https://mail.google.com/
Username:  fftbc@gmail.com
Password:  }yXDt;^Z1J%<

41:
URL:  https://mail.google.com/
Username:  jozwv@gmail.com
Password:  Mf?w@=$`]mT|

42:
URL:  https://mail.google.com/
Username:  ijllo@gmail.com
Password:  ZM~fWHd2Nc(+

43:
URL:  https://mail.google.com/
Username:  ahlxn@gmail.com
Password:  kj:"[q{+8~m+
"""

# 使用正则表达式删除以数字和冒号开头的行
pattern = re.compile(r'^\d+:', re.MULTILINE)
result = re.sub(pattern, '', data)

# 打印删除后的文本
print(result)
