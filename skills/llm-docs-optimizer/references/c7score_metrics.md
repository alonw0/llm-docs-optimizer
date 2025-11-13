# C7Score Metrics Reference

## Overview

c7score evaluates documentation quality for Context7 using 5 metrics divided into two groups:
- **LLM Analysis** (Metrics 1-2): AI-powered evaluation
- **Text Analysis** (Metrics 3-5): Rule-based checks

## Metric 1: Question-Snippet Comparison (LLM)

**What it measures:** How well code snippets answer common developer questions about the library.

**Scoring approach:**
- LLM generates 15 common questions developers might ask about the library
- Each snippet is evaluated on how well it answers these questions
- Higher scores for snippets that directly address practical usage questions

**Optimization strategies:**
- Include code examples that answer "how do I..." questions
- Provide working code snippets for common use cases
- Address setup, configuration, and basic operations
- Show real-world usage patterns, not just API signatures
- Include examples that demonstrate the library's main features

**What scores well:**
- "How do I initialize the client?" with full working example
- "How do I handle authentication?" with complete code
- "How do I make a basic query?" with error handling included

**What scores poorly:**
- Partial code that doesn't run standalone
- API reference without usage examples
- Theoretical explanations without practical code

## Metric 2: LLM Evaluation (LLM)

**What it measures:** Overall snippet quality including relevancy, clarity, and correctness.

**Scoring criteria:**
- **Relevancy**: Does the snippet provide useful information about the library?
- **Clarity**: Is the code and explanation easy to understand?
- **Correctness**: Is the code syntactically correct and using proper APIs?
- **Uniqueness**: Are snippets providing unique information or duplicating content?

**Optimization strategies:**
- Ensure each snippet provides distinct, valuable information
- Use clear variable names and structure
- Add brief explanatory comments where helpful
- Verify all code is syntactically correct
- Remove or consolidate duplicate snippets
- Test code examples to ensure they work

**What causes low scores:**
- High rate of duplicate snippets (>25% identical copies)
- Unclear or confusing code structure
- Syntax errors or incorrect API usage
- Snippets that don't add new information

## Metric 3: Formatting (Text Analysis)

**What it measures:** Whether snippets have the expected format and structure.

**Checks performed:**
- Are categories missing? (e.g., no title, description, or code)
- Are code snippets too short or too long?
- Are language tags actually descriptions? (e.g., "FORTE Build System Configuration")
- Are languages set to "none" or showing console output?
- Is the code just a list or argument descriptions?

**Optimization strategies:**
- Follow consistent snippet structure: TITLE / DESCRIPTION / CODE
- Use 40-dash delimiters between snippets (----------------------------------------)
- Set proper language tags (python, javascript, typescript, bash, etc.)
- Avoid very short snippets (<3 lines) unless absolutely necessary
- Avoid very long snippets (>100 lines) - break into focused examples
- Don't use lists in place of code

**Example good format:**
```
Getting Started with Authentication
----------------------------------------
Initialize the client with your API key and authenticate requests.

```python
from library import Client

client = Client(api_key="your_api_key")
client.authenticate()
```
```

**What to avoid:**
- Language tags like "CLI Arguments" or "Configuration File"
- Pretty-printed tables instead of code
- Numbered/bulleted lists masquerading as code
- Missing titles or descriptions
- Inconsistent formatting

## Metric 4: Project Metadata (Text Analysis)

**What it measures:** Presence of irrelevant project information that doesn't help developers use the library.

**Checks performed:**
- BibTeX citations (would have language tag "Bibtex")
- Licensing information
- Directory structure listings
- Project governance or administrative content

**Optimization strategies:**
- Remove or minimize licensing snippets
- Avoid directory tree representations
- Don't include citation information
- Focus on usage, not project management
- Keep administrative content out of code documentation

**What to remove or relocate:**
- LICENSE files or license text
- CONTRIBUTING.md guidelines
- Directory listings or project structure
- Academic citations (BibTeX, APA, etc.)
- Governance policies

**Exception:** Brief installation or setup instructions that mention directories are okay if needed for library usage.

## Metric 5: Initialization (Text Analysis)

**What it measures:** Snippets that are only imports or installations without meaningful content.

**Checks performed:**
- Snippets that are just import statements
- Snippets that are just installation commands (pip install, npm install)
- No additional context or usage examples

**Optimization strategies:**
- Combine imports with usage examples
- Show installation in context of setup process
- Always follow imports with actual usage code
- Make installation snippets include next steps

**Good approach:**
```python
# Installation and basic usage
# First install: pip install library-name

from library import Client

# Initialize and make your first request
client = Client()
result = client.get_data()
```

**Poor approach:**
```python
# Just imports
import library
from library import Client
```

```bash
# Just installation
pip install library-name
```

## Scoring Weights

Default c7score weights (can be customized):
- Question-Snippet Comparison: 0.8 (80%)
- LLM Evaluation: 0.05 (5%)
- Formatting: 0.05 (5%)
- Project Metadata: 0.05 (5%)
- Initialization: 0.05 (5%)

The question-answer metric dominates because Context7's primary goal is helping developers answer practical questions about library usage.

## Overall Best Practices

1. **Focus on answering questions**: Think "How would a developer actually use this?"
2. **Provide complete, working examples**: Not just fragments
3. **Ensure uniqueness**: Each snippet should teach something new
4. **Structure consistently**: TITLE / DESCRIPTION / CODE format
5. **Use proper language tags**: python, javascript, typescript, etc.
6. **Remove noise**: No licensing, directory trees, or pure imports
7. **Test your code**: All examples should be syntactically correct
8. **Keep it practical**: Real-world usage beats theoretical explanation

