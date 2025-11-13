# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**llm-docs-optimizer** is a Claude Code plugin that optimizes documentation for AI coding assistants (Claude, GitHub Copilot, etc.). It provides two core capabilities:

1. **C7Score Optimization**: Transforms documentation to score highly on Context7's benchmark - the leading quality metric for AI-assisted coding documentation
2. **llms.txt Generation**: Creates standardized navigation files (llmstxt.org format) that help LLMs quickly understand and navigate project documentation

## Architecture

### This is NOT a Traditional Codebase

This is a **Claude Code skill/plugin** where the "code" is markdown. There are no build tools, test frameworks, or compilation steps for the main plugin.

```
skills/llm-docs-optimizer/
├── SKILL.md (21,827 lines)    # Main skill logic - the "code"
├── references/                 # Knowledge base
│   ├── c7score_metrics.md     # Scoring rubrics for 5 metrics
│   ├── optimization_patterns.md # 20+ transformation examples
│   └── llmstxt_format.md      # llms.txt specification
├── examples/                   # Before/after samples
└── scripts/
    └── analyze_docs.py        # Optional Python analysis tool
```

### Component Interaction

- **SKILL.md**: Contains structured workflows for both optimization and generation. This is where all logic lives.
- **Reference Materials**: Knowledge base that SKILL.md references during execution
- **Python Script**: Optional standalone tool for automated documentation scanning
- **c7score/**: Separate TypeScript reference implementation (Upstash's package) - not directly used by the skill

### Key Architectural Pattern: Structured Workflows

**C7Score Optimization (6 Steps)**:
1. Analyze current documentation
2. Generate 15-20 developer questions
3. Map questions to existing snippets
4. Optimize based on priority (80% weight on question-answering)
5. Validate optimizations
6. Evaluate c7score impact with before/after scoring

**llms.txt Generation (7 Steps)**:
1. Analyze project structure
2. Determine project category (library, CLI, framework, skill)
3. Create appropriate structure
4. Format links properly (full URLs with descriptions)
5. Organize sections by priority
6. Handle different repository structures
7. Validate the file

### Scoring Methodology

C7Score uses a weighted average across 5 metrics:
- **Question-Snippet Matching: 80%** (most important - focus here!)
- LLM Evaluation: 10%
- Formatting: 5%
- Metadata Removal: 2.5%
- Initialization: 2.5%

Common transformation patterns (see `references/optimization_patterns.md`):
- API Reference → Complete Usage Example
- Import-Only → Quick Start with Usage
- Multiple Small Snippets → One Comprehensive Example
- Remove Metadata (licenses, directory trees, citations)

### User Interaction Pattern

When a user requests c7score optimization, the skill **always asks** if they also want llms.txt generation (using AskUserQuestion). This is intentional - both capabilities are complementary.

## Development Commands

### Plugin Installation

```bash
# Marketplace installation (recommended)
/plugin marketplace add alonw0/llm-docs-optimizer
/plugin install llm-docs-optimizer@llm-docs-optimizer-marketplace

# Manual installation
git clone https://github.com/alonw0/llm-docs-optimizer.git ~/.claude/plugins/llm-docs-optimizer
/plugin reload
```

### Usage

The skill activates via natural language in Claude Code:
- "Optimize my documentation for c7score"
- "Create an llms.txt file for my project"
- "Improve my README for AI coding assistants"
- "Analyze my documentation quality"

### Optional: Python Analysis Script

```bash
cd skills/llm-docs-optimizer/scripts
python analyze_docs.py /path/to/documentation.md
```

### C7Score Reference (in c7score/ subdirectory)

This is a separate TypeScript package for reference only:

```bash
cd c7score
npm install          # Install dependencies
npm test            # Run tests
npm run build       # Build TypeScript
```

## Important Files to Consult

When working on the skill logic, always reference:

1. **`references/c7score_metrics.md`**: Detailed scoring rubrics - essential for understanding what makes good documentation
2. **`references/optimization_patterns.md`**: 20+ before/after examples - use these as templates
3. **`references/llmstxt_format.md`**: Complete llmstxt.org specification - required for llms.txt generation
4. **`examples/`**: Sample inputs and outputs for testing changes

## Configuration Files

- **`.claude-plugin/plugin.json`**: Plugin manifest (name, version 1.3.0, description, keywords)
- **`.claude-plugin/marketplace.json`**: Marketplace distribution config
- **`.gitignore`**: Excludes c7score/ directory, Python cache, IDE files

## Key Insights for Working in This Codebase

1. **All logic is in SKILL.md**: When modifying behavior, edit the markdown workflow in SKILL.md
2. **Question-answering is 80% of the score**: Always prioritize creating comprehensive examples that answer developer questions
3. **The c7score/ directory is for reference only**: The skill doesn't execute TypeScript code; it uses Claude for evaluation
4. **Test changes by running the skill**: No unit tests - validation is done through actual usage
5. **Three knowledge bases**: Keep references/ files in sync with SKILL.md logic
6. **Always offer llms.txt**: Part of the user experience is suggesting both capabilities together

## External References

- **Context7 c7score**: Quality benchmark for AI-assisted coding docs
- **llmstxt.org**: Official specification for llms.txt format
- **Claude API**: Used for automated documentation evaluation

## Version Information

Current Version: 1.3.0 (November 2025)

Recent changes:
- Added automated c7score evaluation with Claude-based scoring
- Renamed from "c7score-optimizer" to "llm-docs-optimizer"
- Added llms.txt generation capability (v1.1.0)
