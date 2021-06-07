import dbconnect
import morpheme
import yaml

db = dbconnect.SqlCommunication()
komo = morpheme.Komo()

def yaml_trainer():
    #try:
        with open('hanseo_chatbot_corpus.yaml', encoding = 'UTF-8') as corpus:
            corpus_deployment = yaml.load(corpus, Loader=yaml.FullLoader)

        sql = '''INSERT INTO conversation(input_text, output_text, pos_tags, tagging)VALUES(%s, %s, %s, %s);'''
        for i in range (int(len(corpus_deployment['Conversations']))):
            user_question = corpus_deployment['Conversations'][i][0]
            user_response = corpus_deployment['Conversations'][i][1]
            converted_question_pos = komo.komo_pos(user_question)
            converted_question_pos_v2 = komo.komo_pos_v2_str(user_question)

            val = (str(user_question), str(user_response), str(converted_question_pos_v2), str(converted_question_pos))

            db.execute(sql, val)
            db.commit()

        print('완료.')
    #except:
        print("말뭉치 파일을 열 수 없습니다.")
        exit()



def training():
    print("학습시킬 질문을 입력하세요. : ",end = '')
    user_question = input()
    converted_question_pos = komo.komo_pos(user_question)
    converted_question_pos_v2 = komo.komo_pos_v2(user_question)
    print("학습시킬 답변을 입력하세요. : ",end = '')
    user_response = input()
    print(converted_question_pos)
    print(converted_question_pos_v2)

    #sql = '''INSERT INTO conversation(input_text, output_text, pos_tags, tagging)VALUES(%s, %s, %s, %s)'''
    #val = (str(user_question), str(user_response), str(converted_question_pos_v2), str(converted_question_pos)
    #)

    #db.execute(sql, val)
    #db.commit()

training()
    