---

## Self-Evaluation Rubrics

When evaluating documentation quality using c7score methodology, use these detailed rubrics:

### 1. Question-Snippet Matching Rubric (80% weight)

**Score: 90-100 (Excellent)**
- All major developer questions have complete answers
- Code examples are self-contained and runnable
- Examples include imports, setup, and usage context
- Common use cases are clearly demonstrated
- Error handling is shown where relevant
- Examples progress from simple to advanced

**Score: 70-89 (Good)**
- Most questions are answered with working code
- Examples are mostly complete but may miss minor details
- Some context or imports may be implicit
- Common use cases covered
- Minor gaps in error handling

**Score: 50-69 (Fair)**
- Some questions answered, others partially addressed
- Examples require significant external knowledge
- Missing imports or setup context
- Limited use case coverage
- Error handling largely absent

**Score: 30-49 (Poor)**
- Few questions fully answered
- Examples are fragments without context
- Unclear how to actually use the code
- Major use cases not covered
- No error handling

**Score: 0-29 (Very Poor)**
- Questions not addressed in documentation
- No practical examples
- Only API signatures without usage
- Cannot determine how to use the library

### 2. LLM Evaluation Rubric (10% weight)

**Unique Information (30% of metric):**
- 100%: Every snippet provides unique value, no duplicates
- 75%: Minimal duplication, mostly unique content
- 50%: Some repeated information across snippets
- 25%: Significant duplication
- 0%: Many duplicate snippets

**Clarity (30% of metric):**
- 100%: Well-worded, professional, no errors
- 75%: Clear with minor grammar/wording issues
- 50%: Understandable but awkward phrasing
- 25%: Confusing or poorly worded
- 0%: Unclear, incomprehensible

**Correct Syntax (40% of metric):**
- 100%: All code syntactically perfect
- 75%: Minor syntax issues (missing semicolons, etc.)
- 50%: Some syntax errors but code is recognizable
- 25%: Multiple syntax errors
- 0%: Code is not valid

**Final LLM Evaluation Score** = (Unique×0.3) + (Clarity×0.3) + (Syntax×0.4)

### 3. Formatting Rubric (5% weight)

**Score: 100 (Perfect)**
- All snippets have proper language tags (python, javascript, etc.)
- Language tags are actual languages, not descriptions
- All code blocks use triple backticks with language
- Code blocks are properly closed
- No lists within CODE sections
- Minimum length requirements met (5+ words)

**Score: 80-99 (Minor Issues)**
- 1-2 snippets missing language tags
- One or two incorrectly formatted blocks
- Minor inconsistencies

**Score: 50-79 (Multiple Problems)**
- Several snippets missing language tags
- Some use descriptive strings instead of language names
- Inconsistent formatting

**Score: 0-49 (Significant Issues)**
- Many snippets improperly formatted
- Widespread use of wrong language tags
- Code not in proper blocks

### 4. Metadata Removal Rubric (2.5% weight)

**Score: 100 (Clean)**
- No license text in code examples
- No citation formats (BibTeX, RIS)
- No directory structure listings
- No project metadata
- Pure code and usage examples

**Score: 75-99 (Minimal Metadata)**
- One or two snippets with minor metadata
- Brief license mentions that don't dominate

**Score: 50-74 (Some Metadata)**
- Several snippets include project metadata
- Directory structures present
- Some citation content

**Score: 0-49 (Heavy Metadata)**
- Significant license/citation content
- Multiple directory listings
- Project metadata dominates

### 5. Initialization Rubric (2.5% weight)

**Score: 100 (Excellent)**
- All examples show usage beyond setup
- Installation combined with first usage
- Imports followed by practical examples
- No standalone import/install snippets

**Score: 75-99 (Mostly Good)**
- 1-2 snippets are setup-only
- Most examples show actual usage

**Score: 50-74 (Some Init-Only)**
- Several snippets are just imports/installation
- Mixed quality

**Score: 0-49 (Many Init-Only)**
- Many snippets are only imports
- Many snippets are only installation
- Lack of usage examples

### Scoring Best Practices

**When evaluating:**
1. **Read entire documentation** before scoring
2. **Count specific examples** (e.g., "7 out of 10 snippets...")
3. **Be consistent** between before/after evaluations
4. **Explain scores** with concrete evidence
5. **Use percentages** when quantifying (e.g., "80% of examples...")
6. **Identify improvements** specifically
7. **Calculate weighted average**: (Q×0.8) + (L×0.1) + (F×0.05) + (M×0.025) + (I×0.025)

**Example Calculation:**
- Question-Snippet: 85/100 × 0.8 = 68
- LLM Evaluation: 90/100 × 0.1 = 9
- Formatting: 100/100 × 0.05 = 5
- Metadata: 100/100 × 0.025 = 2.5
- Initialization: 95/100 × 0.025 = 2.375
- **Total: 86.875 ≈ 87/100**

### Common Scoring Mistakes to Avoid

❌ **Being too generous**: Score based on evidence, not potential
❌ **Ignoring weights**: Question-answer matters most (80%)
❌ **Vague explanations**: Say "5 of 8 examples lack imports" not "some issues"
❌ **Inconsistent standards**: Apply same rubric to before/after
❌ **Forgetting context**: Consider project type and audience
✅ **Be specific, objective, and consistent**
