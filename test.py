# 引入 ChatBot
from chatterbot import ChatBot

# 建立一個 ChatBot 物件
chatbot = ChatBot(
    'Ron Obvious',
    trainer = 'chatterbot.trainers.ChatterBotCorpusTrainer'
)

# 基於英文的自動學習套件
chatbot.train("chatterbot.corpus.chinese")

# 與 ChatBot 對話，並且取得回應
chatbot.get_response("Hello, how are you today?")