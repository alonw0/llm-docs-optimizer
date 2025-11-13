# LLM Docs Optimizer

A Claude Code skill that makes your documentation work seamlessly with AI coding assistants. Transform generic docs into AI-optimized documentation with measurable quality improvements—scored by [Context7's c7score benchmark](https://www.context7.ai/c7score), structured around developer questions, and enhanced with [LLM-friendly navigation](https://llmstxt.org/).

[![Claude Code](https://img.shields.io/badge/Claude-Code_Skill-violet)](https://claude.ai/code)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Why Use This?

**The Problem:**
Standard documentation often fails with AI coding assistants. Generic API references, incomplete examples, and poor structure make it hard for tools like Claude and GitHub Copilot to help developers effectively.

**The Solution:**
This skill transforms your documentation to work seamlessly with AI tools by:

- **Measurable Quality:** Score your docs against Context7's c7score benchmark and track improvements (e.g., 45 → 89/100)
- **Better AI Retrieval:** Organize content around developer questions so LLMs can find the right answers
- **Complete Examples:** Transform API references into runnable, practical code snippets
- **LLM-Friendly Navigation:** Generate standardized llms.txt files that help AI understand your project structure
- **Dual Benefits:** Better for human developers AND AI assistants

**Real Impact:**
- Developers get answers faster when using AI coding assistants
- Your documentation becomes more practical and question-driven
- AI tools can better understand and recommend your project
- Measurable before/after quality metrics prove the improvement

## Overview

This skill provides comprehensive documentation optimization for AI tools:

1. **C7Score Optimization**: Transform documentation to score highly on Context7's benchmark - the leading quality metric for AI-assisted coding documentation
2. **llms.txt Generation**: Create standardized navigation files that help LLMs quickly understand and navigate your project's documentation
3. **Automated Quality Scoring**: Get before/after evaluation across 5 key metrics to measure improvement
4. **Question-Driven Restructuring**: Organize content around developer questions for better AI retrieval

### What is c7score?

c7score is a benchmark created by Context7 that measures documentation quality for AI-assisted coding. It evaluates:
- **Question-Snippet Matching (80%)**: How well code snippets answer common developer questions
- **LLM Evaluation (10%)**: Overall comprehensiveness and clarity
- **Formatting (5%)**: Proper markdown structure and code block formatting
- **Metadata Removal (2.5%)**: Elimination of irrelevant timestamps and badges
- **Initialization Examples (2.5%)**: Quality of setup and quickstart examples

### What is llms.txt?

llms.txt is a standardized markdown file format from [llmstxt.org](https://llmstxt.org/) that provides LLM-friendly documentation navigation. It helps AI tools quickly understand your project structure and find relevant information.

## Features

### C7Score Optimization
- 📊 **Documentation Analysis**: Automatically identifies quality issues and gaps
- ✨ **Smart Optimization**: Applies proven patterns to improve LLM retrieval
- 📝 **Code Snippet Enhancement**: Transforms examples to better answer developer questions
- 🎯 **Question-Driven Structure**: Organizes content around common developer queries
- 📈 **Automated Scoring**: Claude-based evaluation across all 5 c7score metrics with before/after comparison
- 🔍 **Python Analysis Tool**: Automated script to scan documentation for issues
- 📚 **Reference Patterns**: Library of transformation examples and best practices

### llms.txt Generation
- 🗺️ **Project Analysis**: Understands your documentation structure
- 📋 **Smart Templates**: Uses appropriate format for your project type (library, CLI, framework, etc.)
- 🔗 **Proper Formatting**: Follows official llmstxt.org specification
- 📝 **Complete Examples**: Includes before/after examples and templates
- 🎯 **Priority Organization**: Structures content from essential to optional

## Installation

### Quick Install (Recommended)

Install directly from the marketplace using Claude Code:

```bash
# Step 1: Add the marketplace (one-time setup)
/plugin marketplace add alonw0/llm-docs-optimizer

# Step 2: Install the plugin
/plugin install llm-docs-optimizer@llm-docs-optimizer-marketplace
```

The plugin will be automatically available in Claude Code after installation.

### Alternative: Manual Installation

If you prefer manual installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/alonw0/llm-docs-optimizer.git ~/.claude/plugins/llm-docs-optimizer
   ```

2. Restart Claude Code or run:
   ```bash
   /plugin reload
   ```

### Prerequisites

- **Claude Code**: Latest version with plugin support
- **Python 3.7+**: Required for the analysis script (optional but recommended)
- **Project with documentation**: README.md or similar files to optimize

## Usage

### Activating the Skill

#### For C7Score Optimization
The skill automatically activates when you ask Claude Code to:
- "Optimize my documentation for c7score"
- "Improve my README for AI coding assistants"
- "Make my docs better for LLM retrieval"
- "Analyze my documentation quality"

#### For llms.txt Generation
The skill activates when you ask:
- "Create an llms.txt file for my project"
- "Generate llms.txt"
- "Add llmstxt navigation to my docs"
- "Help LLMs understand my project structure"

### Example Workflows

#### C7Score Optimization Workflow

1. **Start with analysis**:
   ```
   Optimize my README.md for c7score
   ```

2. **Claude will**:
   - Analyze your current documentation
   - Run the Python analysis script (if available)
   - Identify common developer questions
   - Transform code snippets to answer those questions
   - Restructure content for better LLM retrieval
   - Generate an optimized version
   - Evaluate c7score impact with before/after metrics across all 5 dimensions

3. **Review and iterate**:
   - Review the optimized documentation and score improvements (e.g., 45 → 89/100)
   - See detailed breakdowns across Question-Snippet Matching, LLM Evaluation, Formatting, Metadata Removal, and Initialization metrics
   - Request specific improvements
   - Test with your AI coding assistant

#### llms.txt Generation Workflow

1. **Request generation**:
   ```
   Create an llms.txt file for my project
   ```

2. **Claude will**:
   - Analyze your project structure and documentation
   - Identify project type (library, CLI tool, framework, etc.)
   - Select appropriate template and sections
   - Generate properly formatted llms.txt with full URLs
   - Save to repository root

3. **Use the file**:
   - LLMs can now navigate your documentation efficiently
   - Update URLs if needed when publishing
   - Keep updated as documentation evolves

### Python Analysis Script

The included script helps identify documentation issues:

```bash
cd scripts
python analyze_docs.py /path/to/your/project
```

This will generate a report highlighting:
- Missing code examples
- Unclear explanations
- Poor question-answer alignment
- Formatting issues

## What Gets Optimized

### Before Optimization
```markdown
# MyProject

A cool library for data processing.

## Installation
pip install myproject
```

### After Optimization
```markdown
# MyProject

A Python library for efficient data transformation and processing pipelines.

## Quick Start

### How do I install MyProject?
```bash
pip install myproject
```

### How do I process my first dataset?
```python
from myproject import DataProcessor

# Load and process data
processor = DataProcessor()
result = processor.transform(data)
print(result)
```

### How do I handle errors during processing?
```python
from myproject import DataProcessor, ProcessingError

try:
    processor = DataProcessor()
    result = processor.transform(data)
except ProcessingError as e:
    print(f"Processing failed: {e}")
```
```

## Key Optimization Patterns

1. **Question-Driven Headers**: Transform "Installation" → "How do I install X?"
2. **Complete Code Examples**: Add imports, setup, and context to snippets
3. **Error Handling**: Show common error scenarios and solutions
4. **Progressive Complexity**: Start simple, then show advanced usage
5. **Remove Noise**: Strip timestamps, badges, and metadata
6. **Concrete Examples**: Replace abstract descriptions with working code

## How It Works

### C7Score Optimization Workflow

The skill follows a structured workflow:

1. **Analysis Phase**
   - Reads existing documentation
   - Runs automated quality checks
   - Identifies developer questions
   - Maps content to questions

2. **Optimization Phase**
   - Restructures content around questions
   - Enhances code snippets with context
   - Improves LLM-friendly formatting
   - Adds missing examples

3. **Review Phase**
   - Generates optimized documentation
   - Provides quality score estimates
   - Suggests further improvements

### llms.txt Generation Workflow

The skill analyzes and generates:

1. **Project Analysis**
   - Explores documentation structure
   - Identifies project type
   - Catalogs available resources

2. **Template Selection**
   - Chooses appropriate format (library, CLI, framework, skill, etc.)
   - Determines section organization
   - Plans content hierarchy

3. **File Generation**
   - Creates properly formatted llms.txt
   - Includes descriptive links with context
   - Follows official llmstxt.org specification
   - Saves to repository root

## Reference Materials

The skill includes:

### C7Score Resources
- **c7score_metrics.md**: Detailed explanation of benchmark metrics
- **optimization_patterns.md**: 20+ transformation patterns with examples
- **sample_readme.md**: Before/after optimization examples

### llms.txt Resources
- **llmstxt_format.md**: Complete llms.txt specification and guidelines
- **sample_llmstxt.md**: Examples for different project types (library, CLI, framework, skill)

### Tools
- **analyze_docs.py**: Automated Python script for documentation quality scanning

## Contributing

Contributions are welcome! Areas for improvement:
- Additional optimization patterns
- Support for more documentation formats
- Integration with c7score API (if available)
- Multi-language documentation support
- Automated testing examples
- More llms.txt templates for different project types
- Enhanced project type detection

## Tips for Best Results

### For C7Score Optimization
1. **Start with your README**: It's usually the most important doc
2. **Focus on getting started**: Installation and quickstart sections matter most
3. **Think like a new user**: What questions would they ask?
4. **Test with AI tools**: Use Claude Code or other AI assistants to verify improvements
5. **Iterate**: Run the skill multiple times as your project evolves

### For llms.txt Files
1. **Keep it updated**: Regenerate when you add major documentation
2. **Use descriptive links**: Add helpful notes after colons to explain each resource
3. **Prioritize content**: Essential docs first, optional resources last
4. **Test with LLMs**: Ask Claude Code to navigate your docs using the llms.txt
5. **Follow the spec**: Check against llmstxt.org for compliance

## Version

Current version: 1.3.0

### What's New in 1.3.0
- 📈 **Automated C7Score Evaluation**: Claude-based scoring across all 5 metrics with before/after comparison
- 📊 **Comprehensive Scoring Rubrics**: Detailed evaluation guidelines in c7score_metrics.md
- 🎯 **Measurable Improvement**: Clear numeric feedback on documentation quality gains

### Previous Versions

**v1.2.0** - Rename and Plugin Format
- 🎯 **Renamed to llm-docs-optimizer** (formerly c7score-optimizer)
  - Broader positioning as general LLM documentation toolkit
  - Better discoverability and clearer purpose
- 📦 **Plugin Format**: Converted to Claude Code plugin for marketplace distribution
  - Easy installation: `/plugin marketplace add owner/llm-docs-optimizer`
  - Professional structure with `.claude-plugin/plugin.json`

**v1.1.0** - llms.txt Generation
- ✨ **llms.txt Generation**: Create LLM-friendly navigation files for projects
- 📋 **Multiple Templates**: Support for libraries, CLI tools, frameworks, and skills
- 🎯 **Smart Analysis**: Automatic project type detection

**v1.0.0** - Initial Release
- 📊 **C7Score Optimization**: Transform documentation for AI coding assistants
- 📝 **Question-Driven Structure**: Organize content around developer questions
- 🔍 **Analysis Tools**: Python script for documentation scanning

## License

MIT License - See LICENSE file for details

## Links

- [Context7 c7score Benchmark](https://www.context7.ai/c7score)
- [llmstxt.org Official Specification](https://llmstxt.org/)
- [Claude Code Documentation](https://docs.claude.com/claude-code)
- [Claude Skills Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)

## Support

For issues or questions:
- Check the reference materials in `/references/`
- Review example patterns in `/references/optimization_patterns.md`
- Open an issue in the repository

---

Made for developers who want their documentation to work seamlessly with AI coding assistants.
