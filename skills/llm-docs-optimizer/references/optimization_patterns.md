# Documentation Optimization Patterns for C7Score

## Analysis Workflow

### Step 1: Audit Current Documentation

Review the existing documentation and categorize snippets:

1. **Question-answering snippets**: Count how many snippets directly answer developer questions
2. **API reference snippets**: Count pure API documentation without usage examples
3. **Installation/import-only snippets**: Count snippets that are just setup with no usage
4. **Metadata snippets**: Count licensing, directory structures, citations
5. **Duplicate snippets**: Identify repeated or very similar content
6. **Formatting issues**: Note inconsistent formats, wrong language tags, etc.

### Step 2: Generate Common Questions

Use an LLM to generate 15-20 common questions a developer would ask about the library:

**Example questions:**
- How do I install and set up [library]?
- How do I [main feature 1]?
- How do I [main feature 2]?
- How do I handle errors?
- How do I configure [common setting]?
- What are the authentication options?
- How do I integrate with [common use case]?
- What are the rate limits and how do I handle them?
- How do I use [advanced feature]?
- How do I test code using [library]?

### Step 3: Map Questions to Snippets

Create a mapping:
- Which questions are well-answered by existing snippets?
- Which questions have weak or missing answers?
- Which snippets don't answer any important questions?

### Step 4: Optimize High-Impact Areas

Focus optimization efforts based on c7score weights:

**Priority 1 (80% of score): Question-Snippet Matching**
- Add missing snippets for unanswered questions
- Enhance snippets that partially answer questions
- Ensure each snippet addresses at least one common question

**Priority 2 (5% each): Other Metrics**
- Remove duplicates
- Fix formatting inconsistencies
- Remove metadata snippets
- Combine import-only snippets with usage

## Snippet Transformation Patterns

### Pattern 1: API Reference → Usage Example

**Before:**
```
Client.authenticate(api_key: str) -> bool
Authenticates the client with the provided API key.
Parameters:
  - api_key (str): Your API key
Returns:
  - bool: True if authentication succeeded
```

**After:**
```
Authenticating Your Client
----------------------------------------
Authenticate your client using your API key from the dashboard.

```python
from library import Client

# Initialize with your API key
client = Client(api_key="your_api_key_here")

# Authenticate
if client.authenticate():
    print("Successfully authenticated!")
else:
    print("Authentication failed")
```
```

### Pattern 2: Import-Only → Complete Setup

**Before:**
```python
from library import Client, Query, Response
```

**After:**
```
Quick Start: Making Your First Request
----------------------------------------
Install the library, import the client, and make your first API call.

```python
# Install: pip install library-name
from library import Client

# Initialize and authenticate
client = Client(api_key="your_api_key")

# Make your first request
response = client.query("SELECT * FROM data LIMIT 10")
for row in response:
    print(row)
```
```

### Pattern 3: Multiple Small → One Comprehensive

**Before (3 separate snippets):**
```python
client = Client()
```
```python
client.connect()
```
```python
client.query("SELECT * FROM table")
```

**After (1 comprehensive snippet):**
```
Complete Workflow: Connect and Query
----------------------------------------
Full example showing initialization, connection, and querying.

```python
from library import Client

# Initialize the client
client = Client(
    api_key="your_api_key",
    region="us-west-2"
)

# Establish connection
client.connect()

# Execute query
result = client.query("SELECT * FROM users WHERE active = true")

# Process results
for row in result:
    print(f"User: {row['name']}, Email: {row['email']}")

# Close connection
client.close()
```
```

### Pattern 4: Remove Metadata Snippets

**Remove these entirely:**
```
Project Structure
----------------------------------------
myproject/
├── src/
│   ├── main.py
│   └── utils.py
├── tests/
└── README.md
```

```
License
----------------------------------------
MIT License
Copyright (c) 2024...
```

```
Citation
----------------------------------------
@article{library2024,
  title={The Library Paper},
  ...
}
```

## README Optimization

### Structure Your README for High Scores

**1. Quick Start Section (High Priority)**
```markdown
## Quick Start

```python
# Install
pip install your-library

# Import and use
from your_library import Client

client = Client(api_key="key")
result = client.do_something()
print(result)
```
```

**2. Common Use Cases (High Priority)**

For each major feature, provide:
- Clear section title answering "How do I...?"
- Brief description
- Complete, working code example
- Expected output or result

**3. API Reference (Lower Priority)**

Keep it, but ensure each API method has at least one usage example.

**4. Configuration Examples (Medium Priority)**

Show common configuration scenarios with full context.

**5. Error Handling (Medium Priority)**

Demonstrate proper error handling in realistic scenarios.

### What to Minimize or Remove

