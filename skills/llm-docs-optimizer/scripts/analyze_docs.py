#!/usr/bin/env python3
"""
Documentation Analyzer for C7Score Optimization

Analyzes README and documentation files to identify:
- Snippets that are import-only or installation-only
- Potential formatting issues
- Metadata content (licensing, citations, directory structures)
- Duplicate or near-duplicate code blocks
- Missing question-answering examples
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple
from collections import Counter


class CodeSnippet:
    def __init__(self, language: str, code: str, context: str, line_num: int):
        self.language = language
        self.code = code.strip()
        self.context = context  # Text before the code block
        self.line_num = line_num
        self.issues = []

    def __repr__(self):
        return f"CodeSnippet(lang={self.language}, lines={len(self.code.splitlines())}, line={self.line_num})"


def extract_code_snippets(content: str) -> List[CodeSnippet]:
    """Extract all code blocks from markdown content."""
    snippets = []
    lines = content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i]
        # Match code block start
        if line.strip().startswith('```'):
            # Extract language
            language = line.strip()[3:].strip() or 'unknown'
            start_line = i
            
            # Get context (previous non-empty lines up to 5)
            context_lines = []
            for j in range(max(0, i-5), i):
                if lines[j].strip():
                    context_lines.append(lines[j].strip())
            context = ' '.join(context_lines[-3:])  # Last 3 lines of context
            
            # Collect code until end marker
            i += 1
            code_lines = []
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            
            code = '\n'.join(code_lines)
            snippets.append(CodeSnippet(language, code, context, start_line + 1))
        
        i += 1
    
    return snippets


def analyze_snippet(snippet: CodeSnippet) -> List[str]:
    """Analyze a single code snippet for c7score issues."""
    issues = []
    code = snippet.code.strip()
    lines = [l.strip() for l in code.split('\n') if l.strip()]
    
    # Check 1: Import-only snippets
    if lines:
        import_patterns = [
            r'^import\s+',
            r'^from\s+\S+\s+import\s+',
            r'^require\s*\(',
            r'^const\s+\S+\s*=\s*require',
            r'^using\s+',
        ]
        
        import_count = sum(1 for line in lines if any(re.match(p, line) for p in import_patterns))
        if import_count == len(lines) and len(lines) <= 5:
            issues.append("⚠️  Import-only snippet (Metric 5: Initialization)")
    
    # Check 2: Installation-only snippets
    install_patterns = [
        r'pip install',
        r'npm install',
        r'yarn add',
        r'cargo install',
        r'go get',
        r'gem install',
    ]
    
    if len(lines) <= 2 and any(any(pattern in line for pattern in install_patterns) for line in lines):
        issues.append("⚠️  Installation-only snippet (Metric 5: Initialization)")
    
    # Check 3: Snippet length
    if len(lines) < 3:
        issues.append("⚠️  Very short snippet (<3 lines) (Metric 3: Formatting)")
    elif len(lines) > 100:
        issues.append("⚠️  Very long snippet (>100 lines) (Metric 3: Formatting)")
    
    # Check 4: Language tag issues
    problematic_languages = [
        'configuration', 'config', 'cli arguments', 'arguments',
        'none', 'console', 'output', 'text', 'plaintext'
    ]
    
    if snippet.language.lower() in problematic_languages:
        issues.append(f"⚠️  Problematic language tag: '{snippet.language}' (Metric 3: Formatting)")
    
    # Check 5: Looks like a list
    if len(lines) > 3:
        list_markers = sum(1 for line in lines if re.match(r'^\s*[-*\d.]+\s', line))
        if list_markers / len(lines) > 0.5:
            issues.append("⚠️  Appears to be a list, not code (Metric 3: Formatting)")
    
    # Check 6: Directory structure
    if any(all(char in line for char in ['├', '│', '─', '└']) for line in lines):
        issues.append("⚠️  Directory structure detected (Metric 4: Project Metadata)")
    
    # Check 7: License or citation markers
    license_markers = ['license', 'copyright', 'mit', 'apache', 'gpl', 'bsd']
    citation_markers = ['@article', '@book', 'bibtex', 'doi:', 'citation']
    
    code_lower = code.lower()
    if any(marker in code_lower for marker in license_markers) and len(code) > 100:
        issues.append("⚠️  License content detected (Metric 4: Project Metadata)")
    
    if any(marker in code_lower for marker in citation_markers):
        issues.append("⚠️  Citation content detected (Metric 4: Project Metadata)")
    
    return issues


def find_duplicates(snippets: List[CodeSnippet]) -> List[Tuple[int, int]]:
    """Find duplicate or near-duplicate snippets."""
    duplicates = []
    
    for i, snippet1 in enumerate(snippets):
        for j, snippet2 in enumerate(snippets[i+1:], start=i+1):
            # Normalize for comparison
            code1 = re.sub(r'\s+', ' ', snippet1.code.lower()).strip()
            code2 = re.sub(r'\s+', ' ', snippet2.code.lower()).strip()
            
            # Exact duplicate
            if code1 == code2:
                duplicates.append((i, j))
            # Near duplicate (>80% similar)
            elif len(code1) > 20 and len(code2) > 20:
                # Simple similarity check
                min_len = min(len(code1), len(code2))
                max_len = max(len(code1), len(code2))
                if min_len / max_len > 0.8:
                    # Check if one contains most of the other
                    if code1 in code2 or code2 in code1:
                        duplicates.append((i, j))
    
    return duplicates


def generate_question_suggestions(content: str) -> List[str]:
    """Suggest questions that should be answered in the documentation."""
    # Extract apparent project name
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    project_name = title_match.group(1) if title_match else "this library"
    
    questions = [
        f"How do I install {project_name}?",
        f"How do I get started with {project_name}?",
        f"How do I initialize/configure {project_name}?",
        f"How do I authenticate with {project_name}?",
        f"What are the main features and how do I use them?",
        f"How do I handle errors in {project_name}?",
        f"How do I perform [common operation]?",
        f"What are common configuration options?",
        f"How do I integrate {project_name} with [common tools]?",
        f"How do I test code using {project_name}?",
    ]
    
    return questions


def analyze_documentation(file_path: str) -> Dict:
    """Analyze documentation file for c7score optimization opportunities."""
    path = Path(file_path)
    
    if not path.exists():
        return {"error": f"File not found: {file_path}"}
    
    content = path.read_text(encoding='utf-8')
    snippets = extract_code_snippets(content)
    
    # Analyze each snippet
    snippet_issues = []
    for snippet in snippets:
        issues = analyze_snippet(snippet)
        if issues:
            snippet_issues.append({
                'snippet': snippet,
                'issues': issues
            })
    
    # Find duplicates
    duplicates = find_duplicates(snippets)
    
    # Calculate statistics
    total_snippets = len(snippets)
    snippets_with_issues = len(snippet_issues)
    
    # Language distribution
    language_dist = Counter(s.language for s in snippets)
    
    # Issue type counts
    issue_types = Counter()
    for item in snippet_issues:
        for issue in item['issues']:
            # Extract metric number
            if "Metric 3" in issue:
                issue_types["Formatting (M3)"] += 1
            elif "Metric 4" in issue:
                issue_types["Metadata (M4)"] += 1
            elif "Metric 5" in issue:
                issue_types["Initialization (M5)"] += 1
    
    return {
        'file': file_path,
        'total_snippets': total_snippets,
        'snippets_with_issues': snippets_with_issues,
        'issue_breakdown': dict(issue_types),
        'duplicates': len(duplicates),
        'language_distribution': dict(language_dist),
        'detailed_issues': snippet_issues,
        'duplicate_pairs': duplicates,
        'question_suggestions': generate_question_suggestions(content),
    }


def print_report(analysis: Dict):
    """Print a formatted analysis report."""
    if 'error' in analysis:
        print(f"❌ {analysis['error']}")
        return
    
    print(f"\n{'='*70}")
    print(f"C7Score Documentation Analysis: {analysis['file']}")
    print(f"{'='*70}\n")
    
    print(f"📊 Summary Statistics")
    print(f"{'─'*70}")
    print(f"Total code snippets: {analysis['total_snippets']}")
    print(f"Snippets with issues: {analysis['snippets_with_issues']}")
    print(f"Duplicate snippets: {analysis['duplicates']}")
    
    if analysis['total_snippets'] > 0:
        issue_rate = (analysis['snippets_with_issues'] / analysis['total_snippets']) * 100
        print(f"Issue rate: {issue_rate:.1f}%")
    
    print(f"\n📝 Language Distribution")
    print(f"{'─'*70}")
    for lang, count in sorted(analysis['language_distribution'].items(), key=lambda x: x[1], reverse=True):
        print(f"  {lang}: {count}")
    
    if analysis['issue_breakdown']:
        print(f"\n⚠️  Issue Breakdown by Metric")
        print(f"{'─'*70}")
        for issue_type, count in sorted(analysis['issue_breakdown'].items(), key=lambda x: x[1], reverse=True):
            print(f"  {issue_type}: {count}")
    
    if analysis['detailed_issues']:
        print(f"\n🔍 Detailed Issues (Showing first 10)")
        print(f"{'─'*70}")
        for i, item in enumerate(analysis['detailed_issues'][:10], 1):
            snippet = item['snippet']
            print(f"\n{i}. Line {snippet.line_num} [{snippet.language}] ({len(snippet.code.splitlines())} lines)")
            for issue in item['issues']:
                print(f"   {issue}")
            # Show first 2 lines of code
            code_preview = '\n'.join(snippet.code.split('\n')[:2])
            print(f"   Preview: {code_preview[:80]}...")
    
    if analysis['duplicate_pairs']:
        print(f"\n🔄 Duplicate Snippets")
        print(f"{'─'*70}")
        for i, (idx1, idx2) in enumerate(analysis['duplicate_pairs'][:5], 1):
            print(f"{i}. Snippets at lines {snippets[idx1].line_num} and {snippets[idx2].line_num} are duplicates")
    
    print(f"\n💡 Suggested Questions to Answer")
    print(f"{'─'*70}")
    for i, question in enumerate(analysis['question_suggestions'], 1):
        print(f"{i}. {question}")
    
    print(f"\n✅ Recommendations")
    print(f"{'─'*70}")
    
    recommendations = []
    
    if analysis['issue_breakdown'].get('Initialization (M5)', 0) > 0:
        recommendations.append(
            "• Combine import-only and installation-only snippets with actual usage examples"
        )
    
    if analysis['issue_breakdown'].get('Formatting (M3)', 0) > 0:
        recommendations.append(
            "• Fix formatting issues: use proper language tags, avoid very short/long snippets"
        )
    
    if analysis['issue_breakdown'].get('Metadata (M4)', 0) > 0:
        recommendations.append(
            "• Remove or relocate metadata content (licensing, citations, directory trees)"
        )
    
    if analysis['duplicates'] > 0:
        recommendations.append(
            f"• Remove or consolidate {analysis['duplicates']} duplicate snippets (reduces LLM score)"
        )
    
    if analysis['total_snippets'] < 10:
        recommendations.append(
            "• Add more comprehensive code examples answering common developer questions"
        )
    
    if not recommendations:
        recommendations.append("• Documentation looks good! Consider running actual c7score for detailed metrics")
    
    for rec in recommendations:
        print(rec)
    
    print(f"\n{'='*70}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_docs.py <path-to-readme-or-doc.md>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    analysis = analyze_documentation(file_path)
    print_report(analysis)
