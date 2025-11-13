# Example: Before and After C7Score Optimization

This example demonstrates the transformation of a typical README into an optimized version that scores higher on the c7score benchmark.

---

## BEFORE Optimization (Low c7score)

```markdown
# DataFlow

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Version](https://img.shields.io/badge/version-2.3.1-blue)
Last updated: March 15, 2024

DataFlow is a Python library for processing data streams.

## Features

- Stream processing
- Data transformation
- Multiple output formats
- Error handling

## Installation

```bash
pip install dataflow
```

## Usage

```python
from dataflow import Stream
s = Stream()
```

## API

See the API documentation for details.

## License

MIT
```

### Issues with the BEFORE version:
- ❌ Metadata badges and timestamps (reduce c7score)
- ❌ Vague descriptions without concrete examples
- ❌ Code snippets lack context and imports
- ❌ No question-driven structure
- ❌ Missing error handling examples
- ❌ No progressive complexity
- ❌ Features listed without demonstrations
- ❌ Incomplete quickstart example

---

## AFTER Optimization (High c7score)

```markdown
# DataFlow

A Python library for processing data streams with real-time transformations and multiple output formats.

## Quick Start

### How do I install DataFlow?

```bash
pip install dataflow
```

For development installation:
```bash
git clone https://github.com/example/dataflow.git
cd dataflow
pip install -e ".[dev]"
```

### How do I process my first data stream?

```python
from dataflow import Stream, Processor

# Create a stream and add data
stream = Stream()
stream.add_data([1, 2, 3, 4, 5])

# Process the stream
processor = Processor()
result = processor.transform(stream, lambda x: x * 2)

print(result.to_list())  # Output: [2, 4, 6, 8, 10]
```

### How do I handle different data sources?

```python
from dataflow import Stream, FileSource, APISource

# Load from a file
file_stream = Stream.from_source(
    FileSource('data.csv', format='csv')
)

# Load from an API
api_stream = Stream.from_source(
    APISource('https://api.example.com/data', auth_token='your_token')
)

# Process both streams
for item in file_stream:
    print(f"Processing: {item}")
```

## Common Use Cases

### How do I transform data in a stream?

```python
from dataflow import Stream, Transformer

stream = Stream.from_list([
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25}
])

# Apply transformations
transformed = stream.map(lambda x: {
    **x,
    'age_group': 'adult' if x['age'] >= 18 else 'minor'
})

for person in transformed:
    print(person)
# Output: {'name': 'Alice', 'age': 30, 'age_group': 'adult'}
#         {'name': 'Bob', 'age': 25, 'age_group': 'adult'}
```

### How do I filter data in a stream?

```python
from dataflow import Stream

stream = Stream.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Filter even numbers
evens = stream.filter(lambda x: x % 2 == 0)

print(evens.to_list())  # Output: [2, 4, 6, 8, 10]
```

### How do I export stream data to different formats?

```python
from dataflow import Stream

stream = Stream.from_list([
    {'id': 1, 'value': 100},
    {'id': 2, 'value': 200}
])

# Export to JSON
stream.to_json('output.json', indent=2)

# Export to CSV
stream.to_csv('output.csv', headers=True)

# Export to parquet (requires pyarrow)
stream.to_parquet('output.parquet', compression='snappy')
```

## Error Handling

### How do I handle errors during stream processing?

```python
from dataflow import Stream, ProcessingError

stream = Stream.from_list([1, 2, 'invalid', 4, 5])

try:
    result = stream.map(lambda x: x * 2)
except ProcessingError as e:
    print(f"Error processing stream: {e}")
    print(f"Failed at item: {e.item}")
    print(f"Position: {e.position}")
```

### How do I skip invalid items in a stream?

```python
from dataflow import Stream

stream = Stream.from_list([1, 2, 'invalid', 4, 5])

# Skip invalid items with error handling
def safe_transform(x):
    try:
        return x * 2
    except TypeError:
        return None