- **Installation only**: Always combine with first usage
- **Long lists**: Convert to example-driven content
- **Project governance**: Move to separate CONTRIBUTING.md
- **Licensing**: Link to LICENSE file, don't duplicate
- **Directory trees**: Remove unless essential for setup
- **Academic citations**: Remove from main docs

## Testing Documentation Quality

### Manual Quality Checks

Before finalizing, verify each snippet:

1. ✅ **Can run standalone**: Copy-paste the code and it works (with minimal setup)
2. ✅ **Answers a question**: Clearly addresses a "how do I..." query
3. ✅ **Unique information**: Doesn't duplicate other snippets
4. ✅ **Proper format**: Has title, description, and code with correct language tag
5. ✅ **Practical focus**: Shows real-world usage, not just theory
6. ✅ **Complete imports**: Includes all necessary imports
7. ✅ **No metadata**: No licensing, citations, or directory trees
8. ✅ **Correct syntax**: Code is valid and would actually run

### Question Coverage Matrix

Create a checklist:
- [ ] Installation and setup
- [ ] Basic initialization
- [ ] Authentication methods
- [ ] Primary use case 1
- [ ] Primary use case 2
- [ ] Configuration options
- [ ] Error handling
- [ ] Advanced features
- [ ] Integration examples
- [ ] Testing approaches

Each checkbox should map to at least one high-quality snippet.

## Iteration and Refinement

After creating optimized documentation:

1. Run c7score to get baseline metrics
2. Identify lowest-scoring metric
3. Apply targeted improvements for that metric
4. Re-run c7score
5. Repeat until reaching target score (typically 85+)

### Common Score Ranges

- **90-100**: Excellent, comprehensive, question-focused documentation
- **80-89**: Good documentation with some gaps or formatting issues
- **70-79**: Adequate but needs more complete examples or has duplicates
- **60-69**: Significant gaps in question coverage or many formatting issues
- **Below 60**: Major restructuring needed

## Example: Full Snippet Transformation

### Original (Low Score)

```markdown
## Installation

```bash
npm install my-library
```

## Usage

Import the library:

```javascript
const MyLibrary = require('my-library');
```

## API

### connect(options)
Connects to the service.

### query(sql)
Executes a query.
```

### Optimized (High Score)

```markdown
## Getting Started: Installation and First Query

```javascript
// Install the library
// npm install my-library

const MyLibrary = require('my-library');

// Connect to your database
const client = new MyLibrary({
  host: 'your-host.example.com',
  apiKey: 'your-api-key',
  database: 'production'
});

await client.connect();

// Run your first query
const results = await client.query('SELECT * FROM users LIMIT 5');
console.log(results);

// Always close the connection
await client.close();
```

## Common Use Cases

### Authenticating with OAuth

```javascript
const MyLibrary = require('my-library');

// OAuth authentication flow
const client = new MyLibrary({
  authMethod: 'oauth',
  clientId: 'your-client-id',
  clientSecret: 'your-client-secret'
});

// Get auth URL for user
const authUrl = client.getAuthUrl('http://localhost:3000/callback');
console.log(`Visit: ${authUrl}`);

// After user authorizes, exchange code for token
const tokens = await client.exchangeCode(authCode);
await client.connect();
```

### Handling Errors and Retries

```javascript
const MyLibrary = require('my-library');

const client = new MyLibrary({
  host: 'your-host.example.com',
  apiKey: 'your-api-key',
  // Configure automatic retries
  retries: 3,
  retryDelay: 1000
});

try {
  await client.connect();
  const results = await client.query('SELECT * FROM users');
  console.log(results);
} catch (error) {
  if (error.code === 'TIMEOUT') {
    console.error('Query timed out, try a smaller result set');
  } else if (error.code === 'AUTH_ERROR') {
    console.error('Authentication failed, check your API key');
  } else {
    console.error('Unexpected error:', error.message);
  }
} finally {
  await client.close();
}
```

### Advanced: Batch Operations

```javascript
const MyLibrary = require('my-library');

const client = new MyLibrary({
  host: 'your-host.example.com',
  apiKey: 'your-api-key'
});

await client.connect();

// Batch insert for better performance
const users = [
  { name: 'Alice', email: 'alice@example.com' },
  { name: 'Bob', email: 'bob@example.com' },
  { name: 'Charlie', email: 'charlie@example.com' }
];

const result = await client.batchInsert('users', users);
console.log(`Inserted ${result.rowCount} users`);

await client.close();
```
```

**Score Impact:**
- Question coverage: +40 points (answers 4 major questions)
- Removes import-only: +5 points
- Consistent formatting: +5 points
- Working examples: +20 points
- No duplicates: +10 points
- **Total improvement: ~80 point increase**
