def deletestr(a,b): #문자열 삭제
    return a.replace(b,'')
    
def deletesymbol(a): #절댓값
    return (a**2)**0.5
    
def add(a,b): #더하기
    if 'str' in str(type(a)) or 'str' in str(type(b)):
        return str(a)+str(b)
    elif 'float' in str(type(a)) or 'float' in str(type(b)):
        return a+b
    elif 'int' in str(type(a)) or 'int' in str(type(b)):
        return a+b
        
def lastdigit(a): #마지막 글자
    return a[len(a)-1]
    
def dellastobj(a): #마지막 항목 삭제(리스트)
    a.remove(a[len(a)-1])
    
def average(a): #평균
    b=0
    for i in range(len(a)):
        b+=a[i]
    b=b/(len(a))
    return b
    
def mode(a): #최빈값
    d=[]
    b=[]
    b.append(a[0])
    for i in range (len(a)):
        c=0
        for j in range (len(b)):
            if a[i]==b[j]:pass
            else:
                c=c+1
        if c==len(b):
            b.append(a[i])
    for i in range (len(b)):
        d.append('')
    for i in range (len(b)):
        hm=0
        for j in range (len(a)):
            if b[i]==a[j]:
                hm=hm+1
        d[i]=hm
    hmm=max(d)
    largest=[]
    h=0
    for i in range (len(d)):
        if d[i]==d[0]:
            h=h+1
    if h==len(d):
        return 'There is no mode.'
    else:
        for i in range (len(d)):
            if max(d)==d[i]:
                largest.append(b[i])
        return largest
        
def median(a): #중앙값
    d=[]
    for i in range (len(a)):
        d.append(a[i])
    d.sort()
    if len(d)%2==0:
        b=(d[int((len(d))/2)]+d[int((len(d))/2-1)])/2
    elif len(d)%2==1:
        b=d[int((len(d)-1)/2)]
    return b
def deviation(a): #편차
    b=0
    for i in range (len(a)):
        b+=a[i]
    b=b/(len(a))
    c=[]
    for i in range (len(a)):
        c.append(a[i]-b)
    return c
def variance(a): #분산
    b=0
    for i in range (len(a)):
        b+=a[i]
    b=b/(len(a))
    c=[]
    for i in range (len(a)):
        c.append(a[i]-b)
    d=0
    for i in range (len(a)):
        d=d+((c[i])**2)
    d=d/5
    return d
def standevia(a): #표준편차
    b=0
    for i in range (len(a)):
        b+=a[i]
    b=b/(len(a))
    c=[]
    for i in range (len(a)):
        c.append(a[i]-b)
    d=0
    for i in range (len(a)):
        d=d+((c[i])**2)
    d=d/5
    d=d**(1/2)
    return d
def triangle(a,b): #삼각형 넓이
    c=a*b/2
    return c
def square(a,b): #사각형 넓이
    c=a*b
    return c
def circle(a): #원 넓이
    c=a*a*3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
    return c
def sphere(a): #구 넓이
    c=a*a*3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679/3*4
    return c
