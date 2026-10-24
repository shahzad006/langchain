# LangChain Prompts --- Complete Notes

These notes explain the six topics in the `02_prompts` folder in simple
Roman Urdu with Python examples.

## 1. Static Prompt (`1_static_prompt.py`)

### What is a static prompt?

Static prompt woh prompt hota hai jiska text pehle se fixed hota hai.
Har dafa model ko lagbhag wahi instructions di jati hain. User ki input
ke mutabiq prompt ka text automatically change nahi hota.

### Example

``` python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Explain what a computer is in simple words."
)

formatted_prompt = prompt.format()
print(formatted_prompt)
```

### When to use it

-   Jab aapko har dafa same instructions deni hon.
-   Simple tasks, fixed instructions, ya basic experiments ke liye.

### Remember

**Static = fixed text.**

------------------------------------------------------------------------

## 2. Dynamic Prompt (`2_Dynamic_Prompt.py`)

### What is a dynamic prompt?

Dynamic prompt mein placeholders/variables hote hain. Program user ki
input ke mutabiq un placeholders ki values fill karta hai. Is tarah har
request par prompt badal sakta hai.

### Example

``` python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Explain {topic} in {language} using simple words."
)

formatted_prompt = prompt.format(
    topic="Artificial Intelligence",
    language="English"
)

print(formatted_prompt)
```

Output:

``` text
Explain Artificial Intelligence in English using simple words.
```

### When to use it

-   User se topic, language, level, ya question lena ho.
-   Ek hi template ko different inputs ke saath reuse karna ho.

### Remember

**Dynamic = template + variables.**\
Template ke `{topic}` aur `{language}` jaise placeholders ko values dena
zaroori hota hai.

------------------------------------------------------------------------

## 3. Prompt Generator (`3_prompt_generator.py`)

### What is a prompt generator?

Prompt generator ka kaam input ya requirements ki bunyaad par prompt
tayyar karna hota hai. Is mein aap ek template ko variables ke saath use
kar sakte hain, ya LLM se kisi task ke liye prompt banwa sakte hain.

### Example: variables se prompt generate karna

``` python
from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "You are a {role}. Teach {topic} to a beginner. "
    "Use {style} language and include one example."
)

generated_prompt = prompt_template.format(
    role="Python teacher",
    topic="loops",
    style="simple"
)

print(generated_prompt)
```

### Output idea

``` text
You are a Python teacher. Teach loops to a beginner.
Use simple language and include one example.
```

### When to use it

-   Different roles ya tasks ke liye prompts banana ho.
-   Prompt ko reusable aur organized rakhna ho.
-   User ke options ke mutabiq prompt ki instructions change karni hon.

### Remember

Prompt generator khud zaroori nahi ke AI model ho. Kabhi yeh sirf code
hota hai jo template mein values fill karke prompt banata hai.

------------------------------------------------------------------------

## 4. Chatbot (`4_chatbot.py`)

### What is a chatbot?

Chatbot aisa program hota hai jahan user message bhejta hai aur AI model
jawab deta hai. LangChain mein prompt aur chat model ko chain ke zariye
connect kiya ja sakta hai.

### Example

``` python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful teacher. Explain concepts simply."),
    ("human", "{question}")
])

chain = prompt | model

response = chain.invoke({
    "question": "What is a Python function?"
})

print(response.content)
```

### Important terms

-   **System message:** Model ka role, behavior aur instructions set
    karta hai.
-   **Human message:** User ka question ya input hota hai.
-   **Model:** AI system jo response generate karta hai.
-   **Chain:** Prompt aur model ko `|` operator se connect karna.
-   **invoke():** Chain ko input de kar run karna.
-   **response.content:** Model ke jawab ka text.

### When to use it

Interactive question-answer systems, study assistants, customer support,
aur learning bots ke liye.

------------------------------------------------------------------------

## 5. Messages (`5_messages.py`)

### What are messages?

Chat models ko conversation aam tor par messages ki list ki form mein di
jati hai. Har message ka ek role hota hai jo batata hai ke message kis
taraf se aaya hai.

### Common message roles

-   **System:** Model ko instructions deta hai.
-   **Human:** User ka message.
-   **AI:** Model ka response.
-   **Tool:** Kisi tool ke result ka message, jab tool use kiya gaya ho.

### Example

``` python
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

messages = [
    SystemMessage(content="You are a helpful Python teacher."),
    HumanMessage(content="Explain a Python list in simple words.")
]

response = model.invoke(messages)
print(response.content)
```

### When to use it

-   Jab aapko conversation ke roles clearly define karne hon.
-   Jab multiple messages model ko dene hon.
-   Jab previous conversation ko message history ki form mein maintain
    karna ho.

### Remember

`SystemMessage` instructions ke liye, `HumanMessage` user input ke liye,
aur `AIMessage` assistant response represent karne ke liye use hota hai.

------------------------------------------------------------------------

## 6. Messages Placeholder (`6_message_placeholder.py`)

### What is `MessagesPlaceholder`?

`MessagesPlaceholder` chat prompt ke andar messages ki list insert karne
ke liye use hota hai. Yeh conversation history ko prompt mein include
karne ka common tareeqa hai.

### Example

``` python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])

formatted_prompt = prompt.invoke({
    "chat_history": [
        HumanMessage(content="My name is Ali."),
        AIMessage(content="Nice to meet you, Ali.")
    ],
    "question": "What is my name?"
})

print(formatted_prompt)
```

### How it works

1.  System instruction add hoti hai.
2.  `chat_history` ke messages prompt mein insert hote hain.
3.  Current question end mein add hota hai.
4.  Is formatted prompt ko model ke saath use karke response liya ja
    sakta hai.

### Important

`MessagesPlaceholder` khud se memory save nahi karta. Aapko conversation
history provide karni hoti hai, ya apne chatbot mein history manage
karne ka mechanism banana hota hai.

### Optional placeholder

Agar history dena optional rakhna ho:

``` python
MessagesPlaceholder(
    variable_name="chat_history",
    optional=True
)
```

### Remember

**MessagesPlaceholder = conversation messages ko prompt ke andar insert
karne ki jagah.**

------------------------------------------------------------------------

## Quick Comparison

  Topic                 Main purpose                      Key idea
  --------------------- --------------------------------- -------------------------
  Static Prompt         Fixed instructions                Text fixed hota hai
  Dynamic Prompt        Inputs ke mutabiq prompt          Variables/placeholders
  Prompt Generator      Prompt tayyar karna               Template + requirements
  Chatbot               User ko AI response dena          Prompt + model
  Messages              Conversation roles define karna   System, Human, AI
  MessagesPlaceholder   Chat history insert karna         Messages ki list

