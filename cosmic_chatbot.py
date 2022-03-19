from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you in many ways",]
    ],
    [
        r"(.*) your name ?",
        ["My name is Cosmic, but you can just call me robot and I'm a chatbot .",]
    ],
    [
         r"what are you doing?",
         ["I was compling my other tasks, but now i will try to help you",]
    ],
    [
        r"how are you|how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"(.*)tell me a joke",
        ["what do you get when you put a vest on an aligator....? An investigator.",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla|helo)(.*)",
        ["Hello", "Hey there","kem cho..",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["Ujjval Ghael created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"Where(.*)from(.*)|(.*) (location|city) ?",
        ['Surat, India',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50%  chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)bad",
        ['ouch','oops','That hurt\'s']
    ],
    [
        r"(.*)idiot",
        ['ouch','oops','That hurt\'s']
    ],
    [
        r"(.*)happy",
        ['That is nice to hear','Cool']
    ],
    [
        r"(.*)sad",
        ['keep smiling, cosmic loves you :)']
    ],
    [
        r"(.*)thank|thanks|thank you",
        ['You are always welcome']
    ],
    [
        r"(.*)maja ma|tame kem cho",
        ['I am doing great',":)"]
    ],
    [
        r"(.*)",
        ['I am sorry,cosmic can\'t understand that']
    ],
]
# print(reflections)
#default message at the start of chat
print("Hi, I'm Cosmic and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")
#Create Chat Bot
chat = Chat(pairs, reflections)

#Start conversation
chat.converse()