def duum(a,showcomment=True): #두음법칙
    if showcomment:
        print('아직 미 구현된 두음법칙 기능입니다. 그래도 ㄴ으로 시작하는 것들은 다 되며 ㄹ도 차차 추가될 예정입니다. 이 메시지는 duum(-,showcomment=False)로 설정해서 끌 수 있습니다.')
    if a=='녀':
        return '여'
    elif a=='녁':
        return '역'
    elif a=='년':
        return '연'
    elif a=='녇':
        return '엳'
    elif a=='녈':
        return '열'
    elif a=='념':
        return '염'
    elif a=='녑':
        return '엽'
    elif a=='녓':
        return '엿'
    elif a=='녕':
        return '영'
    elif a=='녖':
        return '옂'
    elif a=='녗':
        return '옃'
    elif a=='녘':
        return '옄'
    elif a=='녙':
        return '옅'
    elif a=='녚':
        return '옆'
    elif a=='녛':
        return '옇'
    elif a=='녂':
        return '엮'
    elif a=='녔':
        return '였'
    elif a=='녃':
        return '엯'
    elif a=='녅':
        return '엱'
    elif a=='녆':
        return '엲'
    elif a=='녉':
        return '엵'
    elif a=='녊':
        return '엶'
    elif a=='녋':
        return '엷'
    elif a=='녌':
        return '엸'
    elif a=='녍':
        return '엹'
    elif a=='녎':
        return '엺'
    elif a=='녏':
        return '엻'
    elif a=='녒':
        return '엾'
    elif a=='녜':
        return '예'
    elif a=='녝':
        return '옉'
    elif a=='녠':
        return '옌'
    elif a=='녣':
        return '옏'
    elif a=='녤':
        return '옐'
    elif a=='녬':
        return '옘'
    elif a=='녭':
        return '옙'
    elif a=='녯':
        return '옛'
    elif a=='녱':
        return '옝'
    elif a=='녲':
        return '옞'
    elif a=='녳':
        return '옟'
    elif a=='녴':
        return '옠'
    elif a=='녵':
        return '옡'
    elif a=='넾':
        return '엪'
    elif a=='넿':
        return '엫'
    elif a=='뇨':
        return '요'
    elif a=='뇩':
        return '욕'
    elif a=='뇬':
        return '뇬'
    elif a=='뇯':
        return '욛'
    elif a=='뇰':
        return '욜'
    elif a=='뇸':
        return '욤'
    elif a=='뇹':
        return '욥'
    elif a=='뇻':
        return '욧'
    elif a=='뇽':
        return '용'
    elif a=='뇾':
        return '욪'
    elif a=='뇿':
        return '욫'
    elif a=='눀':
        return '욬'
    elif a=='눁':
        return '욭'
    elif a=='눂':
        return '욮'
    elif a=='눃':
        return '욯'
    elif a=='뇪':
        return '욖'
    elif a=='뇼':
        return '욨'
    elif a=='뇫':
        return '욗'
    elif a=='뇭':
        return '욙'
    elif a=='뇮':
        return '욚'
    elif a=='뇱':
        return '욝'
    elif a=='뇲':
        return '욞'
    elif a=='뇳':
        return '욟'
    elif a=='뇴':
        return '욠'
    elif a=='뇵':
        return '욡'
    elif a=='뇶':
        return '욢'
    elif a=='뇷':
        return '욣'
    elif a=='뇺':
        return '욦'
    elif a=='뉴':
        return '유'
    elif a=='뉵':
        return '육'
    elif a=='뉸':
        return '윤'
    elif a=='뉻':
        return '윧'
    elif a=='뉼':
        return '율'
    elif a=='늄':
        return '윰'
    elif a=='늅':
        return '윱'
    elif a=='늇':
        return '윳'
    elif a=='늉':
        return '융'
    elif a=='늊':
        return '윶'
    elif a=='늋':
        return '윷'
    elif a=='늌':
        return '윸'
    elif a=='늍':
        return '윹'
    elif a=='늎':
        return '윺'
    elif a=='늏':
        return '윻'
    elif a=='뉶':
        return '윢'
    elif a=='늈':
        return '윴'
    elif a=='뉷':
        return '윣'
    elif a=='뉹':
        return '윥'
    elif a=='뉺':
        return '윦'
    elif a=='뉽':
        return '윩'
    elif a=='뉾':
        return '윪'
    elif a=='뉿':
        return '윫'
    elif a=='늀':
        return '윬'
    elif a=='늁':
        return '윭'
    elif a=='늂':
        return '윮'
    elif a=='늃':
        return '윯'
    elif a=='니':
        return '이'
    elif a=='닉':
        return '익'
    elif a=='닌':
        return '인'
    elif a=='닏':
        return '읻'
    elif a=='닐':
        return '일'
    elif a=='님':
        return '임'
    elif a=='닙':
        return '입'
    elif a=='닛':
        return '잇'
    elif a=='닝':
        return '잉'
    elif a=='닞':
        return '잊'
    elif a=='닟':
        return '잋'
    elif a=='닠':
        return '잌'
    elif a=='닡':
        return '잍'
    elif a=='닢':
        return '잎'
    elif a=='닣':
        return '잏'
    elif a=='닊':
        return '읶'
    elif a=='닜':
        return '있'
    elif a=='닋':
        return '읷'
    elif a=='닍':
        return '읹'
    elif a=='닎':
        return '읺'
    elif a=='닑':
        return '읽'
    elif a=='닒':
        return '읾'
    elif a=='닓':
        return '읿'
    elif a=='닔':
        return '잀'
    elif a=='닕':
        return '잁'
    elif a=='닖':
        return '잂'
    elif a=='닗':
        return '잃'
    elif a=='윲':
        return '윲'
    elif a=='라':
        return '나'
    elif a=='락':
        return '낙'
    elif a=='란':
        return '난'
    elif a=='랃':
        return '낟'
    elif a=='랄':
        return '날'
    elif a=='람':
        return '남'
    elif a=='랍':
        return '납'
    elif a=='랏':
        return '낫'
    elif a=='랑':
        return '낭'
    elif a=='랒':
        return '낮'
    elif a=='랓':
        return '낯'
    elif a=='랔':
        return '낰'
    elif a=='랕':
       return '낱'
    elif a=='랖':
       return '낲'
    elif a=='랗':
       return '낳'
    elif a=='띾':
       return '낚'
    elif a=='랐':
       return '났'
    elif a=='띿':
       return '낛'
    elif a=='랁':
       return '낝'
    elif a=='랂':
       return '낞'
    elif a=='랆':
       return '낢'
    elif a=='랇':
       return '낣'
    elif a=='랈':
       return '낤'
    elif a=='랉':
       return '낥'
    elif a=='랊':
       return '낦'
    elif a=='랋':
       return '낧'
    elif a=='랎':
       return '낪'
    elif a=='략':
       return '약'
    elif a=='랸':
        return '얀'
    elif a=='랻':
        return '얃'
    elif a=='랼':
        return '얄'
    elif a=='럄':
        return '얌'
    elif a=='럅':
        return '얍'
    elif a=='럇':
        return '얏'
    elif a=='량':
        return '양'
    elif a=='럊':
        return '낮'
    elif a=='럋':
        return '냧'
    elif a=='럌':
        return '얔'
    elif a=='럍':
        return '얕'
    elif a=='럎':
        return '냪'
    elif a=='럏':
        return '냫'
    elif a=='랶':
        return '냒'
    elif a=='럈':
        return '냤'
    elif a=='랷':
        return '냓'
    elif a=='랹':
        return '냕'
    elif a=='랺':
        return '냖'
    elif a=='랽':
        return '얅'
    elif a=='랾':
        return '얆'
    elif a=='랿':
        return '얇'
    elif a=='럀':
        return '얈'
    elif a=='럁':
        return '얉'
    elif a=='럂':
        return '얊'
    elif a=='럃':
        return '얋'
    elif a=='럆':
        return '얎'
    elif a=='려':
        return '여'
    elif a=='력':
        return '역'
    elif a=='련':
        return '연'
    elif a=='렫':
    	return '엳'
    elif a=='렬':
    	return '열'
    elif a=='렴':
    	return '염'
    elif a=='렵':
    	return '엽'
    elif a=='렷':
    	return '엿'
    elif a=='령':
    	return '영'
    elif a=='렺':
    	return '옂'
    elif a=='렻':
    	return '옃'
    elif a=='렼':
    	return '옄'
    elif a=='렽':
    	return '옅'
    elif a=='렾':
    	return '옆'
    elif a=='렿':
    	return '옇'
    elif a=='렦':
    	return '엮'
    elif a=='렸':
    	return '였'
    elif a=='렧':
    	return '엯'
    elif a=='렩':
    	return '엱'
    elif a=='렪':
    	return '엲'
    elif a=='렭':
    	return '엵'
    elif a=='렮':
    	return '엶'
    elif a=='렯':
    	return '엷'
    elif a=='렰':
    	return '엸'
    elif a=='렱':
    	return '엹'
    elif a=='렲':
    	return '엺'
    elif a=='렳':
    	return '엻'
    elif a=='렶':
    	return '엾'
    else:
        return a

def percent(int): #확률
	from random import randrange
	if randrange(1,101)<=int and int<=100:
		return True
	else:
		return False