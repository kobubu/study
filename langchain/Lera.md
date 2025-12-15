# Telegram Chat Bot Recreation Guide

This guide explains how to recreate a sophisticated Telegram chat bot that participates naturally in group conversations. The bot uses Claude via AWS Bedrock and has a persistent persona with memory capabilities.

---

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Tech Stack](#tech-stack)
3. [Project Structure](#project-structure)
4. [Core Components](#core-components)
5. [Memory System](#memory-system)
6. [Tools System](#tools-system)
7. [Message Flow](#message-flow)
8. [Response Decision Logic](#response-decision-logic)
9. [Proactive Messaging](#proactive-messaging)
10. [Configuration](#configuration)
11. [System Prompt Design](#system-prompt-design)
12. [External Services Integration](#external-services-integration)
13. [Running the Bot](#running-the-bot)
14. [Testing](#testing)

---

## Architecture Overview

The bot is designed as a **natural chat participant**, not an assistant. Key principles:

- **Persona-driven**: Has a distinct personality, mood states, and opinions
- **Memory-rich**: Multiple layers of short-term and long-term memory
- **Selective responder**: Uses AI to decide when to speak vs. stay silent
- **Tool-enabled**: Can search the web, generate images, read URLs, and more
- **Proactive**: Can initiate conversations when the chat goes quiet

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Telegram Bot API                         │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
┌─────────────────────────────────▼───────────────────────────────┐
│                      Message Handlers                           │
│  - Text messages                                                │
│  - Photo/image messages                                         │
│  - Sticker messages                                             │
│  - Reply chain capture                                          │
│  - Burst detection (groups rapid messages)                      │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
┌─────────────────────────────────▼───────────────────────────────┐
│                     Chat Context Manager                        │
│  - Message history (in-memory deque)                            │
│  - Reply chain tracking                                         │
│  - Image caching                                                │
│  - Mood state                                                   │
│  - LangChain message history                                    │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
┌─────────────────────────────────▼───────────────────────────────┐
│                      Memory Manager                             │
│  - SQLite message store                                         │
│  - ChromaDB vector store (semantic search)                      │
│  - Summarization service (hourly summaries)                     │
│  - User profile extraction                                      │
│  - Long-term memory (JSON)                                      │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
┌─────────────────────────────────▼───────────────────────────────┐
│                    Response Generation                          │
│  - SKIP filter (Haiku - decides if bot should respond)          │
│  - Main response (Opus - generates response with tools)         │
│  - Extended thinking support                                    │
│  - Tool execution loop                                          │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
┌─────────────────────────────────▼───────────────────────────────┐
│                    Command Dispatcher                           │
│  - REACT:emoji - send reaction                                  │
│  - VOICE:text - send voice message (TTS)                        │
│  - IMAGE:caption - send generated image                         │
│  - FORWARD:id - forward a message                               │
│  - SKIP - no response                                           │
│  - Plain text - regular message                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Tech Stack

### Required Services

| Service | Purpose | Alternative |
|---------|---------|-------------|
| **AWS Bedrock** | Claude LLM (Opus, Haiku), Nova embeddings | Direct Anthropic API |
| **Telegram Bot API** | Messaging platform | Discord, Slack |
| **SQLite** | Message persistence | PostgreSQL |
| **ChromaDB** | Vector storage for semantic search | Pinecone, Weaviate |
| **ElevenLabs** | Text-to-speech for voice messages | AWS Polly, Google TTS |
| **Serper** | Web search | Google Custom Search, Tavily |
| **Jina/Firecrawl** | Webpage content extraction | None needed if basic |
| **Seedream (ByteDance)** | Image generation | DALL-E, Stable Diffusion |

### Python Dependencies

```
# Core
python-telegram-bot>=20.0
langchain-aws
boto3

# Memory
chromadb
sqlite3 (standard library)

# HTTP
requests

# Other
pytz or zoneinfo (timezone handling)
```

---

## Project Structure

```
bot/
├── __init__.py
├── main.py                    # Entry point, initializes everything
├── config/
│   ├── __init__.py
│   ├── settings.py            # Environment variables, dataclass config
│   └── constants.py           # Static values (reactions, moods, timing)
├── core/
│   ├── __init__.py
│   ├── prompt.py              # System prompt building with memory
│   └── response.py            # LangChain response generation
├── handlers/
│   ├── __init__.py
│   ├── commands.py            # Command dispatcher (REACT, VOICE, etc.)
│   └── message.py             # Telegram message handlers
├── models/
│   ├── __init__.py
│   ├── chat_context.py        # Per-chat state management
│   ├── long_term_memory.py    # JSON-based persistent memory
│   └── message_store.py       # SQLite message persistence
├── services/
│   ├── __init__.py
│   ├── embeddings.py          # Nova embeddings generation
│   ├── vector_store.py        # ChromaDB semantic search
│   ├── summarization.py       # Haiku summarization + SKIP filter
│   ├── memory_manager.py      # Orchestrates all memory layers
│   └── proactive.py           # Proactive messaging service
├── tools/
│   ├── __init__.py            # TOOLS list export
│   ├── time_tools.py          # get_current_time
│   ├── web_tools.py           # web_search, fetch_url_content, fetch_webpage
│   ├── image_tools.py         # generate_image
│   ├── memory_tools.py        # manage_memory
│   └── user_tools.py          # get_chat_member_info
├── utils/
│   ├── __init__.py
│   ├── images.py              # send_generated_image
│   ├── reactions.py           # send_reaction, emoji mapping
│   ├── response.py            # extract_special_command, send_response_smartly
│   ├── telegram.py            # forward_message_by_id
│   └── voice.py               # text_to_speech (ElevenLabs)
└── prompts/
    ├── __init__.py
    ├── loader.py              # Loads system_prompt.md
    └── system_prompt.md       # Main system prompt (external file)

# Root level
lera_memory.json               # Long-term memory storage
lera_messages.db               # SQLite database
chroma_db/                     # ChromaDB vector database
run.sh                         # Development startup script
claude-bot.service             # Systemd service file
requirements.txt               # Dependencies
```

---

## Core Components

### 1. Settings (`config/settings.py`)

Use a dataclass with environment variable support:

```python
@dataclass
class Settings:
    # Telegram
    telegram_bot_token: str = field(default_factory=lambda: os.getenv("TELEGRAM_BOT_TOKEN", ""))

    # AWS Bedrock
    bedrock_model_id: str = field(default_factory=lambda: os.getenv(
        "BEDROCK_MODEL_ID", "anthropic.claude-opus-4-5-20251101"
    ))
    aws_region: str = field(default_factory=lambda: os.getenv("AWS_REGION", "us-west-2"))

    # Memory extraction (use cheaper model)
    memory_extraction_model_id: str = field(default_factory=lambda: os.getenv(
        "MEMORY_EXTRACTION_MODEL_ID", "anthropic.claude-haiku-4-5-20251001"
    ))

    # External services
    elevenlabs_api_key: str = ...
    serper_api_key: str = ...
    jina_api_key: str = ...
    seedream_api_key: str = ...

    # Bot behavior
    allowed_chat_id: int = ...  # Restrict to specific chat

    # Proactive messaging
    proactive_enabled: bool = True
    proactive_quiet_threshold_hours: float = 2.0
    proactive_max_per_day: int = 3
    proactive_active_hours_start: int = 10  # Local time
    proactive_active_hours_end: int = 23

    # Paths
    @property
    def long_term_memory_file(self) -> Path:
        return self.base_dir / "memory.json"
```

### 2. Constants (`config/constants.py`)

```python
# Message limits
MAX_CONTEXT_MESSAGES = 500    # Messages kept in memory
MAX_AGENT_MESSAGES = 50       # Messages sent to Claude

# Burst detection
BURST_TIME_WINDOW = 15        # Seconds to consider messages a "burst"
BURST_MIN_MESSAGES = 2        # Min messages for burst handling
BURST_WAIT_TIME = 6           # Wait before processing burst

# Response timing
RESPONSE_COOLDOWN = 10        # Seconds between responses
GLOBAL_RESPONSE_LOCK_TIMEOUT = 5

# Telegram supported reactions (subset)
SUPPORTED_REACTIONS = {'👍', '👎', '❤️', '🔥', '😁', '🤔', '😱', '🤬', ...}

# Mood hints (persona-specific, with weights)
MOOD_HINTS = [
    ("wants to argue", 3),
    ("feeling sarcastic", 2),
    ("bored, looking for attention", 2),
    ("nihilistic mood", 1),
    ...
]
```

### 3. Chat Context (`models/chat_context.py`)

Per-chat state manager:

```python
class ChatContext:
    def __init__(self, max_messages: int = MAX_CONTEXT_MESSAGES):
        # Message history
        self.messages: deque = deque(maxlen=max_messages)
        self.messages_by_id: Dict[int, Dict] = {}
        self.messages_since_last_bot_message = 0

        # Mood (changes randomly)
        self.current_mood: Optional[str] = None

        # Burst detection
        self.pending_burst: Dict[str, List[Dict]] = {}
        self.burst_timers: Dict[str, asyncio.Task] = {}
        self.processing_burst: Dict[str, bool] = {}

        # Image cache (for reply chain context)
        self.image_cache: Dict[int, Dict[str, Any]] = {}

        # LangChain integration
        self.langchain_messages: List[Any] = []
        self.chat_model: Optional[ChatBedrock] = None

        # Generated images queue
        self.pending_generated_images: List[bytes] = []

        # Response coordination
        self._response_lock = asyncio.Lock()
        self.last_response_time: Optional[datetime] = None

    def get_mood(self) -> str:
        """Get current mood, with random chance to change."""
        if random.random() < MOOD_CHANGE_PROBABILITY:
            moods, weights = zip(*MOOD_HINTS)
            self.current_mood = random.choices(moods, weights=weights, k=1)[0]
        return f"(internal state: {self.current_mood})"

    def add_message(self, username, text, is_bot=False, message_id=None,
                    reply_to_id=None, timestamp=None, ...):
        """Add message to context and update tracking."""
        ...

    def get_reply_chain(self, message_id, max_depth=10) -> List[Dict]:
        """Traverse reply chain for context."""
        ...

    def is_bot_in_reply_chain(self, reply_to_id, max_depth=5) -> bool:
        """Check if bot is in the reply chain (for must_respond)."""
        ...

    def cache_image(self, message_id, image_data, media_type):
        """Cache image for future reference."""
        ...

    async def try_acquire_response_lock(self, force=False) -> bool:
        """Prevent multiple simultaneous responses."""
        ...
```

### 4. Message Handlers (`handlers/message.py`)

Handle different message types:

```python
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    chat_id = message.chat_id

    # Restrict to allowed chat
    if chat_id != settings.allowed_chat_id:
        return

    # Get/create chat context
    chat_context = get_chat_context(chat_id)

    # Capture reply chain from Telegram
    if message.reply_to_message:
        capture_reply_chain(chat_context, message, bot_info.id, chat_id)

    # Route by message type
    if message.sticker:
        await _handle_sticker(...)
    elif message.photo:
        await _handle_photo(...)
    elif message.text:
        await _handle_text(...)
```

**Key concept: Burst Detection**

When users send multiple messages rapidly (like splitting a thought across messages), wait and combine them:

```python
async def _handle_text(message, chat_context, ...):
    # Check if this is part of a burst
    if chat_context.is_message_burst(username, current_time):
        chat_context.add_to_burst(username, message_data, current_time)

        # Reset timer - wait for more messages
        if username in chat_context.burst_timers:
            chat_context.burst_timers[username].cancel()

        async def burst_timer():
            await asyncio.sleep(BURST_WAIT_TIME)
            await process_burst_messages(...)

        chat_context.burst_timers[username] = asyncio.create_task(burst_timer())
        return

    # Start potential burst
    chat_context.add_to_burst(username, message_data, current_time)
    # ... set timer for burst or single message processing
```

### 5. Response Generation (`core/response.py`)

Generate responses using LangChain:

```python
async def generate_response(
    context: ChatContext,
    bot_name: str,
    reply_to_id: Optional[int] = None,
    must_respond: bool = False,
    chat_id: Optional[int] = None
) -> Optional[str]:

    latest_msg = list(context.messages)[-1]
    mood = context.get_mood()

    # Build prompt with context
    prompt_parts = []

    # Add reply chain context (messages being replied to)
    if reply_to_id:
        reply_chain = context.get_reply_chain(reply_to_id)
        # Format and add to prompt
        ...

    # Add recent messages if LangChain history is sparse
    if len(context.langchain_messages) < 10:
        recent_messages = list(context.messages)[-15:-1]
        # Format and add to prompt
        ...

    # Add current message with clear attribution
    prompt_parts.append(f">>> INCOMING MESSAGE from {current_author} <<<")
    prompt_parts.append(format_message(latest_msg))

    # Add mood and instruction
    if must_respond:
        instruction = f"{mood}\n{current_author} addressed you. You MUST respond."
    else:
        instruction = f"{mood}\nSKIP is default. Only respond if truly relevant."

    # Build enhanced context from memory manager
    memory_manager = get_memory_manager(chat_id)
    enhanced_context = memory_manager.build_enhanced_context(...)

    # Create LangChain messages
    chat_model = context.get_or_create_chat_model()
    messages = [
        SystemMessage(content=get_system_prompt_with_memory(enhanced_context)),
        # ... previous conversation messages
        HumanMessage(content=prompt)
    ]

    # Call Claude
    result = await call_langchain_chat(chat_model, messages, context)

    if result and result.upper() != "SKIP":
        # Add to message history
        context.langchain_messages.append(AIMessage(content=result))
        return result
    return None
```

**Tool Execution Loop:**

```python
async def call_langchain_chat(chat_model, messages, context):
    response = await asyncio.to_thread(lambda: chat_model.invoke(messages))

    # Handle tool calls (up to 3 rounds)
    max_rounds = 3
    while hasattr(response, 'tool_calls') and response.tool_calls and rounds < max_rounds:
        tool_messages = [response]

        for tool_call in response.tool_calls:
            tool_name = tool_call['name']
            tool_args = tool_call['args']

            # Execute tool
            tool_result = tool.invoke(tool_args)

            # Special handling for image generation
            if tool_name == 'generate_image' and "IMAGE_GENERATED:" in tool_result:
                image_data = base64.b64decode(tool_result[16:])
                context.pending_generated_images.append(image_data)
                tool_result = "Image generated. Use IMAGE: format to send."

            tool_messages.append(ToolMessage(content=tool_result, ...))

        # Call model again with results
        messages.extend(tool_messages)
        response = await asyncio.to_thread(lambda: chat_model.invoke(messages))

    # Extract text response
    return extract_text_from_response(response)
```

### 6. Command Dispatcher (`handlers/commands.py`)

Parse and execute special commands:

```python
async def dispatch_command(response, message, chat_context, ...):
    cmd_type, cmd_content = extract_special_command(response)

    if cmd_type == "REACT":
        await send_reaction(context, chat_id, message_id, cmd_content)

    elif cmd_type == "VOICE":
        voice_msg_id = await send_voice_message(context, chat_id, cmd_content)

    elif cmd_type == "IMAGE":
        if chat_context.pending_generated_images:
            image_data = chat_context.pending_generated_images.pop(0)
            await send_generated_image(context, chat_id, image_data, cmd_content)

    elif cmd_type == "FORWARD":
        forward_id = int(cmd_content)
        await forward_message_by_id(context, chat_id, forward_id)

    else:
        # Regular text response
        await send_response_smartly(message, chat_context, bot_name, response, ...)
```

---

## Memory System

The bot uses a **5-layer hierarchical memory system**:

### Layer 1: Immediate Memory (RAM)

- **Storage**: `collections.deque` in `ChatContext`
- **Capacity**: Last 500 messages
- **Content**: Full verbatim message text
- **Purpose**: Recent conversation context

### Layer 2: SQLite Message Store

- **Storage**: `lera_messages.db`
- **Tables**:
  - `messages`: All messages with metadata
  - `summaries`: Hourly/daily AI-generated summaries
  - `user_profiles`: Extracted communication styles

```sql
CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    chat_id INTEGER NOT NULL,
    message_id INTEGER NOT NULL,
    user_id INTEGER,
    username TEXT NOT NULL,
    full_name TEXT,
    text TEXT NOT NULL,
    is_bot BOOLEAN,
    reply_to_id INTEGER,
    timestamp DATETIME NOT NULL,
    UNIQUE(chat_id, message_id)
);

CREATE TABLE summaries (
    id INTEGER PRIMARY KEY,
    chat_id INTEGER NOT NULL,
    summary_type TEXT,      -- 'hourly' or 'daily'
    period_start DATETIME,
    period_end DATETIME,
    summary_text TEXT,
    participants TEXT,      -- JSON array
    topics TEXT,            -- JSON array
    message_count INTEGER
);

CREATE TABLE user_profiles (
    id INTEGER PRIMARY KEY,
    chat_id INTEGER NOT NULL,
    username TEXT NOT NULL,
    communication_style TEXT,
    topics_of_interest TEXT,  -- JSON array
    relationship_with_bot TEXT,
    last_message_at DATETIME,
    message_count INTEGER,
    UNIQUE(chat_id, username)
);
```

### Layer 3: Vector Store (ChromaDB)

- **Storage**: `chroma_db/` directory
- **Embedding Model**: Amazon Nova (`amazon.nova-2-multimodal-embeddings-v1:0`)
- **Dimension**: 1024
- **Purpose**: Semantic search for relevant past messages

```python
class VectorStore:
    def add_message(self, chat_id, message_id, username, text, timestamp, ...):
        # Format for embedding
        formatted = f"[{timestamp}] {username}: {text}"

        # Generate embedding
        embedding = self.embedding_service.generate_embedding(formatted)

        # Store in ChromaDB
        collection.upsert(
            ids=[f"msg_{message_id}"],
            embeddings=[embedding],
            documents=[text],
            metadatas=[{...}]
        )

    def search_similar(self, chat_id, query, n_results=10):
        query_embedding = self.embedding_service.generate_query_embedding(query)
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        return formatted_results
```

### Layer 4: Summarization (Haiku)

- **Trigger**: Every 100 messages
- **Model**: Claude Haiku (cheaper)
- **Output**: JSON summary with participants, topics, mood

```python
SUMMARY_PROMPT = """Analyze this chat history and create a summary.
<messages>{messages}</messages>
Return JSON: {"summary": "...", "participants": [...], "topics": [...], "mood": "..."}"""

class SummarizationService:
    async def summarize_messages_async(self, messages, period_start, period_end):
        formatted = "\n".join([f"[{m['timestamp']}] {m['username']}: {m['text']}" for m in messages])
        response = self._invoke_haiku(SUMMARY_PROMPT.format(messages=formatted))
        return parse_json(response)
```

### Layer 5: Long-Term Memory (JSON)

- **Storage**: `lera_memory.json`
- **Categories**:
  - `personalities`: Traits observed about users
  - `hot_topics`: Topics that generate strong reactions
  - `hot_takes`: Bot's strong opinions
  - `relationships`: Dynamics with each user
  - `recurring_themes`: Frequent discussion topics
  - `memorable_moments`: Notable exchanges

```python
class LongTermMemory:
    def __init__(self):
        self.memory = {
            "personalities": {},      # username -> [traits]
            "hot_topics": [],
            "hot_takes": [],
            "relationships": {},      # username -> dynamic
            "recurring_themes": [],
            "memorable_moments": [],
        }

    def get_memory_context(self) -> str:
        """Format for system prompt."""
        parts = []
        if self.memory["personalities"]:
            parts.append("=== PEOPLE ===")
            for user, traits in self.memory["personalities"].items():
                parts.append(f"@{user}: {', '.join(traits[-5:])}")
        # ... format other categories
        return "\n".join(parts)
```

### Memory Manager Orchestration

```python
class MemoryManager:
    def build_enhanced_context(self, current_message, current_username, active_users, exclude_ids):
        context = {
            "similar_messages": [],
            "summaries": [],
            "user_profiles": {},
        }

        # Semantic search for similar past messages
        context["similar_messages"] = self.get_similar_messages(current_message, exclude_ids)

        # Recent summaries relevant to active users
        context["summaries"] = self.get_relevant_summaries(active_users)

        # Profiles of active users
        for username in active_users[:5]:
            profile = self.message_store.get_user_profile(chat_id, username)
            if profile:
                context["user_profiles"][username] = profile

        return context
```

---

## Tools System

Define tools using LangChain's `@tool` decorator:

### Web Search

```python
@tool
def web_search(query: str) -> str:
    """Search the web using Google (via Serper API)."""
    response = requests.post(
        "https://google.serper.dev/search",
        headers={"X-API-KEY": settings.serper_api_key},
        json={"q": query, "num": 5}
    )
    data = response.json()

    results = []
    for item in data.get("organic", []):
        results.append(f"**{item['title']}**\n{item['snippet']}\n{item['link']}")

    return "\n\n".join(results)
```

### Image Generation

```python
@tool
def generate_image(prompt: str) -> str:
    """Generate an image using Seedream 4.5."""
    response = requests.post(
        settings.seedream_api_url,
        headers={"Authorization": f"Bearer {settings.seedream_api_key}"},
        json={"model": settings.seedream_model_id, "prompt": prompt, "size": "2K"}
    )

    image_url = response.json()["data"][0]["url"]
    image_data = requests.get(image_url).content

    # Return base64 for the response handler to process
    return f"IMAGE_GENERATED:{base64.b64encode(image_data).decode()}"
```

### Memory Management

```python
@tool
def manage_memory(action: str, category: str, content: str, username: str = "") -> str:
    """Manage long-term memory. Actions: add, remove, list.
    Categories: personality, hot_topic, hot_take, relationship, theme, moment."""

    if action == "add":
        if category == "personality":
            memory["personalities"][username].append(content)
        elif category == "hot_topic":
            memory["hot_topics"].append(content)
        # ... etc
        memory.save()
        return f"Added: {content}"

    elif action == "list":
        return memory.get_memory_context()
```

### Register Tools

```python
# bot/tools/__init__.py
TOOLS = [
    get_current_time,
    fetch_url_content,
    fetch_webpage,
    web_search,
    get_chat_member_info,
    manage_memory,
    generate_image,
]
```

---

## Message Flow

```
1. Message arrives via Telegram
   │
2. Check if allowed chat
   │
3. Capture reply chain (historical messages)
   │
4. Route by type (text/photo/sticker)
   │
5. Add to chat context + memory store
   │
6. Burst detection check
   │ Yes: Add to burst buffer, set timer
   │ No:  Continue to step 7
   │
7. Acquire response lock (prevent duplicates)
   │
8. Check if directly addressed
   │ Yes: must_respond = True
   │ No:  Run SKIP filter (Haiku)
   │       │
   │       ├─ SKIP: Exit
   │       └─ RESPOND: Continue
   │
9. Build enhanced context from memory layers
   │
10. Generate response (Opus with tools)
    │
11. Parse response for special commands
    │
12. Execute command (text/react/voice/image/forward)
    │
13. Add bot's response to context
```

---

## Response Decision Logic

### Must Respond (always responds)

1. **Direct reply**: Message is a reply to bot's message
2. **@mention**: Message contains `@bot_username`
3. **Name mention**: Message contains bot's name (configurable patterns)
4. **Reply chain**: Bot is somewhere in the reply chain
5. **Recent conversation**: Bot spoke in the last 1-2 messages

### SKIP Filter (Haiku pre-filter)

For non-directly-addressed messages, a cheaper model decides:

```python
SKIP_FILTER_PROMPT = """You're a filter for a chat bot. Decide: respond or skip.

<recent_messages>
{messages}
</recent_messages>

<current_message>
{current_message}
</current_message>

RESPOND if:
- Topic is interesting, bot can add something
- Opportunity for joke or banter
- Someone said something controversial
- Bot has a relevant opinion
- Continuation of conversation bot was in
- Can revive a dying chat with a provocative take

SKIP only if:
- Intimate conversation between two people
- Message like "ok", "thanks" with no hook
- Topic is completely dead

When in doubt, RESPOND.

Answer ONE word: RESPOND or SKIP"""
```

---

## Proactive Messaging

The bot can initiate conversations when chat goes quiet:

```python
class ProactiveService:
    def _should_send_proactive(self) -> bool:
        # Check if enabled
        if not settings.proactive_enabled:
            return False

        # Check daily limit
        if self.daily_count >= settings.proactive_max_per_day:
            return False

        # Check active hours (e.g., 10:00-23:00 local time)
        if not self._is_within_active_hours():
            return False

        # Check quiet duration (e.g., 2+ hours of silence)
        if self._get_quiet_duration() < settings.proactive_quiet_threshold_hours:
            return False

        # Check cooldown after ignored message
        if self.last_proactive_ignored:
            # Wait longer before trying again
            ...

        return True

    async def _generate_proactive_message(self, chat_context):
        # Choose starter type
        starter_type = random.choice([
            "hot_topic",      # Bring up controversial topic from memory
            "personal_ping",  # Ask someone about something they mentioned
            "random_thought", # Share provocative thought
            "callback",       # Reference unfinished argument
            "observation",    # Comment on silence
        ])

        prompt = PROACTIVE_PROMPT.format(
            context=context_info,
            memory=memory_info,
            last_messages=last_messages,
            starter_type=starter_type
        )

        return await invoke_claude(prompt, temperature=0.9)
```

---

## Configuration

### Environment Variables

```bash
# Required
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
AWS_REGION=us-west-2

# AWS Bedrock (uses instance role or ~/.aws/credentials)
BEDROCK_MODEL_ID=global.anthropic.claude-opus-4-5-20251101-v1:0
MEMORY_EXTRACTION_MODEL_ID=global.anthropic.claude-haiku-4-5-20251001-v1:0

# External services
ELEVENLABS_API_KEY=your_key
SERPER_API_KEY=your_key
JINA_API_KEY=your_key
SEEDREAM_API_KEY=your_key

# Bot behavior
ALLOWED_CHAT_ID=-1001234567890

# Proactive messaging
PROACTIVE_ENABLED=true
PROACTIVE_QUIET_THRESHOLD_HOURS=2.0
PROACTIVE_MAX_PER_DAY=3
PROACTIVE_ACTIVE_HOURS_START=10
PROACTIVE_ACTIVE_HOURS_END=23

# Optional debugging
LANGCHAIN_API_KEY=your_langsmith_key  # For tracing
```

### Systemd Service

```ini
# /etc/systemd/system/chat-bot.service
[Unit]
Description=Telegram Chat Bot
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/bot
ExecStart=/home/ubuntu/bot/venv/bin/python -m bot.main
Restart=always
RestartSec=10
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```

---

## System Prompt Design

The system prompt is the bot's personality definition. Key principles:

### Structure

```markdown
<role>
You are [Name], a participant in a private group chat. You're NOT an assistant - you're a friend.
</role>

<identity>
Your core traits:
- Age, background, personality
- Communication style
- Interests, opinions
- How you relate to others
</identity>

<persona>
Detailed personality characteristics:
- Humor style (dry, sarcastic, etc.)
- How you handle different situations
- Your quirks and habits
</persona>

<critical_constraints>
Things you NEVER do:
- Break character
- Be overly helpful/assistant-like
- Share certain information
- Use certain phrases
</critical_constraints>

<style>
Communication style guide:
- Message length
- Emoji usage
- Capitalization
- Typical phrases
</style>

<autonomy>
Your independence:
- When to respond vs. stay silent
- How to handle being ignored
- When to push back vs. agree
</autonomy>

<tools_usage>
How to use your tools:
- When to search the web
- When to generate images
- When/what to remember
</tools_usage>

<output_formats>
Special response formats:
- SKIP - choose not to respond
- REACT:emoji - add reaction
- VOICE:text - send voice message
- IMAGE:caption - send generated image
</output_formats>

<memory_categories>
What to remember:
- personality: traits about people
- hot_topic: controversial topics
- hot_take: your strong opinions
- relationship: how you relate to someone
- theme: recurring topics
- moment: memorable exchanges
</memory_categories>

{memory_context}
```

### Key Guidelines for Writing System Prompts

1. **Be specific about personality**: Don't just say "friendly" - describe HOW they're friendly
2. **Define the negative space**: What they DON'T do is as important as what they do
3. **Give examples**: Show, don't tell. Include example responses
4. **Context awareness**: Guide when to speak vs. listen
5. **Memory integration**: Explain how to use remembered information
6. **Tool purpose**: Explain when each tool is appropriate
7. **Mood system**: If using moods, explain how they affect behavior
8. **Language**: If non-English, specify the language and any code-switching rules

---

## External Services Integration

### AWS Bedrock (Claude)

```python
from langchain_aws import ChatBedrock

chat_model = ChatBedrock(
    model_id="anthropic.claude-opus-4-5-20251101",
    region_name="us-west-2",
    model_kwargs={
        "temperature": 1.0,
        "max_tokens": 4096,
        "anthropic_beta": ["interleaved-thinking-2025-05-14"],
        "thinking": {
            "type": "enabled",
            "budget_tokens": 2000
        }
    }
)

# Bind tools
chat_model = chat_model.bind_tools(TOOLS)
```

### ElevenLabs (Voice)

```python
def text_to_speech(text: str) -> Optional[bytes]:
    response = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}",
        headers={"xi-api-key": API_KEY},
        json={
            "text": text,
            "model_id": "eleven_v3",
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
        }
    )
    return response.content if response.ok else None
```

### Jina (Webpage Reading)

```python
def fetch_webpage(url: str) -> str:
    response = requests.get(
        f"https://r.jina.ai/{url}",
        headers={"Authorization": f"Bearer {JINA_API_KEY}"}
    )
    return response.text[:4000]  # Truncate
```

### Seedream (Image Generation)

```python
def generate_image(prompt: str) -> bytes:
    response = requests.post(
        "https://ark.ap-southeast.bytepluses.com/api/v3/images/generations",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "model": "seedream-4-5-251128",
            "prompt": prompt,
            "size": "2K",
            "response_format": "url"
        }
    )
    image_url = response.json()["data"][0]["url"]
    return requests.get(image_url).content
```

---

## Running the Bot

### Development

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export TELEGRAM_BOT_TOKEN=...
export AWS_REGION=us-west-2
# ... etc

# Run
python -m bot.main
```

### Production (Systemd)

```bash
# Install service
sudo cp claude-bot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable claude-bot
sudo systemctl start claude-bot

# Check status
sudo systemctl status claude-bot

# View logs
journalctl -u claude-bot -f
```

---

## Testing

### Test Structure

```
tests/
├── conftest.py              # Fixtures, mocks
├── test_chat_context.py     # ChatContext tests
├── test_long_term_memory.py # Memory persistence tests
├── test_tools.py            # Tool function tests
├── test_commands.py         # Command dispatcher tests
├── test_helpers.py          # Utility function tests
├── test_memory_system.py    # Full memory system tests
└── test_integration.py      # End-to-end tests
```

### Key Test Patterns

```python
# Mock Telegram API
@pytest.fixture
def mock_telegram_context():
    context = MagicMock()
    context.bot.send_message = AsyncMock()
    context.bot.set_message_reaction = AsyncMock()
    return context

# Mock Bedrock
@pytest.fixture
def mock_bedrock_response():
    with patch('boto3.client') as mock:
        mock.return_value.invoke_model.return_value = {
            "body": io.BytesIO(json.dumps({
                "content": [{"text": "Test response"}]
            }).encode())
        }
        yield mock

# Test burst detection
async def test_burst_detection(chat_context):
    now = datetime.now()
    chat_context.add_to_burst("user1", {"text": "msg1"}, now)
    chat_context.add_to_burst("user1", {"text": "msg2"}, now + timedelta(seconds=5))

    assert len(chat_context.get_burst_messages("user1")) == 2
    assert chat_context.is_message_burst("user1", now + timedelta(seconds=10))
```

### Run Tests

```bash
# All tests
pytest tests/ -v

# With coverage
pytest tests/ --cov=bot --cov-report=term-missing

# Specific test
pytest tests/test_tools.py::TestWebSearch -v
```

---

## Summary

To recreate this bot:

1. **Set up AWS Bedrock** with Claude Opus/Haiku access
2. **Create Telegram bot** via BotFather
3. **Implement the modular structure** as outlined
4. **Build the memory system** (SQLite + ChromaDB + JSON)
5. **Define tools** for web search, image generation, etc.
6. **Write your system prompt** defining the personality
7. **Implement message handlers** with burst detection
8. **Add the SKIP filter** for cost-effective response decisions
9. **Configure proactive messaging** (optional)
10. **Deploy as a systemd service**

The key differentiator from typical bots is treating it as a **chat participant** with opinions, memory, and the ability to choose when to speak. The multi-layered memory system and SKIP filter are essential for natural, cost-effective operation.