result = stream.map(safe_transform).filter(lambda x: x is not None)
print(result.to_list())  # Output: [2, 4, 8, 10]
```

## Advanced Usage

### How do I chain multiple transformations?

```python
from dataflow import Stream

result = (
    Stream.from_list([1, 2, 3, 4, 5])
    .filter(lambda x: x > 2)           # Keep values > 2
    .map(lambda x: x * 2)               # Double them
    .map(lambda x: {'value': x})        # Convert to dict
    .to_list()
)

print(result)
# Output: [{'value': 6}, {'value': 8}, {'value': 10}]
```

### How do I process streams in parallel?

```python
from dataflow import Stream, ParallelProcessor

stream = Stream.from_list(range(1000))

# Process with 4 worker threads
processor = ParallelProcessor(workers=4)
result = processor.map(stream, lambda x: expensive_operation(x))

for item in result:
    print(item)
```

### How do I aggregate data from a stream?

```python
from dataflow import Stream

stream = Stream.from_list([1, 2, 3, 4, 5])

# Calculate sum
total = stream.reduce(lambda acc, x: acc + x, initial=0)
print(f"Sum: {total}")  # Output: Sum: 15

# Calculate average
count = stream.count()
average = total / count
print(f"Average: {average}")  # Output: Average: 3.0
```

## Performance

### How do I optimize stream processing performance?

```python
from dataflow import Stream, BufferedStream

# Use buffering for better performance
stream = BufferedStream.from_source(
    source=large_data_source,
    buffer_size=1000  # Process in chunks of 1000
)

# Enable lazy evaluation
result = stream.lazy().map(transform_fn).filter(filter_fn)

# Only evaluate when needed
final_data = result.to_list()
```

## Requirements

- Python 3.7 or higher
- Optional dependencies:
  - `pyarrow` for Parquet support
  - `pandas` for DataFrame integration

## Installation Options

Standard installation:
```bash
pip install dataflow
```

With optional dependencies:
```bash
pip install dataflow[parquet]  # For Parquet support
pip install dataflow[pandas]   # For pandas integration
pip install dataflow[all]      # All optional features
```

## License

MIT License - see LICENSE file for details
```

### Improvements in the AFTER version:
- ✅ Removed metadata badges and timestamps
- ✅ Question-driven headers throughout
- ✅ Complete code examples with imports and context
- ✅ Progressive complexity (basic → advanced)
- ✅ Error handling examples
- ✅ Multiple use cases demonstrated
- ✅ Concrete outputs shown in comments
- ✅ Installation options clearly explained
- ✅ Common questions answered with working code

---

## C7Score Impact Estimate

### BEFORE Version Metrics:
- Question-Snippet Matching: ~40/100 (incomplete examples, poor alignment)
- LLM Evaluation: ~50/100 (vague descriptions)
- Formatting: ~70/100 (basic markdown, code blocks present)
- Metadata Removal: ~30/100 (badges and timestamps present)
- Initialization Examples: ~50/100 (incomplete quickstart)

**Estimated BEFORE c7score: ~45/100**

### AFTER Version Metrics:
- Question-Snippet Matching: ~90/100 (excellent Q&A alignment)
- LLM Evaluation: ~95/100 (comprehensive, clear)
- Formatting: ~95/100 (proper structure, complete blocks)
- Metadata Removal: ~100/100 (all noise removed)
- Initialization Examples: ~95/100 (complete, progressive)

**Estimated AFTER c7score: ~92/100**

---

## Key Transformation Patterns Used

1. **Question Headers**: "Installation" → "How do I install DataFlow?"
2. **Complete Examples**: Added imports, setup, and expected outputs
3. **Progressive Complexity**: Basic → Common → Advanced sections
4. **Error Scenarios**: Dedicated error handling examples
5. **Concrete Outputs**: Included actual output in code comments
6. **Noise Removal**: Stripped badges and timestamps
7. **Context Addition**: Every snippet is runnable as-is
8. **Multiple Paths**: Showed different ways to achieve goals

Use this example as a template for optimizing your own documentation!
