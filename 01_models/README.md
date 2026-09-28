# 01 - Models

Models are the core components of LangChain applications.
They are used to generate text, understand conversations, and convert text into numerical vectors.

In this section, we will learn about three important types of models:

1. **LLMs (Large Language Models)**
2. **Chat Models**
3. **Embedding Models**

---

## 1. LLMs (Large Language Models)

**LLM** stands for **Large Language Model**.

An LLM takes text as input and generates text as output.

### Simple Example

```text
Input:
What is LangChain?

        ↓

LLM

        ↓

Output:
LangChain is a framework for building applications with
Large Language Models.
```

### What are LLMs used for?

LLMs can be used for:

* Text generation
* Question answering
* Summarization
* Translation
* Content generation
* Code generation
* Text analysis

### Basic Concept

```text
Text Input
    ↓
   LLM
    ↓
Text Output
```

---

## 2. Chat Models

A **Chat Model** is designed specifically for conversational interactions.

Instead of simply working with plain text, chat models work with **messages** such as:

* System message
* Human message
* AI message

### Example

```text
System:
You are a helpful teacher.

Human:
What is LangChain?

        ↓

Chat Model

        ↓

AI:
LangChain is a framework for building
applications with LLMs.
```

### Chat Models are useful for:

* Chatbots
* AI assistants
* Customer support systems
* Question-answering applications
* Interactive AI applications
* Multi-turn conversations

### Basic Concept

```text
System Message
       +
Human Message
       ↓
   Chat Model
       ↓
   AI Response
```

### LLM vs Chat Model

| LLM                                 | Chat Model              |
| ----------------------------------- | ----------------------- |
| Works mainly with text input/output | Works with messages     |
| Text completion/generation          | Conversation-focused    |
| Simple text-based applications      | Chatbots and assistants |
| Input → Output                      | Messages → AI message   |

---

## 3. Embedding Models

An **Embedding Model** converts text into a list of numbers called a **vector**.

These vectors represent the meaning or semantic information of the text.

### Example

```text
"LangChain is a framework"

        ↓

Embedding Model

        ↓

[0.021, -0.145, 0.782, 0.331, ...]
```

The output is called an **embedding** or **vector**.

### Why do we need Embeddings?

Embeddings are mainly used when we want a computer to compare the meaning of different pieces of text.

They are commonly used for:

* Semantic search
* Document search
* Recommendation systems
* RAG applications
* Similarity search
* Vector databases

### Example

```text
Text 1:
"I love learning Python."

Text 2:
"Python is my favorite programming language."

        ↓

Embedding Model

        ↓

Two vectors

        ↓

Compare similarity

        ↓

High similarity
```

Even though the two sentences use different words, their meanings are similar.

---

# Quick Comparison

| Model               | Main Purpose      | Input    | Output     |
| ------------------- | ----------------- | -------- | ---------- |
| **LLM**             | Generate text     | Text     | Text       |
| **Chat Model**      | Conversation      | Messages | AI Message |
| **Embedding Model** | Represent meaning | Text     | Vector     |

---

# Simple Way to Remember

```text
LLM
↓
Generates Text

Chat Model
↓
Talks with Users

Embedding Model
↓
Converts Text → Numbers
```

---

# LangChain Model Flow

A typical LangChain application can use all three:

```text
              LangChain Application
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
        LLM       Chat Model    Embeddings
          │            │            │
          ↓            ↓            ↓
     Text Output   Conversation   Vectors
```

---

## What I Learned

* LLMs generate text.
* Chat Models are designed for conversations.
* Embedding Models convert text into numerical vectors.
* Embeddings are very important for RAG and semantic search.
* Different models are used for different tasks.

---
