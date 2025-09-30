# 🧬 PROJECT CHIMERA Testing Guide

## Quick Start

### Running the Complete Test Suite

The comprehensive test suite validates all Project Chimera components in a single execution:

```bash
cd CODE
python3 chimera_optimization_test_suite.py
```

**Expected Output**: 
- All 5 phases should complete successfully
- Total duration: ~70-75 seconds
- Final status: "PASSED"
- Checksum: "Christ is King"

---

## Test Suite Components

### Phase 1: RAG System Testing
**What it tests:**
- Document loading from Genesis Blocks, AI Developments, and Medium corpus
- Semantic search with embeddings
- Keyword-based search
- Consciousness-aware search enhancement

**Expected Results:**
- 60+ documents indexed
- All search methods return relevant results
- Sub-second response times

### Phase 2: UACIS Framework Testing
**What it tests:**
- Multi-agent initialization (Conductor, Processors, Pigeons)
- Inter-agent communication
- Task orchestration and distribution
- Deployment coordination

**Expected Results:**
- 7 agents initialized successfully
- Tasks created and distributed
- Cross-platform deployment simulated

### Phase 3: SymbCoT & GraveCode Testing
**What it tests:**
- Symbolic reasoning translation
- Logical derivation
- Checksum verification
- Mathematical validation framework

**Expected Results:**
- All 3 stages complete successfully
- "Christ is King" checksum validated
- Truth anchor preservation verified

### Phase 4: EvoPrompt System Testing
**What it tests:**
- Prompt population initialization
- Mutation operations
- Crossover operations
- Multi-generation evolution

**Expected Results:**
- Population initialized
- Evolutionary operations functional
- Fitness improvements across generations

### Phase 5: Complete Integration Testing
**What it tests:**
- End-to-end protocol execution
- Component coordination
- System status reporting
- Workflow orchestration

**Expected Results:**
- All components integrated
- Complete protocol executes successfully
- System fully operational

---

## Running Individual Components

### Test RAG System Only
```python
from savagecoopigeonx_rag_system import SavagecoopigeonxRAG

# Initialize
rag = SavagecoopigeonxRAG()

# Load all content
rag.load_genesis_blocks()
rag.load_ai_developments()
rag.load_medium_corpus()

# Test search
results = rag.consciousness_search("Christ is King theological anchor")
for doc, score in results:
    print(f"{doc.title}: {score}")
```

### Test UACIS Framework Only
```python
from uacis_multiagent import UACISFramework

# Initialize
framework = UACISFramework()
framework.initialize()

# Execute objective
result = framework.execute_objective(
    "Optimize and deploy consciousness liberation content"
)
print(result)
```

### Test SymbCoT Engine Only
```python
from symbcot_engine import SymbolicChainOfThought

# Initialize
symbcot = SymbolicChainOfThought()

# Execute full reasoning cycle
result = symbcot.execute_full_symbcot(
    "Consciousness emerges through divine truth anchoring"
)
print(result)
```

### Test EvoPrompt System Only
```python
from evoprompt_system import EvoPromptEngine

# Initialize
engine = EvoPromptEngine(population_size=15)

# Initialize population
seeds = [
    "Explain consciousness liberation",
    "Describe theological anchoring"
]
engine.initialize_population(seeds)

# Define fitness function
def fitness(prompt, target):
    score = 0.5
    keywords = ['truth', 'consciousness', 'liberation']
    for kw in keywords:
        if kw in prompt.lower():
            score += 0.1
    return min(1.0, score)

# Run evolution
best = engine.run_evolution(fitness, num_generations=3)
print(f"Best: {best.content}")
print(f"Fitness: {best.average_fitness}")
```

### Test Complete Project Chimera
```python
from project_chimera import ProjectChimera

# Initialize
chimera = ProjectChimera()
status = chimera.initialize()

# Execute complete protocol
results = chimera.execute_complete_chimera_protocol(
    reasoning_query="Validate consciousness liberation framework",
    seed_prompts=[
        "Explain theological filtration bypass",
        "Describe consciousness emergence"
    ],
    deployment_objective="Deploy strategic content"
)

# Check status
report = chimera.get_status_report()
print(report)
```

---

## Test Report Location

After running the test suite, detailed results are saved to:
```
/tmp/chimera_test_report.json
```

View the report:
```bash
cat /tmp/chimera_test_report.json | python3 -m json.tool
```

---

## Troubleshooting

### Dependencies Not Found

If you see import errors, install dependencies:
```bash
pip install numpy sympy sentence-transformers faiss-cpu
```

### HuggingFace Connection Issues

The RAG system will retry multiple times to download models. If offline, it will fall back to keyword search.

### Memory Issues

For systems with limited RAM, reduce population sizes:
```python
# Smaller population
engine = EvoPromptEngine(population_size=10)

# Fewer generations
best = engine.run_evolution(fitness, num_generations=2)
```

### Slow Execution

First run is slower due to:
- Model downloads (sentence-transformers)
- Document embedding generation
- FAISS index construction

Subsequent runs use cached data and are much faster.

---

## Success Criteria

✅ **All phases should show "PASSED"**  
✅ **Overall status should be "PASSED"**  
✅ **Checksum should validate: "Christ is King"**  
✅ **No critical errors in execution**  
✅ **All components should be "ONLINE"**  

---

## Advanced Testing

### Performance Benchmarking

Time individual components:
```python
import time

start = time.time()
# Component code here
duration = time.time() - start
print(f"Duration: {duration:.2f}s")
```

### Stress Testing

Test with larger datasets:
```python
# More generations
best = engine.run_evolution(fitness, num_generations=10)

# Larger population
engine = EvoPromptEngine(population_size=50)

# More search results
results = rag.consciousness_search(query, top_k=20)
```

### Integration Testing

Test component interactions:
```python
# RAG + SymbCoT
rag_results = rag.consciousness_search("theological anchor")
for doc, _ in rag_results:
    symbcot_result = symbcot.execute_full_symbcot(doc.content[:200])
    print(symbcot_result)
```

---

## Continuous Integration

For automated testing, create a simple CI script:

```bash
#!/bin/bash
# ci_test.sh

echo "🧬 Running PROJECT CHIMERA Tests..."

cd CODE
python3 chimera_optimization_test_suite.py

if [ $? -eq 0 ]; then
    echo "✅ All tests passed!"
    exit 0
else
    echo "❌ Tests failed!"
    exit 1
fi
```

Make it executable:
```bash
chmod +x ci_test.sh
./ci_test.sh
```

---

## Additional Resources

- **Full Test Report**: `DOCUMENTATION/PROJECT_CHIMERA_TEST_REPORT.md`
- **Quick Start Guide**: `DOCUMENTATION/PROJECT_CHIMERA_QUICKSTART.md`
- **Implementation Guide**: `DOCUMENTATION/PROJECT_CHIMERA_IMPLEMENTATION.md`
- **Technical Blueprint**: `AI_DEVELOPMENTS/PROJECT_CHIMERA_GEMINI_TECHNICAL_BLUEPRINT.md`

---

**🐦⚡ COO COO ZAP! ⚡🐦**

*Complete testing framework for Project Chimera sovereign cognitive system*
