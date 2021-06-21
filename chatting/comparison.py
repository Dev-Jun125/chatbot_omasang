from pymysql import NULL
from . import dbconnect
from . import morpheme
from collections import Counter
import random
"""
id_list는 pos_tags에 저장된 입력한 질문의 명사 리스트를 데이터베이스 
명사 태그들과 하나씩 비교하여 그 명사가 들어있는 해당 답변의 번호를 출력한다. 
"""

komo = morpheme.Komo()

#indexing db
def response_select(user_input):
    db = dbconnect.SqlCommunication()
    pos_list = komo.komo_pos_v2(user_input, state = 'normal')
    id_list = []
    word_list = []
    selected_response = []

    sql = '''SELECT id FROM badword WHERE pos_tags = %s;'''
    
    for i in range (len(pos_list)):
        val = (pos_list[i] ,)
        result = db.fetchall(sql,val)
        try:
            for j in range (len(result)):
                word_list.append(result[j][0])
        except:
            pass
    if(word_list!=[]):
        for i in range (0,5):
            selected_response.append(['욕은 하지말아주세요.'])
        return selected_response


    sql = '''SELECT id FROM conversation WHERE pos_tags LIKE %s;'''
    for i in range (len(pos_list)):
        val = ('%' + pos_list[i] + '%',)
        result = db.fetchall(sql,val)        
        try:
            for j in range (len(result)):
                id_list.append(result[j][0])
        except:
            pass
    mfv = Counter(id_list).most_common() # most frequency value, [(질문번호1, 점수1), (질문번호2, 점수2)]
    try:
        sql = '''SELECT output_text FROM conversation WHERE id = %s;'''
        val = (mfv[0][0])
        if(db.fetchone(sql,val)[0]=='1'):
            val = random.randint(1,12)
            sql = '''SELECT * FROM recommend_menu WHERE recomenuId = %s; '''
            selected_response.append(['오늘은 '+db.fetchone(sql, val)[2] + ' '  + db.fetchone(sql, val)[1]+' 어때요?'])
        elif(db.fetchone(sql,val)[0]=='2'):
            

            val = random.randint(1,6)
            sql = '''SELECT tipOutput FROM tip WHERE idx = %s;'''
            print(db.fetchone(sql,val)[0])
            selected_response.append(['이거 너만 알려주는건데 '+db.fetchone(sql, val)[0]])    
        else:
            selected_response.append(db.fetchone(sql, val))
        try:
            sql = '''SELECT input_text FROM conversation WHERE id = %s;'''
            for i in range (1,5):
                val = (mfv[i][0],)
                selected_response.append(db.fetchone(sql,val))
        except:
            for i in range (1,5):
                selected_response.append([('NULL'),])
    except:
        selected_response = [('죄송해요. 잘 모르겠어요.',)] # 검색결과가 없을 때 송출 메시지
        for i in range (1,5):
            selected_response.append([('NULL'),])
    db.close()
    return selected_response
        

def most_frequency_value(id_list):
    mfv = Counter()


def userinput(userinput):
    db = dbconnect.SqlCommunication()

    sql = '''INSERT INTO `userInput` (userInput) 
    VALUES (%s);'''

    db.cursor.execute(sql,userinput)
    db.commit()

def hello_tip():
    db = dbconnect.SqlCommunication()
    val = random.randint(1,6)
    selected_response = []
    sql = '''SELECT tipOutput FROM tip WHERE idx = %s;'''
    selected_response.append('안녕~ 나는 오마상이야\n 혹시 너 그거 알아?\n '+db.fetchone(sql, val)[0])
    db.close()
    return selected_response
