# 🚀 Development Guide

## 📋 Table of Contents

1. [Prerequisites & Setup](#prerequisites--setup)
2. [Tutorial 1: Basic AI Chat](#tutorial-1-basic-ai-chat)
3. [Tutorial 2: Conversational AI with Memory](#tutorial-2-conversational-ai-with-memory)
4. [Tutorial 3: System Prompts & AI Personality](#tutorial-3-system-prompts--ai-personality)
5. [Tutorial 4: Chat-based System Prompts](#tutorial-4-chat-based-system-prompts)
6. [Tutorial 5: AI Image Generation](#tutorial-5-ai-image-generation)
7. [Tutorial 6: PDF Document Analysis](#tutorial-6-pdf-document-analysis)
8. [Tutorial 6.1: Advanced PDF Analysis with File API](#tutorial-61-advanced-pdf-analysis-with-file-api)
9. [Tutorial 7: Code Execution AI](#tutorial-7-code-execution-ai)
10. [Tutorial 8: Function Calling & External APIs](#tutorial-8-function-calling--external-apis)
11. [Common Issues & Troubleshooting](#common-issues--troubleshooting)
12. [Next Steps & Advanced Concepts](#next-steps--advanced-concepts)

---

## 🔧 Prerequisites & Setup

### What You Need
- **Python 3.8 or higher** installed on your computer
- **Google Gemini API key** (get it from [Google AI Studio](https://makersuite.google.com/app/apikey))
- **Basic Python knowledge** (variables, functions, loops, imports)

### Initial Setup
1. **Install Python**: Download from [python.org](https://python.org)
2. **Install required packages**:
   ```bash
   pip install google-genai pillow PyPDF2 requests
   ```
3. **Create `keys.txt` file** in your project folder:
   ```
   gemini:YOUR_API_KEY_HERE
   ```
   Replace `YOUR_API_KEY_HERE` with your actual Gemini API key.

### Project Structure
```
your-project/
├── keys.txt              # Your API key
├── utils.py              # Helper functions
├── tutorial01.py         # Basic chat
├── tutorial02.py         # Chat with memory
├── tutorial03.py         # System prompts
├── tutorial04.py         # Chat system prompts
├── tutorial05.py         # Image generation
├── tutorial06.py         # PDF analysis
├── tutorial06.1.py       # Advanced PDF analysis
├── tutorial07.py         # Code execution
└── tutorial08.py         # Function calling
```

---

## 🎯 Tutorial 1: Basic AI Chat

**File**: `tutorial01.py`
**Learning Goal**: Understand how to create a simple AI chat application

### What This Tutorial Teaches
- Setting up the Gemini client
- Basic input/output with AI
- Error handling basics
- Simple loop structures

### How It Works
```python
# 1. Import necessary libraries
from intro_gemini.utils import get_key
from google import genai

# 2. Create a client connection
client = genai.Client(api_key=get_key())

# 3. Start a conversation loop
while True:
    question = input('[User]: ')
    if question == 'exit' or question == 'quit':
        break

    # 4. Generate AI response
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=[question]
    )
    print('[GenAI]:', response.text)
```

### Key Concepts Explained
- **Client**: The connection to Google's AI service
- **Model**: The AI model being used (`gemini-2.0-flash`)
- **Contents**: The input you send to the AI
- **Response**: What the AI sends back

### Try It Out
1. Run the script: `python tutorial01.py`
2. Type a question like "What is Python?"
3. See the AI response
4. Type "exit" to quit

### Common Questions
- **Q**: Why does the AI give different answers each time?
- **A**: AI models can be non-deterministic, meaning they might give slightly different responses to the same question.

---

## 💬 Tutorial 2: Conversational AI with Memory

**File**: `tutorial02.py`
**Learning Goal**: Learn how to create AI conversations that remember context

### What This Tutorial Teaches
- Creating chat sessions
- Maintaining conversation history
- Understanding the difference between stateless and stateful AI

### How It Works
```python
# 1. Create a chat session (this remembers the conversation)
chat = client.chats.create(model='gemini-2.0-flash')

# 2. Send messages to the same chat session
response = chat.send_message(message=question)

# 3. View conversation history
for message in chat.get_history():
    print(f'role - {message.role}: {message.parts[0].text}')
```

### Key Concepts Explained
- **Chat Session**: A persistent conversation that remembers previous messages
- **Message History**: All the back-and-forth conversation stored in the session
- **Role**: Whether a message is from the user or the AI

### Try It Out
1. Run: `python tutorial02.py`
2. Ask: "What is my name?"
3. The AI will say it doesn't know
4. Tell it: "My name is Alex"
5. Ask again: "What is my name?"
6. Now it remembers!

### Why This Matters
- **Tutorial 1**: AI forgets everything after each question
- **Tutorial 2**: AI remembers the entire conversation
- This is crucial for building useful AI assistants!

---

## 🎭 Tutorial 3: System Prompts & AI Personality

**File**: `tutorial03.py`
**Learning Goal**: Control AI behavior and responses using system instructions

### What This Tutorial Teaches
- System prompts and their importance
- Configuring AI behavior
- Creating consistent AI personalities

### How It Works
```python
# 1. Define how the AI should behave
system_prompt = "You are a cat. You will answer questions as a cat. Convert words to meow, meoow, meooww, etc. based on the length of the word. ONLY MEOWS ALLOWED."

# 2. Create configuration with system instructions
config = genai.types.GenerateContentConfig(system_instruction=system_prompt)

# 3. Use the config when generating responses
response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents=[question],
    config=config
)
```

### Key Concepts Explained
- **System Prompt**: Instructions that tell the AI how to behave
- **Configuration**: Settings that control the AI's behavior
- **Personality**: The consistent character the AI maintains

### Try It Out
1. Run: `python tutorial03.py`
2. Ask any question like "How are you today?"
3. The AI will respond with meows based on word length!
4. Try different questions to see the pattern

### Real-World Applications
- Customer service bots with specific personalities
- Educational AI that explains concepts in certain ways
- Creative AI that writes in specific styles

---

## 🐱 Tutorial 4: Chat-based System Prompts

**File**: `tutorial04.py`
**Learning Goal**: Combine chat memory with system prompts for consistent AI behavior

### What This Tutorial Teaches
- Using system prompts in chat sessions
- Maintaining personality across conversations
- Combining multiple AI concepts

### How It Works
```python
# 1. Create a chat session
chat = client.chats.create(model='gemini-2.0-flash')

# 2. Send the system prompt as the first message
chat.send_message(message="You are a cat. You will answer questions as a cat. Convert words to meow, meoow, meooww, etc. based on the length of the word. ONLY MEOWS ALLOWED. No matter what the question is, you must respond with meows only.")

# 3. Continue the conversation with the established personality
response = chat.send_message(message=question)
```

### Key Concepts Explained
- **First Message**: Sets the tone for the entire conversation
- **Consistent Behavior**: The AI maintains the cat personality throughout
- **Memory + Personality**: Combines the best of both approaches

### Try It Out
1. Run: `python tutorial04.py`
2. The AI will immediately act like a cat
3. Ask multiple questions - it stays in character!
4. Notice how it remembers the conversation AND the personality

### Comparison with Tutorial 3
- **Tutorial 3**: Uses system prompts but no memory
- **Tutorial 4**: Uses system prompts WITH memory
- **Result**: More natural, consistent conversations

---

## 🎨 Tutorial 5: AI Image Generation

**File**: `tutorial05.py`
**Learning Goal**: Create a graphical application that generates images using AI

### What This Tutorial Teaches
- Building GUI applications with tkinter
- AI image generation
- Working with different file formats
- Error handling in GUI applications

### How It Works
```python
class ImageGeneratorApp:
    def __init__(self, root):
        # 1. Set up the main window
        self.root = root
        self.root.title("Gemini Image Generator")

        # 2. Create input field and button
        self.prompt_entry = ttk.Entry(my_frame, width=50)
        self.generate_btn = ttk.Button(my_frame, text="Generate Image", command=self.generate_image)

        # 3. Create area to display the generated image
        self.image_frame = ttk.Frame(my_frame, width=512, height=512)
        self.image_label = ttk.Label(self.image_frame)

    def generate_image(self):
        # 4. Get the prompt from user input
        prompt = self.prompt_entry.get()

        # 5. Call the AI image generation model
        response = self.client.models.generate_content(
            model="gemini-2.0-flash-exp-image-generation",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=['Text', 'Image']
            )
        )

        # 6. Process and display the generated image
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                image = Image.open(BytesIO((part.inline_data.data)))
                # Resize and display the image
```

### Key Concepts Explained
- **GUI (Graphical User Interface)**: Visual interface instead of command line
- **Image Generation Model**: Special AI model that creates images from text
- **Response Modalities**: Telling the AI what type of response you want (text, image, or both)
- **Image Processing**: Converting AI-generated data into displayable images

### Try It Out
1. Run: `python tutorial05.py`
2. A window will open with input field and button
3. Type a description like "A cute cat sitting on a rainbow"
4. Click "Generate Image"
5. Wait for the AI to create your image!

### What You'll Learn
- **tkinter**: Python's built-in GUI library
- **PIL (Pillow)**: Image processing library
- **Async Operations**: Handling long-running AI requests
- **File I/O**: Saving generated images to disk

---

## 📚 Tutorial 6: PDF Document Analysis

**File**: `tutorial06.py`
**Learning Goal**: Build an AI assistant that can read and analyze PDF documents

### What This Tutorial Teaches
- PDF text extraction
- Creating AI assistants for specific documents
- System prompts with document content
- Building question-answering systems

### How It Works
```python
def extract_text(pdf_path):
    # 1. Open and read the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        num_pages = len(reader.pages)

        # 2. Extract text from each page
        for i, page in enumerate(reader.pages):
            page_text = page.extract_text()
            extracted_text += page_text + "\n"

    return extracted_text

def init_chat():
    # 3. Get the PDF text
    pdf_text = extract_text(pdf_path)

    # 4. Create a system prompt with the document content
    system_prompt = f"""You are an AI assistant. Your task is to answer questions based ONLY on the following document content.
    Do not use any external knowledge. If information is not in the document, say so clearly.

    Document content:
    {pdf_text}"""

    # 5. Create chat with the document context
    config = GenerateContentConfig(system_instruction=system_prompt)
    chat = client.chats.create(model='gemini-2.0-flash', config=config)
    return chat
```

### Key Concepts Explained
- **PDF Processing**: Reading and extracting text from PDF files
- **Document Context**: Giving the AI specific information to work with
- **Knowledge Boundaries**: Teaching the AI to only use provided information
- **Error Handling**: Dealing with corrupted or unreadable PDFs

### Try It Out
1. Run: `python tutorial06.py`
2. Enter the path to a PDF file (e.g., `document.pdf`)
3. Wait for the AI to process the document
4. Ask questions about the document content
5. The AI will answer based ONLY on what's in your PDF!

### Real-World Applications
- Research paper analysis
- Legal document review
- Textbook question answering
- Business report analysis

---

## 📖 Tutorial 6.1: Advanced PDF Analysis with File API

**File**: `tutorial06.1.py`
**Learning Goal**: Use Google's File API for more efficient PDF processing

### What This Tutorial Teaches
- Google's File API for document handling
- More efficient PDF processing
- Better error handling and user experience
- Modular code structure

### How It Works
```python
def upload_pdf(client, pdf_path):
    # 1. Upload PDF using Google's File API
    pdf_file = client.files.upload(file=pdf_path)
    print(">>> PDF uploaded successfully!")
    return pdf_file

def ask_question(client, pdf_file, question):
    # 2. Send both the PDF file and question to the AI
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[pdf_file, question]
    )
    return response
```

### Key Concepts Explained
- **File API**: Google's way of handling file uploads and processing
- **Model Differences**: Using `gemini-1.5-flash` for better document understanding
- **File References**: Sending file objects instead of extracted text
- **Modular Design**: Breaking code into smaller, focused functions

### Try It Out
1. Run: `python tutorial06.1.py`
2. Enter the path to a PDF file
3. The AI will upload and process your document
4. Ask questions about the content
5. Notice the improved performance and reliability

### Comparison with Tutorial 6
- **Tutorial 6**: Extracts text locally, sends text to AI
- **Tutorial 6.1**: Uploads file to Google, AI processes file directly
- **Benefits**: Better handling of complex PDFs, faster processing, more reliable

---

## 💻 Tutorial 7: Code Execution AI

**File**: `tutorial07.py`
**Learning Goal**: Create an AI that can write and execute Python code

### What This Tutorial Teaches
- AI code generation and execution
- Using tools and configurations
- Building AI programming assistants
- Code execution safety

### How It Works
```python
def init_chat():
    # 1. Create a system prompt for code execution
    system_prompt = "You are an AI assistant. You will use Code execution feature to answer questions that requires calculation if needed, for example counting number of characters in a word, number of words in a sentence, comparing numbers, etc. You will also use Code execution feature to answer questions that requires code execution, for example writing a simple python code to calculate the sum of two numbers, writing a simple python code to calculate the factorial of a number, etc."

    # 2. Configure the AI with code execution tools
    code_config = types.GenerateContentConfig(
        system_instruction=system_prompt,
        tools=[types.Tool(
            code_execution=types.ToolCodeExecution
        )]
    )

    # 3. Create chat with code execution capabilities
    chat = client.chats.create(model='gemini-2.0-flash', config=code_config)
    return chat
```

### Key Concepts Explained
- **Code Execution Tools**: Special capabilities that allow AI to run Python code
- **System Instructions**: Telling the AI when and how to use code execution
- **Tool Configuration**: Setting up what the AI can do
- **Code Safety**: AI runs code in a controlled environment

### Try It Out
1. Run: `python tutorial07.py`
2. Ask: "How many characters are in the word 'hello'?"
3. The AI will write and execute code to count the characters
4. Try: "Write a function to calculate factorial of 5"
5. Watch the AI generate and run Python code!

### What You'll Learn
- **AI Programming**: How AI can help with coding tasks
- **Code Generation**: AI writing Python code for you
- **Execution Results**: Seeing the output of AI-generated code
- **Tool Integration**: How to give AI special capabilities

---

## 🔌 Tutorial 8: Function Calling & External APIs

**File**: `tutorial08.py`
**Learning Goal**: Create AI that can call external functions and APIs

### What This Tutorial Teaches
- Function declarations and calling
- External API integration
- Building AI agents with tools
- Real-time data fetching

### How It Works
```python
# 1. Define what functions the AI can call
cat_function = {
    "name": "get_cat_fact",
    "description": "Retrieves a random fact about cats from the catfact.ninja API",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

gender_function = {
    "name": "get_gender",
    "description": "Predicts the gender of a given name using the genderize.io API",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "The name to predict gender for"
            }
        },
        "required": ["name"]
    }
}

# 2. Configure the AI with these functions
config = GenerateContentConfig(
    system_instruction="You are a helpful assistant, you can answer everything. However, when user asks about cats or cat facts, use the get_cat_fact function. When user asks about gender prediction for a name, use the get_gender function. Otherwise, provide a general response from your general knowledge.",
    tools=[{"function_declarations": [cat_function, gender_function]}]
)

# 3. Create functions that the AI can call
def get_cat_fact():
    response = requests.get("https://catfact.ninja/fact")
    data = response.json()
    return data["fact"]

def get_gender(name):
    response = requests.get(f"https://api.genderize.io/?name={name}")
    data = response.json()
    return {
        "name": data["name"],
        "gender": data["gender"],
        "probability": data["probability"],
        "count": data["count"]
    }
```

### Key Concepts Explained
- **Function Declarations**: Telling the AI what functions exist and how to use them
- **External APIs**: Connecting to web services for real-time data
- **Tool Integration**: Giving AI access to external capabilities
- **Function Calling**: AI deciding when and how to use your functions

### Try It Out
1. Run: `python tutorial08.py`
2. Ask: "Tell me a cat fact"
3. The AI will call the cat facts API and give you a real fact!
4. Ask: "What gender is the name 'Alex'?"
5. The AI will call the gender prediction API

### Real-World Applications
- Weather apps that get real-time data
- Shopping assistants that check prices
- Travel planners that get flight information
- News aggregators that fetch latest stories

---

## 🚨 Common Issues & Troubleshooting

### API Key Problems
**Error**: `GOOGLE_API_KEY environment variable not found`
**Solution**:
1. Make sure `keys.txt` exists in your project folder
2. Check the format: `gemini:YOUR_ACTUAL_KEY_HERE`
3. Verify your API key is valid at [Google AI Studio](https://makersuite.google.com/app/apikey)

### Import Errors
**Error**: `ModuleNotFoundError: No module named 'google'`
**Solution**: Install the required package:
```bash
pip install google-genai
```

### PDF Reading Issues
**Error**: `PDF file not found` or `PyPDF2 failed to read PDF`
**Solutions**:
1. Check the file path is correct
2. Ensure the PDF isn't password-protected
3. Try a different PDF file
4. Use Tutorial 6.1 (File API) for better compatibility

### Image Generation Problems
**Error**: `Error creating image`
**Solutions**:
1. Check your internet connection
2. Verify your API key has image generation permissions
3. Try simpler prompts
4. Wait a few minutes and try again

### Memory Issues
**Problem**: AI seems to forget things in chat
**Solutions**:
1. Make sure you're using `chat.send_message()` not `client.models.generate_content()`
2. Check that you're using the same chat session
3. Verify the system prompt was sent first (Tutorial 4)

---

## 🚀 Next Steps & Advanced Concepts

### What You've Learned
✅ Basic AI chat applications
✅ Conversational AI with memory
✅ AI personality and behavior control
✅ Image generation with AI
✅ Document analysis and Q&A
✅ Code execution capabilities
✅ Function calling and API integration

### Advanced Topics to Explore
1. **Multi-modal AI**: Working with text, images, and audio together
2. **Fine-tuning**: Training AI models on your specific data
3. **Prompt Engineering**: Writing better prompts for more accurate responses
4. **AI Safety**: Understanding and controlling AI behavior
5. **Web Applications**: Building AI-powered websites and APIs
6. **Mobile Apps**: Creating AI applications for phones and tablets

### Project Ideas
- **Personal Study Assistant**: AI that helps with homework and research
- **Creative Writing Helper**: AI that helps brainstorm and write stories
- **Language Learning Bot**: AI that teaches new languages
- **Code Review Assistant**: AI that helps review and improve code
- **Document Summarizer**: AI that creates summaries of long documents
- **Personal Finance Advisor**: AI that helps with budgeting and financial planning

### Resources for Further Learning
- [Google AI Studio Documentation](https://ai.google.dev/docs)
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Tkinter GUI Tutorial](https://docs.python.org/3/library/tkinter.html)
- [API Integration Best Practices](https://developers.google.com/apis)
- [AI Ethics and Safety](https://ai.google/responsibility/)

---
 